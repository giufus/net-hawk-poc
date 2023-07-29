import asyncio
import aiohttp
import timeit

import requests
from net_hawk_poc.api import fetch, sync_fetch
from config import settings



async def main():

    async with aiohttp.ClientSession() as session:
        tasks = asyncio.gather(
            fetch(session, f'https://{settings.HOST}/restconf/data/ietf-interfaces:interfaces'),
            fetch(session, f'https://{settings.HOST}/restconf/data/ietf-interfaces:interfaces'),
            fetch(session, f'https://{settings.HOST}/restconf/data/ietf-interfaces:interfaces'),
            return_exceptions=True,
        )
    
        print(await tasks)

def sync_main():
    session = requests.Session()
    print([sync_fetch(session, f'https://{settings.HOST}/restconf/data/ietf-interfaces:interfaces') for i in range(3)])

if __name__ == "__main__":
    
    start = timeit.default_timer()
    asyncio.run(main())
    stop = timeit.default_timer()

    print(f"Async Program Executed in {stop - start}")

    """      
    start = timeit.default_timer()
    sync_main()
    stop = timeit.default_timer()

    print(f"Sync Program Executed in {stop - start}") """
 


