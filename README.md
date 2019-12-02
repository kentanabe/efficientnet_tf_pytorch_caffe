### build
  * pip install tensorflow torch torchvision
  * pip3 install tensorflow torch torchvision
  * git clone https://github.com/xxworkspace/caffe.git
    * Then build caffe width cpu-only

### TensorFlow to PyTorch Conversion
  * Download tf-model
    * cd pretrained_tensorflow
    * bash download.sh ckptsaug efficientnet-b0
  * Convert tf-model to pytorch-model
    * cd convert_tf_pt
    * mkdir -p ../pretrained_pytorch/ckptsaug
    * python3 convert_params_tf_pytorch.py --model_name efficientnet-b0 --tf_checkpoint ../pretrained_tensorflow/ckptsaug/efficientnet-b0/ --output_file ../pretrained_pytorch/ckptsaug/efficientnet-b0.pth
      * Using python3 convert_params_tf_pytorch.py -h
  * Test
    * python test_pytorch.py ckptsaug/efficientnet-b0

### PyTorch to Caffe
  * Convert pytorch-model to caffe .prototxt
    * mkdir -p ../caffemodel/ckptsaug
    * python pytorch2caffe.py ckptsaug/efficientnet-b0
  * Convert pytorch-model to caffe .caffemodel
    * python pytorch2caffe_model.py ckptsaug/efficientnet-b0
  * Test
    * pytorch test_caffe.py ckptsaug/efficientnet-b0

### data process RGB
mean = [0.485, 0.456, 0.406]
std = [0.229, 0.224, 0.225]
