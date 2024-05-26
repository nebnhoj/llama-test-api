import os
from multiprocessing import Lock
from multiprocessing.managers import BaseManager
from llama_index.core import  SummaryIndex
from llama_index.readers.mongodb import SimpleMongoReader
from llama_index.core import Settings
from llama_index.llms.ollama import Ollama
import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))
# NOTE: for local testing only, do NOT deploy with your key hardcoded
os.environ["OPENAI_API_KEY"] ="" 

index = None
lock = Lock()
# NOTE: for local testing only, do NOT deploy with your key hardcoded
uri = ""
#Open AI API key
 #db name
db_name = "house"
#collection
collection_name = "budget"
# query_dict is passed into db.collection.find()
query_dict = {}
#fields
field_names = ["name","price"]
index = None
Settings.llm = Ollama(model="llama3", request_timeout=60.0)

def initialize_index():
    global index
    reader = SimpleMongoReader(uri=uri)
    documents = reader.load_data(
        db_name, collection_name, field_names, query_dict=query_dict
    )


    index = SummaryIndex.from_documents(documents)
    pass


def query_index(query_text):
    global index
    query_engine = index.as_query_engine()
    response = query_engine.query(query_text)
    return str(response)


if __name__ == "__main__":
    print("initializing index...")
    initialize_index()

    manager = BaseManager(("", 5602), b"password")
    manager.register("query_index", query_index)
    server = manager.get_server()

    print("starting server...")
    server.serve_forever()