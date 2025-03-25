import requests, os

url = 'https://oxhcuvzcbzfpsiujftzq.supabase.co/rest/v1/electricity_usage'
API_KEY = os.environ.get("API_KEY")
SECRET_KEY = os.environ.get("SECRET_KEY")

def get_forbrug_api():
    header = {
        "apikey": API_KEY,
        "Content-Type": "application/json"
    }

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
        return response_extracted
    else:
        return {
            "error": "Failed to fetch data from API", "status_code": response.status_code
        }
