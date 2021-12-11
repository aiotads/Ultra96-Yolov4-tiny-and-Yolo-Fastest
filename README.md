# Ultra96 Yolov4-tiny and Yolo-Fastest

### Requment
 - Training framework: tensorflow v2.2.0rc4 (keras v2.3.0-tf)

 - Transfer Xilinx model: vitis-ai tensorflow1

### Training and transfor step by step

1. Prepare your dataset for training and label them. 
2. Use `txt2xml.py` to  transfer the dataset bounding box.txt to .xml. 
3. Use  `paser_dataset.py` or `voc_annotation.py`  to integrate data path, bounding box from .xml and class together.
   ```
   # example: paser_data.txt
   /path/picture1.png 40,192,257,420,0
   /path/picture2.png 282,370,618,576,1
   ```
4. We use trnsorflow v2.2.0rc4 to training. Please fill in your training information in `train.py`.
   ```
    annotation_path = 'paser_data.txt'
    classes_path = 'class.txt'
    anchors_path = 'yolo_anchors.txt'
    weights_path = 'last1.h5'
      .
      .
      . 
    log_dir = 'output/'
    ``` 
   you will get a model.json when you start training. You can print `model_body.summary()` to double check your training model. Like following shows.
   
   ```
      _________________________________________________________________________________
      Layer (type)                    Output Shape        Param #  Connected to
      =================================================================================
      input_1 (InputLayer)           [(None, 320, 320, 3) 0
      _________________________________________________________________________________
      zero_padding2d (ZeroPadding2D) (None, 321, 321, 3)  0        input_1[0][0]
      _________________________________________________________________________________
      conv2d (Conv2D)                (None, 160, 160, 32) 864      zero_padding2d[0][0]
                                          
   ```

   Also, you can verify model with .h5 use `predict.py` before you transfer model to .pb

5. Change to tensorflow1 after finish training. We will start to transfer model in tensorflow1.   
6. Use `keras_to_tensorflowing.py` to transfer .h5 to .pb
   ```
      python keras_to_tensorflow.py --input_model=path.h5 --input_model_json=model_config.json --output_model=output.pb
   ```
   Also, you can verify model with .pb use `core/tf_predict.py` before you transer model to xmodel
7. Use `script/2_vitisAI_tf_quantize.sh` to quantize model.
   ```
      vai_q_tensorflow quantize \
      --input_frozen_graph ./output/output.pb \
      --input_nodes input_1 \
      --input_shapes ?,320,320,3 \
      --output_nodes conv2d_20/BiasAdd,conv2d_23/BiasAdd \
      --method 1 \
      --input_fn input_fn.calib_input \
      --gpu 0 \
      --calib_iter 161 \
   ```
8. Use `script/3_vitisAI_tf_compile.sh` to compile model to xmodel.
   ```
      vai_c_tensorflow --arch ./kv260_arch.json  -f quantize_eval_model.pb --output_dir compile_result -n model_name --options "{'mode':'normal','save_kernel':'', 'input_shape':'1,320,320,3'}"
   ```


### Introduction from the author

1. We convert dataset to VOC format. I use UA-DETRAC dataset, and we can use ./VOCdevkit/ files to convert dataset.

2. In the official yolov4-tiny, there is a slice operation to realize  the CSPnet, but the quantitative tools don't support the operation, so I use a 1*1 convolution to replace it.

3. Then we can use train.py to train the model, and save the model structure and weights as model.json and model.h5. I use TensorFlow-gpu 2.2.0.

4. Then we can generate pb file that is suitable for deployment tools. We can see ./frozon_result/readme.md for details.

5. Then we use Vitis-AI to quantify our model. We can use ./scripts/1_vitisAI_tf_printNode.sh to find the input and output, and use ./scripts/2_vitisAI_tf_quantize.sh to quantify our model.

6. We can compile our model. We can use ./scripts/3_vitisAI_tf_compile.sh to compile our model.

7. We should use vivado and Vitis to build the hardware platform. (./edge/readme.md)

8. The last, we can run our model on Ultra96-v2 board. There is an example that using yolo model to detate vehicles (./edge/dpu_yolo_v4_tiny.ipynb). There are the results, the fps is 25 with 320*320 images.

   ![1](https://github.com/yss9701/Ultra96-Yolov4-tiny/raw/main/img/1.png)

   ![2](https://github.com/yss9701/Ultra96-Yolov4-tiny/raw/main/img/2.png)

9. In order to achieve faster detection speed, I try to use Yolo-Fastest ([Yolo-Fastest](https://github.com/dog-qiuqiu/Yolo-Fastest)) and implement it with tensorflow, then deploy it to Ultra96-v2 board. There are the results, it can achieve 30fps+.

   ![3](https://github.com/yss9701/Ultra96-Yolov4-tiny/raw/main/img/3.png)

   ![4](https://github.com/yss9701/Ultra96-Yolov4-tiny/raw/main/img/4.png)

10. Now we support model pruning. We use [keras-surgeon](https://github.com/BenWhetton/keras-surgeon) 0.2.0 and [nni](https://github.com/microsoft/nni) 1.5 to prune the model, you can see in ./Model_pruning. I modified the source code of nni (compressor.py) and fixed some bugs, then we can choose the layer that we want to prune, and I gave a demo that use FPGM to prune the model.

   

   

   

   References:

   [Yolov4-tiny-tf2](https://github.com/bubbliiiing/yolov4-tiny-tf2)

   [Yolo-v3-Xilinx](https://github.com/Xilinx/Vitis-AI-Tutorials/tree/ML-at-Edge-yolov3)

   [Yolo-v4-tutorial-Xilinx](https://github.com/Xilinx/Vitis-Tutorials/tree/33d6cf9686398ef1179778dc0da163291c68b465/Machine_Learning/Design_Tutorials/07-yolov4-tutorial)

   [Yolo-v3-dnndk](https://github.com/Xilinx/Vitis-AI/blob/v1.1/mpsoc/vitis_ai_dnndk_samples/tf_yolov3_voc_py/tf_yolov3_voc.py)

   [UA-DETRAC to VOC](https://blog.csdn.net/weixin_38106878/article/details/88684280?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-3.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-3.control)

   [Vitis-AI 1.1](https://www.xilinx.com/html_docs/vitis_ai/1_1/zkj1576857115470.html)

   [Yolo-Fastest](https://github.com/dog-qiuqiu/Yolo-Fastest)

   [keras-surgeon](https://github.com/BenWhetton/keras-surgeon)

   [nni](https://github.com/microsoft/nni)

