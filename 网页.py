import streamlit as st
import joblib
import numpy as np
import pandas as pd
import shap
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.font_manager import FontProperties
from xgboost import XGBClassifier
import xgboost as xgb

# 添加红色主题的 CSS 样式，并添加新的类用于红色框框
st.markdown("""
    <style>
  .main {
        background-color: #990000;  /* 红色主题背景色 */
        color: #ffffff;
        font-family: 'Arial', sans-serif;
    }
  .title {
        font-size: 48px;
        color: #660000;
        font-weight: bold;
        text-align: center;
        margin-bottom: 30px;
    }
  .subheader {
        font-size: 28px;
        color: #FFD700;  /* 金色副标题文字颜色 */
        margin-bottom: 25px;
        text-align: center;
        border-bottom: 2px solid #DDA0DD;
        padding-bottom: 10px;
        margin-top: 20px;
    }
  .input-label {
        font-size: 18px;
        font-weight: bold;
        color: #DDA0DD;
        margin-bottom: 10px;
    }
  .footer {
        text-align: center;
        margin-top: 50px;
        font-size: 16px;
        color: #D8BFD8;
        background-color: #660000;  /* 页脚背景色 */
        padding: 20px;
        border-top: 1px solid #6A5ACD;
    }
  .button {
        background-color: #CC0000;  /* 按钮红色背景 */
        border: none;
        color: white;
        padding: 12px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 18px;
        margin: 20px auto;
        cursor: pointer;
        border-radius: 10px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.5);
        transition: background-color 0.3s, box-shadow 0.3s;
    }
  .button:hover {
        background-color: #990000;  /* 按钮悬停颜色 */
        box-shadow: 0px 6px 10px rgba(0, 0, 0, 0.7);
    }
  .stSelectbox,.stNumberInput,.stSlider {
        margin-bottom: 20px;
    }
  .stSlider > div {
        padding: 10px;
        background: #E6E6FA;
        border-radius: 10px;
    }
  .prediction-result {
        font-size: 24px;
        color: #ffffff;
        margin-top: 30px;
        padding: 20px;
        border-radius: 10px;
        background: #6A5ACD;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3);
    }
  .advice-text {
        font-size: 20px;
        line-height: 1.6;
        color: #ffffff;
        background: #8A2BE2;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3);
        margin-top: 15px;
    }
    /* 新添加的类用于红色框框 */
  .recommendation-box {
        border: 2px solid #FF0000;  /* 红色边框 */
        padding: 10px;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='main'>", unsafe_allow_html=True)

# 页面标题
st.markdown('<div class="title">国潮新茶饮推荐茶饮预测</div>', unsafe_allow_html=True)

# Streamlit 界面设置
st.markdown('<div class="subheader">请填写以下信息以进行推荐茶饮预测：</div>', unsafe_allow_html=True)

# 年龄输入
age = st.number_input("您的年龄为：", min_value=1, max_value=120, value=10)

# 性别选择
sex_options = {1: '男性', 2: '女性'}
sex = st.selectbox("您的性别为：", options=list(sex_options.keys()), format_func=lambda x: sex_options[x])

# 产品类型选择
A_options = {1: '水果茶', 2: '鲜奶茶', 3: '气泡茶', 4: '冷泡茶', 5: '奶盖茶'}
A = st.selectbox("请选择您最日常喜爱的新茶饮产品类型： ", options=list(A_options.keys()), format_func=lambda x: A_options[x])

# 对将传统茶饮的经典口味与现代国潮文化元素相结合的产品满意度滑块
satisfaction = st.slider("您对将传统茶饮的经典口味与现代国潮文化元素相结合的产品满意度评分为（1 - 5）：", min_value=1, max_value=5, value=3)

# 对未来尝试新口味或创新饮品的兴趣程度滑块
sleep_status = st.slider("您对未来尝试新口味或创新饮品的兴趣程度为（1 - 5）：", min_value=1, max_value=5, value=3)


def predict():
    st.markdown("<div class='recommendation-box'>"  # 将整个推荐内容包裹在新的类中
                "<div class='recommendation-title'>茶饮推荐</div>"
                "<div class='recommendation-item'>根据我们的库，我们建议您尝试：</div>"
                "<div class='recommendation-item'>①霸王茶姬 伯牙绝弦</div>"
                "<div class='recommendation-item'>②茉莉奶白 栀子奶白</div>"
                "</div>", unsafe_allow_html=True)

if st.button("预测", key="predict_button"):
    predict()

# 页脚
st.markdown('<div class="footer">© 2024 All rights reserved.</div>', unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
