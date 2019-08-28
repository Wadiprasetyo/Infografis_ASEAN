#############################INFOGRAFIS ASEAN##############################

import mysql.connector
import pandas as pd 
import matplotlib.pyplot as plt 
import plotly.graph_objects as go 

conn = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = 'Kukuruyuk06',
    database = 'world'
)

# Query nomor 1-3
q = '''
select co.Name as Negara_ASEAN, co.Population as Populasi_Negara, co.GNP, ci.Name as Ibukota, ci.Population as Populasi_Ibukota
from city ci inner join country co
on ci.id = co.Capital
where co.Name in ('Brunei','Cambodia','East Timor','Indonesia','Laos','Malaysia',
'Myanmar','Philippines','Singapore','Thailand','Vietnam')
order by Negara_ASEAN asc;
'''

# Query nomor 4
q1 = '''
select co.Name as Negara_ASEAN, co.SurfaceArea
from country co
where co.Name in ('Brunei','Cambodia','East Timor','Indonesia','Laos','Malaysia',
'Myanmar','Philippines','Singapore','Thailand','Vietnam')
order by Negara_ASEAN asc;
'''
Kursor = conn.cursor()
df = pd.read_sql(q, con=conn) # query untuk nomor 1-3
df = pd.read_sql(q1, con=conn) # query untuk nomor 4

# dijalankan dengan comment 2 variabel yang tidak dipakai, sehingga menjalankan yang hanya dipakai saja ex: x & y, x & y1, x & y2
x = list(df['Negara_ASEAN']) # list nomor 1,2,3,4
y = list(df['Populasi_Negara']) # list nomor 1 & 2
y1 = list(df['GNP']) # list nomor 3
y2 = list(df['SurfaceArea']) # list nomor 4

####comment nomor yang tidak ingin dijalankan beserta query nya
## Soal no.1
for a,b in zip(x, y):
    plt.text(a,b, str(b), ha='center', size=6)

plt.bar(x, y, color=['tan', 'navy', 'green', 'red', 'maroon', 'blue', 'pink', 'orange', 'brown', 'magenta', 'lightblue'])
plt.title('Populasi Negara ASEAN')
plt.xlabel('Negara')
plt.ylabel('Populasi(x100jt jiwa)')
plt.grid(True)
plt.xticks(rotation=45, size=6)
plt.show()

## Soal no.2
color=['tan', 'navy', 'green', 'red', 'maroon', 'blue', 'pink', 'orange', 'brown', 'magenta', 'lightblue']
plt.pie(y, labels=x, colors=color,
startangle=180, counterclock=False,
autopct='%1.1f%%',
textprops={'color':'black'}
)
plt.show()

## Soal No.3
for a,b in zip(x, y1):
    plt.text(a,b, str(b), ha='center', size=6)

plt.bar(x, y1, color=['tan', 'navy', 'green', 'red', 'maroon', 'blue', 'pink', 'orange', 'brown', 'magenta', 'lightblue'])
plt.title('Pendapatan Bruto Nasional ASEAN')
plt.xlabel('Negara')
plt.ylabel('Gross National Products (US$)')
plt.grid(True)
plt.xticks(rotation=45, size=6)
plt.show()

## Soal No.4
color=['tan', 'navy', 'green', 'red', 'maroon', 'blue', 'pink', 'orange', 'brown', 'magenta', 'lightblue']
plt.pie(y2, labels=x, colors=color,
startangle=180, counterclock=False,
autopct='%1.1f%%',
textprops={'color':'black'}
)
plt.show()