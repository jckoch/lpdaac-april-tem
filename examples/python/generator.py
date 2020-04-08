from common import util

LOGGER = util.get_logger()

RANGE_END = 5


def gen():
    for i in range(RANGE_END):
        LOGGER.info(f'yielding the value...')
        yield i


g = gen()
# g is a generator object
LOGGER.info(g)

# iterate through it twice
LOGGER.info(next(g))
LOGGER.info(next(g))

# consume the rest of it
for i in g:
    LOGGER.info(i)


g = (i for i in range(RANGE_END))
# g is a generator expression
LOGGER.info(g)

# iterate through it twice
LOGGER.info(next(g))
LOGGER.info(next(g))

# consume the rest of it
for i in g:
    LOGGER.info(i)
