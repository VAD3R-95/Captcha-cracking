import os
import urllib.request
import re
import base64
import http.cookiejar
from PIL import Image
from pytesseract import *
import time

url = 'http://challenge01.root-me.org/programmation/ch8/'
headers = {}                                               # user agent spoofing not required here ;-)
headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686) Applewebkit/537.17 (KHTML, like Gecko Chrome/24.0.1312.27 Safari/537.17'


def main():
    start_time = time.time()
    cj = http.cookiejar.CookieJar()       # using httpcookiejar for automatic handling of cookies
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    urllib.request.install_opener(opener)

    req = urllib.request.Request(url, headers=headers) # GET request to ch8 page
    resp = urllib.request.urlopen(req)
    respData = resp.read()
    
    print(cj)
    print("############################")
    print(respData)
    print("############################")
    paragraphs = re.findall(r';base64,(.*?)" />', str(respData))
    for eachP in paragraphs:
        r = eachP
    print (r)
    text = base64.b64decode(r) # decoding and writing our image to a file
    with open('img.png', 'wb') as f:
        data = f.write(text)

    img = Image.open("img.png")
    img = img.convert("RGBA")
    pixdata = img.load()

    for y in range(img.size[1]):          # to process image
        for x in range(img.size[0]):      # allot all non - black(dark) to white pixels
            if pixdata[x, y][0] < 25:
                pixdata[x, y] = (255, 255, 255, 255)

    img.save("image1.png", "PNG")
    orgimg = Image.open("image1.png")       # resizing image for ocr
    sizeimg = orgimg.resize((250, 100), 2)
    ext = ".tif"
    img.save("result"+ ext)

    image = Image.open("result.tif")
    captcha = image_to_string(image)
    print(captcha)

    ans = post(captcha)
    print(ans)
    
    answer = urllib.request.urlopen(url, ans) # POST req to ch8 page with captcha
    raw = answer.read()
    raw = raw.decode('utf-8')
    print(raw)

    print("--- %s seconds ---" % (time.time() - start_time))
    
def post(passw):
    entry={'cametu':passw}       # entering captcha with dic-values at cametu place
    senddata = urllib.parse.urlencode(entry)
    return bytes(senddata, 'utf-8')


if  __name__ =='__main__':
    main()    
    
