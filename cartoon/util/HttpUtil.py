# coding=utf-8
import requests
import json


def getCartoonTypes():
    types = ('少女','少男','耽美','搞笑','魔幻','生活','动作','科幻','悬疑','恐怖',
             '校园','玄幻','恋爱','都市','百合','古风','热血','励志','竞技','同人','完结')
    return types


def getCartoons(type,start):
    start = str(start)
    type = str(type)
    url = 'http://dajiaochong.517w.com/dacu_app/get_tag_book.php?tag={type}&type=0&start={start}&label_type=0'
    url = url.replace('{start}', start)
    url = url.replace('{type}', type)
    result = requests.get(url)
    result = str(result.content)
    result = json.loads(result)
    data = result['data']['data']
    for d in data:
        if len(d['description']) > 12:
            d['description'] = d['description'][0:12]+'...'
        if len(d['description']) == 0:
            d['description'] = '暂无介绍...'
        if len(d['title']) > 10:
            d['title'] = d['title'][0:10] + '...'
        if len(d['update_chapter_name']) > 13:
            d['update_chapter_name'] = d['update_chapter_name'][0:13]+'...'
        if len(d['update_chapter_name']) == 0:
            d['update_chapter_name'] = '暂无更新'
    result = {
        'data': data,
    }
    return result


def getCatalogs(id):
    url = 'http://dajiaochong.517w.com/dacu_app/get_chapter_info.php?id={id}&beginId=0'
    url = url.replace('{id}', id)
    result = requests.get(url).content
    result = json.loads(result)['data']['chapter']
    return result


def getChapterImgs(cid):
    url = 'http://dajiaochong.517w.com/dacu_app/get_chapter.php?cid={cid}'
    url = url.replace("{cid}",cid)
    result = requests.get(url).content
    result = json.loads(result)['data']
    for d in result:
        d['image'] = 'http://cdn.517w.com/'+d['image']
    return result


def getSearchResult(key):
    url = 'http://dajiaochong.517w.com/dacu_app/get_filter.php?type=0&str={key}&start=0&click=1'
    url = url.replace("{key}", key)
    result = json.loads(requests.get(url).content)
    result = result['data']
    try:
        if len(result['data']) > 0:
            for d in result['data']:
                if len(d['description']) > 12:
                    d['description'] = d['description'][0:12]+'...'
                if len(d['description']) == 0:
                    d['description'] = '暂无介绍...'
                if len(d['title']) > 10:
                    d['title'] = d['title'][0:10] + '...'
                if len(d['update_chapter_name']) > 13:
                    d['update_chapter_name'] = d['update_chapter_name'][0:13]+'...'
                if len(d['update_chapter_name']) == 0:
                    d['update_chapter_name'] = '暂无更新'
    except :
        pass
    return result




