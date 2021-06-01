import pyupbit

f = open("upbit.txt")
lines = f.readlines()
access = lines[0].strip()   # access key
secret = lines[1].strip()   # secret key
f.close()
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-XRP"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회