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

    actions = [ "addalbum", "addday", "addphoto" ]
    url = "http://mybizcloud.ru/album/upload"
    files = {'file': iFile}
    data = {
        "cmd":actions[sender.superview['action'].selected_index],
        "title":sender.superview['descr'].text,
        "parent":sender.superview['parentid'].text,
        "ord":"2"
    }
    r = requests.post(url, files=files, data=data)
    sender.superview['comments'].text = r.text
    #sender.title = r.text

    #resTxt = sender.superview['action'].segments[sender.superview['action'].selected_index] + "\n"
    #resTxt += sender.superview['parentid'].text + "\n"
    #resTxt += sender.superview['descr'].text + "\n"
    #sender.superview['comments'].text = resTxt
    
imgList = appex.get_images_data()
iFiles = appex.get_images()
iFile = imgList[0]

#fList = []
#for i in range(len(imgList)):
#    fnn = iFiles[i].filename
#    sz = len(imgList[i])
#    fList.append('fn:'+fnn+', sz:'+str(sz))
#fileInfo = "*".join(fList)

ui.load_view('test-brn').present('sheet')
