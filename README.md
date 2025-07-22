# TCP Command Service

TCP/IPソケット通信を介して、シンプルなコマンドのやり取りを行うためのサーバーおよびクライアント機能を提供するPythonパッケージです。

## 機能

*   **コマンドサーバー**:
    *   指定したTCPポートでクライアントからの接続を待ち受けます。
    *   受信したコマンドラインを解析し、登録されたコマンドを実行します。
    *   コマンドの実行結果をクライアントに返します。
    *   `socketserver.ThreadingTCPServer` を利用しており、複数のクライアント接続を同時に処理できます。
    *   新しいコマンドを簡単に追加できる仕組みを提供します。
*   **コマンドクライアント**:
    *   指定したホストとポートのコマンドサーバーに接続します。
    *   コマンドライン文字列をサーバーに送信し、結果を受け取ります。

## インストール

リポジトリをクローンし、pipでインストールします。

```bash
git clone https://github.com/your_username/tcp_command_svc.git
cd tcp_command_svc
pip install .
```

## 使い方

### サーバーの起動

このパッケージにはサンプルサーバーが含まれています。以下のコマンドでサーバーを起動できます。
デフォルトではポート`54321`で待ち受けます。

```bash
python -m tcp_command_svc.sample_server
```

別のポートを指定する場合:

```bash
python -m tcp_command_svc.sample_server --port 12345
```

### クライアントからのコマンド実行

`CmdClient`を使用してサーバーにコマンドを送信します。
以下はPythonの対話モードでの実行例です。

```python
from tcp_command_svc import CmdClient

# サーバーに接続するクライアントを作成
client = CmdClient(svr_host='localhost', svr_port=54321)

# "HELLO"コマンドを送信
response = client.call("HELLO")
print(response)
# 出力例: OK HELLO

# サンプルサーバーの"ECHO"コマンドを送信
response = client.call("ECHO Hello World")
print(response)
# 出力例: OK Hello World

# サンプルサーバーの"NOW"コマンドを送信
response = client.call("NOW")
print(response)
# 出力例: OK 2023-10-27 10:00:00.123456
```

## ライブラリとして利用する (コマンドの追加方法)

`CmdServer`をインスタンス化し、`add_cmd()`メソッドを使用することで、独自のコマンドを簡単に追加できます。

詳細な実装例については、`samples`ディレクトリ内のファイルを参照してください。

*   **サーバー側の実装例:** [`samples/custom_server.py`](./samples/custom_server.py)
*   **クライアント側の実装例:** [`samples/custom_client.py`](./samples/custom_client.py)

これらのサンプルを実行するには、まずサーバーを起動します。

```bash
python samples/custom_server.py
```

次に、別のターミナルでクライアントを実行します。

```bash
python samples/custom_client.py
```

## 依存ライブラリ

*   [click](https://click.palletsprojects.com/)

## ライセンス

このプロジェクトは **MIT** ライセンスのもとで公開されています。
詳細は `LICENSE` ファイルを参照してください。
