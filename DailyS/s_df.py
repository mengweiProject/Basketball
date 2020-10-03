import pandas as pd
import numpy as np
from Helper.Tools import map_s


def func1():
    df = pd.DataFrame([{"secucode": 132423, "n_port_id": 3245345},
                       {"secucode": 657567, "n_port_id": 678678},
                       {"secucode": 132423, "n_port_id": 678678},
                       {"secucode": 3453, "n_port_id": 3245345},
                       {"secucode": 56456, "n_port_id": 457457},
                       {"secucode": 8676543, "n_port_id": 123132}])
    # print(df)
    # df.set_index("secucode", inplace=True)
    # print(df[df["n_port_id"].isin([132423])])
    print("asdf"[:2])


def func2():
    list = [1, 1, 3, 5, 5, 7, 9, 9, 6]
    rule = {1: 0, 5: 1, 3: 2, 4: 3, 2: 4, 7: 5, 8: 6, 6: 7, 9: 8, 0: 9}
    newList = sorted(list, key=lambda x: rule[x])
    # print(newList)
    print([""] * 10)


def func3():
    merge_s = pd.Series(data=[i for i in map_s.upper()], name="LETTERS")
    merge_s = merge_s.iloc[0:20:2]
    print(merge_s)
    nav_s = pd.Series(data=[i for i in map_s], index=[i for i in range(26)], name="LETTER")
    nav_s = nav_s.iloc[:18]
    print(nav_s)
    merge_s = pd.DataFrame(merge_s).join(nav_s, how="inner")
    print(merge_s)


if __name__ == '__main__':
    func3()