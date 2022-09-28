import subprocess
from flask import Flask, request, jsonify
from flask_sse import sse


class Server(object):
    def __init__(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(sse, url_prefix="/stream")

        @self.app.route("/create", methods=["POST"])
        def postUser():
            request_data = request.get_json()
            if not request_data["url"]:
                return "Bad Request!"
            try:
                self.initPKC(request_data["url"])
                return "ok"
            except Exception as e:
                return str(e)

    def initPKC(self, url):
        command = ("python3 extension.py " + url).split()

        p = subprocess.Popen(
            command,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
        )
        stdout, stderr = p.communicate()

        if p.returncode == 0:
            return True
        else:
            return stderr


if __name__ == "__main__":
    from waitress import serve

    server = Server()
    serve(server.app, host="127.0.0.1", port=5000)
