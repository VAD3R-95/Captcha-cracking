import os
import urllib.request
import re
import base64
import http.cookiejar
from PIL import Image
from pytesseract import *
import time

url = ' '                                                  # the url to get/post
headers = {}                                               # user agent spoofing ;-) required sometimes
headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686) Applewebkit/537.17 (KHTML, like Gecko Chrome/24.0.1312.27 Safari/537.17'


def main():
    start_time = time.time()
    cj = http.cookiejar.CookieJar()                             # using httpcookiejar for automatic handling of cookies
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    urllib.request.install_opener(opener)

    req = urllib.request.Request(url, headers=headers)          # GET request to url page
    resp = urllib.request.urlopen(req)
    respData = resp.read()
    
    print(cj)                                                      
    print("############################")
    print(respData)
    print("############################")
    paragraphs = re.findall(r';<img>(.*?)" />', str(respData)) # the tag to get the imgae from (different methods can be used here)
    
    for eachP in paragraphs:                                   # downloading the img src page can also work but this is pretty fast
        r = eachP                                              # with regex and saving to file on working dir. as image file
    print (r)
    with open('img.png', 'wb') as f:
        data = f.write(text)                                    

    img = Image.open("img.png")
    img = img.convert("RGBA")
    pixdata = img.load()

    for y in range(img.size[1]):                                # for Pre-processing,Segmentation and image Sampling of image
        for x in range(img.size[0]):                            # allot all non - black(dark) to white pixels
            if pixdata[x, y][0] < 25:                           # can be further processed as per requirements
                pixdata[x, y] = (255, 255, 255, 255)

    img.save("image1.png", "PNG")
    orgimg = Image.open("image1.png")                           # reopening ,resizing image for ocr
    sizeimg = orgimg.resize((250, 100), 2)
    ext = ".tif"
    img.save("result"+ ext)

    image = Image.open("result.tif")                             # convert image to string with ocr
    captcha = image_to_string(image)
    print(captcha)

    ans = post(captcha)
    print(ans)
    
    answer = urllib.request.urlopen(url, ans)                   # POST req to url page with captcha
    raw = answer.read()
    raw = raw.decode('utf-8')
    print(raw)                                                  # print response from page

    print("--- %s seconds ---" % (time.time() - start_time))    # total time to run the program
    
def post(captcha):
    values={}
    values{'captcha_place': captcha}                           # entering captcha as dic-values at captcha place(your_place) taken from tags
    senddata = urllib.parse.urlencode(values)                   # different methods can be used here also
    return bytes(senddata, 'utf-8')                            # returing as bytes for python3


if  __name__ =='__main__':
    main()    
    
