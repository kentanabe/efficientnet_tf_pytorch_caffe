#!/usr/bin/env bash

# This script accepts a single command-line argument, which specifies which model to download.
# Only the b0, b1, b2, and b3 models have been released, so your command must be one of them.

# For example, to download efficientnet-b0, run:
#   ./download.sh efficientnet-b0
# And to download efficientnet-b3, run:
#   ./download.sh efficientnet-b3

TYPE=$1
MODEL=$2
mkdir -p ${TYPE}
pushd ${TYPE}
wget https://storage.googleapis.com/cloud-tpu-checkpoints/efficientnet/${TYPE}/${MODEL}.tar.gz
tar xvf ${MODEL}.tar.gz
rm ${MODEL}.tar.gz
popd
