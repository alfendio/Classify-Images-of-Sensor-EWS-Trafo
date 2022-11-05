from struct import unpack
from tqdm import tqdm
import os
import glob
import PIL as Image

from Duplicate_Gambar_2 import MAIN_IMAGE_PATH

marker_mapping = {
    0xffd8: "Start of Image",
    0xffe0: "Application Default Header",
    0xffdb: "Quantization Table",
    0xffc0: "Start of Frame",
    0xffc4: "Define Huffman Table",
    0xffda: "Start of Scan",
    0xffd9: "End of Image"
}

class JPEG:
    def __init__(self, image_file):
        with open(image_file, 'rb') as f:
            self.img_data = f.read()
    
    def decode(self):
        data = self.img_data
        while(True):
            marker, = unpack(">H", data[0:2])
            # print(marker_mapping.get(marker))
            if marker == 0xffd8:
                data = data[2:]
            elif marker == 0xffd9:
                return
            elif marker == 0xffda:
                data = data[-2:]
            else:
                lenchunk, = unpack(">H", data[2:4])
                data = data[2+lenchunk:]            
            if len(data)==0:
                break        
            
bads = []

MAIN_IMAGE_PATH = 'C:/Users/alfen/OneDrive/Pictures/Duplikat Dataset Sensor EWS Trafo_2/Training/LM 35'

for image_path in glob.glob(MAIN_IMAGE_PATH):
  image = Image.open(image_path)
  try:
    image.decode()   
  except:
    bads.append(image)


for name in bads:
  os.remove(name)
  print(name)
# 1334 gambar