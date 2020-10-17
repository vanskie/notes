#! /usr/bin/python3

import re
import requests
import hashlib

'''
get raw request, find string to hash, hash string and POST it.
'''
boxUrl = 'http://139.59.202.58:31902/'
# you forgot the cookie man ... that was so frurstrating but very rewarding
# don't forget that requests has the session() function which handles cookies
r = requests.session()
# get request to site
page = r.get(boxUrl)
# extract html as text
pageHTML = page.text
# find the string we need with regex
# find >(\w any char or num) 20 of them which end with <
matchObj = re.findall(r'>\w{20}<', pageHTML)
# extact the string from the matchObj list and remove ><
# before we hex the string we need to 'utf8' encode it
#matchStr = matchObj[0][1:-1].encode('utf-8')
matchStr = matchObj[0][1: -1]
# now hex has the string
# we need to supply the utf8 string with %s formatting
# it was a pain in the ass, because after encoding the string it becomes b'string'
# but that doesn't mean you can use hash.update() cause you still need to add b'%s'string
#result = hashlib.md5(b'%s' % matchStr.encode('utf8')).hexdigest()
result = hashlib.md5(matchStr.encode('utf-8')).hexdigest()
boxData = {'hash': result}
# now we need to POST the result and print the response
postit = r.post(url = boxUrl, data = boxData)
print(postit.text)
