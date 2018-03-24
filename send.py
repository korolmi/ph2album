import ui
import appex
import requests
from PIL import Image

iFile = None

def snd(sender):
    global iFile
    if not appex.is_running_extension():
        print('Running not in Pythonista extension mode, exiting...')
        return

    url = "http://mybizcloud.ru/album/upload"
    #fin = open('1.jpg', 'rb')
    files = {'file': iFile}
    data = {"cmd":"addphoto","title":"33Estepona","parent":"2312","ord":"2"}
    try:
        r = requests.post(url, files=files, data=data)

        #url = 'http://mybizcloud.ru/album/upload'
        #files = {'file':img}
        #r=requests.post(url,files=files,data={'name':'my test photo'})
        #print(r.text)

    sender.title = r.text

#imgList = appex.get_images_data()
iFiles = appex.get_images()
iFile = iFiles[0]

#fList = []
#for i in range(len(imgList)):
#    fnn = iFiles[i].filename
#    sz = len(imgList[i])
#    fList.append('fn:'+fnn+', sz:'+str(sz))
#fileInfo = "*".join(fList)

ui.load_view('test-brn').present('sheet')
