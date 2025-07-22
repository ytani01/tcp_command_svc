import click
from tcp_command_svc import CmdClient

@click.command()
@click.argument('command', nargs=-1, required=True)
@click.option('--host', default='localhost', help='Server host.')
@click.option('--port', default=54321, help='Server port.')
@click.option('--debug', '-d', 'dbg', is_flag=True, default=False, help='Debug flag.')
def main(command, host, port, dbg):
    """Sends a command to the TCP Command Server."""
    cmd_line = " ".join(command)
    if not cmd_line:
        print("Error: No command provided.")
        return

    client = CmdClient(svr_host=host, svr_port=port, dbg=dbg)
    
    print(f"Sending: '{cmd_line}'")
    response = client.call(cmd_line)
    print(f"Response: {response}")

if __name__ == '__main__':
    main()