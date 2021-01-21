# GeoJSONインポーター v0.2
import glob     # フォルダ内のファイルの一覧を取得用モジュール

import json
from collections import OrderedDict
import pprint

import googlemaps
import csv
import time

googleapikey = ' >>>APIkey<<< '
gmaps = googlemaps.Client(key=googleapikey)

# Geocoding 処理
def geocordingByGoogleMaps(address4geocode):
    result = gmaps.geocode(address4geocode)
    lat = result[0]["geometry"]["location"]["lat"]
    lng = result[0]["geometry"]["location"]["lng"]
    addressresult = result[0]["address_components"]["long_name"]
    print (address4geocode,lat,lng,addressresult)
    time.sleep(0.5)
    return()

# 指定したGeoJSONファイル内の address 属性 value を表示
def getGeoJSONaddress(filepath):
    with open(filepath) as f:
        src = json.load(f) # JSON形式の文字列を辞書型で取得
        ii = 0
        for i in src.get('features'):
            ftr = src.get('features')[ii]    # n番目のフィーチャー    	
            prop = ftr.get('properties')    # property情報の取得 
            #print(prop['address'])  # 住所属性 address をキーに n番目のフィーチャーの住所情報を引っ張り出す
            geocordingByGoogleMaps(prop['address'])
            ii = ii+1  # iiのインクリメント
    return()


# 指定されたディレクトリ内のファイル情報を取得する関数
def getallfilesinfolder(path):
	files = glob.glob(path) # カレントディレクトリ内のGCPsフォルダに入っているファイルをすべて選択
	for file in files:
		print(file)
		getGeoJSONaddress(file)
	return()



#getallfilesinfolder("./GCPs/*.geojson")  # 対象をGCPsフォルダ内すべてのGeoJSONファイルとする本番用
getallfilesinfolder("./GCPshoge/*.geojson")  # 対象をテスト用 GCPshoge フォルダ内のすべてのGeoJSONファイルとする実験コマンド
 