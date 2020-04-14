import requests
from functools import partial
from concurrent.futures import ThreadPoolExecutor
from common import util

LOGGER = util.get_logger()
MAX_THREADS = 10
TEST_URL = 'https://lpdaac.usgs.gov/'


def _get_url_info(url):
    # simply get the response headers
    resp = requests.get(url)
    return resp.headers


def _future_done(thread_num, fut):
    LOGGER.info(f'Future {fut} on thread {thread_num} is complete.')


def main():
    thread_pool = ThreadPoolExecutor(MAX_THREADS)

    # submit work to the pool
    scheduled_workers = []
    for thread in range(0, MAX_THREADS):
        worker = thread_pool.submit(_get_url_info, TEST_URL)
        # attach a callback to this Future
        worker.add_done_callback(partial(_future_done, thread))

        scheduled_workers.append(worker)

    # get the results back
    for worker in scheduled_workers:
        LOGGER.info(worker.result())


if __name__ == '__main__':
    main()
