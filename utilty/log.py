import logging.config
import os
from structlog import configure, processors, stdlib, threadlocal

# Disable Django's logging setup
LOGGING_CONFIG = None

LOGLEVEL = '{{log_level}}'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'json': {
            'class': 'conf.json_logger.CustomJsonLogger',
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'json',
        },
        'logfile': {
            'level': LOGLEVEL,
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'alps_orchestration.log'),
            'maxBytes': 1024 * 1024 * 10,
            'backupCount': 0,
            'formatter': 'json',
        },
    },
    'loggers': {
        'apps': {
            'level': LOGLEVEL,
            'handlers': ['console', 'logfile'],
            'propagate': False
        }
    }
})
configure(
    context_class=threadlocal.wrap_dict(dict),
    logger_factory=stdlib.LoggerFactory(),
    wrapper_class=stdlib.BoundLogger,
    processors=[
        stdlib.filter_by_level,
        stdlib.add_logger_name,
        stdlib.add_log_level,
        stdlib.PositionalArgumentsFormatter(),
        processors.TimeStamper(fmt="iso"),
        processors.StackInfoRenderer(),
        processors.format_exc_info,
        processors.UnicodeDecoder(),
        stdlib.render_to_log_kwargs
    ]
)