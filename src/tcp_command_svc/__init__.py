#
# Copyright (c) 2023 Yoichi Tanibayashi
#
from importlib.metadata import version

__version__ = version(__package__)

from .cmd_server import CmdServer
from .cmd_client import CmdClient
from .my_logger import get_logger

__all__ = [
    __version__,
    'CmdServer',
    'CmdClient',
    'get_logger'
]
