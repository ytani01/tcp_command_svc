import datetime
import click
from tcp_command_svc import CmdServer, get_logger

# ロガーの初期化
log = get_logger(__name__, debug=True)

# --- 独自のコマンドを実装する ---
# argsはコマンドラインをスペースで分割したリスト。
# 例: "MYCMD 123" -> ['MYCMD', '123']

def cmd_reverse(args):
    """引数を逆順にして返すコマンド"""
    log.debug(f"args={args}")
    if len(args) < 2:
        return "NG missing argument"
    
    # 最初の要素はコマンド名なので、それ以降を処理
    reversed_arg = args[1][::-1]
    return f"OK {reversed_arg}"

def cmd_status(args):
    """サーバーのステータスを返すコマンド"""
    log.debug(f"args={args}")
    return "OK server is running"

def cmd_echo(args):
    log.debug(f"args={args}")
    return 'OK ' + ' '.join(args[1:])

def cmd_now(args):
    log.debug(f"args={args}")
    if len(args) != 1:
        return 'NG'

    s = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    return 'OK ' + s

@click.command()
@click.option('--port', default=54321, help='Port to listen on.')
def main(port):
    # CmdServerを初期化
    server = CmdServer(port=port, debug=True)

    # 作成したコマンドをサーバーに登録
    server.add_cmd("REVERSE", cmd_reverse)
    server.add_cmd("STATUS", cmd_status)
    server.add_cmd("ECHO", cmd_echo)
    server.add_cmd("NOW", cmd_now)

    log.info("My custom server starting...")
    try:
        # サーバーを起動
        server.serve_forever()
    except KeyboardInterrupt:
        log.info("Server stopped.")

if __name__ == '__main__':
    main()