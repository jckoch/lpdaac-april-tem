import asyncio
import aiohttp
from common import util

LOGGER = util.get_logger()
DOWNLOADS = [
    {'file_name': 'node-v10.16.3-linux-x64.FILE_1.tar.gz', 'url': 'https://nodejs.org/download/release/v10.16.3/node-v10.16.3-linux-x64.tar.gz'},
    {'file_name': 'node-v10.16.3-linux-x64.FILE_2.tar.gz', 'url': 'https://nodejs.org/download/release/v10.16.3/node-v10.16.3-linux-x64.tar.gz'},
    {'file_name': 'node-v10.16.3-linux-x64.FILE_3.tar.gz', 'url': 'https://nodejs.org/download/release/v10.16.3/node-v10.16.3-linux-x64.tar.gz'}
]
# chunk size in bytes
DOWNLOAD_CHUNK_SIZE = 1024 * 1024 * 10  # 10 MB


async def _download_file(url, file_path):
    LOGGER.info(f'downloading {url} as {file_path} ...')
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            with open(file_path, 'wb') as f:
                while True:
                    LOGGER.info(f'getting {DOWNLOAD_CHUNK_SIZE} B chunk for {file_path} ...')
                    chunk = await response.content.read(DOWNLOAD_CHUNK_SIZE)
                    if not chunk:
                        break
                    f.write(chunk)
                LOGGER.info('file written')


async def main():
    tasks = (
        _download_file(item['url'], item['file_name'])
        for item in DOWNLOADS
    )
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
