from ast import Num
from flask import Flask, request
import googlemaps

# Read the number from the file
with open('api_key.txt', 'r') as f:
  apiKeyInTxtFile = f.read()

api_key = apiKeyInTxtFile

app = Flask(__name__)

@app.route('/find-nearby-places')
def find_nearby_places():
  # Get the place type, radius, and location from the query parameters
  place_type = request.args.get('place_type')
  radius = request.args.get('radius')
  location = request.args.get('location')

  # Create a client
  gmaps = googlemaps.Client(key=api_key)

  # Use the nearby search API to find nearby places
  places = gmaps.places_nearby(location=location, radius=radius, type=place_type)

  # Return the names of the places as a JSON object
  return {'places': [place['name'] for place in places['results']]}

if __name__ == '__main__':
  app.run()
