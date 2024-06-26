![HSV-AI Logo](https://hsv.ai/wp-content/uploads/2022/03/logo_v11_2022.png)


# Welcome

- Vision
- Mission
- How to Connect - [Signup](https://hsv.ai/subscribe)

# Why use Weaviate?

- Provides free hosting of the database for prototyping
- It supports both vector and object storage, allowing for hybrid search capabilities that combine vector similarity with traditional filtering and keyword search
- It can handle extremely large datasets, scaling to hundreds of billions of vectors
- Feels **much** faster than ChromaDB, while being as easy to use

# Weaviate Setup

- Create an account
- Create a sandbox (valid for 14 days) on the free tier
- Install the weaviate python library
- Find the url and api key for your cluster
- Add the url and api key to your environment

# Background Information

For this example, we are using a trove of NASA documents that we have previously broken into chunks and created embeddings for. There are a lot of different methods for chunking documents that are not covered in this discussion.

There are also many different models that can be used for embeddings with tradeoffs to be considered. That is also outside the scope of this discussion.

# Inserting Data Objects

After installing the weaviate client, we can import the necessary classes for the client connection, configuration, and collections.

```python
import weaviate
import weaviate.classes as wvc
```
Then we use the cluster URL and Weaviate API key to connect the client.

```python
# Create the client for Weaviate and connect
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.getenv("WCD_URL"),
    auth_credentials=weaviate.auth.AuthApiKey(os.getenv("WCD_API_KEY")),
    additional_config=wvc.init.AdditionalConfig(timeout=(180, 180))
)

# Check to see if the connection is ready
client.is_ready()
```

Initially had a problem with the gprc call for inserting object timing out. Had to figure out how to update the Configuration of the client to add timeout values. Assuming these are in seconds, since the documentation doesn't specify the unit of measure.

Finally found more documentation on the timeout values [HERE](https://weaviate.io/developers/weaviate/client-libraries/python#timeout-values)

It looks like weaviate doesn't have a way to get_or_create a collection. Instead, we have to check for an existing and then create if we don't find one.

```python
collection = None
if client.collections.exists("Chunks"):
    collection = client.collections.get("Chunks")
else:
    collection = client.collections.create(
        name="Chunks",
        vectorizer_config=wvc.config.Configure.Vectorizer.none()
    )
```
We also are going to use our own vectors, instead of having Weaviate compute these for us. That's why we're using Vectorizer.none() above. I believe that Weaviate can be configured to use OpenAI or other APIs (along with passing your key) if you want to use that approach.

Now we can insert objects as a list, or individually. In our case, we are looping over a list of chunks from the NASA documentation. The properties of the data object can be whatever you want, except for a few restricted keys such as 'id'.

```python
chunk_list = list()

# For each item in our list of chunks:
chunk_list.append(wvc.data.DataObject(
    properties={
        "key": doc_id,
        "page": page,
        "chunk": chunk,
    },
    vector=embedding.tolist()
))
```
After we have a list of DataObjects, we can insert with a single line:
```python
collection.data.insert_many(chunk_list)    # This uses batching under the hood
```
If you are using the hosting solution for Weaviate, you can now view your cluster, collection, and see how many objects have been uploaded.

# Querying Data Objects

Now for the query side of this walkthrough, we can create the client and connect in the same way as we did before.

```python
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.getenv("WCD_URL"),
    auth_credentials=weaviate.auth.AuthApiKey(os.getenv("WCD_API_KEY")),
    additional_config=wvc.init.AdditionalConfig(timeout=(180, 180))
)

# Check connection
client.is_ready()
```

We are going to use our own encoding as well for the query, remembering that the encoding approach of the query has to match the encoding approach of the data.

We're using the SentenceTransformer library with the bge-small model for these encodings.

```python
model = SentenceTransformer('BAAI/bge-small-en-v1.5', device='cuda')

text = "What is the ration of fuel to weight necessary for lunar liftoff?"
text_embed = model.encode(text)
```
Now we have an embedding of the text we are going to use for a semantic search in our query.

```python
collection = client.collections.get("Chunks")

response = collection.query.near_vector(
    near_vector=text_embed.tolist(), # your query vector goes here
    limit=5,
    return_metadata=MetadataQuery(distance=True)
)
```
Weaviate provides a set of values in the metadata return for each query. There are a few parameters that are available by default and others that are available based on the type of query and modules that you have connected with your Weaviate instance. In our case, we are going to use the distance metric to see how well our results match our query.

Now we can print the results and see what type of matches we had.

```python
for o in response.objects:
    print(o.properties)
    print(o.metadata.distance)
```
In this case, we are querying a lot of NASA documents that we have previously chunked, embedded, and inserted to our vector store. Here are the top three results from the query, along with the distance parameter of each. We're using cosine similarity as our distance metric, so a lower value is better.

```
{'key': '20130014470', 'page': 253.0, 'chunk': 'Mass: The total mass at launch was 1,964.6 pounds (891 kg), consisting of 1,290 pounds (585 kg) for the spacecraft and 674.6 pounds (306 kg) of hydrazine fuel.'}
0.21913838386535645
{'key': '20220006404', 'page': 16.0, 'chunk': '• Remaining fuel used to lower perigee prior to spacecraft passivation'}
0.237518310546875
{'key': '19650025648', 'page': 3.0, 'chunk': 'The required input power t\nh\na t corresponds t o these specif icaSilver-zinc b\na\nt t e\nr\ni e s have a capacity of approximately On t\nh\ni s bas i s, the b\na\nt t e\nr\ny weight f\no\nr the 1-hour mission i\ns\n7 3 pounds.\nThis b\na\nt t e\nr\ny weight i s compatible with a\nt\no t a l spacecraft weight of 350 pounds, which the assigned launch vehicle - the'}
```

You can also filter the objects before the query is applied. This is useful if you have different categories of items in your vector store that you only want to filter. So if we want to restrict the results to only come from the first document with a key of "20130014470", we can do that.

```python
response = collection.query.near_vector(
    near_vector=text_embed.tolist(), # your query vector goes here
    limit=5,
    filters=wvc.query.Filter.by_property("key").equal("20130014470"),
    return_metadata=MetadataQuery(distance=True)
)
```
And get the following return:
```
{'key': '20130014470', 'page': 253.0, 'chunk': 'Mass: The total mass at launch was 1,964.6 pounds (891 kg), consisting of 1,290 pounds (585 kg) for the spacecraft and 674.6 pounds (306 kg) of hydrazine fuel.'}
0.21913838386535645
{'key': '20130014470', 'page': 258.0, 'chunk': 'low cost (< $80M), less than 1000 kg, kinetic impactor that would excavate water ice from the Moon, if it were present.\nThe program office noted that if the project were to breach $79M, weigh more than 1000 kg, or fail to meet schedule with the launch of LRO, it would be subject to a termination review.'}
0.26032769680023193
{'key': '20130014470', 'page': 18.0, 'chunk': 'If the Moon has water ice in sufficient quantities, it would represent a very compelling rationale for future exploration and lunar outposts could be located in the vicinity of this invaluable resource.\nWater ice, after all, could be converted to consumable water, breathable oxygen, and rocket fuel, and potentially even serve as a means for construction when combined with regolith or as shielding from solar radiation.\nDelivering mass to the moon is incredibly expensive and water is very heavy for a small volume.\nDelivering a ½ liter bottle of water to the Moon is projected to cost a minimum of $15,000 by weight.\nTherefore, having this resource available in situ to future explorers and inhabitants of the Moon is clearly worth investigating.'}
0.28107452392578125
```

# Local Instance

Another good reason to use Weaviate is that they provide a docker container loaded with the same product that they host. You can run this locally for prototyping, or host it privately if you have constraints that keep you from using their hosted version.

To run with docker:
```bash
 docker run -p 8080:8080 -p 50051:50051 cr.weaviate.io/semitechnologies/weaviate:1.25.5
 ```

 To connect to the local instance, you just change the connection call for the client:

 ```python
 client = weaviate.connect_to_local()
 ```
There are a lot of available configurations, modules that can be loaded, and options for securing the instance.

# More information

[Weaviate Quickstart Guide](https://weaviate.io/developers/weaviate/quickstart)