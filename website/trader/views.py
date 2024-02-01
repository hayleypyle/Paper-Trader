from django.shortcuts import render
from django.http import HttpResponse
from json import dumps
import yfinance as yahooFinance 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

def home(request):
    return render(request, 'index.html')

def aapl(request):
    aapl_ticker = yahooFinance.Ticker("AAPL")
    data = aapl_ticker.history(interval="1d")
    close = data['Close']
    date= close.index
    price = close[0]
    return render(request, 'aapl.html', {'date': date, 'price': close, 'data':data})


def low(request):
    return render(request,'low.html' )

def mcd(request):
    return render(request,'mcd.html')