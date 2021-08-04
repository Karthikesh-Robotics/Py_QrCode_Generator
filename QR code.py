import pyqrcode

url = 'www.youtube.com/c/karthikeshrobotics'
k = pyqrcode.create(url)
k.svg('kkr.svg', scale=10)




