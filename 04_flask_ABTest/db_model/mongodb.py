import pymongo

MONGO_HOST = 'localhost'
MONGO_CONN = pymongo.MongoClient('mongodb://%s' % (MONGO_HOST))

# 컬렉션에 연결하는 해서 컬렉션 객체를 만들고, 컬렉션 객체를 리턴하는 함수


def conn_mongodb():
    try:
        MONGO_CONN.admin.command('ismaster')
        blog_ab = MONGO_CONN.blog_session_db.blog_ab
    except:
        MONGO_CONN = pymongo.MongoClient('mongodb://%s' % (MONGO_HOST))
        blog_ab = MONGO_CONN.blog_session_db.blog_ab
    return blog_ab
