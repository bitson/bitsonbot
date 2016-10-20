#! /usr/bin/env python
# -*- coding:utf-8 -*-

# Standard lib imports
import logging.handlers
import sys
import time
# Third Party imports
from rainbow_logging_handler import RainbowLoggingHandler
# BITSON imports

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

log_format = "".join(["[%(asctime)s] %(levelname)8s: ",
                      "%(message)s"])

formatter = logging.Formatter(fmt=log_format)
# Format UTC Time
formatter.converter = time.gmtime

# Console Handler
ch = RainbowLoggingHandler(sys.stderr)
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)
