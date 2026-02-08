from flask import Flask, request, jsonify
import jieba
import pandas as pd
import pickle
from config import Config
import warnings
from predict_fun import predict
warnings.filterwarnings('ignore')
pd.set_option('display.max_columns', None)

app = Flask(__name__)

@app.route('/predict', methods=['POST'])

def predict_api():
    # 获取 JSON 输入
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'Missing text field in JSON'}), 400

    # 调用预测函数
    result = predict(data)

    # 返回 JSON 结果
    return jsonify(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001, debug=True)