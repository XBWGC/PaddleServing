# Copyright (c) 2020 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# pylint: disable=doc-string-missing

from paddle_serving_client.httpclient import HttpClient
import sys
import numpy as np
import time
np.random.seed(2022)

client = HttpClient()
client.load_client_config("uci_housing_client/serving_client_conf.prototxt")
''' 
if you want use GRPC-client, set_use_grpc_client(True)
or you can directly use client.grpc_client_predict(...)
as for HTTP-client,set_use_grpc_client(False)(which is default)
or you can directly use client.http_client_predict(...)
'''
#client.set_use_grpc_client(True)
'''
if you want to enable Encrypt Module,uncommenting the following line
'''
#client.use_key("./key")
'''
if you want to compress,uncommenting the following line
'''
#client.set_response_compress(True)
#client.set_request_compress(True)
'''
we recommend use Proto data format in HTTP-body, set True(which is default)
if you want use JSON data format in HTTP-body, set False
'''
#client.set_http_proto(True)
client.connect(["127.0.0.1:8080"])
fetch_list = client.get_fetch_names()

for i in range(10):
    new_data = np.random.rand(1, 13).astype("float32")
    fetch_map = client.predict(
        feed={"x": new_data}, fetch=fetch_list, batch=True)
    print(fetch_map)
