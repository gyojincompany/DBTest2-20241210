import time

import requests
from bs4 import BeautifulSoup
import datetime

url = f"https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo=860"  # 로또 1회차 당첨번호 출력 url

html = requests.get(url)
# print(html.text)

soup = BeautifulSoup(html.text, "html.parser")
print(soup)

# 로또 당첨번호 6개를 list 타입으로 반환
lottoNumber = soup.find("div",{"class":"num win"}).find("p").text.strip().split("\n")
print(lottoNumber)

# 로또 당첨 보너스 번호 1개를 반환
bonusNumber = soup.find("div",{"class":"num bonus"}).find("p").text.strip()
print(bonusNumber)

# 로또 추첨일 반환
lottoDate = soup.find("p",{"class":"desc"}).text.strip()
print(lottoDate)
lottoDate = datetime.datetime.strptime(lottoDate, "(%Y년 %m월 %d일 추첨)")  # 문자열 날짜->날짜 type 으로 변환
print(lottoDate)

lottoData = {"date":lottoDate, "lottoNum":lottoNumber, "bonusNum":bonusNumber} # 한 회차의 로또 당첨 결과 레코드

# 가장 최근의 로또 당첨 회차 회수 가져오기
url = f"https://dhlottery.co.kr/common.do?method=main"  # 동행복권 홈페이지의 첫페이지 url->최근 로또 당첨 회차수 출력

html = requests.get(url)
soup = BeautifulSoup(html.text, "html.parser")
recentCount = soup.find("strong",{"id":"lottoDrwNo"}).text.strip()  # 가장 최근의 로또 회차 번호
recentCount = int(recentCount) # range 함수에 넣을 값이므로 int로 변환
print(recentCount)

lottoNumList = []  # 로또 당첨 결과 레코드가 저장될 빈 리스트

for count in range(1, recentCount+1):  # 1~1150회까지 반복

    url = f"https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={count}"  # 로또 1회차 당첨번호 출력 url

    html = requests.get(url)
    # print(html.text)

    soup = BeautifulSoup(html.text, "html.parser")

    # 로또 당첨번호 6개를 list 타입으로 반환
    lottoNumber = soup.find("div", {"class": "num win"}).find("p").text.strip().split("\n")
    print(lottoNumber)

    # 로또 당첨 보너스 번호 1개를 반환
    bonusNumber = soup.find("div", {"class": "num bonus"}).find("p").text.strip()
    print(bonusNumber)

    # 로또 추첨일 반환
    lottoDate = soup.find("p", {"class": "desc"}).text.strip()
    print(lottoDate)
    lottoDate = datetime.datetime.strptime(lottoDate, "(%Y년 %m월 %d일 추첨)")  # 문자열 날짜->날짜 type 으로 변환
    print(lottoDate)

    lottoData = {"date": lottoDate, "lottoNum": lottoNumber, "bonusNum": bonusNumber}  # 한 회차의 로또 당첨 결과 레코드

    lottoNumList.append(lottoData)

    time.sleep(1)

print(lottoNumList)