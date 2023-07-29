
import json
from typing import Any
import pytest
from config import settings
import asyncio
import aiohttp
import requests
import responses

from net_hawk_poc.api import fetch




json_data = {}

class AsyncMock:
    async def __aenter__(self):
        return self

    async def __aexit__(self, *error_info):
        return self

    async def json(self):
        return json_data
    

@pytest.mark.asyncio
async def test_fetch_return_json(monkeypatch):
    
    
    # mock function must respect signature of original function
    def mock_client_get(url, allow_redirects: bool = True, **kwargs: Any):
        mock_response = AsyncMock()
        mock_response.status = 200

        return mock_response

    monkeypatch.setattr("aiohttp.ClientSession.get", mock_client_get)

    async with aiohttp.ClientSession() as session:
        actual = await fetch(session, settings.host)

        assert actual[0] == 200
        assert isinstance(actual[1], dict)
        
    
