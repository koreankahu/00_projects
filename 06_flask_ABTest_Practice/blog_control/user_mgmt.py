from flask_login import UserMixin
from db_model.mysql import conn_mysqldb


class User(UserMixin):
    def __init__(self, user_id, user_email, blog_id):
        self.id = user_id
        #! id 는 flask 로긴에서 바꾸면, 에러가남 그래서 id 라고 적어줘야해!!!
        self.user_email = user_email
        self.blog_id = blog_id

    def get_id(self):
        return str(self.id)

    @staticmethod
    def get(user_id):
        mysql_db = conn_mysqldb
        db_cursor = mysql_db.cursor()
        sql = "SELECT * FROM user_info WHERE USER_ID = '" + str(user_id) + "'"
        db_cursor.execute(sql)
        user = db_cursor.fetchone()

        if not user:
            return None

        user = User(user_id=user[0], user_email=user[1], blog_id=user[2])
        return user
