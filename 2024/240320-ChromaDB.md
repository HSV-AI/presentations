![HSV-AI Logo](https://hsv.ai/wp-content/uploads/2022/03/logo_v11_2022.png)

# Welcome

- Vision
- Mission
- How to Connect - [Signup](https://hsv.ai/subscribe)

# ChromaDB

After we built our SpaceApps application, there was a large shift in the AI space for products that help with creating, storing, and querying embeddings. These include:
- ChromaDB
- PineCone
- FAISS (Facebook AI Similarity Search)

And other traditional databases began to add a similar capability, such as PostgreSQL

For our application, we're going with ChromaDB initially because it's very easy to work with and provides both a direct implementation and a client-server approach. This lets us easily test with the ~500 documents we currently use, but we can scale up to the full set of NASA documents by splitting the ChromaDB off as its own server.

# Super Duper Easy

```bash
pip install chromadb
```

```python
# Import ChromaDB
import chromadb

# Create the client (either local or connect to server)
chroma_client = chromadb.Client()

# Create a collection, or get a collection, or both
collection = chroma_client.create_collection(name="my_collection")

# Add some documents. You can also replace existing,
# or upsert to create or replace.
collection.add(
    documents=["This is a document", "This is another document"],
    metadatas=[{"source": "my_source"}, {"source": "my_source"}],
    ids=["id1", "id2"]
)

# If you already have embeddings (which we do) 
# you can just add them directly
collection.add(
    embeddings=[[1.2, 2.3, 4.5], [6.7, 8.2, 9.2]],
    documents=["This is a document", "This is another document"],
    metadatas=[{"source": "my_source"}, {"source": "my_source"}],
    ids=["id1", "id2"]
)

# Then later on, you can query the database to find documents that are closest.
results = collection.query(
    query_texts=["This is a query document"],
    n_results=2
)
```

In our case, the query is also sent as an embedding. The requirement is that the documents in the database and the query all have to use the same embedding approach.

For embeddings, we using SentenceTransformer with the [BAAI/bge-small-en-v1.5](https://huggingface.co/BAAI/bge-small-en-v1.5) model.

You can also change the distance function used. The default is "l2" which is the squared L2 norm.

- Squared L2	'l2'	$d = \sum\left(A_i-B_i\right)^2$
- Inner product	'ip'	$d = 1.0 - \sum\left(A_i \times B_i\right) $
- Cosine similarity	'cosine'	$d = 1.0 - \frac{\sum\left(A_i \times B_i\right)}{\sqrt{\sum\left(A_i^2\right)} \cdot \sqrt{\sum\left(B_i^2\right)}}$

Another thing I learned after getting ChromaDB integrated is that it sends anonymous usage statistics back to its own server. You can turn this off by:

```python
from chromadb.config import Settings
client = chromadb.Client(Settings(anonymized_telemetry=False))
```

# Performance

So far, I don't have a lot of data to work with, but I am seeing that queries and upserts are taking on the order of 10~20ms.