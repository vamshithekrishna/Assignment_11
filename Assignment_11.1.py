# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 14:35:15 2018

@author: vamshi
"""
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import urllib.request
import nltk
import requests
from collections import Counter
from string import punctuation

response = urllib.request.urlopen('http://php.net/')
html = response.read()
soup = BeautifulSoup(html,"html5lib")

text = (''.join(s.findAll(text=True))for s in soup.findAll('p'))

c = Counter((x.rstrip(punctuation).lower() for y in text for x in y.split()))
print (c.most_common()) # prints most common words staring at most common.

[('the', 104), ('php', 62), ('of', 55), ('for', 38), ('release', 34), ('this', 33), ('and', 32), ('in', 30), ('can', 30), ('is', 27), ('on', 25), ('be', 25), ('to', 23), ('a', 20), ('source', 20), ('downloads', 20), ('found', 20), ('development', 18), ('list', 18), ('you', 17), ('version', 16), ('please', 15), ('7.2.0', 14), ('team', 13), ('visit', 13), ('page', 13), ('changes', 13), ('file', 12), ('upgrading', 12), ('also', 12), ('announces', 12), ('immediate', 12), ('availability', 12), ('users', 12), ('are', 12), ('encouraged', 12), ('our', 12), ('windows', 12), ('binaries', 12), ('read', 11), ('all', 11), ('candidate', 11), ('bug', 8), ('test', 7), ('news', 7), ('or', 7), ('upgrade', 7), ('windows.php.net/download', 7), ('recorded', 7), ('changelog', 7), ('bugs', 7), ('alpha', 6), ('wiki', 6), ('download', 6), ('carefully', 6), ('report', 6), ('any', 6), ('system', 6), ('do', 6), ('not', 6), ('use', 6), ('production', 6), ('it', 6), ('information', 6), ('new', 6), ('features', 6), ('other', 6), ('complete', 6), ('notes', 6), ('these', 6), ('files', 6), ('archive', 6), ('planned', 6), ('thank', 6), ('helping', 6), ('us', 6), ('make', 6), ('better', 6), ('security', 6), ('more', 5), ('incompatibilities', 5), ('tracking', 5), ('preview', 5), ('', 5), ('sources', 5), ('windows.php.net/qa', 5), ('will', 5), ('full', 5), ('releases', 5), ('3', 5), ('first', 4), ('1', 4), ('several', 4), ('at', 4), ('beta', 4), ('7.3.0', 3), ('which', 3), ('next', 3), ('7.2', 3), ('fixes', 3), ('released', 3), ('popular', 2), ('2', 2), ('7.1.18', 2), ('7.1', 2), ('7.2.6', 2), ('bugfix', 2), ('fix', 2), ('5.6.36', 2), ('have', 2), ('been', 2), ('fixed', 2), ('7.1.17', 2), ('7.0.30', 2), ('7.2.5', 2), ('contains', 2), ('7.2.2', 2), ('announced', 2), ('october', 2), ('third', 2), ('general-purpose', 1), ('scripting', 1), ('language', 1), ('that', 1), ('especially', 1), ('suited', 1), ('web', 1), ('fast', 1), ('flexible', 1), ('pragmatic', 1), ('powers', 1), ('everything', 1), ('from', 1), ('your', 1), ('blog', 1), ('most', 1), ('websites', 1), ('world', 1), ('glad', 1), ('announce', 1), ('starts', 1), ('7.3', 1), ('cycle', 1), ('rough', 1), ('outline', 1), ('specified', 1), ('issues', 1), ('reporting', 1), ('an', 1), ('early', 1), ('would', 1), ('june', 1), ('21', 1), ('signatures', 1), ('manifest', 1), ('qa', 1), ('site', 1), ('primarily', 1), ('includes', 1), ('memory', 1), ('corruption', 1), ('exif', 1), ('5.6', 1), ('containing', 1), ('many', 1), ('bugfixes', 1), ('7.0', 1), ('minor', 1), ('with', 1), ('included', 1), ('rc4', 1), ('fourth', 1), ('4', 1), ('26th', 1), ('rc3', 1), ('12th', 1), ('second', 1), ('14th', 1), ('september', 1), ('final', 1), ('31th', 1), ('august', 1), ('improvements', 1), ('relative', 1), ('20th', 1), ('july', 1), ('older', 1), ('entries', 1), ('user', 1), ('group', 1), ('events', 1), ('special', 1), ('thanks', 1), ('social', 1), ('media', 1)]

print ([x for x in c if c.get(x) > 5]) # words appearing more than 5 times
['php', 'is', 'a', 'to', 'development', 'and', 'the', 'in', 'team', 'release', 'of', 'version', 'alpha', 'this', 'wiki', 'for', 'source', 'downloads', 'please', 'visit', 'download', 'page', 'carefully', 'test', 'report', 'any', 'found', 'bug', 'system', 'do', 'not', 'use', 'production', 'it', 'information', 'on', 'new', 'features', 'other', 'changes', 'you', 'can', 'read', 'news', 'file', 'or', 'upgrading', 'complete', 'list', 'notes', 'these', 'files', 'also', 'be', 'archive', 'planned', 'thank', 'helping', 'us', 'make', 'better', 'announces', 'immediate', 'availability', 'all', 'users', 'are', 'encouraged', 'upgrade', 'our', 'windows', 'binaries', 'windows.php.net/download', 'recorded', 'changelog', 'security', 'bugs', '7.2.0', 'candidate']