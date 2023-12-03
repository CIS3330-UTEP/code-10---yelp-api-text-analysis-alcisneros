from yelpapi import YelpAPI
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

api_key = "PUVzI9rX-O-jw9WulF8DIwnENCMtrIGmLlAFt6YYeexFL_1lc-r203Q8FZ4rXYu_1V6UbVrE-iytHR4pAOjitj9sdciRfss6jv54KzOtfhfnxL3cZu2EWFpPg0pMZXYx"

yelp_api_instance = YelpAPI(api_key)
search_term = 'coffee'
location_term = 'El Paso, TX'

serach_results = yelp_api_instance.search_query(
    term = search_term, location=location_term,
   sort_by = 'rating', limit=20, offset = 20) 
print(serach_results)

result_df = pd.DataFrame.from_dict(serach_results['businesses'])
result_df.to_csv('api_results2.csv', index=False)

for business in serach_results ['businesses']:
    print('\n')
    print(business)
# 1
id_for_review = 'game-vault-game-store-and-cafe-el-paso' 
review_response = yelp_api_instance.reviews_query(id=id_for_review)
for review in review_response['reviews']:
    print('\n')
    print(review)
review_df = pd.DataFrame.from_dict(review_response['reviews'])
review_df.to_csv('api_review_game.csv', index=False)

analyzer = SentimentIntensityAnalyzer()
reviews = open('api_review_game.csv')
for review in reviews:
    print(reviews)
    sentiment_score = analyzer.polarity_scores(reviews)
    print(sentiment_score)

#2
id_for_review = 'lucys-coffee-shop-el-paso' 
review_response = yelp_api_instance.reviews_query(id=id_for_review)
for review in review_response['reviews']:
    print('\n')
    print(review)
review_df = pd.DataFrame.from_dict(review_response['reviews'])
review_df.to_csv('api_review_lucys.csv', index=False)

analyzer = SentimentIntensityAnalyzer()
reviews = open('api_review_lucys.csv')
for review in reviews:
    print(reviews)
    sentiment_score = analyzer.polarity_scores(reviews)
    print(sentiment_score)

# 3
id_for_review = 'cocol-cafe-socorro' 
review_response = yelp_api_instance.reviews_query(id=id_for_review)
for review in review_response['reviews']:
    print('\n')
    print(review)
review_df = pd.DataFrame.from_dict(review_response['reviews'])
review_df.to_csv('api_review_cocol.csv', index=False)

analyzer = SentimentIntensityAnalyzer()
reviews = open('api_review_cocol.csv')
for review in reviews:
    print(reviews)
    sentiment_score = analyzer.polarity_scores(reviews)
    print(sentiment_score)

# 4
id_for_review = 'hala-coffee-and-hookah-sweets-el-paso' 
review_response = yelp_api_instance.reviews_query(id=id_for_review)
for review in review_response['reviews']:
    print('\n')
    print(review)
review_df = pd.DataFrame.from_dict(review_response['reviews'])
review_df.to_csv('api_review_hala.csv', index=False)

analyzer = SentimentIntensityAnalyzer()
reviews = open('api_review_hala.csv')
for review in reviews:
    print(reviews)
    sentiment_score = analyzer.polarity_scores(reviews)
    print(sentiment_score)

# 5
id_for_review = 'cofismo-el-paso' 
review_response = yelp_api_instance.reviews_query(id=id_for_review)
for review in review_response['reviews']:
    print('\n')
    print(review)
review_df = pd.DataFrame.from_dict(review_response['reviews'])
review_df.to_csv('api_review_cofismo.csv', index=False)

analyzer = SentimentIntensityAnalyzer()
reviews = open('api_review_cofismo.csv')
for review in reviews:
    print(reviews)
    sentiment_score = analyzer.polarity_scores(reviews)
    print(sentiment_score)