import requests
from twilio.rest import Client
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = ""
NEWS_API_KEY = ""
TWILIO_SID = ""
TWILIO_AUTH_TOKEN = ""


    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily

# Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
stock_params ={
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK_NAME,
    'apikey': STOCK_API_KEY,
}

response =requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()['Time Series (Daily)']
data_list = [value for (key,value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data['4. close']

#Get the day before yesterday's closing stock price

day_before_yesterday = data_list[1]
day_before_closing_price = day_before_yesterday['4. close']

#Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

difference = float(day_before_closing_price) - float(yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = '▲'
else:
    up_down = '🔻'
#Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

diff_percentage = round(difference/float(yesterday_closing_price) * 100)


#If percentage is greater than 5 then print("Get News").
if abs(diff_percentage) < 5:
    news_params ={
        'apikey': NEWS_API_KEY,
        'qInTitle': COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT,params=news_params)
    articles = news_response.json()['articles']


    ## STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    three_articles = articles[:3]
    print(three_articles)
#Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number.

#Create a new list of the first 3 articles headline and description using list comprehension.
    formated_articles =[f"{STOCK_NAME}: {up_down} {diff_percentage}%\n Headline: {article['title']}. \n Brief: {article['description']}"  for article in three_articles]
    #Send each article as a separate message via Twilio.

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in formated_articles:
        message = client.messages.create(
            body=article,
            from_=+13412145931,
            to=+923325578940
    )
