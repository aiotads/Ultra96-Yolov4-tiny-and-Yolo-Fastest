from PIL import Image
import argparse
import os

# parse = argparse.ArgumentParser(discription="input RGB image dir, it will gen new image_dir and convert to gray")
parse = argparse.ArgumentParser()
parse.add_argument('image_dir', type=str)
parse.add_argument('-f', '--format', type=str, default='.png', help='image format')
args = parse.parse_args()

format = args.format

full_path = args.image_dir
file = os.listdir(args.image_dir)

if not os.path.exists(os.path.join(full_path, 'gray')):
    os.mkdir(os.path.join(full_path, 'gray'))
else:
    print('gray folder is exist!\n')
    exit()

for _file in file:
    if _file.endswith(f'{format}'):
        img = Image.open(os.path.join(full_path, _file)).convert('L')
        img.save(f'{full_path}/gray/{_file}')


# img = Image.open('image.png').convert('L')
# img.save('greyscale.png')
