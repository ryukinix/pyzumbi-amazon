#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from time import clock
import urllib.request as urllib
import sys, os



dic = {	'á':'a', 'à':'a', 'ã':'a',
		'é':'e', 'è':'e', 'ê':'e',
		'í':'i',
		'ó':'o', 'õ':'o', 'ô':'o',
		'ú':'u'}


def reporthook(blocknum, blocksize, totalsize):
    readsofar = blocknum * blocksize
    if totalsize > 0:
        percent = readsofar * 1e2 / totalsize
        n = '#' * int(30 * percent / 100)
        s = "\r %*.2f KB |%-30s| %5.1f%% / %5.2f KB" % (len(str(totalsize)), readsofar / 1024, n, percent, totalsize / 1024)
        sys.stderr.write(s)
        if readsofar >= totalsize: # near the end
            sys.stderr.write("\n")
    else: # total size is unknown
        sys.stderr.write("read %d\n" % (readsofar,))


def readWords(url):	
	if not os.path.exists('data.db'):
		print("~Carregando banco de palavras~")
		page = urllib.urlretrieve(url, 'data.db', reporthook)
	with open('data.db', 'r', encoding = 'iso8859') as db:
		words = db.read()

	if len(words) == 0:
		os.remove('data.db')
		return readWords(url)

	return words.split()

def cleanWords(words):
	global dic
	i = 0
	while i < len(words):
		low = words[i].lower()
		words[i] = low
		new = ''
		for c in words[i]:
			if c in dic:
				new += dic[c]
			else:
				new += c
		words[i] = new
		i += 1
	return words