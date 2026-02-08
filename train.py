import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix,classification_report
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib
from config import Config
from tqdm import tqdm  # 引入 tqdm 用于进度条

pd.set_option('display.expand_frame_repr', False)  # 避免宽表格换行
pd.set_option('display.max_columns', None)  # 确保所有列可见
conf = Config()

# 第一步：读取数据
# 读取训练数据集words labels
data=pd.read_csv(conf.process_train_datapath)
words=data["words"]
label=data["label"]
# print(data[:5])

# 第二步：将文本转换为数值特征 features
# 读取停用词文件
# 过滤掉空行，只保留非空的停用词
# stop_words = []  # 初始化空列表
# 逐行读取停用词文件
# for line in open(conf.stop_words_path, encoding="utf-8"):
#     cleaned_line = line.strip()  # 去掉每行首尾的换行、空格、制表符等
#     if cleaned_line:  # 判断清理后的内容是否非空（空行清理后就是""，会被过滤）
#         stop_words.append(cleaned_line)  # 非空才加入列表
# print(stop_words)
stop_words = open(conf.stop_words_path,encoding="utf-8").read().split()
td_idf=TfidfVectorizer(stop_words=stop_words)
features=td_idf.fit_transform(words)
# print("tf-idf=======================")
# print(features.shape)
# print("tf-idf=======================")
# print("原来选中的10个特征词：", td_idf.get_feature_names_out())
# # 查看第1个样本的原始文本
# print("第1个样本的原始words：", words.iloc[3])
# print(features[2].toarray())
#
# 第三步：划分训练集和测试集，模型训练和模型预测评估
x_train,x_test,y_train,y_test=train_test_split(features,label,test_size=0.2,random_state=22)
# # 训练随机森林模型
model = RandomForestClassifier(n_jobs=-1, verbose=2)
for  _ in tqdm(range(1)):
    model.fit(x_train, y_train)
# 模型预测并评估
print("模型评估...")
y_pred=model.predict(x_test)
print("准确率：",accuracy_score(y_test,y_pred))
print("混淆矩阵：",confusion_matrix(y_test,y_pred))
print("精确率 (micro):",precision_score(y_test,y_pred,average='micro'))
print("召回率 (micro):",recall_score(y_test,y_pred,average='micro'))
print("F1-score (micro):",f1_score(y_test,y_pred,average='micro'))
report=classification_report(y_test,y_pred)
print(report)

# 第四步：保存模型和向量化器 pickle
print("保存模型和向量化器...")
with open(conf.rf_model_save_path+ '/rf_model_1.pkl', 'wb') as f:
    pickle.dump(model, f)
with open(conf.rf_model_save_path+ '/vectorizer_1.pkl', 'wb') as f:
    pickle.dump(td_idf, f)

# joblib.dump(model, conf.rf_model_save_path + '/rf_model_1.pkl')
# joblib.dump(td_idf, conf.rf_model_save_path + '/vectorizer_1.pkl')
# joblib.dump(model, conf.rf_model_save_path + '/rf_model_1.pkl', compress=3)
# joblib.dump(td_idf, conf.rf_model_save_path + '/vectorizer_1.pkl', compress=3)
print("模型保存完成！")