# We need to import request to access the details of the POST request
# and render_template, to render our templates (form and response)
# we'll use url_for to get some URLs for the app on the templates
import sys, codecs
reload(sys)
sys.setdefaultencoding('utf-8')
import sqlite3 as sql
from flask import Flask, json, render_template, request, url_for,jsonify
import pygal
from pygal.style import BlueStyle
# Initialize the Flask application
app = Flask(__name__)

@app.route('/')
def form():
    ss = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    bar_chart = pygal.Bar(style=BlueStyle)                                            # Then create a bar graph object
    bar_chart.add('Fibonacci',ss )  # Add some values
    bar_chart.render_to_file('static/bar_chart.svg')                          # Save the svg to a file
    return render_template('bar.html')

# Run the app :)
if __name__ == '__main__':
  app.run(
        host="0.0.0.0",
        port=int("5002")
  )