from dotenv import load_dotenv
import os

def configure():
    load_dotenv()

def main():
    configure()


def get_api():
    url = f'https://maps.googleapis.com/maps/api/place/details/output?parameters{os.getenv("api_key")}'

params = {
  "q": "car wash",
  "location": "utah, United States",
  "hl": "en",
  "gl": "us",
  "google_domain": "google.com",
  "api_key": "secret_api_key"
}

search = GoogleSearch(params)
results = search.get_dict()

main()