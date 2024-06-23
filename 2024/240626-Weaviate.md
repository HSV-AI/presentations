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


# Inserting Data Objects

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


[Quickstart](https://weaviate.io/developers/weaviate/quickstart)