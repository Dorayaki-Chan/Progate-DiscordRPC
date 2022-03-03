from ast import Slice
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from time  import sleep



def chromeURL():
    #sleep(10)
    options = Options()
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9014")

    #chromeドライバーの絶対パス
    driver = webdriver.Chrome( 'D:\Programming\CREATE\Progate-RPC\chromedriver.exe',options=options)

    #driver.get('https://www.google.co.jp')

    url = driver.current_url

    print (url)
    

    return choice(url)

def choice(url):
    if 'https://prog-8.com/' in url:
        s = url.replace('https://prog-8.com/', '')
        sList = s.split('/')

        pageList = ["about", "about", "business_policy", "faqs", "legal", "plans", "policy", "privacy_policy", "success_stories", "dashboard", "settings", "rankings", "docs",""]

        if sList[0] in pageList:
            return "Browsing the Progate"
        elif sList[0] == "courses":
            return "Choosing a course"
        elif "slides" in sList[0]:
            return "Watching slides"
        else:
            return "Studying" + " " +sList[0].upper()
        
    else:
        return "Hanging out😂"

    
     