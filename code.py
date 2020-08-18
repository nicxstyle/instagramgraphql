"""
@author: nicxstyle
www.burakgultekin.com
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json
import requests


driver_path = r"C:\Users\then1cx\Desktop\chromedriver.exe" ## chrome driver path
browser = webdriver.Chrome(executable_path=driver_path)

browser.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
time.sleep(2)
username = "then1cx" ## kullanıcı adı
password = "illmind" ## şifre
 
browser.find_element_by_xpath("//input[@name='username']").send_keys(username)
browser.find_element_by_xpath("//input[@name='password']").send_keys(password)
browser.find_element_by_xpath("//button[contains(.,'Giriş Yap')]").click()

time.sleep(2)
##post shortcode tanımlanan alan. eğer postun linki bu ise  https://www.instagram.com/p/CECXW9bsRzo/ , shortcode budur CECXW9bsRzo
shortcode = "CECXW9bsRzo"
url = 'https://www.instagram.com/graphql/query/?query_hash=33ba35852cb50da46f5b5e889df7d159&variables=%7B"shortcode":"'+shortcode+'","first":50,"after":"0"%7D'
r = requests.get(url)
data = json.loads(r.text)

end_cursor = data['data']['shortcode_media']['edge_media_to_comment']['page_info']['end_cursor']

def fetch_data(shortcode,token):
    url = 'https://www.instagram.com/graphql/query/?query_hash=33ba35852cb50da46f5b5e889df7d159&variables=%7B"shortcode":"'+shortcode+'","first":50,"after":"'+token+'"%7D'
    r = requests.get(url)
    b = json.loads(r.text)
    cursor = b['data']['shortcode_media']['edge_media_to_comment']['page_info']['end_cursor']
    data = b['data']['shortcode_media']['edge_media_to_comment']['edges']
    for x in data:
        ## bu kullanıcı adını verir
        a=x['node']['owner']['username']
        print(a)
    while cursor != "null":
       return fetch_data(shortcode,cursor)

fetch_data(shortcode,"0")
