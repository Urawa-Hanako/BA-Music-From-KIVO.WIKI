import requests
import re

def clean_filename(filename):
    # 使用正则表达式替换 windows 文件名中的无效字符
    return re.sub(r'[<>:"/\\|?*]', '_', filename)

for i in range(451, 602): # 目前有450首歌曲
    url = 'https://api.kivo.wiki/api/v1/musics/' + str(i)

    response = requests.get(url, timeout=10)  # 设置请求超时
    response.encoding = 'utf-8'  # 设置编码
    api_data = response.json()  # 解析json数据
    # print(api_data)

    try:
        title = api_data['data']['title']
        title = clean_filename(title)  # 清理文件名
        download_url = 'https:' + api_data['data']['file']
    except:
        print(f'歌曲{i}下载失败')
        continue  # 跳过下载失败的歌曲（结束本轮i循环）

    print(f'开始下载{title}')  # 添加日志输出
    with open('E:/音乐/BlueArchive/' + title + '.ogg', 'wb') as f: # 注意\需要转义，文件路径中也可以使用/或\\
        f.write(requests.get(download_url).content)  # 写入歌曲文件
print('下载完成')


# 用BeautifulSoup解析网页内容:

# from bs4 import BeautifulSoup

# # 解析网页内容
# soup = BeautifulSoup(response.text, 'html.parser')

# print(soup.prettify())  # 打印网页内容

# # 假设歌曲信息在某个特定的标签里
# songs = soup.find_all('div', class_='song-item')  # 替换为实际的标签和类名

# for song in songs:
#     title = song.find('h2').text  # 替换为实际的标签
#     link = song.find('a')['href']  # 获取链接
#     print(f'歌曲名: {title}, 链接: {link}')

# # 注意遵循网站的爬虫规则，检查robots.txt文件