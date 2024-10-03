import requests
import pandas as pd

url = 'https://gist.github.com/ahmu83/38865147cf3727d221941a2ef8c22a77/raw/c647f74643c0b3f8407c28ddbb599e9f594365ca/US_States_and_Cities.json'

try:
    # Fetch the JSON data
    response = requests.get(url)
    data = response.json()

    # Prepare the data for CSV
    rows = []
    for sate, cities in data.items():
        for city in cities:
            rows.append({'state': sate, 'city': city})

    # create a DataFrame and save CSV
    df = pd.DataFrame(rows)
    df.to_csv('states_and_cities.csv', index=False)

    print("CSV file has been created successfully.")
    
except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
except ValueError as e:
    print(f"Error processing JSON data: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")