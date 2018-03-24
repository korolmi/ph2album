import ui
import appex
import requests
from PIL import Image

def snd(sender):
    if not appex.is_running_extension():
        print('Running not in Pythonista extension mode, exiting...')
        return
    imgList = appex.get_images_data()
    iFiles = appex.get_images()
    fList = []
    for i in range(len(imgList)):
        fnn = iFiles[i].filename
        sz = len(imgList[i])
        fList.append('fn:'+fnn+', sz:'+str(sz))
        #url = 'http://mybizcloud.ru/album/upload'
        #files = {'file':img}
        #r=requests.post(url,files=files,data={'name':'my test photo'})
        #print(r.text)

    sender.title = "*".join(fList)
