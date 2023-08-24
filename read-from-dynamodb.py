import boto3

def lambda_handler(event, context):
    # Initialize DynamoDB client
    dynamodb = boto3.client('dynamodb')
    
    # Specify the table name
    table_name = 'waf-test-block-db'
    
    try:
        # Scan the table to retrieve all items
        response = dynamodb.scan(TableName=table_name)
        
        # Extract and print the ClientIP from each item
        for item in response['Items']:
            client_ip = item['ClientIP']['S']
            print(f"ClientIP: {client_ip}")
    
    except Exception as e:
        print("An error occurred:", str(e))
    
    return {
        'statusCode': 200,
        'body': 'Function executed successfully.'
    }
