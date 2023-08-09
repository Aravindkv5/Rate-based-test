import boto3
import re

def lambda_handler(event, context):
    waf_client = boto3.client('waf-regional')
    waf_client = boto3.client('waf-regional', region_name='ap-south-1')


    ip_set_name = 'block-test'

    print("Listing IP sets:")
    ip_sets = waf_client.list_ip_sets()
    print(ip_sets)

    ip_set_id = 'None'
    for ip_set in ip_sets['IPSets']:
        if ip_set['Name'] == ip_set_name:
            ip_set_id = ip_set['IPSetId']
            break

    if not ip_set_id:
        print(f"IP set '{ip_set_name}' not found.")
        return {
            'statusCode': 400,
            'body': 'IP set not found.'
        }

    print(f"IP set '{ip_set_name}' found with ID: {ip_set_id}")

    # Rest of the code to extract blocked IPs and update the IP set...

    return {
        'statusCode': 200,
        'body': 'IPs added to IP set.'
    }
