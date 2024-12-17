import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
from sqlalchemy import create_engine
import pymysql

def get_recent_lottocount(): # 최신 로또 회차 크롤링 함수(2024년 12월 17일 현재 1150회차)
    url = f"https://dhlottery.co.kr/common.do?method=main"  # 동행복권 홈페이지의 첫페이지 url->최근 로또 당첨 회차수 출력

    html = requests.get(url)
    soup = BeautifulSoup(html.text, "html.parser")
    recentCount = soup.find("strong", {"id": "lottoDrwNo"}).text.strip()  # 가장 최근의 로또 회차 번호
    recentCount = int(recentCount)  # range 함수에 넣을 값이므로 int로 변환

    return recentCount  # 최신 회차 값을 최종적으로 반환

def get_lottoNumber(lottocount):  # 로또 회차를 넣으면 해당 회차의 로또당첨결과를 반환하는 함수
    url = f"https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={lottocount}"  # 로또 1회차 당첨번호 출력 url
    html = requests.get(url)
    soup = BeautifulSoup(html.text, "html.parser")
    # 로또 당첨번호 6개를 list 타입으로 반환
    lottoNumber = soup.find("div", {"class": "num win"}).find("p").text.strip().split("\n")
    # 로또 당첨번호가 문자열이므로, 계산을 위한 int로 변환
    lottoNumberList = []
    for lottoNum in lottoNumber:
        lottoNum = int(lottoNum)
        lottoNumberList.append(lottoNum)

    # 로또 당첨 보너스 번호 1개를 반환
    bonusNumber = int(soup.find("div", {"class": "num bonus"}).find("p").text.strip())
    # 로또 추첨일 반환
    lottoDate = soup.find("p", {"class": "desc"}).text.strip()
    print(lottoDate)
    lottoDate = datetime.datetime.strptime(lottoDate, "(%Y년 %m월 %d일 추첨)")  # 문자열 날짜->날짜 type 으로 변환
    print(lottoDate)

    lottoData = {"date": lottoDate, "lottoNum": lottoNumberList, "bonusNum": bonusNumber}  # 한 회차의 로또 당첨 결과 레코드

    return lottoData
