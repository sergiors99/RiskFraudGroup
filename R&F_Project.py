import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from math import pi
from streamlit_extras.app_logo import add_logo

add_logo("data/UN_Logo.png", height=100)

questions = [
    {
        'question': 'In which phase of the  do you feel your digital channel implementation is?',
        'weight': 0.077,
        'answers': {
            '0. Risk management plan': 0,
            'Answer 1': 1,
            'Answer 2': 2,
            'Answer 3': 3,
            'Answer 4': 4,
            'Answer 5': 5
        },
        'recomendations': {
            0: "**IT Infrastructure:** <br>Develop a detailed risk management plan that includes risk identification, assessment, response planning, and monitoring.<br>Estimated time: 1 week",
            1: "**IT Infrastructure:** <br>Based on the audit results, upgrade the IT infrastructure as necessary. This could involve increasing server capacity, updating software, etc.<br>Estimated time: 2 weeks",
            2: "**IT Infrastructure:** <br>Conduct a thorough audit of the existing IT infrastructure to ensure it can support the new digital channel launch. This step is crucial in mitigating the risk early on.<br>Estimated time: 1 week",
            3: "**IT Infrastructure:** <br>Provide technical training to the team involved in managing the digital channel. They should be able to operate, maintain, and troubleshoot the new channel.<br>Estimated time: 2 weeks",
            4: "**IT Infrastructure:** <br>Despite all efforts, there may still be unforeseen problems. Having a robust contingency plan can help manage these effectively.<br>Estimated time: 1 week",
            5: "**IT Infrastructure:** <br>Implement a structured User Acceptance Testing phase where a select group of end-users try out the new digital channel before it's fully launched. Their feedback can be used to make final adjustments, ensuring the channel meets user expectations and requirements.<br>Estimated time: 2 weeks"
        }
    },
    {
        'question': 'How complete is your technology stack for digital channels?',
        'weight': 0.098,
        'answers': {
            '0. Technology review and enhancement': 0,
            'Answer 1': 1,
            'Answer 2': 2,
            'Answer 3': 3,
            'Answer 4': 4,
            'Answer 5': 5
        },
        'recomendations': {
            0: 'Recomendation for Question 2 - Answer 0',
            1: 'Recomendation for Question 2 - Answer 1',
            2: 'Recomendation for Question 2 - Answer 2',
            3: 'Recomendation for Question 2 - Answer 3',
            4: 'Recomendation for Question 2 - Answer 4',
            5: 'Recomendation for Question 2 - Answer 5'
        }
    },
    {
        'question': 'How do you feel your fundraise strategy is  enough and steady to cover your cost short and long term?',
        'weight': 0.115,
        'answers': {
            '0. Fundraising strategy development': 0,
            'Answer 1': 1,
            'Answer 2': 2,
            'Answer 3': 3,
            'Answer 4': 4,
            'Answer 5': 5
        },
        'recomendations': {
            0: 'Recomendation for Question 2 - Answer 0',
            1: 'Recomendation for Question 2 - Answer 1',
            2: 'Recomendation for Question 2 - Answer 2',
            3: 'Recomendation for Question 2 - Answer 3',
            4: 'Recomendation for Question 2 - Answer 4',
            5: 'Recomendation for Question 2 - Answer 5'
        }
    },
    {
        'question': 'To what extent your helpline maintain confidentiality and ensure the privacy of children seeking help?',
        'weight': 0.159,
        'answers': {
            '0. Security audit': 0,
            'Answer 1': 1,
            'Answer 2': 2,
            'Answer 3': 3,
            'Answer 4': 4,
            'Answer 5': 5
        },
        'recomendations': {
            0: 'Recomendation for Question 2 - Answer 0',
            1: 'Recomendation for Question 2 - Answer 1',
            2: 'Recomendation for Question 2 - Answer 2',
            3: 'Recomendation for Question 2 - Answer 3',
            4: 'Recomendation for Question 2 - Answer 4',
            5: 'Recomendation for Question 2 - Answer 5'
        }
    },
    {
        'question': "How satisfied are you with the timeliness and responsiveness of helpline services in addressing children's needs?",
        'weight': 0.093,
        'answers': {
            '0. Response time monitoring': 0,
            'Answer 1': 1,
            'Answer 2': 2,
            'Answer 3': 3,
            'Answer 4': 4,
            'Answer 5': 5
        },
        'recomendations': {
            0: 'Recomendation for Question 2 - Answer 0',
            1: 'Recomendation for Question 2 - Answer 1',
            2: 'Recomendation for Question 2 - Answer 2',
            3: 'Recomendation for Question 2 - Answer 3',
            4: 'Recomendation for Question 2 - Answer 4',
            5: 'Recomendation for Question 2 - Answer 5'
        }
    },
    {
        'question': 'How confident are you in the overall quality and impact of helpline services for improving the well-being and safety of children?',
        'weight': 0.089,
        'answers': {
            '0. Developing multi-platform accessibility': 0,
            'Answer 1': 1,
            'Answer 2': 2,
            'Answer 3': 3,
            'Answer 4': 4,
            'Answer 5': 5
        },
        'recomendations': {
            0: 'Recomendation for Question 2 - Answer 0',
            1: 'Recomendation for Question 2 - Answer 1',
            2: 'Recomendation for Question 2 - Answer 2',
            3: 'Recomendation for Question 2 - Answer 3',
            4: 'Recomendation for Question 2 - Answer 4',
            5: 'Recomendation for Question 2 - Answer 5'
        }
    },
    {
        'question': 'How knowledgeable are the helpline staff about the specific issues and challenges faced by children in your country?',
        'weight': 0.051,
        'answers': {
            '0. Staff training programs': 0,
            'Answer 1': 1,
            'Answer 2': 2,
            'Answer 3': 3,
            'Answer 4': 4,
            'Answer 5': 5
        },
        'recomendations': {
            0: 'Recomendation for Question 2 - Answer 0',
            1: 'Recomendation for Question 2 - Answer 1',
            2: 'Recomendation for Question 2 - Answer 2',
            3: 'Recomendation for Question 2 - Answer 3',
            4: 'Recomendation for Question 2 - Answer 4',
            5: 'Recomendation for Question 2 - Answer 5'
        }
    },
    {
        'question': 'To what extent are helpline services tailored to meet the diverse cultural and linguistic needs of children in your country?',
        'weight': 0.161,
        'answers': {
            '0. Diversity and inclusion training': 0,
            'Answer 1': 1,
            'Answer 2': 2,
            'Answer 3': 3,
            'Answer 4': 4,
            'Answer 5': 5
        },
        'recomendations': {
            0: 'Recomendation for Question 2 - Answer 0',
            1: 'Recomendation for Question 2 - Answer 1',
            2: 'Recomendation for Question 2 - Answer 2',
            3: 'Recomendation for Question 2 - Answer 3',
            4: 'Recomendation for Question 2 - Answer 4',
            5: 'Recomendation for Question 2 - Answer 5'
        }
    },
    {
        'question': 'How effective are helplines in providing age-appropriate guidance and support to children based on their developmental stages (by adults or peers)?',
        'weight': 0.067,
        'answers': {
            '0. Developmental training for staff': 0,
            'Answer 1': 1,
            'Answer 2': 2,
            'Answer 3': 3,
            'Answer 4': 4,
            'Answer 5': 5
        },
        'recomendations': {
            0: 'Recomendation for Question 2 - Answer 0',
            1: 'Recomendation for Question 2 - Answer 1',
            2: 'Recomendation for Question 2 - Answer 2',
            3: 'Recomendation for Question 2 - Answer 3',
            4: 'Recomendation for Question 2 - Answer 4',
            5: 'Recomendation for Question 2 - Answer 5'
        }
    },
    {
        'question': 'How satisfied are you with the accessibility of helplines for children in terms of availability and ease of contact?',
        'weight': 0.09,
        'answers': {
            '0. 24/7 Availability initiative': 0,
            'Answer 1': 1,
            'Answer 2': 2,
            'Answer 3': 3,
            'Answer 4': 4,
            'Answer 5': 5
        },
        'recomendations': {
            0: 'Recomendation for Question 2 - Answer 0',
            1: 'Recomendation for Question 2 - Answer 1',
            2: 'Recomendation for Question 2 - Answer 2',
            3: 'Recomendation for Question 2 - Answer 3',
            4: 'Recomendation for Question 2 - Answer 4',
            5: 'Recomendation for Question 2 - Answer 5'
        }
    }
]

background_image_url = 'data/UN_Logo.png'

def app():
    st.title('Helpline Evaluation Test')
    st.markdown('The following test aims to evaluate how well is your helpline performing, after answering these 10 questions, you will get a final score from 0 to 5, and a series of recomendations based on your answers')

    answers = {}
    for i, question in enumerate(questions):
        st.subheader(question['question'])
        answer = st.selectbox('Select your answer', list(question['answers'].keys()))
        answers[i] = {
            'answer': question['answers'][answer],
            'recomendation': question['recomendations'][question['answers'][answer]]
        }

    # Calculate final score
    final_score = sum(answer['answer'] * question['weight'] for question, answer in zip(questions, answers.values()))

    if st.button('Submit'):
        st.subheader('Final Score')
        st.write(final_score)

        st.subheader('Recommendations')
        for i, answer in answers.items():
            st.markdown(f"{answer['recomendation']}", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Please select a .csv file")

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

transformed_df = pd.read_csv("transformed_data.csv")

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

if __name__ == '__main__':
    app()