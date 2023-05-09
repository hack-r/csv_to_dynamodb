import sys 
from csv_to_dynamodb import populate_table

access_key = 'YOUR_KEY'
secret_key = 'YOUR_SECRET_KEY'
region = 'YOUR_REGION'
csv_file_path = 'sample_data2.csv'

populate_table(access_key, secret_key, region, csv_file_path)
