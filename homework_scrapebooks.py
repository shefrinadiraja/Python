import requests
import sqlite3
from bs4 import BeautifulSoup

db_connection = sqlite3.connect('books.sqlite')
db_cursor = db_connection.cursor()

db_cursor.execute('create table if not exists books (id integer primary key autoincrement, title TEXT unique, price_usd REAL)')
db_connection.commit

for i in range(1,50):
    response = requests.get(f'https://books.toscrape.com/catalogue/category/books_1/page-{i}.html')
    data = response.text


    
    soup = BeautifulSoup(data,'html.parser')


    books = soup.find_all('article',class_='product_pod')
  


    for book in books:
        text = book.find('h3')
        text = text.get_text()

        price = book.find('p',class_='price_color')
        price = price.get_text().replace('Â£','')

        print(text,price)


        db_cursor.execute('insert or ignore into books(title,price_usd) values(?,?)',(text,price,))
        db_connection.commit()



