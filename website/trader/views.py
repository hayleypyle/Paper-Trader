from django.shortcuts import render
from django.http import HttpResponse
import yfinance as yahooFinance 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

def home(request):
    return render(request, 'index.html')

def stne(request):
    stne_ticker = yahooFinance.Ticker("STNE")
    data = stne_ticker.history(interval="1d")
    close = data['Close']
    date= close.index

    return render(request, 'stne.html', {'date': date, 'price': close})

def low(request):
    return render(request,'low.html' )

def mcd(request):
    return render(request,'mcd.html')