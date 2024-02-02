from flask import Flask,render_template
from datetime import datetime
import socket

app = Flask(__name__)

@app.route("/")
def index():
    try:
        now = datetime.now()
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        return render_template('index.html', hostname=host_name, ip=host_ip, time=now)
    except:
        return render_template('error.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)