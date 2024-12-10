from sqlalchemy import create_engine
import pandas as pd
import pymysql

engine = create_engine("mysql+pymysql://root:12345@localhost:3306/member_addr?charset=utf8mb4")
engine.connect()

data = {'hakbun':[2000, 2001, 2002, 2003, 2004, 2005],'score':[70,60,50,100,90,85]}
df = pd.DataFrame(data=data, columns=['hakbun','score'])
print(df)

df.to_sql(con=engine, name='score_table', index=False, if_exists='replace')
# if_exitst 속성 옵션 -> fail, append, replace