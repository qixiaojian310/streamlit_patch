import streamlit as st
import time

# 初始化 session_state
if "streamed_content" not in st.session_state:
    st.session_state.streamed_content = ""


# 模拟流式请求
def stream_data():
    for i in range(5):
        time.sleep(1)  # 模拟延迟
        yield f"数据块 {i + 1}\n"


# 在 st.status 中进行流式请求
if st.button("开始流式请求"):
    with st.status("流式请求中..."):
        for chunk in stream_data():
            # 更新 session_state
            st.session_state.streamed_content += chunk

# 在 st.status 外部访问 session_state
st.write("### 流式请求的结果")
st.write(st.session_state.streamed_content)
