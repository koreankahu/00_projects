from flask import Blueprint

blog_ab = Blueprint('blog', __name__)
# blog : 블루 프린트 이름이래 ㅡㅡ;;;
# 블루 프린트를 여러개 만들수있으니. 블루 프린트 이름이 필요하네

# url_prefix = 'blog' 라고 했으니
# http://0.0.0.0/8080/blog/blog1  이게 라우팅경로가 되지


@blog_ab.route('/blog1')
def blog():
    return "TEST BLUEPRINT"
