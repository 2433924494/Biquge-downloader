import os
import urllib.request

from lxml import etree

base_url = 'https://www.biquge7.xyz/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
}
Title = ''


def GetBookTitle_chapter(id):
    url = base_url + str(id)
    request = urllib.request.Request(url=url, headers=headers)
    respond = urllib.request.urlopen(request)
    content = respond.read().decode('utf-8')
    tree = etree.HTML(content)
    title = tree.xpath('//div[@class="tit"]/img/@alt')
    global Title
    Title = str(title[0])
    makedir(Title)
    all_chapter = tree.xpath('//div[@class="list"]/ul/li/a/@title')
    return all_chapter


def makedir(name):
    folder = os.getcwd() + '\\' + name + '\\'
    # 获取此py文件路径，在此路径选创建在new_folder文件夹中的test文件夹
    if not os.path.exists(folder):
        os.makedirs(folder)


def download(page):
    global Title
    url = base_url + str(novel_id) + '/' + str(page + 1)
    request = urllib.request.Request(url=url, headers=headers)
    respond = urllib.request.urlopen(request)
    content = respond.read().decode('utf-8')
    tree = etree.HTML(content)
    text = tree.xpath('//div[@class="text"]/text()')
    with open(os.getcwd() + '\\' + Title + '\\' + Title + '.txt', 'a', encoding='utf-8') as fp:
        fp.write(str(chapters[page]))
        fp.write('\n')
        for i in range(0, len(text)):
            fp.write(str(text[i]))
            fp.write('\n\n')
        fp.close()
    print('Chapter ' + str(page + 1) + ':' + str(chapters[page]) + ' Done')


print('请先前往笔趣阁（https://www.biquge7.xyz/）查找书籍')
print('在小说主页的网址如（https://www.biquge7.xyz/50049），后面那一串数字就是id！')
novel_id = input('输入小说id：')
chapters = GetBookTitle_chapter(novel_id)
length = len(chapters)
print('小说名称为：' + Title)
print('共', length, '章')
flag = 1
start = 0
end = 0
while flag == 1:
    print('输入爬取区间')
    start = int(input('起始章节：'))
    end = int(input('结束章节：'))
    if end < start:
        print('结束章节不能小于起始章节')
    elif start <= 0:
        print('起始值应大于等于1')
    elif start > length:
        print('起始超过最大章节')
    elif end <= 0:
        print('结束章节小于等于0')
    elif end > length:
        print('超过最大章节')
    else:
        flag = 0
for i in range(start - 1, end ):
    download(i)
os.system('pause')
