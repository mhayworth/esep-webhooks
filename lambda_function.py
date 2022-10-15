import requests

def lambda_handler(event, context):
    message = "Issue Created: " + event['issue']['html_url']

    url = 'super secret url'

    requests.post(url, json = {"text":message})
