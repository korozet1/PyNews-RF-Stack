# 💎 News-Prism Classifier | 中文新闻文本分类系统

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Framework-Flask%20%7C%20Streamlit-green.svg)](https://flask.palletsprojects.com/)
[![ML](https://img.shields.io/badge/Model-RandomForest-orange.svg)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)](LICENSE)

> **News-Prism** 是一个生产级、全栈式的中文新闻文本分类解决方案。
> 项目实现了从 **数据清洗 (ETL)** -> **特征工程 (TF-IDF)** -> **模型训练** -> **微服务部署 (Flask)** -> **可视化交互 (Streamlit)** 的完整闭环。

---

## 📸 效果演示 (Demo)

![Web Demo](demo_web.png)
*Streamlit 可视化交互界面*

---

## 🚀 快速开始 (Quick Start)

### 1. 环境准备
推荐使用 `Conda` 或 `virtualenv` 创建独立环境。

```bash
# 克隆项目
git clone https://github.com/your-username/News-Prism-Classifier.git
cd News-Prism-Classifier

# 安装依赖
pip install -r requirements.txt
```

### 2. 数据预处理 (ETL)
**首次运行必须执行！** 将原始语料清洗并分词，生成训练所需的 CSV 文件。

```bash
python data_EDA.py
```

### 3. 模型训练 (Model Training)
读取 CSV 数据，进行 TF-IDF 向量化和随机森林训练。
**注意：** 生成的模型文件 (`.pkl`) 约为 **1.5GB**，训练过程可能需要几分钟。

```bash
python train.py
# Output: save_model/rf_model_1.pkl
```

---

## 💻 启动服务 (Run Application)

本项目采用 **前后端分离** 架构，必须**同时启动**后端 API 和前端界面。

### 第 1 步：启动后端 API (Terminal 1)
打开一个新的终端窗口，运行 Flask 服务。它将监听 `8001` 端口，处理预测请求。

```bash
python api.py
```
> *看到 "Running on http://0.0.0.0:8001" 即代表启动成功。请勿关闭此窗口！*

### 第 2 步：启动前端界面 (Terminal 2)
打开第二个终端窗口，启动 Streamlit 可视化服务。

```bash
streamlit run app.py
```
> *浏览器将自动打开交互页面，即可开始输入文本进行测试。*

---

## 📂 核心文件说明 (File Manifest)

### 🛠️ 数据与训练 (Data & Training)
* **`data_EDA.py`** (ETL 清洗)
    * **功能**: 数据预处理入口。
    * **流程**: 读取 `train.txt` -> 调用 `jieba` 分词 -> 截取前30词 -> 生成 CSV。
* **`train.py`** (模型训练)
    * **功能**: 核心训练脚本。
    * **流程**: 读取 CSV -> TF-IDF 向量化 -> 训练随机森林模型 -> 保存 `.pkl` 文件。
* **`predict.py`** (离线验证)
    * **功能**: 批量跑分脚本。用于在 `dev.txt` 数据集上测试模型准确率。

### 🔌 服务与应用 (Service & App)
* **`api.py`** (后端接口)
    * **功能**: Flask 服务端。启动 HTTP 服务 (Port 8001)，提供 `POST /predict` 接口。
* **`app.py`** (前端界面)
    * **功能**: Streamlit 客户端。提供 Web 交互页面，调用后端接口展示结果。
* **`predict_fun.py`** (核心逻辑)
    * **功能**: 推理函数封装。被 `api.py` 调用，负责实时加载模型并进行单次预测。

### ⚙️ 配置与依赖 (Config & Env)
* **`config.py`** (全局配置)
    * **功能**: 路径管理中心。统一管理所有数据和模型的读写路径。
* **`requirements.txt`** (依赖清单)
    * **功能**: 记录项目运行所需的所有 Python 库 (pandas, sklearn, flask 等)。
* **`api_test.py`** (接口测试)
    * **功能**: 简单的请求测试脚本，用于检查 API 是否连通。

---

## 📡 API 文档 (API Documentation)

你也可以直接通过 HTTP 请求调用分类服务。

**接口地址**: `POST http://127.0.0.1:8001/predict`

**请求示例 (Python):**
```python
import requests

url = 'http://127.0.0.1:8001/predict'
data = {'text': "中国男篮在昨晚的比赛中绝杀对手，晋级决赛。"}

res = requests.post(url, json=data)
print(res.json())
```

**响应示例:**
```json
{
    "text": "中国男篮在昨晚的比赛中绝杀对手，晋级决赛。",
    "pred_class": "体育"
}
```

---

## 🤝 贡献 (Contribution)

欢迎提交 Issue 或 Pull Request！

1. Fork 本仓库
2. 新建 Feat_xxx 分支
3. 提交代码
4. 新建 Pull Request

---

## 📄 版权说明 (License)

本项目采用 [MIT License](LICENSE) 开源。
