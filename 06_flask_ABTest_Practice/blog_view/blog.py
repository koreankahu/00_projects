from flask import Flask, Blueprint, request, render_template, make_response, jsonify, redirect, url_for
from flask_login import login_user, current_user
from blog_control.user_mgmt import User
blog_abtest = Blueprint('blog', __name__)

# redirect : 리턴을, 다른 라우팅 경로로 변경해주는 역할


@blog_abtest.route('/set_email', methods=['POST', 'GET'])
def set_email():        # 라우팅 경로와, 함수 이름을 똑같이 해주는게 덜 헥갈림
    if request.method == "GET":
        # print('set_email', request.headers)
        print('set_email', request.args.get('user_email'))
        return redirect(url_for('blog.test_blog'))

    else:
        # print('set_email', request.headers)
        # print('set_email', request.get_json())
        # Content type이 application/josn 인경우 , body 부분의 파라미터값을 가져올수있어
        print('set_email', request.form['user_email'])
        # ! mysql에 넣든, 찾든, 세션정보 만들어줘야해
        user = User.create(request.form['user_email'], 'A')
        login_user(user)  # ! 세션정보 플래스크에서 만들어줌
        return redirect(url_for('blog.test_blog'))

    # return redirect('/blog/test_blog')
    # return make_response(jsonify(success=True), 200)


@blog_abtest.route('/test_blog')
def test_blog():        # 라우팅 경로와, 함수 이름을 똑같이 해주는게 덜 헥갈림
    if current_user.is_authenticated:   # 이거를 호출할때, 내부적으로 , 함수가 호출됨> 어떤?
        # user_loader 함수를 호출함 user_loader가 뭔데?
        # User.get(user_id) 를 리턴하는 함수
        # get(user_id) 는결국 user를 리턴하는데> user는 아래와같지..
        #! user = User(user_id=user[0], user_email=user[1], blog_id=user[2]) 이거를 리턴
        #! 결론> current_user == User 객체가 되네
        return render_template('blog_A.html', user_email=current_user.user_email)
        # current_user 객체는 결국은 User객체래.그래서 user_email을 쓸수있는거지
    else:
        return render_template('blog_A.html')
