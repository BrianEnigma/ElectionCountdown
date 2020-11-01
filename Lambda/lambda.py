#!/usr/bin/env python3

import date_countdown
import json
import settings


def get_cors(event):
    referer = None
    result = 'https://electioncountdown.org'

    # Grab the Referer header, if it exists.
    try:
        referer = event['headers']['Referer']
    except:
        # referer = None
        referer = ''

    # If it doesn't exist at all, return the default.
    if referer is None:
        return result

    # If it exists and is empty, return all.
    if len(referer) == 0:
        return '*'

    # Try the various domain variants
    try:
        if referer.index('www.electioncountdown.org') >= 0:
            return 'https://www.electioncountdown.org'
    except:
        pass
    try:
        if referer.index('electioncountdown.org') >= 0:
            return 'https://electioncountdown.org'
    except:
        pass
    try:
        if referer.index('www.inaugurationcountdown.org') >= 0:
            return 'https://www.inaugurationcountdown.org'
    except:
        pass
    try:
        if referer.index('inaugurationcountdown.org') >= 0:
            return 'https://inaugurationcountdown.org'
    except:
        pass

    # If it exists and it's the naked bucket without CloudFront in front of it, use that.
    try:
        if referer.index('electioncountdown.org.s3-website-us-west-2.amazonaws.com') >= 0:
            result = 'http://electioncountdown.org.s3-website-us-west-2.amazonaws.com'
    except:
        pass

    return result

def lambda_handler(event, context):
    brief_flag = False
    try:
        brief_flag = int(event['queryStringParameters']['brief']) != 0
    except:
        pass
    countdown = date_countdown.DateCountdown(debug=False)
    result = countdown.get_delta(brief=brief_flag)

    return {
        'statusCode': 200,
        'body': json.dumps(result, indent=4),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': get_cors(event)
            },
        }