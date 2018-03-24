import ui
import appex
import requests
from PIL import Image

fileInfo = ""

def snd(sender):
    global fileInfo
    if not appex.is_running_extension():
        print('Running not in Pythonista extension mode, exiting...')
        return
        #url = 'http://mybizcloud.ru/album/upload'
        #files = {'file':img}
        #r=requests.post(url,files=files,data={'name':'my test photo'})
        #print(r.text)

    sender.title = fileInfo

imgList = appex.get_images_data()
iFiles = appex.get_images()
fList = []
for i in range(len(imgList)):
    fnn = iFiles[i].filename
    sz = len(imgList[i])
    fList.append('fn:'+fnn+', sz:'+str(sz))

fileInfo = "*".join(fList)

ui.load_view('test-brn').present('sheet')
