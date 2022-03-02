from PIL import Image
import argparse
import os
import cv2

# parse = argparse.ArgumentParser(discription="input RGB image dir, it will gen new image_dir and convert to gray")
parse = argparse.ArgumentParser()
parse.add_argument('image_dir', type=str)
parse.add_argument('-f', '--format', type=str, default='.png', help='image format')
args = parse.parse_args()

format = args.format

full_path = args.image_dir
file = os.listdir(args.image_dir)
gen_folder = os.path.join(full_path, 'gray')

if not os.path.exists(gen_folder):
    os.mkdir(gen_folder)
else:
    print('gray folder is exist!\n')
    exit()

for _file in file:
    if _file.endswith(f'{format}'):
        image = cv2.imread(os.path.join(full_path, _file))
        print(f'file name:\t{_file}')
        print(f'shape:\t\t{image.shape}')
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        print(f'convert shape:\t{image.shape}')
        cv2.imwrite(os.path.join(gen_folder, _file), image)
        # img = Image.open(os.path.join(full_path, _file)).convert('L')
        # img.save(os.path.join(gen_folder, _file))

print(f'Finish! Please check folder {gen_folder}')