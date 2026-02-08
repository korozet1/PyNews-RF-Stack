# 💎 News-Prism Classifier | 中文新闻文本分类系统

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Framework-Flask%20%7C%20Streamlit-green.svg)](https://flask.palletsprojects.com/)
[![ML](https://img.shields.io/badge/Model-RandomForest-orange.svg)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)](LICENSE)

> **News-Prism** 是一个生产级、全栈式的中文新闻文本分类解决方案。
> 项目实现了从 **数据清洗 (ETL)**、**特征工程 (TF-IDF)**、**模型训练** 到 **微服务部署 (Flask)** 及 **可视化交互 (Streamlit)** 的完整闭环。

---

## 📸 效果演示 (Demo)

| **Web 可视化界面 (Streamlit)** | **API 接口测试 (Postman)** |
|:---:|:---:|
| ![Web Demo](https://via.placeholder.com/600x300?text=Streamlit+Web+UI+Screenshot) | ![API Demo](https://via.placeholder.com/600x300?text=API+Response+Screenshot) |
| *直观的交互式分类面板* | *高性能 RESTful API 响应* |

---

## ✨ 核心特性 (Key Features)

* 🔄 **全链路闭环**: 覆盖数据预处理 -> 模型训练 -> 模型评估 -> 服务上线全流程。
* 🧠 **经典算法实现**: 基于 `RandomForest` (随机森林) + `TF-IDF`，在小样本下依然保持高鲁棒性。
* 🔌 **RESTful API**: 基于 `Flask` 封装标准 HTTP 接口，支持跨语言调用。
* 📊 **交互式 Dashboard**: 基于 `Streamlit` 构建的前端，支持实时文本输入与分类预测。
* 📦 **模型持久化**: 采用 `joblib` 进行模型压缩与存储，实现训练与推理分离。
* ⚡ **工程化代码**: 模块化设计，配置 (`config.py`) 与逻辑分离，易于维护和扩展。

---

## 🏗️ 系统架构 (Architecture)

```mermaid
graph LR
    A[原始语料 train.txt] -->|data_EDA.py| B(数据清洗 & 分词)
    B -->|生成| C[process_train.csv]
    C -->|train.py| D{随机森林模型训练}
    D -->|保存| E[save_model/*.pkl]
    E -->|加载| F[predict_fun.py]
    F --> G[Flask API (后端)]
    F --> H[Streamlit App (前端)]
```

---

## 🚀 快速开始 (Quick Start)

### 1. 环境准备
推荐使用 `Conda` 或 `virtualenv` 创建独立环境。
```bash
git clone https://github.com/your-username/News-Prism-Classifier.git
cd News-Prism-Classifier
pip install -r requirements.txt
```

### 2. 数据预处理 (ETL) ⚠️
**首次运行必须执行！** 将原始语料清洗并分词，生成训练所需的 CSV 文件。
```bash
python data_EDA.py
# Output: data/process_train.csv (约 1.5GB)
```

### 3. 模型训练 (Model Training)
读取 CSV 数据，进行 TF-IDF 向量化和随机森林训练。
*(注：根据机器性能，此步骤可能需要几分钟)*
```bash
python train.py
# Output: save_model/rf_model_1.pkl, save_model/vectorizer_1.pkl
```

### 4. 启动服务 (Launch)

#### 🅰️ 启动可视化界面 (推荐)
```bash
streamlit run app.py
```
> 浏览器将自动打开 `http://localhost:8501`

#### 🅱️ 启动后端 API
```bash
python api.py
```
> 服务将监听 `http://0.0.0.0:8001`

---

## 📡 API 文档 (API Documentation)

启动 `api.py` 后，可以通过 HTTP 请求调用分类服务。

### POST `/predict`

* **功能**: 对输入的中文文本进行分类预测。
* **Content-Type**: `application/json`

**请求示例 (Request):**
```json
{
    "text": "中国男篮在昨晚的比赛中绝杀对手，晋级决赛。"
}
```

**响应示例 (Response):**
```json
{
    "text": "中国男篮在昨晚的比赛中绝杀对手，晋级决赛。",
    "pred_class": "体育"
}
```

**CURL 测试命令:**
```bash
curl -X POST http://127.0.0.1:8001/predict \
     -H "Content-Type: application/json" \
     -d '{"text":"中国男篮在昨晚的比赛中绝杀对手，晋级决赛。"}'
```

---

## 📂 项目目录 (Directory Structure)

```text
News-Prism-Classifier/
├── 📄 api.py               # Flask 后端接口
├── 📄 app.py               # Streamlit 前端应用
├── 📄 config.py            # 全局路径配置 (Config)
├── 📄 data_EDA.py          # ETL 数据清洗脚本
├── 📄 train.py             # 模型训练脚本
├── 📄 predict.py           # 离线批量验证脚本
├── 📄 predict_fun.py       # 核心推理逻辑封装
├── 📄 requirements.txt     # 项目依赖
├── 📂 data/                # 数据仓库
│   ├── class.txt           # 类别标签映射
│   ├── stopwords.txt       # 停用词表
│   └── ...
├── 📂 save_model/          # 模型存储 (Git忽略)
└── 📂 result/              # 预测结果 (Git忽略)
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
