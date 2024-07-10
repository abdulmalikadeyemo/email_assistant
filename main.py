from fastapi import FastAPI
from langserve import add_routes


from graph import graph_app

app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple api server using Langchain's Runnable interfaces",
)

add_routes(
    app,
    graph_app
)
