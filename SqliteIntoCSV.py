import sqlite3
import pandas as pd
conn = sqlite3.connect('/Users/ramyabandi/Downloads/FPA_FOD_20170508.sqlite')
#conn.text_factory = str ## my current (failed) attempt to resolve this
#cur = conn.cursor()
#data = cur.execute("SELECT * FROM mytable")
fires = pd.read_sql_query("SELECT * FROM fires", conn)
fires
fires.to_csv('firecsv.csv', index=False)