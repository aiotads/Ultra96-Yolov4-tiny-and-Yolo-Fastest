# Training flow
- data prepare:
- execute command:
```
python txt2xml.py -img /workspace/wilson/dataset/3_singleUSB_gray_G4_mono8_1200_1200_27fps_20220302/all_photos -txt /workspace/wilson/dataset/3_singleUSB_gray_G4_mono8_1200_1200_27fps_20220302/all_photos -xml /workspace/wilson/dataset/3_singleUSB_gray_G4_mono8_1200_1200_27fps_20220302/all_photos

python splitdata.py /workspace/wilson/dataset/3_singleUSB_gray_G4_mono8_1200_1200_27fps_20220302/all_photos -r 1

python parser_dataset.py
python kmeans_for_anchors.py
python train.py

```

# txt2xml.py
```
python txt2xml.py -img /workspace/wilson/dataset/full_tary_random_21_10_12/all_photos3 -txt /workspace/wilson/dataset/full_tary_random_21_10_12/all_photos3 -xml /workspace/wilson/dataset/full_tary_random_21_10_12/all_photos3

```