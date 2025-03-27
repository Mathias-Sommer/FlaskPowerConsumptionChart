from flask import Flask, render_template, request, jsonify
from api import get_forbrug_api
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/forbrugsrapport')
def forbrugsrapport():
    api_data = get_forbrug_api()
    
    print("API:", api_data)

    return render_template('forbrugsrapport.html', data=api_data)

@app.route('/grafer')
def grafer():
    return render_template('grafer.html')

@app.route("/get_data", methods=["GET"])
def GET_DATA():
    data = get_forbrug_api()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)