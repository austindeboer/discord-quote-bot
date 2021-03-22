import boto3

def create_quote_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.create_table(
        TableName='Quotes',
        KeySchema=[
            {
                'AttributeName': 'author',
                'KeyType': 'HASH'  # Partition key
            },
            {
                'AttributeName': 'quote',
                'KeyType': 'RANGE'  # Sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'author',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'quote',
                'AttributeType': 'S'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )
    return table


if __name__ == '__main__':
    quote_table = create_quote_table()
    print("Table status:", quote_table.table_status)