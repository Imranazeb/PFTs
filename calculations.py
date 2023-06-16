from os import system
import glob
import cv2
from pytesseract import pytesseract
import time
from difflib import SequenceMatcher
from calculations import *


def determine_obstruction(FEV1L, LLN):
    if FEV1L < LLN:
        return 'presence of obstructive lung disease'
    else:
        return 'no evidence of obstruction'


def canProceed(param):
    if param is None:
        print('An error occurred. Program existing')
        exit()
    else:
        pass


def read_pft(filename):

    pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    try:
        img = cv2.imread(filename)
    except:
        print('Error reading data from source file')
        exit()

    text_in_img = pytesseract.image_to_string(img)

    pft_data_raw = (text_in_img.split('\n'))
    pft_data = list(filter(None, pft_data_raw))

    for index, item in enumerate(pft_data):
        similarity = SequenceMatcher(a='SPIROMETRY', b=item).ratio()
        if similarity > 0.75:
            start_index = index
            break
        else:
            start_index = None

    canProceed(start_index)

    FEV1percent = float(pft_data[start_index + 2].split()[-4])
    FEV1L = float(pft_data[start_index + 2].split()[-6])
    FVCpercent = float(pft_data[start_index + 1].split()[-4])

    LLN = float(pft_data[start_index + 2].split()[-2])

    return (f'The FEV1 was {FEV1percent}% predicted and the FVC was {FVCpercent}% predicted. In liters the FEV1 was {FEV1L} and the lower limit of normal for FEV1 was {LLN}.There was {determine_obstruction(FEV1L, LLN)}')


spacer = '----------------------------------------------------------------\n\n'
