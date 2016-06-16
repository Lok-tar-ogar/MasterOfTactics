from django.shortcuts import render
from core.models import *
from django.http import HttpResponse, HttpResponseRedirect
#from PIL import Image,ImageDraw,ImageFont
from math import ceil
import random
import os
import io as cStringIO
from datetime import datetime
import hashlib
from django.core.files.storage import default_storage
import json
import time
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import connection
from django.utils import timezone
try:
    from functools import wraps
except ImportError:
    from django.utils.functional import wraps  # Python 2.4 fallback.
from django.utils.decorators import available_attrs
import base64

import urllib.parse
import urllib
import sys
import http.cookiejar
import json




def index(request):
    return render(request, 'index.html', locals())

