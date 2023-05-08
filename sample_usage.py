import csv_to_dynamodb

table = csv_to_dynamodb.create_table(
    access_key='your_access_key',
    secret_key='your_secret_key',
    region='us-east-1',
    csv_path='path/to/sample.csv',
    table_name='sample_table'
)
