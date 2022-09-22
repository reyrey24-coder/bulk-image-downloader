import pandas as pd
import urllib
import requests

df = pd.read_csv("image_list.csv")
imgs = df.values.tolist()

total = len(imgs)
download_counter = 1

for img in imgs:
    response = requests.get(img[1])
    if response.status_code:
        fp = open(f'images/{img[0]}.jpg', 'wb')
        fp.write(response.content)
        print(img[0], f"[{download_counter}/{total}]")
        download_counter += 1
        fp.close()