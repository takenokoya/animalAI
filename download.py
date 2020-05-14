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

# コマンド実行の際の2番めの引数をanimal_nameに代入
animal_name = sys.argv[1]
# 保存フォルダ指定
save_dir = './' + animal_name

# flickrクライアント
flickr = FlickrAPI(key, secret, format='parsed-json')

# 検索を実行
result = flickr.photos.search(
    text=animal_name,
    per_page=400,
    media='photos',
    sort='relevance',
    safe_search=1,
    extras='url_q, licence'
)

photos = result['photos']
# pprint(photos)

# APIからの取得結果を特定のファイルに保存する
for i, photo in enumerate(photos['photo']):
    url_q = photo['url_q']
    file_path = save_dir + '/' + photo['id'] + '.jpg'
    if os.path.exists(file_path): continue
    # ネット上からファイルをダウンロードし保存するのにurlretrieveを使う
    # arg: 目的のurl, 保存先のファイル名
    urlretrieve(url_q, file_path)
    # ファイルのダウンロード後に1秒の実行遅延をいれる
    time.sleep(wait_time)
