import json, config
from requests_oauthlib import OAuth1Session

MY_ID = config.TWITTER_ID
AK = config.API_KEY
AS = config.API_SECRET_KEY
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET


def get_api_url(ID):
  url = f"https://api.twitter.com/2/users/{ID}/tweets"
  return url

def get_tweet(get_tweet_number, auth, url):
  params = {
    'expansions'  : 'author_id',
    'tweet.fields': 'created_at,public_metrics',
    'user.fields' : 'name',
    'max_results' : get_tweet_number
  }
  res = auth.get(url, params = params)
  return res


def display_tweet(res):
  if res.status_code == 200:
    tl = json.loads(res.text)

    for l in tl['data']:
      print('----------------------------')
      print(l['text'])
      print(l['created_at'])

  else:
      print("Failed: %d" % res.status_code)

ID = "169480493" # @nikkei
n = 5 # 件数セット

auth = OAuth1Session(AK, AS, AT, ATS)
url = get_api_url(ID)
res = get_tweet(n, auth, url)
display_tweet(res)