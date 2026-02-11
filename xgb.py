import pandas as pd
import pickle
import time
from xgboost import XGBClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.model_selection import train_test_split
from config import Config
from sklearn.feature_extraction.text import CountVectorizer

# 1. 配置和读取
conf = Config()
data = pd.read_csv(conf.process_train_datapath)
words = data["words"]
label = data["label"]

# 2. 特征提取
print("正在提取特征...")
stop_words = open(conf.stop_words_path, encoding="utf-8").read().split()
vec = CountVectorizer(stop_words=stop_words, ngram_range=(1, 2))
features = vec.fit_transform(words)

# 3. 标签编码
le = LabelEncoder()
label_encoded = le.fit_transform(label)

# 4. 划分数据
x_train, x_test, y_train, y_test = train_test_split(features, label_encoded, test_size=0.2, random_state=22)

# ================= 🚀 CPU 极速训练模式 =================
print("🔥 开始训练 (CPU Hist模式 - 速度快且稳)...")
start_time = time.time()

model = XGBClassifier(
    n_estimators=500,  # 树的数量：500棵，保证精度
    learning_rate=0.05,  # 学习率
    max_depth=30,  # 【核心】深度30，专门针对文本特征，提升准确率

    # --- 关键加速参数 ---
    device='cpu',  # 强制用 CPU，保证 100% 不出错
    tree_method='hist',  # 【⭐提速神器】开启直方图优化，CPU 也能跑得飞快！
    n_jobs=-1,  # 调用所有 CPU 核心
    # ------------------

    objective='multi:softmax',
    num_class=len(le.classes_),
    subsample=0.8,
    colsample_bytree=0.6,
    random_state=22
)

model.fit(x_train, y_train)
print(f"✅ 训练耗时: {time.time() - start_time:.2f} 秒")

# 6. 预测和评估
print("🤖 模型评估中...")
y_pred = model.predict(x_test)

print("🎯 准确率：", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# 7. 保存模型
print("💾 保存模型...")
with open(conf.rf_model_save_path + '/xgb_model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open(conf.rf_model_save_path + '/vectorizer.pkl', 'wb') as f:
    pickle.dump(vec, f)

with open(conf.rf_model_save_path + '/label_encoder.pkl', 'wb') as f:
    pickle.dump(le, f)

print("🎉 搞定！这次肯定稳了！")