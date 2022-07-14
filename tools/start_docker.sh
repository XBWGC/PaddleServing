#!/bin/bash

docker run \
  --name paddle_serving \
  -v `pwd`:/Serving \
  -p 8080:8080 \
  -it registry.baidubce.com/paddlepaddle/serving:0.9.0-devel \
  bash
