"""Config class"""
from dataclasses import dataclass
import platform


@dataclass
class Config(object):
    """Default config object for flask"""

    PORT = "/dev/ttyUSB0"
    if platform.system() == "Windows":  # pragma: no cover
        PORT = "COM3"

    TESTING = False
    DEBUG = False
    CACHE_TYPE = "SimpleCache"
    CACHE_DEFAULT_TIMEOUT = 3600
    SECRET_KEY = "sadfbiytOybbsadfn"
