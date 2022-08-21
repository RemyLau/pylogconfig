import logging

from pylogconfig import pylogconfig


def test_config_logger_from_dict(capsys):
    config_dict = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "Formatter": {
                "format": "[%(levelname)s][%(name)s] %(message)s",
            },
        },
        "handlers": {
            "ConsoleHandler": {
               "class": "logging.StreamHandler",
               "level": "DEBUG",
               "formatter": "Formatter",
            },
        },
        "loggers": {
            "ConsoleLogger": {
               "level": "INFO",
               "handlers": ["ConsoleHandler"],
               "propagate": False,
            },
        },
    }

    pylogconfig.config_logger(config_dict)
    logger = logging.getLogger("ConsoleLogger")

    # TODO: test more levels
    logger.info("something")
    captured = capsys.readouterr()
    assert "[INFO][ConsoleLogger] something\n" == captured.err
