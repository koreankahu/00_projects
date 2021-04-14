# blog_abtest.py

from flask import Flask, jsonify, request, render_template, make_response
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from flask_cors import CORS
import os
from blog_view import blog

# LoginManager : 이걸로 맨처음 세션관리 등록을 해줘야해
# current_user : 로그인된 user객체를 , 언제든지 참조할수있는 객체
# login_required : 우리는 사용하지 않지만, 로그인된 사용자만 접근할수 있는 api를 만들때
# login_user : 로긴을 하면, 해당객체를 login_user 객체에 넘겨줘, 그다음부터 세션이 만들어지고 >
# -            해당세션으로 통신할수 있도록 구성해준다
# logout_user : 로그 아웃객체에 넘겨주면, 세션이 없어져서 로그아웃됨
# CORS : 스크립트 기반으로 request 요청 하는것은 안됨(같은 서버에서 요청이 있어야지 처리됨!!!!)>
# -      근데 CORS로 다른 서버에서 요청해도 처리해줌
# os : oauth2 와 같이 보안 로그인할대 많이 사용되는 프로토콜이 있다
#      구글로 로긴, 네이버로긴 > 소셜 로그인기능 쓸때


# https 만을 지원 하는 > 기능을 http에서 테스트할 때 필요한 요청
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'


app = Flask(__name__, static_url_path='/static')
CORS(app)
app.secure_key = 'dave_server'
app.register_blueprint(blog.blog_abtest, url_prefix='/blog')

login_manager = LoginManager()
# 객체 생성을 하나하고
login_manager.init_app(app)     # app을 등록 시켜 줘야해
login_manager.session_protection = 'strong'     # strong을 줘야지, 세션을 보다 복잡하게 만들어줌


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@login_manager.unauthorized_handler
def unauthorized():
    return make_response(jsonify(success=False), 401)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port="8081", debug=True)
