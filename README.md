# Captcha-cracking
### Python Captcha Cracking

A simple yet efficient script to crack online captchas. Step by step detailed guide:
1. Install OCR tesseract (google) on your linux machine with following command: 

   **$sudo apt-get install tesseract-ocr**
 
   More Details about  [OCR tesseract engine](https://github.com/tesseract-ocr/tesseract)
 
2. Download the pillow(PIL) module in python3 if you don`t already have it, most linux distros have them.

   **$sudo pip install pillow**

   More Details about [pillow](http://pillow.readthedocs.io/en/3.1.x/installation.html)

3. Install pytesseract (python wrapper for ocr tesseract) , pytesser is also available. Use the command:
   
   **$sudo pip install pytesseract**
   
   More Details about [pytesseract](https://pypi.python.org/pypi/pytesseract/0.1)

4. Download the script and run on python3 and you are good to go.
   
   After downloading the scipt on your pyhton3 ide run the script to get the image from the url/page/tag, *img.png* fill be formed in your working directory .
   
   Which will be proceesed to generate image1.png and finally resized to result.tif for feeding to the OCR pytessercat
   
5. I have added some sample image file for testing the captcha cracker . The detailed explanation about the script can be    read  from the script and other documentation links given on here and other pages.
   
6. Reference:
  
   [captcha cracking](http://www.pythonlovers.net/bypass-online-captcha/)
  
   [urllib](https://docs.python.org/3/library/urllib.request.html)
  
   [http.cookiejar](https://docs.python.org/3.1/library/http.cookiejar.html)
  
   [regex](https://docs.python.org/2/library/re.html)

*Happy Cracking* :fire:   
   
