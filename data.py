import requests
import json

base_url = 'https://jobs.github.com/positions.json'
params = {
    'description': 'python',
    'location': 'new york'
}
headers = {
    'Content-Type': 'application/json'
}


def getJobListings():
    """Retrive data from Github API"""
    r = requests.get(base_url, params=params, headers=headers)
    return(r.json())


jobs = getJobListings()
