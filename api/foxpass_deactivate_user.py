#!/usr/bin/env python

"""
This script requires the external libraries from requests
pip install requests

To run:
python foxpass_deactivate_user.py --api-key <api_key> --user <username>
"""
import argparse
import json
import requests

URL = 'https://api.foxpass.com/v1/'
ENDPOINT = 'users/'
DATA = {'is_active': False}

def main():
    parser = argparse.ArgumentParser(description='List groups in Foxpass')
    parser.add_argument('--api-key', required=True, help='Foxpass API Key')
    parser.add_argument('--user', required=True, help='Foxpass username')
    args = parser.parse_args()

    header = {'Authorization': 'Token ' + args.api_key}
    r = requests.put(URL + ENDPOINT + args.user + '/', headers=header, data=json.dumps(DATA))
    print r.json()

if __name__ == '__main__':
    main()