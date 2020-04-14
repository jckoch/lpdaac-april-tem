from concurrent.futures import ProcessPoolExecutor
from common import util

LOGGER = util.get_logger()
MAX_THREADS = 10
TEST_URL = 'https://lpdaac.usgs.gov/'


def _sum(*args):
    LOGGER.info(f'adding {args[0]} ...')
    return sum(*args)


def main():
    sum_inputs = [(1, 2), (3, 4)]
    all_sums = []

    with ProcessPoolExecutor() as pool:
        # the process pool creates N number of Python interp processes
        # where Ni s the number of available CPUs

        # parallel calculation by mapping
        for s in pool.map(_sum, sum_inputs):
            all_sums.append(s)

    # sum of the sums
    total = sum(all_sums)
    LOGGER.info(f'total = {total}')


if __name__ == '__main__':
    main()
