import requests

cookies = {
    'Hm_lvt_cdb524f42f0ce19b169a8071123a4797': '1710839732,1711007963',
    '_ga': 'GA1.2.1545164685.1705456225',
    '_ga_ETPBRPM9ML': 'GS1.2.1711007963.3.1.1711010614.60.0.0',
    'Hm_Iuvt_cdb524f42f23cer9b268564v7y735ewrq2324': 'ncmNniFcJKydRCX7esEhQJCMXB5fZT84',
    'Hm_lpvt_cdb524f42f0ce19b169a8071123a4797': '1711007982',
    '_gid': 'GA1.2.1849104302.1711007963',
    '_gat': '1',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    # 'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    # 'Referer': 'http://www.kuwo.cn/search/list?key=%E5%91%A8%E6%B7%B1',
    # 'Cookie': 'Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1710839732,1711007963; _ga=GA1.2.1545164685.1705456225; _ga_ETPBRPM9ML=GS1.2.1711007963.3.1.1711010614.60.0.0; Hm_Iuvt_cdb524f42f23cer9b268564v7y735ewrq2324=ncmNniFcJKydRCX7esEhQJCMXB5fZT84; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1711007982; _gid=GA1.2.1849104302.1711007963; _gat=1',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}

response = requests.get(
    'http://www.kuwo.cn/search/searchMusicBykeyWord?vipver=1&client=kt&ft=music&cluster=0&strategy=2012&encoding=utf8&rformat=json&mobi=1&issubtitle=1&show_copyright_off=1&pn=0&rn=20&all=%E5%91%A8%E6%B7%B1',
    cookies=cookies,
    headers=headers,
)

abslist = response.json()['abslist']

for song in abslist:
    album_id = song['ALBUMID']
    music_id = song['MUSICRID'].replace('MUSIC_', '')
    song_name = song['NAME']
    song_artist = song['ARTIST']
    print(album_id, music_id, song_name, song_artist)
