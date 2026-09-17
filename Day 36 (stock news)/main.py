import requests
from requests_cache import CachedSession
import os
from dotenv import load_dotenv
from datetime import timedelta, date
import smtplib
from email.message import EmailMessage

load_dotenv()
STOCK_API = os.getenv("STOCK_API")
NEWS_API = os.getenv("NEWS_API")
MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

session = CachedSession('stock_cache', expire_after=3600)

url = "https://www.alphavantage.co/query"

parameters = {"apikey": STOCK_API,
              "function": "TIME_SERIES_DAILY",
              "symbol": STOCK,
              }

data = session.get(url, params=parameters)
data.raise_for_status()
stock_data = data.json()
#edgecase market close days
today = date.today()
yesterday = today - timedelta(days=1)

def previous_trading_day(day):
    if day.weekday() == 0:
        yesterday = day - timedelta(days=3)
        return yesterday
    elif day.weekday() == 6:
        yesterday = day - timedelta(days=2)
        return yesterday
    else:
        yesterday = day - timedelta(days=1)
        return yesterday


yesterday = previous_trading_day(today)
day_before = previous_trading_day(yesterday)

yesterday_string = yesterday.strftime("%Y-%m-%d")

day_before_string = day_before.strftime("%Y-%m-%d")

stock_yesterday = float(stock_data["Time Series (Daily)"][yesterday_string]["4. close"])
stock_day_before = float(stock_data["Time Series (Daily)"][day_before_string]["4. close"])

difference = ((stock_yesterday - stock_day_before)/stock_day_before) * 100

if abs(difference) >= 5: #change to 5
    print("Get News")

    session_news = CachedSession("news_cache", expire_after=3600 )
    url = "https://newsapi.org/v2/everything"

    news_parameters = {"apiKey": NEWS_API,
                       "q": COMPANY_NAME,
                       "pageSize": 3
                       }

    news_data = session_news.get(url, params= news_parameters)
    news_data.raise_for_status()
    data = news_data.json()

    news_articles = [(articles["title"], articles["description"], articles["url"]) for articles in data["articles"][0:3]]
    # print(news_articles)

    if difference > 0:
        image = "🔺"
    else: 
        image = "🔻"

    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    message = EmailMessage()
    message["Subject"]= f"{STOCK}:{image}{round(difference, 2)}%"
    message["To"]=MY_EMAIL
    message["From"]=MY_EMAIL

    def news_body():
        news = ""
        for article in news_articles:
            body = f"Headline: {article[0]}" 
            title = f"Brief: {article[1]}"
            url = article[2]
            news += f"{body}\n{title}\n{url}\n\n"
        return news

    body = news_body()
    message.set_content(body)

    connection.send_message(message)
    connection.close()