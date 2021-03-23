from pprint import pprint
import boto3
from botocore.exceptions import ClientError


def get_quote(quote, author, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('quotes')

    try:
        response = table.get_item(Key={'author': author, 'quote': quote})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Item']


if __name__ == '__main__':
    quote = get_quote("Example quote", "Example author")
    if movie:
        print("Get quote succeeded:")
        pprint(quote, sort_dicts=False)