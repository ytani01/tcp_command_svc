import pytest
import subprocess
import time
import os
import signal
import sys
import re
from tcp_command_svc import CmdClient

SERVER_HOST = 'localhost'
SERVER_PORT = 54322  # Use a different port for testing
SERVER_STARTUP_WAIT = 2  # seconds

@pytest.fixture(scope="module")
def custom_server():
    """Fixture to start and stop the custom server for tests."""
    server_process = None
    try:
        # Construct the absolute path to custom_server.py
        server_script_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'samples', 'custom_server.py'))

        # Start the server in the background using the current Python executable
        server_process = subprocess.Popen(
            [sys.executable, server_script_path, '--port', str(SERVER_PORT)],
            preexec_fn=os.setsid,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        # Wait for the server to start up
        time.sleep(SERVER_STARTUP_WAIT)
        # Check if the server process is still alive
        if server_process.poll() is not None:
            stdout, stderr = server_process.communicate()
            raise Exception(f"Server exited prematurely. Stdout: {stdout.decode()}, Stderr: {stderr.decode()}")

        yield  # Yield control to the tests

    except Exception as e:
        pytest.fail(f"Failed to start server: {e}")

    finally:
        if server_process:
            # Terminate the process group
            os.killpg(os.getpgid(server_process.pid), signal.SIGTERM)
            try:
                server_process.wait(timeout=5)  # Wait for a few seconds for it to terminate
            except subprocess.TimeoutExpired:
                # If it doesn't terminate, force kill
                os.killpg(os.getpgid(server_process.pid), signal.SIGKILL)
                server_process.wait()

def test_hello_command(custom_server):
    """Test sending a HELLO command to the custom server."""
    client = CmdClient(svr_host=SERVER_HOST, svr_port=SERVER_PORT)
    response = client.call('HELLO')
    assert response == 'OK HELLO'

def test_echo_command(custom_server):
    """Test sending an ECHO command to the custom server."""
    client = CmdClient(svr_host=SERVER_HOST, svr_port=SERVER_PORT)
    response = client.call('ECHO test message')
    assert response == 'OK test message'

def test_mycmd_with_argument(custom_server):
    """Test sending a MYCMD command with an argument to the custom server."""
    client = CmdClient(svr_host=SERVER_HOST, svr_port=SERVER_PORT)
    response = client.call('MYCMD argument')
    assert response == 'OK tnemugra'

def test_mycmd_without_argument(custom_server):
    """Test sending a MYCMD command without an argument to the custom server."""
    client = CmdClient(svr_host=SERVER_HOST, svr_port=SERVER_PORT)
    response = client.call('MYCMD')
    assert response == 'NG missing argument'

def test_status_command(custom_server):
    """Test sending a STATUS command to the custom server."""
    client = CmdClient(svr_host=SERVER_HOST, svr_port=SERVER_PORT)
    response = client.call('STATUS')
    assert response == 'OK server is running'

def test_now_command(custom_server):
    """Test sending a NOW command to the custom server."""
    client = CmdClient(svr_host=SERVER_HOST, svr_port=SERVER_PORT)
    response = client.call('NOW')
    # Check if the response starts with 'OK ' and matches a datetime pattern
    assert response.startswith('OK ')
    # Example pattern: OK 2023-10-27 10:00:00.123456
    datetime_pattern = r'^OK \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}$'
    assert re.match(datetime_pattern, response)

def test_now_command_with_extra_argument(custom_server):
    """Test sending a NOW command with an extra argument to the custom server."""
    client = CmdClient(svr_host=SERVER_HOST, svr_port=SERVER_PORT)
    response = client.call('NOW extra_arg')
    assert response == 'NG'
