from flask import Flask, Blueprint, request, render_template, make_response, jsonify, redirect, url_for, session
from flask_login import login_user, current_user, logout_user
from blog_control.user_mgmt import User
from blog_control.session_mgmt import BlogSession
import datetime
blog_abtest = Blueprint('blog', __name__)

# redirect : 리턴을, 다른 라우팅 경로로 변경해주는 역할


@blog_abtest.route('/set_email', methods=['POST', 'GET'])
def set_email():        # 라우팅 경로와, 함수 이름을 똑같이 해주는게 덜 헥갈림
    if request.method == "GET":
        # print('set_email', request.headers)
        print('set_email', request.args.get('user_email'))
        return redirect(url_for('blog.blog_fullstack1'))

    else:
        # print('set_email', request.headers)
        # print('set_email', request.get_json())
        # Content type이 application/josn 인경우 , body 부분의 파라미터값을 가져올수있어
        # print('set_email', request.form['user_email'])
        # print('set_email', request.form['blog_id'])
        # ! mysql에 넣든, 찾든, 세션정보 만들어줘야해
        user = User.create(request.form['user_email'], request.form['blog_id'])
        login_user(user, remember=True, duration=datetime.timedelta(days=365))
        # ! 세션정보 플래스크에서 만들어줌
        return redirect(url_for('blog.blog_fullstack1'))

    # return redirect('/blog/test_blog')
    # return make_response(jsonify(success=True), 200)


@blog_abtest.route('/logout')
def logout():
    User.delete(current_user.id)
    logout_user()
    return redirect(url_for('blog.blog_fullstack1'))

#! 이함수를 실행하기 전에 before_request가 불리운 상태임!!!


@blog_abtest.route('/blog_fullstack1')
def blog_fullstack1():        # 라우팅 경로와, 함수 이름을 똑같이 해주는게 덜 헥갈림
    # BlogSession.get_blog_page()  # ! 이거 자체가 html페이지라서 render_template에 넣을수있다
    if current_user.is_authenticated:
        # 이거를 호출할때, 내부적으로 , 함수가 호출됨> 어떤?
        # user_loader 함수를 호출함 user_loader가 뭔데? get함수
        # User.get(user_id) 를 리턴하는 함수
        # get(user_id) 는결국 user를 리턴하는데> user는 아래와같지..
        #! user = User(user_id=user[0], user_email=user[1], blog_id=user[2]) 이거를 리턴
        #! 결론> current_user == User 객체가 되네
        webpage_name = BlogSession.get_blog_page(current_user.blog_id)
        BlogSession.save_session_info(
            session['client_id'], current_user.user_email, webpage_name)
        return render_template(webpage_name, user_email=current_user.user_email)
        # current_user 객체는 결국은 User객체래.그래서 user_email을 쓸수있는거지
    else:
        webpage_name = BlogSession.get_blog_page()
        BlogSession.save_session_info(
            session['client_id'], 'anonymous', webpage_name)
        #! user_email은 모르는 상태
        return render_template(webpage_name)
