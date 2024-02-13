from django.shortcuts import render
from django.http import HttpResponse
import yfinance as yahooFinance
from plotly.offline import plot
from plotly.graph_objs import Scatter
import plotly.express as px
from .forms import TickerForm




def index(request):
    form = TickerForm(request.GET or None)
    



    aapl_close = yahooFinance.download("AAPL", period="1y", actions=True).Close
    aapl_last_quote = round(aapl_close.iloc[-1], 2)
    aapl_date = aapl_close.index
    aapl_x_data = aapl_date
    aapl_y_data = aapl_close
    fig_appl = px.line(
        x=aapl_x_data,
        y=aapl_y_data,
        title="Apple",
    ).update_layout(xaxis_title="Date", yaxis_title="Close Price")
    appl_chart = fig_appl.to_html()

    msft_close = yahooFinance.download("MSFT", period="1y", actions=True).Close
    msft_last_quote = round(msft_close.iloc[-1], 2)
    msft_date = msft_close.index
    msft_x_data = msft_date
    msft_y_data = msft_close
    fig_msft = px.line(
        x=msft_x_data,
        y=msft_y_data,
        title="Microsoft"
    ).update_layout(xaxis_title="Date", yaxis_title="Close Price")
    
    msft_chart = fig_msft.to_html()

    goog_close = yahooFinance.download("GOOG", period="1y", actions=True).Close
    goog_last_quote = round(goog_close.iloc[-1], 2)
    goog_date = goog_close.index
    goog_x_data = goog_date
    goog_y_data = goog_close
    fig_goog = px.line(
        x=goog_x_data,
        y=goog_y_data,
        title="Google"
    ).update_layout(xaxis_title="Date", yaxis_title="Close Price")
    goog_chart = fig_goog.to_html()


    if request.method == "GET" and form.is_valid():  # Check if form is submitted and valid
        ticker = form.cleaned_data["company"]

        if ticker == "2":
            return render(request, 'index.html', {'aapl_plot_div': appl_chart, "aapl_last_quote":aapl_last_quote, 
                                        "msft_last_quote":msft_last_quote,
                                        "goog_last_quote":goog_last_quote,
                                        "form":form})
        elif ticker == "3":
            return render(request, 'index.html', {'msft_plot_div': msft_chart, "aapl_last_quote":aapl_last_quote, 
                                        "msft_last_quote":msft_last_quote,
                                        "goog_last_quote":goog_last_quote,
                                        "form":form})
        elif ticker == "4":
            return render(request, 'index.html', {'goog_plot_div': goog_chart,"aapl_last_quote":aapl_last_quote, 
                                        "msft_last_quote":msft_last_quote,
                                        "goog_last_quote":goog_last_quote,
                                        "form":form})

        
        

    return render(request, 'index.html', {
                                        "aapl_last_quote":aapl_last_quote, 
                                        "msft_last_quote":msft_last_quote,
                                        "goog_last_quote":goog_last_quote,
                                        "form":form})


