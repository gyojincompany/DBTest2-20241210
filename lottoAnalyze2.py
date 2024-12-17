# 특정 월 로또 당첨번호 통계
import pandas
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

# pandas 날짜 타입으로 변환 -> 추첨월만 추출
lotto_df["추첨일"] = pandas.to_datetime(lotto_df["추첨일"])
# print(lotto_df)
lotto_df["추첨월"] = lotto_df["추첨일"].dt.month  # 추첨월만 추출하여 "추첨월" 칼럼 추가
print(lotto_df)

lotto_december = lotto_df[lotto_df["추첨월"] == 12]  # 추첨월이 12월인 값만 추출
print(lotto_december)

lottoAllData = list(lotto_december["당첨번호1"])+list(lotto_december["당첨번호2"])+list(lotto_december["당첨번호3"])+list(lotto_december["당첨번호4"])+list(lotto_december["당첨번호5"])+list(lotto_december["당첨번호6"])+list(lotto_december["보너스번호"])
lottoCountData = collections.Counter(lottoAllData)  # 로또번호 빈도수 계산
print(lottoCountData)

lottoSeries = pd.Series(lottoCountData)  # DataFrame을 Series로 변환
lottoSeries = lottoSeries.sort_values(ascending=False)  # 로또번호 빈도수의 내림차순 정렬
print(lottoSeries)
lottoSeries = lottoSeries.head(6)  # 빈도수가 높은 순으로 상위 10개만 추출
lottoSeries = lottoSeries.sort_values()
# lottoSeries = lottoSeries.sort_index()  # 로또 번호(1~45 순서) 오름차순 정렬
print(lottoSeries)

lottoSeries.plot(figsize=(10,10), kind="barh", grid=True, title="12월 로또 당첨 번호별 통계")

plt.show()

cur.close()
conn.close()