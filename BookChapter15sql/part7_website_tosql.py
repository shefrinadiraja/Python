import requests 
import sqlite3
db_connection = sqlite3.connect('quotes.sqlite')
db_cur = db_connection.cursor()

db_cur.execute ('create table if not exists quotes (id integer primary key autoincrement, quote TEXT, author TEXT)')
db_cur.execute ('create table if not exists authors (id integer primary key autoincrement, author TEXT unique)')

db_connection.commit()

for i in range(1,10):
    response = requests.get(f'https://quotes.toscrape.com/page/{i}/')
    data = response.text

    from bs4 import BeautifulSoup

    soup = BeautifulSoup(data,'html.parser')


    quotes = soup.find_all('div',class_='quote')

    for quote in quotes:
        text = quote.find('span',class_='text')
        text = text.get_text(strip=True)
        print(text)

        author=quote.find('small', class_='author').get_text(strip=True)
        print(author)

        db_cur.execute('insert into quotes (quote,author) values (?,?)',(text,author))
        db_cur.execute('insert or ignore into authors (author) values (?)',(author,))
        
db_connection.commit()








