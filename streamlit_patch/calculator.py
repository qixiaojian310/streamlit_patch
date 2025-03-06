import streamlit as st
import pandas as pd
import numpy as np


class EchartCalculator:
    def __init__(self, data):
        self.calc_container = st.container()
        self.res_container = st.container()

    def inject_content(self):
        with self.calc_container:
            st.markdown(
                """<style>
            .stSlider [data-baseweb=slider]{
                width: 400px;
            }
            </style>""",
                unsafe_allow_html=True,
            )

            st.write("📝 Calculator")
            price = st.slider("Price", 0, 130, 25)
            flat = st.slider("Flat rate", 0, 130, 25)
            profit = st.slider("Profit", 0, 130, 25)
            st.button("Submit")
        self.calc_container.float(
            f"left: 0px; bottom: 0; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); border-radius: 10px;padding: 30px; width: 400px;box-sizing:content-box;z-index:999992"
        )

        with self.res_container:
            chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
            st.line_chart(chart_data, width=600, use_container_width=False, height=400)
            st.button("Close")
        self.res_container.float(
            f"background-color: white; left: 460px; bottom: 0%;transform: translate(0%,0%); box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); border-radius: 10px;box-sizing:content-box;padding: 30px; width: 600px; overflow: auto;height:450px;z-index:999992"
        )
