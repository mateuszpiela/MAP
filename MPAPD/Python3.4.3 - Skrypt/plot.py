# Import Bibliotek
import mysql.connector
import pandas as pd
import plotly
from plotly.graph_objs import Scatter, Layout
#Ustawienia bazy danych
USER = "arduino"
PASSWORD = "ZC5sVJrG95KA6Qbe"
HOST = "localhost"
DATABASE = "arduino"

#Połączenie do bazy danych
mysql = mysql.connector.connect(user=USER, password=PASSWORD,host=HOST,database=DATABASE)
cur = mysql.cursor()
query = cur.execute('SELECT * FROM temp')
row = cur.fetchall()
df = pd.DataFrame( [[ij for ij in i] for i in row] )
df.rename(columns={0: 'ID', 1: 'TEMP', 2: 'timestamp'}, inplace=True);
df = df.sort_values(['timestamp'], ascending=[1]);

plotly.offline.plot({
    "data": [Scatter(x=df['timestamp'], y=df['TEMP'])],
    "layout": Layout(title="Temperatura")
})
