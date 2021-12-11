#!/bin/bash

# Compile

vai_c_tensorflow --arch ./kv260_arch.json  -f ./../quantize_results/quantize_eval_model.pb --output_dir compile_result -n usb_test --options "{'mode':'normal','save_kernel':'', 'input_shape':'1,320,320,3'}"



echo "#####################################"
echo "COMPILATION COMPLETED"
echo "#####################################"
