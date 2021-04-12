from flask import Flask
import requests

app = Flask(__name__)
if not app.debug:
    import logging
    from logging.handlers import RotatingFileHandler    # logging 핸들러 이름을 적어줌
    file_handler = RotatingFileHandler(
        "dave_server.log", maxBytes=2000, backupCount=10)
    file_handler.setLevel(logging.WARNING)  # 어느단계까지 로깅을 할지 적어줌
    # app.looger.addHandler() 에 등록을 시켜줘야 app.logger 로 사용가능
    app.logger.addHandler(file_handler)


@app.errorhandler(404)
def page_not_found(error):
    app.logger.error(error)
    return "<h1>해당 경로에 맞는 웹페이가 없어 , 문제가 지속되면, 관리자한테 연락하지마</h1>", 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080", debug=False)
