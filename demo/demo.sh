#!/bin/bash

python ../text-train.py -f  train_file
python ../text-predict.py -f  test_file train_file.model predict_result
python demo.py
