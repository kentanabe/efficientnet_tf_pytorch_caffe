# EfficientNet for BVLC Caffe

This is a conversion tool for [EfficientNet](https://github.com/tensorflow/tpu/tree/master/models/official/efficientnet) from TensorFlow to BVLC Caffe, based on efficientnet_tf_pytorch_caffe by [xxworkspace](https://github.com/xxworkspace/efficientnet_tf_pytorch_caffe).
This fork uses only BVLC standard layers, instead of broadcast_Mull and Swish layers.

## Install packages

### Install pip packages

```
pip install tensorflow torch torchvision --user
pip3 install tensorflow torch torchvision --user
```

### Install BVLC Caffe

```
sudo apt update
sudo apt install caffe-cpu
```

## Convert models

|Preprocessing         | Architecture            |Download file             |
|----------------------|-------------------------|--------------------------|
|Standard (ckpts)      |efficientnet-b[1-5]      |efficientnet-b[1-5]       |
|AutoAugment (ckptsaug)|efficientnet-b[1-7]      |efficientnet-b[1-7]       |
|RandAugment (randaug) |efficientnet-b[57]       |efficientnet-b[57]-randaug|
|AdvProp (advprop)     |efficientnet-b[0-8]      |efficientnet-b[0-8]       |

## TensorFlow to PyTorch Conversion

### Download tf-model

```
pushd pretrained_tensorflow
download.sh ckptsaug efficientnet-b0
popd
```

### Convert tf-model to pytorch-model

```
mkdir -p pretrained_pytorch/ckptsaug
pushd convert_tf_pt
python3 convert_params_tf_pytorch.py \
 --model_name efficientnet-b0 \
 --tf_checkpoint ../pretrained_tensorflow/ckptsaug/efficientnet-b0/ \
 --output_file ../pretrained_pytorch/ckptsaug/efficientnet-b0.pth
popd
```

### Test PyTorch model

```
pushd convert_tf_pt
python3 test_pytorch.py ckptsaug efficientnet-b0
popd
```

## PyTorch to Caffe

### Convert pytorch-model to caffe .prototxt

```
mkdir -p caffemodel/ckptsaug
pushd convert_tf_pt
python3 pytorch2caffe.py ckptsaug efficientnet-b0
popd
```

### Convert pytorch-model to caffe .caffemodel

```
pushd convert_tf_pt
python3 pytorch2caffe_model.py ckptsaug efficientnet-b0
popd
```

### Test

```
pushd convert_tf_pt
python3 test_caffe.py ckptsaug efficientnet-b0
popd
```

## data process RGB

* mean = [0.485, 0.456, 0.406] x 255
* std = [0.229, 0.224, 0.225] x 255

## Correspondence table of conversion

| Input size | Tensorflow layer                             | Caffe layers                                                                                                                  |
|------------|----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| Odd        |conv2d (kernel_size: 2, stride: 2, pad: same) | Convolution (kernel_size: 2, stride: 2, pad: 1)                                                                               |
| Even       |conv2d (kernel_size: 2, stride: 2, pad: same) | Convolution (kernel_size: 2, stride: 2, pad: 2) + <br> Convolution (kernel_size: 2, stride: 2, pad: 1) + <br> Crop (offset: 1)|
| ---------- |depthwise_conv2d                              | Convolution (group=num_output)                                                                                                |
| ---------- |swish                                         | Sigmoid + Eltwise (operation: PROD)                                                                                           |
| ---------- |broadcast_mul                                 | Flatten + Scale (with 2 bottom blobs)                                                                                         |

## Result of conversion

### efficientnet-b0 on Netscope

https://kentanabe.github.io/netscope/#/preset/efficientnet-b0

![efficientnet-b0.block1](efficientnet-b0.block1.png)

