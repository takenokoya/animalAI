from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os, time, sys
from os.path import join, dirname
from dotenv import load_dotenv


# 環境変数
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# APIキーの情報
key = os.environ.get('API_KEY')
secret = os.environ.get('API_SECRET')
wait_time = 1

# 保存フォルダ指定
animalname = sys.argv[1]
savedir = './' + animalname

# flickrクライアント
flickr = FlickrAPI(key, secret, format='parsed-json')

# 検索を実行
result = flickr.photos.search(
    text=animalname,
    per_page=400,
    media='photos',
    sort='relevance',
    safe_search=1,
    extras='url_q, licence'
)

photos = result['photos']
pprint(photos)
