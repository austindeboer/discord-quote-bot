from decimal import Decimal
import json
import boto3


def load_quotes(quotes, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('quotes')
    for q in quotes:
        author = q['author']
        quote = q['quote']
        print("Adding quote:", author, quote)
        table.put_item(Item=q)


if __name__ == '__main__':
    with open("quotedata.json") as json_file:
        quote_list = json.load(json_file, parse_float=Decimal)
    load_quotes(quote_list)