# Training flow
- data prepare: use labelImg to label image to yolo formate

please change current path to this repo folder Ultra96-Yolov4-tiny-and-Yolo-Fastest

- execute command:
```
python txt2xml.py -img /workspace/wilson/dataset/3_singleUSB_gray_G4_mono8_1200_1200_27fps_20220302/all_photos -txt /workspace/wilson/dataset/3_singleUSB_gray_G4_mono8_1200_1200_27fps_20220302/all_photos -xml /workspace/wilson/dataset/3_singleUSB_gray_G4_mono8_1200_1200_27fps_20220302/all_photos
python splitdata.py /workspace/wilson/dataset/3_singleUSB_gray_G4_mono8_1200_1200_27fps_20220302/all_photos -r 1
python parser_dataset.py
python kmeans_for_anchors.py /workspace/wilson/dataset/3_singleUSB_gray_G4_mono8_1200_1200_27fps_20220302/all_photos -s 320 -a 6
```
# Start training
```
python train.py -s 320 -o /workspace2/wilson/_Singel_USB_u3_keras-yolov4-tiny_p100_320_320_3_220307/
```
TODO : channel add in args

# txt2xml.py
```
python txt2xml.py -img /workspace/wilson/dataset/full_tary_random_21_10_12/all_photos3 -txt /workspace/wilson/dataset/full_tary_random_21_10_12/all_photos3 -xml /workspace/wilson/dataset/full_tary_random_21_10_12/all_photos3
```
