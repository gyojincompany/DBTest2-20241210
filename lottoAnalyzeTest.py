# 로또 당첨 번호별 통계

import pymysql
import pandas as pd
import matplotlib.pyplot as plt
import collections

# 시각화 한글 깨짐 방지
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

conn = pymysql.connect(host="localhost", user="root", password="12345", db="lotto")
# 파이썬과 mysql간의 커넥션 생성

sql = "SELECT * FROM lottotbl"  # 로또DB에서 모든 로또 데이터 가져오기

cur = conn.cursor()  # cursor 생성
cur.execute(sql)  # sql문 실행

result = cur.fetchall()  # select 문의 반환 결과->tuple타입으로 반환

# print(result)


# 로또DB 모든 레코드 tuple을 DataFrame으로 변환
lotto_df = pd.DataFrame(data=result, columns=["추첨회차","추첨일","당첨번호1","당첨번호2","당첨번호3","당첨번호4","당첨번호5","당첨번호6","보너스번호"])
print(lotto_df)

# print(list(lotto_df["당첨번호1"]))

# 모든 로또 당첨번호가 포함되어 있는 list 만들기
lottoAllData = list(lotto_df["당첨번호1"])+list(lotto_df["당첨번호2"])+list(lotto_df["당첨번호3"])+list(lotto_df["당첨번호4"])+list(lotto_df["당첨번호5"])+list(lotto_df["당첨번호6"])+list(lotto_df["보너스번호"])
# print(lottoAllData)

countSum = 0
for i in range(1, 46):  # 1~45까지 회전
    count = 0
    for num in lottoAllData:  # lottoAllData->8050개의 로또 당첨번호 숫자 리스트
        if num == i and num <= 10:
            count = count + 1
    countSum = countSum + count
    print(f"{i}번의 빈도수 : {count}")
    print(f"{i}번의 비율 {count/len(lottoAllData)*100:.2f}")
print(f"1-10번의 비율 {countSum / len(lottoAllData) * 100:.2f}")


# lottoCountData = collections.Counter(lottoAllData)  # 로또번호 빈도수 계산
# print(lottoCountData)
#
# lottoSeries = pd.Series(lottoCountData)  # DataFrame을 Series로 변환
# print(lottoSeries)
# lottoSeries = lottoSeries.sort_index()  # 로또 번호(1~45 순서) 오름차순 정렬
# print(lottoSeries)
#
# lottoSeries.plot(figsize=(10,10), kind="barh", grid=True, title="로또 당첨 번호별 통계")
#
# plt.show()

cur.close()
conn.close()