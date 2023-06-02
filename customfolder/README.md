# Training flow
- data prepare: use labelImg to label image to yolo formate

- execute command:

Please change current path to this repo folder Ultra96-Yolov4-tiny-and-Yolo-Fastest first.

```
IMAGE_SOURCE=/workspace/wilson/dataset/3_singleUSB_gray_G4_mono8_1200_1200_27fps_20220302/all_photos
python txt2xml.py -img $IMAGE_SOURCE -txt $IMAGE_SOURCE -xml $IMAGE_SOURCE
python splitdata.py $IMAGE_SOURCE -r 1
python parser_dataset.py
python kmeans_for_anchors.py $IMAGE_SOURCE -s 320 -a 6
```
# Start training
Usge

```
python train.py -s <input size> -o <save weight dir> -ty <training mode>
```

Example

```
python train.py -s 320 -o /workspace2/wilson/_Singel_USB_u3_keras-yolov4-tiny_p100_320_320_3_220307/ -ty tfrec
```
