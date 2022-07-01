"""Config class"""
import platform
from dataclasses import dataclass


@dataclass
class Config:
    """Default config object for flask"""

    PORT = "/dev/ttyUSB0"
    if platform.system() == "Windows":  # pragma: no cover
        PORT = "COM3"

    TESTING = False
    DEBUG = False
    CACHE_TYPE = "SimpleCache"
    CACHE_DEFAULT_TIMEOUT = 3600
    SECRET_KEY = "sadfbiytOybbsadfn"
