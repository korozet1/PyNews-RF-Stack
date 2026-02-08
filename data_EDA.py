# 导入必要的库
import pandas as pd
import jieba
from config import Config
# 初始化配置文件
conf = Config()
#设置处理的及分析的文件路径，默认为 train.txt
# current_path=conf.train_datapath
# current_path=conf.test_datapath
# current_path=conf.dev_datapath
# 第一步：读取数据
train_data=pd.read_csv(conf.train_datapath, sep='\t', names=['text', 'label'])
print(train_data.head())

# 第二步：进行分词预处理 cut_sentence
def cut_sentence(s):
    # ' '.join(list(jieba.cut(s))[:30])
    final_s=" ".join(jieba.lcut(s)[0:30])
    return final_s

train_data['words']=train_data['text'].apply(cut_sentence)
print(train_data.head(5))

# 第三步：保存处理后的数据
train_data.to_csv(conf.process_train_datapath, index=False)# 将处理后的数据保存到CSV文件
