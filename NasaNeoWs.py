import requests
import json
import dotenv
dotenv.load_dotenv(dotenv.find_dotenv())
def getURL(StartDate, EndDate):
    url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={StartDate}&end_date={EndDate}&api_key={dotenv.get_key(dotenv.find_dotenv(), 'NASA_KEY')}"
    return url

def getNEOData():
    startDate = ""
    endDate = ""
    while startDate == "" or endDate == "" or startDate > endDate or startDate < "1900-01-01" or endDate > "2099-12-31" or startDate > "2099-12-31" or endDate < "1900-01-01":
            startDate = input("Enter the start date (YYYY-MM-DD): ")
            endDate = input("Enter the end date (YYYY-MM-DD)(Can't be more than 7 days after start date): ")

    url = getURL(startDate, endDate)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f" Data from {startDate} to {endDate}: ")
        print(f"Amount of NEOs: {data['element_count']}")
        for dates in data['near_earth_objects']:
            print(f"Date: {dates}")
            for neo in data['near_earth_objects'][dates]:
                print(f"Name: {neo['name']}, Diameter: {neo['estimated_diameter']['meters']['estimated_diameter_max']} meters, Potentially Hazardous: {neo['is_potentially_hazardous_asteroid']}")
    else:
        print(f"Error: {response.status_code} - {response.text}")

getNEOData()
