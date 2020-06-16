from flask import Flask, request 
import pandas as pd 

# call data source
catalogues = pd.read_csv("data/books_c.csv")

# get list of books with above average rating
average_total = round(catalogues.average_rating.mean(),3)
above_average = catalogues[catalogues['average_rating'] >= average_total]

# get list of books published in english language
english = catalogues[(catalogues['language_code'] == "eng") | (catalogues['language_code'] == "en-US") |  
(catalogues['language_code'] == "en-CA")]

# get list of books published in non-english language
non_english = catalogues[(catalogues['language_code'] != "eng") & (catalogues['language_code'] != "en-US") &  
(catalogues['language_code'] != "en-CA")]

app = Flask(__name__) 

@app.route('/')
def welcome():
    return '''<h1> Selamat Datang </h1>'''

# get complete list of books
@app.route('/data/get/catalogues', methods=['GET']) 
def get_catalogues():
    return (catalogues.to_json())

# get list of books with above average rating
@app.route('/data/get/above_average', methods=['GET']) 
def get_above_average(): 
    return (above_average.to_json())

# get list of books with english language
@app.route('/data/get/english', methods=['GET']) 
def get_english(): 
    return (english.to_json())

# get list of books with non-english language
@app.route('/data/get/non_english', methods=['GET']) 
def get_non_english(): 
    return (non_english.to_json())

@app.route('/data/get/equal/catalogues/<column>/<value>', methods=['GET']) 
def get_data_equal(catalogues, column, value):
    data = catalogues 
    mask = data[column] == value
    data = data[mask]
    return (data.to_json())

if __name__ == '__main__':
    app.run(debug=True, port=5000) 
