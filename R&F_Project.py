import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from math import pi
from streamlit_extras.dataframe_explorer import dataframe_explorer


st.sidebar.markdown("# UN POP Helpline")

questions = [
    {
        'question': 'In which phase of the  do you feel your digital channel implementation is?',
        'weight': 0.077,
        'answers': {
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5
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
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5
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
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5
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
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5
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
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5
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
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5
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
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5
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
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5
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
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5
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
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5
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

hovers = {
    'hover': {
        0: 'Risk management plan', # Digital 1
        1: 'Technology review and enhancement', # Tech used 2
        2: 'Fundraising strategy development', # Fundraising 3
        3: 'Security audit', # Confidentiality 4
        4: 'Response time monitoring', #Responsiveness 5
        5: 'Developing multi-platform accessibility', # User experience 6
        6: 'Staff training programs', # Staff expertise 7
        7: 'Diversity and inclusion training', # Cultural and linguistic sensitivity 8
        8: 'Developmental training for staff', # Age 9
        9: '24/7 Availability initiative' # Accessibility 10
    }
}

dictionary_values = list(hovers["hover"].values())

st.title('Helpline Evaluation Test')
st.markdown('The following test aims to evaluate how well is your helpline performing, after answering these 10 questions, you will get a final score from 0 to 5, and a series of recomendations based on your answers')

answers = {}
for i, question in enumerate(questions):
    st.subheader(question['question'])
    answer = st.selectbox(f'Select your answer for:\n{dictionary_values[i]}', list(question['answers'].keys()))
    answers[i] = {
        'answer': question['answers'][answer],
        'recomendation': question['recomendations'][question['answers'][answer]]
    }

final_score = sum(answer['answer'] * question['weight'] for question, answer in zip(questions, answers.values()))

if st.button('Submit'):
    st.subheader('Final Score')
    st.write(final_score)

    st.subheader('Recommendations')
    for i, answer in answers.items():
        st.markdown(f"{answer['recomendation']}", unsafe_allow_html=True)