# 💎 News-Prism Classifier | 中文新闻文本分类系统

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Framework-Flask%20%7C%20Streamlit-green.svg)](https://flask.palletsprojects.com/)
[![ML](https://img.shields.io/badge/Model-RandomForest-orange.svg)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)](LICENSE)

> **News-Prism** 是一个生产级、全栈式的中文新闻文本分类解决方案。
> 项目实现了从 **数据清洗 (ETL)** -> **特征工程 (TF-IDF)** -> **模型训练** -> **微服务部署 (Flask)** -> **可视化交互 (Streamlit)** 的完整闭环。

---

## 📸 效果演示 (Demo) --> Streamlit 可视化交互界面

![Web Demo](demo_web.png)


---

## 🚀 快速开始 (Quick Start)

### 1. 环境准备
推荐使用 `Conda` 或 `virtualenv` 创建独立环境。

```bash
# 克隆项目
git clone https://github.com/korozet1/PyNews-RF-Stack.git
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
> *看到 "Running on [http://0.0.0.0:8001](http://0.0.0.0:8001)" 即代表启动成功。请勿关闭此窗口！*

### 第 2 步：启动前端界面 (Terminal 2)
打开第二个终端窗口，启动 Streamlit 可视化服务。

```bash
streamlit run app.py
```
> *浏览器将自动打开交互页面，即可开始输入文本进行测试。*

---

## 📂 核心文件说明 (File Manifest)

| 文件 (File) | 类型 | 功能简介 (Description) |
| :--- | :--- | :--- |
| **`data_EDA.py`** | 🧹 清洗 | **数据预处理**。读取语料 -> 结巴分词 -> 截取前30词 -> 生成CSV。 |
| **`train.py`** | 🧠 训练 | **模型训练**。读取CSV -> TF-IDF向量化 -> 随机森林训练 -> 保存模型。 |
| **`api.py`** | 🔌 后端 | **Flask 服务端**。提供 `POST /predict` 接口，端口 8001。 |
| **`app.py`** | 🖥️ 前端 | **Streamlit 客户端**。Web 交互页面，调用后端接口展示结果。 |
| **`predict_fun.py`** | ⚙️ 核心 | **推理逻辑封装**。包含 `predict()` 函数，负责加载模型与预测。 |
| **`config.py`** | 🔧 配置 | **全局配置**。统一管理文件路径 (Path)，避免硬编码。 |
| **`predict.py`** | 🧪 验证 | **离线跑分**。在 `dev.txt` 上批量验证模型准确率。 |
| **`api_test.py`** | 🚦 测试 | **接口测试**。检测 Flask 服务是否连通的简单脚本。 |
| **`requirements.txt`**| 📦 依赖 | **环境清单**。记录项目运行所需的所有 Python 库。 |

---

## 📡 API 文档 (API Documentation)

你也可以直接通过 HTTP 请求调用分类服务。

**接口地址**: `POST http://127.0.0.1:8001/predict`

**请求示例 (Python):**
```python
import requests

url = '[http://127.0.0.1:8001/predict](http://127.0.0.1:8001/predict)'
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
