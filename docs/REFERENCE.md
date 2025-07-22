# TCP Command Service ライブラリ リファレンス

このドキュメントは、`tcp_command_svc` Python ライブラリのリファレンスを提供する。

## `CmdServer` クラス

`CmdServer` は、クライアントからのコマンドラインリクエストを処理するマルチスレッドTCPサーバー。

### `__init__(self, port=54321, debug=False)`

`CmdServer` を初期化する。

*   **`port`** (`int`, オプション): リッスンするポート番号。デフォルトは `54321`。
*   **`debug`** (`bool`, オプション): `True` の場合、デバッグログを有効にする。デフォルトは `False`。

### `add_cmd(self, cmd_name, func)`

サーバーに新しいコマンドを登録する。

*   **`cmd_name`** (`str`): コマンド名（例: "ECHO", "REVERSE"）。
*   **`func`** (`callable`): コマンドが受信されたときに呼び出される関数。この関数は、コマンドとその引数を表す文字列のリスト（例: `['ECHO', 'メッセージ']`）を1つの引数として受け取る。文字列の応答を返す。

### `cmd_hello(self, args)`

デフォルトコマンド: 挨拶メッセージを返す。

*   **`args`** (`list` of `str`): コマンド引数。

### `cmd_commands(self, args)`

デフォルトコマンド: 登録されているすべてのコマンドをカンマ区切りのリストで返す。

*   **`args`** (`list` of `str`): コマンド引数。追加の引数は期待されない。

## `CmdClient` クラス

`CmdClient` は、`CmdServer` にコマンドを送信するためのTCPクライアント。

### `__init__(self, svr_host='localhost', svr_port=54321, debug=False)`

`CmdClient` を初期化する。

*   **`svr_host`** (`str`, オプション): サーバーのホスト名またはIPアドレス。デフォルトは `'localhost'`。
*   **`svr_port`** (`int`, オプション): サーバーのポート番号。デフォルトは `54321`。
*   **`debug`** (`bool`, オプション): `True` の場合、デバッグログを有効にする。デフォルトは `False`。

### `call(self, msg)`

サーバーにコマンドメッセージを送信し、応答を返す。

*   **`msg`** (`str`): 送信するコマンドメッセージ（例: "ECHO hello world"）。
*   **戻り値**: (`str`) サーバーの応答。

## `get_logger` 関数

`get_logger(name, debug=False)`

指定された名前のロガーインスタンスを取得する。

*   **`name`** (`str`): ロガーの名前。
*   **`debug`** (`bool` または `int`, オプション): `True` の場合、ログレベルを `DEBUG` に設定する。`int` の場合、ログレベルを指定された整数値に設定する。デフォルトは `False` （INFOレベル）。
*   **戻り値**: (`logging.Logger`) ロガーインスタンス。
