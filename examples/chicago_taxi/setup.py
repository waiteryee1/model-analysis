# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Setup dependencies for local and cloud deployment."""
import setuptools

TF_VERSION = '1.9.0'

if __name__ == '__main__':
  setuptools.setup(
      name='tfx_chicago_taxi',
      version='0.9.2',
      packages=setuptools.find_packages(),
      install_requires=[
          'apache-beam[gcp]==2.6.0',
          'jupyter==1.0',
          'numpy==1.13.3',
          'protobuf==3.6.0',
          'tensorflow=='+TF_VERSION,
          'tensorflow-data-validation==0.9.0',
          'tensorflow-metadata==0.9.0',
          'tensorflow-model-analysis==0.9.2',
          'tensorflow-serving-api==1.9.0',
          'tensorflow-transform==0.9.0',
      ])
