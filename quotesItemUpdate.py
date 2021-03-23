from decimal import Decimal
from pprint import pprint
import boto3


def update_quote(quote, author, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('quotes')

    response = table.update_item(
        Key={
            'quote': quote,
            'author': author
        },
        UpdateExpression="set info.quote=:q,",
        ExpressionAttributeValues={
            ':q': quote,
        },
        ReturnValues="UPDATED_NEW"
    )
    return response


if __name__ == '__main__':
    update_response = update_quote(
        "Example quote", "Example author",)
    print("Update quote succeeded:")
    pprint(update_response, sort_dicts=False)