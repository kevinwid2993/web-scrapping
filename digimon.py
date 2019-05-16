from bs4 import BeautifulSoup
import requests

url = 'https://wikimon.net/Visual_List_of_Digimon'
web = requests.get(url)
soup = BeautifulSoup(web.content, 'html.parser')

digimon = []

images = soup.find_all('img')

for image in images:
    my_dict = {
        'nama' : image.get('alt'),
        'gambar' : 'https://wikimon.net'+ image.get('src')
        }
    digimon.append(my_dict)

#hasil webscrap ke csv
import csv
with open('digimon.csv', 'w', newline='', encoding='utf8') as csv_file: #digimon as csv_file
    isi = ['nama','gambar']
    writer = csv.DictWriter(csv_file, fieldnames=isi)
    writer.writeheader()
    for i in range(len(digimon)-2):
        writer.writerow(digimon[i])

#masukin ke mysql

import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'kevin',
    passwd = 'kevin29101993!',
    database = 'digimon'
)

cursor = mydb.cursor()

for i in range(len(digimon)-2):
    nama = digimon[i]['nama']
    gambar = digimon[i]['gambar']
    cursor.execute('INSERT INTO digimon (nama,gambar) values (%s, %s)',(nama, gambar))
    mydb.commit()