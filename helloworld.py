
from ctypes import windll
user32 = windll.user32
user32.SetProcessDPIAware()
from PIL import Image
import xlsxwriter
import PIL.ImageOps
import pytesseract
import pyscreenshot as ImageGrab

workbook = xlsxwriter.Workbook('spotifyactivity.xlsx')
worksheet_data = workbook.add_worksheet('data')
worksheet_analysis = workbook.add_worksheet('analysis')
workbook.close()

if __name__ == '__main__':
    # part of the screen

    im = ImageGrab.grab(bbox=(3400, 220, 3800, 550))  # X1,Y1,X2,Y2

    im.save('im.png')

    image = Image.open('im.png')

    inverted_image = PIL.ImageOps.invert(image)

    inverted_image.save('im.png')

    inverted_image.show()

    text = pytesseract.image_to_string(inverted_image, lang='eng')

    print(text)

    a, b, c, d = text.split(' ', 3)
    print(a) #First Name
    print(b) #Last Name
    print(c) #Song and Artist
    print(d) #Source
