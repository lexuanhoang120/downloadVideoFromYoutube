from genericpath import isdir
from pytube import YouTube
import sys
import pandas as pd
import logging
import os
logging.basicConfig(filename="log.txt", level=logging.INFO)

def download( link,folder):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try: 
        youtubeObject.download(output_path= folder )
        logging.info(f'Success: {link} have downloaded')

    except:
        logging.info(f'Fail: {link} havenot downloaded')
        
input = sys.argv

links = pd.read_csv(input[1])
folder = input[2]
if not os.path.isdir(folder):
    os.mkdir(folder)

for link in links['link-href']:
    download(link,folder=folder)
    

# link = 'https://www.youtube.com/watch?v=_82l5dvzZfQ&ab_channel=Codingforkids'
