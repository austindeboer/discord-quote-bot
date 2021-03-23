from pprint import pprint
import boto3


def put_quote(quote, author, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('Quotes')
    response = table.put_item(
       Item={
            'author': author,
            'quote': quote,
        }
    )
    return response


if __name__ == '__main__':
    quote_resp = put_quote("Example Quote", "Example Author")
    print("Put quote succeeded:")
    pprint(quote_resp, sort_dicts=False)