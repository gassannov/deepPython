import sys
from collections import deque
import logging.config
import logging


LOGG_CONFIG = {
    'version': 1,
    'formatters': {
        'command_line': {
            'format': '[%(levelname)s] - %(message)s',
        },
        'log_file': {
            'format': '%(asctime)s\t%(name)s\t%(levelname)s\t%(message)s',
        },
        'debug_log_file': {
            'format': '[%(levelname)s] - %(message)s',
        },
    },
    'handlers': {
        'log_file': {
            'filename': 'lru_logging.log',
            'class': 'logging.FileHandler',
            'formatter': 'log_file',
        },
        'command_line': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'command_line',
        },
        'debug_log_file': {
            'filename': 'debug_lru_logging.log',
            'class': 'logging.FileHandler',
            'formatter': 'debug_log_file',
        },
    },
    'loggers': {
        'command_line': {
            'level': 'INFO',
            'handlers': ['log_file', 'command_line'],
        },
        'logger_file': {
            'level': 'INFO',
            'handlers': ['log_file'],
        },
        'debug_logger_file': {
            'level': 'DEBUG',
            'handlers': ['debug_log_file'],
        },
    },
}


class LRUCache:
    def __init__(self, logger: logging.Logger, limit=42):
        self.limit = limit
        self.dict_lru = {}
        self.deque_lru = deque()
        self.logger = logger

    def get(self, key):
        if key in self.deque_lru:
            self.deque_lru.remove(key)
            self.deque_lru.append(key)
            self.logger.info(f'for key: {key} found value: {self.dict_lru[key]}')
            return self.dict_lru[key]
        self.logger.error(f'key: {key} not in lru')
        return None

    def set(self, key, value):
        self.deque_lru.append(key)
        self.logger.debug(key)
        if len(self.deque_lru) > self.limit:
            removed = self.deque_lru.popleft()
            self.logger.info(f'for set [key: {key} value: {value}] reach limit: {self.limit}; key: {removed} remove')
            del self.dict_lru[removed]
            self.logger.debug(f'removed in dict (excpected False): {removed in self.dict_lru}')
        self.dict_lru[key] = value
        self.logger.info(f'set [key: {key} value: {value}]: len lru cache: {len(self.deque_lru)}; limit: {self.limit}')


if __name__ == '__main__':
    FILENAME = 'lru_logging.log'

    logging.config.dictConfig(LOGG_CONFIG)
    if len(sys.argv) > 1 and '-s' in sys.argv:
        if '-s' in sys.argv:
            logger = logging.getLogger('command_line')
        elif '-d' in sys.argv:
            logger = logging.getLogger('debug_logger_file')
    else:
        logger = logging.getLogger('logger_file')

    cache = LRUCache(logger=logger, limit=2)
    cache.set('k1', 'val1')  # set отсутствующего ключа
    cache.set('k2', 'val2')  # set отсутствующего ключа
    cache.set('k3', 'val3')  # set отсутствующего ключа, когда достигнута ёмкость
    k1_value = cache.get('k1')  # get существующего ключа
    k2_value = cache.get('k2')  # get существующего ключа
    not_found_value = cache.get('k5')  # get отсутствующего ключа
