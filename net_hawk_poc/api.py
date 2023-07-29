import asyncio
from aiohttp import BasicAuth, ClientResponse, ClientSession
import requests
from config import settings


headers = {'Content-Type': 'application/yang-data+json',
               'Accept': 'application/yang-data+json'}

async def fetch(session: ClientSession, url):
    basic_auth = BasicAuth(settings.USERNAME, settings.PASSWORD)
    
    response: ClientResponse
    async with session.get(url, auth=basic_auth, headers=headers, ssl=False) as response:
        return (response.status, await response.json())


def sync_fetch(session: requests.Session, url):
    return session.get(url, auth=(settings.USERNAME, settings.PASSWORD), headers=headers, verify=False).json()
