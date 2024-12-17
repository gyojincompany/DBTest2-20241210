# 로또 당첨 번호별 통계

import pymysql
import pandas as pd
import matplotlib.pyplot as plt
import collections

conn = pymysql.connect(host="localhost", user="root", password="12345", db="lotto")
# 파이썬과 mysql간의 커넥션 생성

sql = "SELECT * FROM lottotbl"  # 로또DB에서 모든 로또 데이터 가져오기

cur = conn.cursor()  # cursor 생성
cur.execute(sql)  # sql문 실행

result = cur.fetchall()  # select 문의 반환 결과->tuple타입으로 반환

print(result)
