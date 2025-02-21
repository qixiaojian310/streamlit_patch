import streamlit as st
from streamlit_float import *
from streamlit_echarts import st_echarts
import streamlit as st
import re


# 定义一个替换<text>标签为EChartsToggleButton按钮的函数
def process_markdown_and_create_buttons(text):
    options = {
        "title": {"text": "ECharts Example"},
        "tooltip": {},
        "xAxis": {"data": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]},
        "yAxis": {},
        "series": [
            {"name": "Sales", "type": "bar", "data": [120, 200, 150, 80, 70, 110, 130]}
        ],
    }
    # 使用正则表达式按 <link> 分割文本
    parts = re.split(r"(《.*?》)", text)  # 使用括号保留标签本身，非贪婪匹配
    button_name = ""

    for part in parts:
        if part.startswith("《") and part.endswith("》"):  # 判断是否为标签
            button_name = part[1:-1]
            # 显示图表
            display_echarts_with_toggle(
                options, button_name, f"show_echart_{button_name}"
            )
        else:
            # 否则直接添加文本
            st.markdown(button_name + " " + part, unsafe_allow_html=True)


# 定义一个函数封装组件的逻辑
def display_echarts_with_toggle(options, button_name="Click me", button_key=""):
    options["title"]["text"] = button_name
    # 初始化float功能
    float_init()

    # 使用 session_state 来保存容器显示状态
    if button_key not in st.session_state:
        st.session_state[button_key] = False  # 默认不显示容器

    # 按钮点击时改变变量的值
    if st.button(button_name):
        st.session_state[button_key] = not st.session_state[button_key]

    # 根据变量显示或隐藏容器
    if st.session_state[button_key]:
        container = st.container()
        with container:
            st_echarts(options=options)
        container.float(
            f"background-color: white; transform: translate(calc({len(button_name) + 2} * 10px), -60px); box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); border-radius: 10px;padding: 10px; position: absolute;"
        )
