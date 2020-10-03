import pymysql
from Helper import Tools
import pandas as pd


class forDBs:
    def __init__(self):
        self.conn = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='666666',
            db='data_analysis',
            charset='utf8'
        )
        self.cur = self.conn.cursor()

    def sql(self, sql):
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as E:
            try:
                with open('wrongToDBs.txt', 'a') as f:
                    f.write("""{}, {}""".format(E,sql) + '\n')
            except:
                print(E, sql)
            self.conn.rollback()


tt = forDBs()


def do_query(sql):
    try:
        tt.cur.execute(sql)
        return tt.cur.fetchall()
    except:
        return None


def do_execute(sql):
    try:
        tt.cur.execute(sql)
        tt.conn.commit()
        return Tools.success
    except Exception as e:
        print(e)
        return Tools.fail


def query_to_df(sql):
    try:
        # ret = do_query(sql)
        df = pd.read_sql(sql, tt.conn)
        df.columns = [str(i).upper() for i in df.columns]
        # print(df.columns)
        return df
    except:
        return None


def get_players(id=None):
    try:
        sql_query = """
                        SELECT id, name, number NUMBER, age AGE, position POSITION, nationality NATIONALITY 
                        FROM b_player_basicinfo
                        """
        if id:
            sql_query += " WHERE id = {};"
        df = query_to_df(sql_query)
        # print(df)
        return df

    except Exception as e:
        # print(e)
        return None


def get_players_all():
    try:
        sql_query = """
                        SELECT name, number, age, position, nationality 
                        FROM b_player_basicinfo
                        """
        df = do_query(sql_query)
        print(df)
        return df
    except Exception as e:
        # print(e)
        return None


if __name__ == '__main__':
    # sql = """
    #         SELECT * FROM basic_info;
    #         """
    # basic_info_df = query_to_df(sql)
    # print(type(basic_info_df))
    # sql = 'INSERT INTO basic_info (u_name) VALUES("小可爱爱爱爱爱");'
    # do_execute(sql)
    get_players()