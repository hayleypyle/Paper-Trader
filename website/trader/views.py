from django.shortcuts import render
from django.http import HttpResponse
import yfinance as yahooFinance
from plotly.offline import plot
from plotly.graph_objs import Scatter




def index(request):
    aapl_close = yahooFinance.download("AAPL", period="1y", actions=True).Close
    aapl_date = aapl_close.index
    aapl_x_data = aapl_date
    aapl_y_data = aapl_close
    aapl_plot_div = plot([Scatter(x=aapl_x_data, y=aapl_y_data,
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
                output_type='div')
    
    msft_close = yahooFinance.download("MSFT", period="1y", actions=True).Close
    msft_date = msft_close.index
    msft_x_data = msft_date
    msft_y_data = msft_close
    msft_plot_div = plot([Scatter(x=msft_x_data, y=msft_y_data,
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
                output_type='div')
    
    goog_close = yahooFinance.download("MSFT", period="1y", actions=True).Close
    goog_date = goog_close.index
    goog_x_data = goog_date
    goog_y_data = goog_close
    goog_plot_div = plot([Scatter(x=goog_x_data, y=goog_y_data,
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
                output_type='div')

    return render(request, 'index.html', {'aapl_plot_div': aapl_plot_div, 'msft_plot_div': msft_plot_div,'goog_plot_div': goog_plot_div })


def aapl(request):
    aapl_close = yahooFinance.download("AAPL", period="1y", actions=True).Close
    aapl_date = aapl_close.index
    x_data = aapl_date
    y_data = aapl_close
    aapl_plot_div = plot([Scatter(x=x_data, y=y_data,
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
                output_type='div')
    
    return render(request, 'aapl.html', {'aapl_plot_div': aapl_plot_div,})

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