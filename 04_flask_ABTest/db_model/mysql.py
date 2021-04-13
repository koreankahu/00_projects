import pymysql

MYSQL_HOST = 'localhost'
MYSQL_CONN = pymysql.connect(
    host=MYSQL_HOST,
    port=3306,
    user='theonetop',
    passwd='dnjsxkq2@',
    db='blog_db',
    charset='utf8'
)

# db에 연결, 함수네, 오류나면 다시 실행해서 접속하고.


def conn_mysqldb():
    if not MYSQL_CONN.open:
        MYSQL_CONN.ping(reconnect=True)
    return MYSQL_CONN
