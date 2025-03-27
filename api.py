import requests, os
from flask import jsonify

url = 'https://oxhcuvzcbzfpsiujftzq.supabase.co/rest/v1/electricity_usage'
API_KEY = os.environ.get("API_KEY")
SECRET_KEY = os.environ.get("SECRET_KEY")

header = {
        "apikey": API_KEY,
        "Content-Type": "application/json"
    }

def get_forbrug_api():
    response = requests.get(url, headers=header)
    if response.status_code == 200:
        response_extracted = []
        
        for row in response.json():
            response_extracted.append({
                'id': row.get('id'),
                'upload_date': row.get('upload_date'),
                'uge_forbrug': row.get('uge_forbrug'),
                'data_source': row.get('data_source'),
                'tidligere_uge_forbrug': row.get('tidligere_uge_forbrug'),
                'date': row.get('date')
            })

        response_extracted.sort(key=lambda x: x['id']) #sorter fra A-Z på ID.
        return response_extracted
    else:
        return {
            "error": "Failed to fetch data from API", "status_code": response.status_code
        }

def data_for_chart():
    response = requests.get(url, headers=header)
    
    if response.status_code == 200:
        data = response.json()

        data.sort(key=lambda x: x.get('date'))
        
        # Extract `date` and `uge_forbrug` values
        labels = [row.get('date') for row in data]
        values = [float(row.get('uge_forbrug').replace(',', '.')) for row in data]  # Convert to float

        return jsonify({
            "labels": labels,
            "datasets": [{
                "label": "Dagligt forbrug (kWh)",
                "data": values,
                "borderColor": "rgba(54, 162, 235, 1)",  
                "backgroundColor": "rgba(54, 162, 235, 0.2)",
                "borderWidth": 2,
                "fill": True
            }]
        })
    else:
        return jsonify({"error": "Failed to fetch data", "status_code": response.status_code})
