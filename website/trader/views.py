from django.shortcuts import render
from django.http import HttpResponse
import yfinance as yahooFinance
from plotly.offline import plot
from plotly.graph_objs import Scatter




def index(request):
    return render(request, 'index.html')

def aapl(request):
    aapl_close = yahooFinance.download("AAPL", period="1y", actions=True).Close
    date = aapl_close.index
    x_data = date
    y_data = aapl_close
    plot_div = plot([Scatter(x=x_data, y=y_data,
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
                output_type='div')

    return render(request, 'aapl.html', {'plot_div': plot_div})

def msft(request):
    msft_close = yahooFinance.download("MSFT", period="1y", actions=True).Close
    date = msft_close.index
    x_data = date
    y_data = msft_close
    plot_div = plot([Scatter(x=x_data, y=y_data,
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
                output_type='div')

    return render(request,'msft.html', {'plot_div': plot_div} )

def goog(request):
    goog_close = yahooFinance.download("MSFT", period="1y", actions=True).Close
    date = goog_close.index
    x_data = date
    y_data = goog_close
    plot_div = plot([Scatter(x=x_data, y=y_data,
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
                output_type='div')
    return render(request,'goog.html',  {'plot_div': plot_div})