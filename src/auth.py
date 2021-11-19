import upwork
import json


def get_tokens():
    with open('keys.json', 'r') as json_file:
        config = json.load(json_file)


    client = upwork.Client(upwork.Config(config))
    token = client.get_request_token()

    print(token)

    verifier = input(
        'Please enter the verification code you get '
        'following this link:\n{0}\n\n> '.format(
            client.get_authorization_url()))

    access_token, access_token_secret = client.get_access_token(verifier)

    print(access_token, access_token_secret)


get_tokens()
