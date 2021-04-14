# session_mgmt.py
from db_model.mongodb import conn_mongodb
from datetime import datetime


class BlogSession():
    blog_page = {"A": 'blog_A.html', 'B': 'blog_B.html'}
    session_count = 0

    @staticmethod
    def save_session_info(session_ip, user_email, webpage_name):
        now = datetiem
