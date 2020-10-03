

import sys
import time
from time import sleep
from datetime import datetime, date


# time.sleep(5)     #阻塞函数
# print("end")
# for i in range(1000):
#     time.sleep(0.5)
#     print(i)
#



# print(time.time())
# print(time.asctime())
# print(time.localtime())
# print(time.localtime(time.time()))
# print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
# for i in range(1000):
#     time.sleep(1)
#     print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())), end = '\r')
#     # print('\r', i, end='')
#     print("\b" * (len(str(i)) * 2), end="", flush=True)


# for i in range(1000):
#     time.sleep(1)
#     print("%d"%(i), end='\r')

# print(datetime.now())
# print(date(2019, 12, 13))
# print(datetime.today())
# begin_date = time.time()
# time.sleep(5)
# end_date = time.time()
# print(end_date - begin_date)
#
# print(time.time())
print(time.clock())
sleep(4)
print(time.clock())
sleep(4)
print(time.clock())
