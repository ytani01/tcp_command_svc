
import pytest
import subprocess
import time
import os
import signal
from tcp_command_svc import CmdClient

SERVER_HOST = 'localhost'
SERVER_PORT = 54321  # Use a different port for testing
SERVER_STARTUP_WAIT = 2  # seconds

@pytest.fixture(scope="module")
def server():
    """Pytest fixture to start and stop the server."""
    server_process = None
    try:
        # Start the server in the background
        server_process = subprocess.Popen(
            ['uv', 'run', 'python', 'samples/custom_server.py'],
            preexec_fn=os.setsid
        )
        time.sleep(SERVER_STARTUP_WAIT)
        yield
    finally:
        if server_process:
            os.killpg(os.getpgid(server_process.pid), signal.SIGTERM)
            server_process.wait()

def test_hello_command(server):
    """Test sending a HELLO command to the server."""
    client = CmdClient(svr_host=SERVER_HOST, svr_port=SERVER_PORT)
    response = client.call('HELLO')
    assert response == 'OK HELLO'

def test_echo_command(server):
    """Test sending an ECHO command to the server."""
    client = CmdClient(svr_host=SERVER_HOST, svr_port=SERVER_PORT)
    response = client.call('ECHO test message')
    assert response == 'OK test message'
