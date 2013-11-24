#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os
sys.path += ['..']
from libshorttext.analyzer import *

if __name__ == '__main__':
    predict_result = InstanceSet('predict_result')
    analyzer = Analyzer('train_file.model')
    insts = predict_result.select(wrong, with_labels(['女装', '钱包']), sort_by_dec, subset(100))
    analyzer.info(insts)
    analyzer.gen_confusion_table(insts)
    insts.load_text()
    print(insts[0])
    analyzer.analyze_single(insts[0], 0)
    print(insts[1])
    analyzer.analyze_single(insts[1], 0)
    print(insts[2])
    analyzer.analyze_single(insts[2], 0)
    analyzer.analyze_single('冬季新款保暖', 0)
