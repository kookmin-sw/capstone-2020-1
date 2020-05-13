import requests
from bs4 import BeautifulSoup
import re
import json
from urllib.parse import urljoin        
from google.cloud import translate
from google.cloud import storage
import google.auth
import sys

headers = {
    'User-Agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'), 
}

def spellingCheck(comment):

    for comment_key in comment:
        row = comment[comment_key]['comment']
        content = row.replace('\ufeff', '')
        if(len(content)) < 500:
            url = 'https://m.search.naver.com/p/csearch/ocontent/util/SpellerProxy?'
            params = {}
            params['_callback'] = 'jQuery112409312646700220539_1557421638284'
            params['q'] = content
            params['where'] = "nexearch"
            params['color_blindness'] = 0
            params['_'] = 1557292527466

            response = requests.get(url,params=params).text
            response = response.replace(params['_callback'] + '(','')
            response = response.replace(');','')
            try:
                response_dict = json.loads(response)

                result_text = response_dict['message']['result']['html']
                result_text = re.sub(r'<\/?.*?>','',result_text)
                removed_emoji = result_text
                trans = translate_client.translate(removed_emoji, target_language='ko')
                s = trans['translatedText']
                for i in range(0,len(emoticon_list)):
                    s = s.replace(emoticon_list[i],emotion_list[i])
                comment[comment_key]['cor_comment'] = s
            except:
                comment[comment_key]['cor_comment'] = content
        else:
            comment[comment_key]['cor_comment'] = content
   
    return comment