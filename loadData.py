import pymysql
import pandas as pd


def get_data_from_aliyun(user, password, db, port=3306, host='127.0.0.1'):
    conn = pymysql.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        db=db,
        charset="utf8"
    )
    cursor = conn.cursor()
    sql = "select * from wuxia"
    res = cursor.execute(sql)
    print(res)
    df = pd.read_sql(sql=sql, con=conn)
    print(df)

    cursor.close()
    conn.close()

    if res:
        print("登录成功")
    else:
        print('登录失败')


get_data_from_aliyun(user='sheep431', password='xssxyby198566', db='novel', host='sheep431.mysql.rds.aliyuncs.com')
