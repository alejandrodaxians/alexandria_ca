import logging


log_folder = '../../../logs'

log_format_string = "[%(asctime)s] %(levelname)s %(name)s \
                     [%(funcName)s] - %(message)s"

log_format_date = "%Y-%m-%d %H:%M:%S"

logger_types = {
    'database': {
        'log_level': logging.DEBUG,
        'log_file': 'database.log',
        'log_format': log_format_string
    },
    'main': {
        'log_level': logging.DEBUG,
        'log_file': 'main.log',
        'log_format': log_format_string
    }
}
