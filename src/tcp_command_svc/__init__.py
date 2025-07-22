from importlib.metadata import version
  
__version__ = version(__package__)

def hello() -> str:
    return "Hello from tcp-command-svc!"
