"""
一些工具函数
"""

from datetime import datetime
from DAO import MysqlHelper


map_s = "abcdefghijklmnopqrstuvwxyz"

#万能正则
patternForUrl = r'href="/firm_([\s\S]*?).html"'

# 初始时间
begin_time = datetime.now()

fail = 4
success = 0


pi = 3.141592653589793


def calc_run_time(func):
    def inner_func(*parm):
        begin_time = datetime.now()
        ret = func(*parm)
        end_time = datetime.now()
        print(end_time - begin_time)
        return ret
    return inner_func


def get_user_info(username, pwd):
    try:
        sql = """
                SELECT user_name, password FROM user_info WHERE user_name = "{}";
                """
        sql = sql.format(username)
        print(sql)
        info = MysqlHelper.do_query(sql)
        print(info)
        return info
    except Exception as e:
        # print(e.message)
        return None


def create_user_info(username, pwd):
    try:
        sql = """
                INSERT INTO user_info(user_name, password) VALUES("{}", "{}");
                """
        sql = sql.format(username, pwd)
        print(sql)
        res = MysqlHelper.do_execute(sql)
        return res
    except Exception as e:
        return fail


def insert_into_b_player_info(name, age, number, position, weight, height, nationality):
    try:
        sql = """
                INSERT INTO b_player_basicinfo(name, age, number, position, weight, height, nationality) 
                VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}');
                """
        sql = sql.format(name, age, number, position, weight, height, nationality)
        # print(sql)
        ret = MysqlHelper.do_execute(sql)
        return ret
    except Exception as e:
        print(e)
        return fail


def modify_b_player_info(p_id, name, age, number, position, weight, height, nationality):
    try:
        sql = """
                UPDATE b_player_basicinfo SET name='{}', age='{}', number='{}', 
                position='{}', weight='{}', height='{}', nationality='{}' WHERE id = {};
                """
        sql = sql.format(name, age, number, position, weight, height, nationality, p_id)
        print(sql)
        ret = MysqlHelper.do_execute(sql)
        return ret
    except Exception as e:
        print(e)
        return fail


def myprint(s):
    print("\33[0;33m {} \33[0m".format(s))


def remove_str(gen_str, com_str):
    """
    传入两个字符串，从前一个字符串中删除所包含的所有第二个字符串
    :param gen_str: 包含需要删除字符的字符串
    :param com_str: 需要删除的字符串
    :return: 删除后的字符串
    """



if __name__ == '__main__':
    # get_user_info("mengwei", 132456)
    print(len({}))