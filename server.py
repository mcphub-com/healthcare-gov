import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/community/api/healthcare-gov'

mcp = FastMCP('healthcare-gov')

@mcp.tool()
def content_objects(post_title: Annotated[str, Field(description='')]) -> dict: 
    '''Content objects: the body content and metadata for each post on this website'''
    url = 'https://community-healthcaregov.p.rapidapi.com/what-is-the-health-insurance-marketplace.json'
    headers = {'x-rapidapi-host': 'community-healthcaregov.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'post-title': post_title,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def content_collections(content_type: Annotated[str, Field(description='')]) -> dict: 
    '''Collections are a list of post objects by content type. The following content types are available: articles, blog, questions, glossary, states, and topics.'''
    url = 'https://community-healthcaregov.p.rapidapi.com/api/glossary.json'
    headers = {'x-rapidapi-host': 'community-healthcaregov.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'content-type': content_type,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def content_index() -> dict: 
    '''The index is an abridged list of metadata for all posts on this website. Use it to get an aggregate view of content and to generate additional queries of post objects.'''
    url = 'https://community-healthcaregov.p.rapidapi.com/api/index.json'
    headers = {'x-rapidapi-host': 'community-healthcaregov.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
