import requests
import re

save_path = 'E:/音乐/BlueArchive' # 保存路径(注意\需要转义，文件路径中也可以使用/或\\)
ids = range(1, 602)  # 要下载的歌曲 id 范围

def clean_filename(filename):
    # 使用正则表达式替换 windows 文件名中的无效字符
    return re.sub(r'[<>:"/\\|?*]', '_', filename)

for id in ids:
    url = 'https://api.kivo.wiki/api/v1/musics/' + str(id)

    response = requests.get(url, timeout=10)  # 设置请求超时
    response.encoding = 'utf-8'  # 设置编码
    api_data = response.json()  # 解析json数据
    # print(api_data)

    try:
        title = api_data['data']['title']
        title = clean_filename(title)  # 清理文件名
        download_url = 'https:' + api_data['data']['file']
    except:
        print(f'歌曲{id}下载失败')
        continue

    print(f'开始下载{title}')
    with open(save_path + '/' + title + '.ogg', 'wb') as f:
        f.write(requests.get(download_url).content)
print('下载完成')
