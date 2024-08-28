import requests

# API endpoint
api_url = 'https://jobicy.com/api/v2/remote-jobs?count=50'

# Make the API call
response = requests.get(api_url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    print(data)
    
    #since i wanted only jobs object
    jobs = data.get('jobs', [])
    print(jobs)
else:
    print("Failed to fetch data from API")