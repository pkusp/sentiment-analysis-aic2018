#!/user/bin/env python
# -*- coding:utf-8 -*-

import os
model_save_path = os.path.abspath('..') + "/data/"
project_path = os.path.abspath('..')
train_data_path = project_path + "/data/ai_challenger_sentiment_analysis_trainingset_20180816/sentiment_analysis_trainingset.csv"#"训练集文件存放路径"
validate_data_path = project_path + "/data/ai_challenger_sentiment_analysis_validationset_20180816/sentiment_analysis_validationset.csv"#"验证集文件存放路径"
test_data_path = project_path + "/data/ai_challenger_sentiment_analysis_testa_20180816/sentiment_analysis_testa.csv"#"测试集文件存放路径"
test_data_predict_out_path = project_path + "/doc/"#"测试集预测结果文件存放路径"


