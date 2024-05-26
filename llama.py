import logging
import sys

from llama_index.llms.ollama import Ollama
from llama_index.core import Settings
from llama_index.core import SummaryIndex
from llama_index.readers.mongodb import SimpleMongoReader
from IPython.display import Markdown, display
import os

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))


#mongodb config
uri = ""
#Open AI API key
os.environ["OPENAI_API_KEY"] ="" 
#LLM settings
Settings.llm = Ollama(model="llama3", request_timeout=60.0)

#db name
db_name = "house"
#collection
collection_name = "budget"
# query_dict is passed into db.collection.find()
query_dict = {}
#fields
field_names = ["name","price"]
#reader
reader = SimpleMongoReader(uri=uri)
documents = reader.load_data(
    db_name, collection_name, field_names, query_dict=query_dict
)


index = SummaryIndex.from_documents(documents)
query_engine = index.as_query_engine()
response = query_engine.query("categorize the budget base on expense data? and convert everything to peso use current conversion of euro and php")
print(response)

