import requests

headers = {
    'authority': 'www.upwork.com',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    'x-odesk-user-agent': 'oDesk LM',
    'sec-ch-ua-mobile': '?0',
    'accept': 'application/json, text/plain, */*',
    'x-oauth2-required': 'true',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.upwork.com/ab/jobs/search/?sort=recency&subcategory2_uid=531770282593251331,531770282589057038,531770282589057039,531770282593251329,1301900647896092672,531770282589057025,531770282589057028,531770282584862733,531770282597445646',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'master_access_token=efbf956d.oauth2v2_43b02d52aa43c7b9c747ba6aaeaf37f0'
}

params = (
    ('initial_request', 'true'),
    ('per_page', '10'),
    ('sort', 'recency'),
    ('subcategory2_uid', '531770282593251331,531770282589057038,531770282589057039,531770282593251329,1301900647896092672,531770282589057025,531770282589057028,531770282584862733,531770282597445646'),
)

response = requests.get('https://www.upwork.com/ab/jobs/search/url', headers=headers, params=params)
json_response = response.json()
jobs = json_response['searchResults']['jobs']

for j in jobs:
    print('{} - {}'.format(j['title'], j['createdOn']))

print('number of jobs: {}'.format(len(jobs)))
print(json_response['searchResults']['paging'])

# print(json_response['searchResults']['jobs'])

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://www.upwork.com/ab/jobs/search/url?initial_request=true&per_page=10&sort=recency&subcategory2_uid=531770282593251331,531770282589057038,531770282589057039,531770282593251329,1301900647896092672,531770282589057025,531770282589057028,531770282584862733,531770282597445646', headers=headers)
