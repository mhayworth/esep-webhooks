import json
import requests

def lambda_handler(event, context):
    message = event.get('issue').get('html_url')

    url = 'super secret url'

    resp = requests.post(url, message)
    
    return resp
