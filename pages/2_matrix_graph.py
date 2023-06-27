import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from math import pi
from streamlit_extras.dataframe_explorer import dataframe_explorer

showWarningOnDirectExecution = False

st.sidebar.markdown("# Matrix Graph")

uploaded_file = st.file_uploader("Please select a .csv file")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    df = pd.DataFrame(data)
    def transform_priority(col):
        if col.name == 'ExpertID':
            return col
        else:
            return 10 - (col * 2)

    transformed_df = df.copy()
    priority_columns = df.columns[1:]
    transformed_df[priority_columns] = transformed_df[priority_columns].apply(transform_priority)

    categories = list(transformed_df.columns[1:])
    N = len(categories)

    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]

    def update_chart(experts):
        fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'polar': True})
        ax.set_theta_offset(pi / 2)
        ax.set_theta_direction(-1)
        for expert in experts:
            if expert == "Average":
                values = np.mean(transformed_df.iloc[:, 1:], axis=0).tolist()
            else:
                values = transformed_df[transformed_df['ExpertID'] == expert].values[0][1:].tolist()
            values += values[:1]

            if expert == "Average":
                ax.plot(angles, values, linewidth=1, linestyle='solid', label="Average")
                ax.fill(angles, values, alpha=0.25)
            else:
                ax.plot(angles, values, linewidth=1, linestyle='solid', label=expert)
                ax.fill(angles, values, alpha=0.25)

        plt.xticks(angles[:-1], categories)
        plt.yticks([2, 4, 6, 8, 10], ["2", "4", "6", "8", "10"], color="grey", size=10)
        plt.ylim(0, 10)
        plt.title("Radar Chart for Experts", size=12)
        st.pyplot(fig)

    expert_list = transformed_df['ExpertID'].tolist()
    expert_list.insert(0, "Average")
    selected_experts = st.multiselect("Select Experts:", expert_list, default=["Average"])
    update_chart(selected_experts)