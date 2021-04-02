from flask import Flask
import requests

app = Flask(__name__)


@app.route('/google')
def get_google():
    response = requests.get('http://google.co.kr')
    return response.text


if __name__ == "__main__":
    app.run(host="127.0.0.1", port="8081", debug="True")
