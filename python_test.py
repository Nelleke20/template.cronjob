
import requests

resulttext = 'this is a test'
requests.get("https://api.telegram.org/{}:{}/sendMessage?chat_id={}&text={}".format('bot5012861040', 'AAGXSZHb0lDwpa2hJHpJF1Tv0tK8AVacBjg', '2012057334', resulttext))