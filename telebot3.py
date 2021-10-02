import pyupbit
import time
import datetime
import telegram

f = open("upbit.txt")
lines = f.readlines()
telgm_token = lines[3].strip()
chat_id = lines[4].strip()
f.close()

bot = telegram.Bot(token = telgm_token)

def cal_target(ticker):
    """변동성 돌파 전략으로 매수 목표가 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * 0.21
    return target

while True:
    target = int(cal_target("KRW-BTC"))
    now = datetime.datetime.now()
    nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')   
    price = int(pyupbit.get_current_price("KRW-BTC"))
    earning_rate = round(((price / target)-1) * 100, 2)

    if now.minute == 00:
        print(f"time: {nowDatetime} \n목표 가격: {target} \n현재 가격: {price} \
        \n괴리율: {earning_rate}")
        bot.sendMessage(chat_id=chat_id, text=(f"time: {nowDatetime} \
        \n목표 가격: {target} \n현재 가격: {price} \n괴리율: {earning_rate}"))
        time.sleep(30)