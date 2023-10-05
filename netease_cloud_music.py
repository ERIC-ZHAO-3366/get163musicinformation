import requests

def get_song_info(song_id):
    url = f'http://music.163.com/api/song/detail/?id={song_id}&ids=[{song_id}]'
    headers = {
        'Referer': 'https://music.163.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data['songs'][0]
    else:
        print(f'Error: {response.status_code}')
        return None

if __name__ == '__main__':
    song_id = input('请输入歌曲ID:')
    song_info = get_song_info(song_id)
    if song_info:
        print(f"歌曲名：{song_info['name']}")
        print(f"歌手：{song_info['artists'][0]['name']}")
        print(f"专辑：{song_info['album']['name']}")
        print(f"时长：{song_info['duration']}秒")
    else:
        print("获取歌曲信息失败")
