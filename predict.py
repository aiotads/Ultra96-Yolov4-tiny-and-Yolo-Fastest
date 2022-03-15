from yolo import YOLO
from PIL import Image
import tensorflow as tf
import time
import os
from tqdm import tqdm
import cv2

gpus = tf.config.experimental.list_physical_devices(device_type='GPU')
for gpu in gpus:
    tf.config.experimental.set_memory_growth(gpu, True)
    
yolo = YOLO()

# while True:
#     img = input('Input image filename:')
#     try:
#         image = Image.open(img)
#     except:
#         print('Open Error! Try again!')
#         continue
#     else:
#         tim1 = time.time()
#         r_image = yolo.detect_image(image)
#         tim2 = time.time() - tim1
#         print("time {:.2f}".format(tim2))
#         print("fps {:.2f}".format(1/tim2))
#         r_image.save('out.png')
#         r_image.show()


def write_items_to_file(image_id, items, fw):
    for item in items:
        fw.write(image_id + " " + " ".join([str(comp) for comp in item]) + "\n")


if __name__ == "__main__":

    with open('./core/test.txt') as fr:
        lines = fr.readlines()
    fw = open('./core/h5_result.txt', "w")
    for line in tqdm(lines):
        img_path = line.strip().split(" ")[0]
        fname = os.path.split(img_path)[-1]
        image_id = os.path.splitext(fname)[0]
        image = Image.open(img_path)
        # image = cv2.imread(img_path)
        items = yolo.detect_image(image)
        print(items)
        write_items_to_file(image_id, items, fw)
    fw.close()
