
# Import Flask packages
import os
from re import L
import requests
import json
from flask import Flask, request, Response
from flask_cors import CORS, cross_origin


# Define an instance of Flask object
app = Flask(__name__)
CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'

""" Stocks for investment strategies"""

# Stocks as per the intense study and survey based on the strategies
ethical_investing = ["AAPL", "TSLA", "ADBE"]
growth_investing = ["OXLC", "ECC", "AMD"]
index_investing = ["VOO", "VTI", "ILTB"]
quality_investing = ["NVDA", "MU", "CSCO"]
value_investing = ["INTC", "BABA", "GE"]


def get_stock_quote(stock_list):
    """Function that calls stock API for each stock to fetch stock details"""

    # Filter defining the data requirement
    param_filter = '?filter=symbol,companyName,latestPrice,latestTime,change,changePercent'

    stock_quote = []

    # Loopping through given stock and appending data to result
    for ticker in stock_list:
        # HTTP GET call to stock API
        resp = requests.get("https://financialmodelingprep.com/api/v3/quote/{}?apikey=aab6fab8b982956be313a36d56ed0e09".format(ticker))
        
        response = {}
        resp = resp.json()
        resp = resp[0]
        
        response["symbol"] = resp["symbol"]
        response["companyName"] = resp["name"]
        response["latestPrice"] = resp["price"]
        response["latestTime"] = resp["timestamp"]
        response["change"] = resp["change"]
        response["changePercent"] = resp["changesPercentage"]
        
        stock_quote.append(response)

    return stock_quote


@app.route('/getData', methods=['POST'])
@cross_origin(origin='*')
def return_data():
    Strategies = request.json['Strategies']
    Amount = request.json['Amount']

    response = []
    amt1 = Amount*0.5
    amt2 = Amount*0.30
    amt3 = Amount*0.20
    responseAmount = []

    responseAmount.append(amt1)
    responseAmount.append(amt2)
    responseAmount.append(amt3)
    

    for x in Strategies:
        print("x",x)
        if x == "Ethical Investing":
            response.append(get_stock_quote(ethical_investing))
        elif x == "Growth Investing":
            response.append(get_stock_quote(growth_investing))
        elif x == "Index Investing":
            print("wahhhhh!!!")
            response.append(get_stock_quote(index_investing))
        elif x == "Quality Investing":
            response.append(get_stock_quote(quality_investing))
        elif x == "Value Investing":
            response.append(get_stock_quote(value_investing))
        else:
            response.append("Invalid Strategy")

    # get_stock_quote(value)
    dict1 = {"strategiesResponse": response, "amountResponse": responseAmount}
    response = Response(json.dumps(dict1), mimetype='application/json')
    return response


if __name__ == "__main__":
    app.run(debug=True)
    

