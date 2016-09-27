from django.shortcuts import render,render_to_response,HttpResponse
from django.template import loader,Context
from cartoon.util import HttpUtil
import logging
import json
# Create your views here.


def index(req):
    types = HttpUtil.getCartoonTypes()
    cartoons = HttpUtil.getCartoons(1, 0)
    return render_to_response('index.html', {'types': types, 'type': 1, 'cartoons': cartoons})


def cartoontype(req,type):
    types = HttpUtil.getCartoonTypes()
    type = int(type)
    cartoons = HttpUtil.getCartoons(type, 0)
    return render_to_response('index.html', {'types': types, 'type': type, 'cartoons': cartoons})

def cartoontypeajax(req,type,start):
    cartoons = HttpUtil.getCartoons(type, start)
    t = loader.get_template('cartoonitem.html')
    html = t.render(Context({'cartoons': cartoons}))
    return HttpResponse(html)


def catalog(req,id):
    catalogs = HttpUtil.getCatalogs(id)
    return render_to_response('catalog.html', {'catalogs': catalogs})

def chapter(req,cid):
    imgs = HttpUtil.getChapterImgs(cid)
    return render_to_response('readcartoon.html', {'chapters': imgs})


