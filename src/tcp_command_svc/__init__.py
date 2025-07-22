#
# Copyright (c) 2023 Yoichi Tanibayashi
#
from importlib.metadata import version

__version__ = version(__package__)

from .cmd_server import CmdServer
from .sample_server import cmdserver
from .cmd_client import CmdClient
from .my_logger import get_logger

__all__ = [
    __version__,
    'CmdServer',
    'cmdserver',
    'CmdClient',
    'get_logger'
]
