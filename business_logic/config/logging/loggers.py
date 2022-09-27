import logging.handlers

from business_logic.config.logging.logging_properties import log_folder, logger_types, log_format_date


def setup_logger(logger_name: str):
    """[Sets up the logger with parameters from logging_properties]

    Args:
        logger_name (str): [Logger name to be setup. If listed in
        logging_properties.logger_types, those properties will be used.
        Else, "main" properties will apply]
    """
    api_logger = logging.getLogger(logger_name)

    log_name = log_folder + logger_types[logger_name]['log_file']
    api_file_handler = logging.handlers.WatchedFileHandler(
        filename=log_name)

    logger_properties = logger_types.get(
        logger_name,
        logger_types['main'])

    api_logger.setLevel(level=logger_properties['log_level'])

    api_log_formatter = logging.Formatter(
        fmt=logger_properties['log_format'],
        datefmt=log_format_date)
    api_file_handler.setFormatter(api_log_formatter)
    api_logger.addHandler(api_file_handler)


def get_logger(logger_name: str) -> logging.Logger:
    """[Returns the requested logger or the main logger if "logger_name"
    is not defined in logging_properties. The returned logger is aleady setup]

    Args:
        logger_name (str): [Name of the pre-defined logger to be returned]

    Returns:
        logging.Logger: [Python logger with the requested name, already setup.]
    """
    if logger_name in logger_types.keys():
        return logging.getLogger(logger_name)
    else:
        return logging.getLogger('main')


for logger_type in logger_types.keys():
    setup_logger(logger_type)
