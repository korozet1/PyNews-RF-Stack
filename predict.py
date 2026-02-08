import pandas as pd
import pickle
from config import Config
import warnings
warnings.filterwarnings('ignore')

# 设置pandas显示选项
pd.set_option('display.max_columns', None)
# 加载配置
conf = Config()
# 第一步：加载保存的模型和向量化器
print("加载模型和向量化器...")
with open(conf.rf_model_save_path + '/rf_model_1.pkl', 'rb') as f:
    model = pickle.load(f)
with open(conf.rf_model_save_path + '/vectorizer_1.pkl', 'rb') as f:
    tfidf = pickle.load(f)
print("读取dev数据...")
dev_df = pd.read_csv(conf.proces_dev_datapath)
print("dev数据前5行:")
print(dev_df.head(5))
print("转换dev数据为数值...")
dev_features = tfidf.transform(dev_df['words'])
# 第四步：进行预测及保存
print("进行预测...")
dev_predictions = model.predict(dev_features)

# 保存预测结果
print("保存预测结果...")
output_df = pd.DataFrame({'words': dev_df['words'], 'predicted_label': dev_predictions})
output_path = conf.model_predict_result + '/dev_predictions.csv'
output_df.to_csv(output_path, index=False)
print(f"预测结果已保存到 {output_path}")
print("预测结果前5行:")
print(output_df.head(5))