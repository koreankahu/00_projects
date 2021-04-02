from flask import Flask, render_template

app = Flask(__name__)


@app.route('/hello/<user>')
def hello_name(user):
    return render_template('variable.html', name1=user, name2="dd")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port='8081')
