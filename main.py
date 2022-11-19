"""
Entry point to application
"""
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def root():
    """
    Entry point to application
    """
    return {'hello': 'world'}
