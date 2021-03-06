import ctypes
import os
from datetime import datetime
from PIL import ImageGrab

MSG_TITLE = 'Print Screen'

try:
  userHome = os.path.expanduser('~')
  desktopPath = userHome + '/Desktop/'
  srcPath = os.path.join(desktopPath, 'screen')
  if not os.path.exists(srcPath):
    os.makedirs(srcPath)

  dt = datetime.today().strftime("%y%m%d-%H%M%S")
  imgPath = 'screen-%s.png' % dt
  imgPath = os.path.join(srcPath, imgPath)

  im = ImageGrab.grab()
  im.save(imgPath,'PNG')

  msg = 'Saved: %s' % imgPath
  print(msg)
  ctypes.windll.user32.MessageBoxA(0, msg, MSG_TITLE, 0)
except Exception as e:
  msg = 'Error: %s' % str(e)
  print(msg)
  ctypes.windll.user32.MessageBoxA(0, msg, MSG_TITLE, 0)
