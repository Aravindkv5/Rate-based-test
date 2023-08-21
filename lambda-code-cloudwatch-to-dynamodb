import json
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table_name = 'waf-test-block-db'  # Replace with your DynamoDB table name
    table = dynamodb.Table(table_name)
    
    for record in event['records']:
        log_payload = json.loads(record['message'])
        
        # Extract relevant information from the log payload
        client_ip = log_payload['httpRequest']['clientIp']
        country = log_payload['httpRequest']['country']
        user_agent = log_payload['httpRequest']['headers'][2]['value']
        request_uri = log_payload['httpRequest']['uri']
        
        # Create a DynamoDB item with the extracted data
        item = {
            'ClientIP': client_ip,
            'Country': country,
            'UserAgent': user_agent,
            'RequestURI': request_uri
        }
        
        # Add the log data to DynamoDB
        table.put_item(Item=item)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Log data processed and added to DynamoDB')
    }
