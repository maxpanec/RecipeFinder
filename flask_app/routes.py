from flask import Blueprint, jsonify, request, session
import requests
from bs4 import BeautifulSoup
import flask_app.scrape as scrape

main = Blueprint('main', __name__)

@main.route('/scrape', methods = ["GET"])
def search_item():
    if request.method=='POST':
        search_data=request.get_json()
        search_item=search_data['search_item']
        return "Done", 201
    elif request.method=="GET":
        args = request.args
        data = {}
        try:
            websites = {
                'allrecipes': args['allrecipes'],
                'epicurious': args['epicurious'],
                'bonappetit': args['bonappetit'],
                'foodnetwork': args['foodnetwork'],
                'search': args['search'],
                'range' : args['range']
            }
            data = scrape.scrapeInfo(websites)
        except KeyError:
            return "Missing Parameter", 400
        return jsonify(data), 200
