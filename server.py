############## Packages
from langchain.chat_models import AzureChatOpenAI
from langchain.prompts import PromptTemplate
from fastapi import FastAPI
from langserve import add_routes
from dotenv import load_dotenv
from langserve import add_routes
from langchain.prompts import ChatPromptTemplate
import openai  
import os
#############
os.environ["OPENAI_API_TYPE"]       = ""
os.environ["OPENAI_API_BASE"]       = ""
os.environ["OPENAI_API_KEY"]        = ""
os.environ["OPENAI_API_VERSION"]    = ""
openai.api_type     = os.environ["OPENAI_API_TYPE"]
openai.api_base     = os.environ["OPENAI_API_BASE"]
openai.api_key      = os.environ["OPENAI_API_KEY"] 
openai.api_version  = os.environ["OPENAI_API_VERSION"]

llm= AzureChatOpenAI(deployment_name='' , verbose=False , temperature=0)

 
app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="Spin up a simple api server using Langchain's Runnable interfaces",
)

add_routes(
    app,
    llm,
    path="/openai",
)


prompt=ChatPromptTemplate.from_template("provide me an essay about {topic}")
prompt1=ChatPromptTemplate.from_template("provide me a poem about {topic}")

add_routes(
    app,
    prompt|llm,
    path="/essay"

)

add_routes(
    app,
    prompt1|llm,
    path="/poem"

)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)