import appex
import requests
from PIL import Image

def main():
    if not appex.is_running_extension():
        print('Running in Pythonista app, using test image...')
        img = Image.open('test:Mandrill')
    else:
        img = appex.get_image_data()
    if img:
        fn = str(dir(appex.get_image()))
        fnn = appex.get_image().filename
        print('fn:'+fnn)
        url = 'http://mybizcloud.ru/album/upload'
        files = {'file':img}
        #r=requests.post(url,files=files,data={'name':'my test photo'})
        #print(r.text)
    else:
        print('No input image found')

if __name__ == '__main__':
    main()
