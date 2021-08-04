import pyqrcode

url = 'www.youtube.com/c/karthikeshrobotics'
k = pyqrcode.create(url)
k.svg('kkk.svg', scale=10)




