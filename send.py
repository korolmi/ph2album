import appex
import requests
from PIL import Image

def main():
    if not appex.is_running_extension():
        print('Running not in Pythonista extension mode, exiting...')
        return
    imgList = appex.get_images_data()
    iFiles = appex.get_images()
    for i in range(len(imgList)):
        fnn = iFiles[i].filename
        print('fn:'+fnn)
        sz = len(imgList[i])
        print('sz:'+sz)
        #url = 'http://mybizcloud.ru/album/upload'
        #files = {'file':img}
        #r=requests.post(url,files=files,data={'name':'my test photo'})
        #print(r.text)

if __name__ == '__main__':
    main()
