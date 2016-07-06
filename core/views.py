#encoding:utf-8
from django.shortcuts import render
from core.models import *
from django.http import HttpResponse, HttpResponseRedirect
# from math import ceil
# import random
import os
# import io as cStringIO
# from datetime import datetime
# import hashlib
# from django.core.files.storage import default_storage
# import json
# import time
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.db import connection
# from django.utils import timezone
try:
    from functools import wraps
except ImportError:
    from django.utils.functional import wraps  # Python 2.4 fallback.
#from django.utils.decorators import available_attrs
#import base64

import urllib.parse
import urllib.request
import sys
import http.cookiejar
import json


#
def ipfrom(ip):
    url = 'http://ip.taobao.com/service/getIpInfo.php?ip=' + ip
    result=post(url,{}).decode()
    return json.loads(result)


def post(url, data):#封装post方法
    return urllib.request.urlopen(url, urllib.parse.urlencode(data).encode('utf-8')).read()

def index(request):
    dic=ipfrom(request.META['REMOTE_ADDR'])
    try:
        iplanguage=dic['country']
        if iplanguage=='德国':
            advs = adv.objects.filter(language='gr')[:3]
            return render(request, 'index_gr.html', locals())
        elif iplanguage=='法国':
            advs = adv.objects.filter(language='fr')[:3]
            return render(request, 'index_fr.html', locals())
        elif iplanguage == '俄罗斯':
            advs = adv.objects.filter(language='rs')[:3]
            return render(request, 'index_rs.html', locals())
        else:
            advs = adv.objects.filter(language='en')[:3]
        return render(request, 'index_en.html', locals())

    except Exception as e:
        advs=adv.objects.filter(language='en')[:3]
        return render(request, 'index_en.html', locals())

