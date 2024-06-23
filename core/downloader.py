import asyncio
import aiohttp

async def download_smart_contract(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status != 200:
                raise Exception(f"Failed to download smart contract from {url}. Status code: {response.status}")
            return await response.text()
