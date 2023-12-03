from yelpapi import YelpAPI
import pandas as pd

api_key = "PUVzI9rX-O-jw9WulF8DIwnENCMtrIGmLlAFt6YYeexFL_1lc-r203Q8FZ4rXYu_1V6UbVrE-iytHR4pAOjitj9sdciRfss6jv54KzOtfhfnxL3cZu2EWFpPg0pMZXYx"

yelp_api_instance = YelpAPI(api_key)
search_term = 'pizza'
location_term = 'El Paso, TX'

serach_results = yelp_api_instance.search_query(
    term = search_term, location=location_term,
   sort_by = 'rating', limit=20, offset = 20) #limit would give you 20 and offset would give you the next 20
print(serach_results)

result_df = pd.DataFrame.from_dict(serach_results['businesses'])
result_df.to_csv('api_results.csv', index=False)

for business in serach_results ['businesses']:
    print('\n')
    print(business)

id_for_review = 'little-habana-el-paso' ##do 5 business
review_response = yelp_api_instance.reviews_query(id=id_for_review)
for review in review_response['reviews']:
    print('\n')
    print(review)

review_df = pd.DataFrame.from_dict(review_response['businesses'])
review_df.to_csv('api_review.csv', index=False)

#CASA Practice
from bs4 import beutifulsuop
import requests
web_url = 'https://www.utep.edu/business/people/faculty-profiles.html'
page_to_scrape = requests.get(web_url)

soup = beutifulsuop(page_to_scrape.text,'html.parser')
