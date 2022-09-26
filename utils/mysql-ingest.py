import os, pandas as pd, pymysql, sys
from sqlalchemy import create_engine

file, name = sys.argv[1], sys.argv[2]

engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
                       .format(user = os.getenv('MYSQL_USER'),
                               pw = os.getenv('MYSQL_PASSWORD'),
                               host=os.getenv('MYSQL_HOST'),
                               db=os.getenv('MYSQL_DATABASE')
                              )
                      )
df = pd.read_csv(file, dtype=str)
df.to_sql(con=engine, name=name, if_exists='replace', index=False)
