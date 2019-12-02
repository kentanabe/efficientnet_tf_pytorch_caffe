import os
os.environ['GLOG_minloglevel'] = '2' 
import sys
import torch
import caffe
from PIL import Image
from torchvision import transforms

if not len(sys.argv) == 3:
  sys.exit("too less argc : model name is needed! -> efficientnet-b0/efficientnet-b1/efficientnet-b2/efficientnet-b3")

type_name = sys.argv[1]
model_name = sys.argv[2]
deploy = "../caffemodel/" + type_name + "/" + model_name + ".prototxt"
caffemodel = "../caffemodel/" + type_name + "/" + model_name + ".caffemodel"

tfms = transforms.Compose([transforms.Resize((224,224)), transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),])
img = tfms(Image.open('test.jpg')).unsqueeze(0).numpy()

model = caffe.Net(deploy,caffemodel,caffe.TEST)
model.blobs['data'].data[...] = img
out = model.forward()
prob= model.blobs["_fc"].data
print(prob.reshape(-1))
print(img.shape)
print(prob.shape)
