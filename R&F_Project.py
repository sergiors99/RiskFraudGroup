import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from math import pi
from streamlit_extras.dataframe_explorer import dataframe_explorer

st.set_page_config(page_title="UN POP Project", page_icon="data/favicon.ico", layout="centered", initial_sidebar_state="auto", menu_items=None)

st.sidebar.markdown("# UN POP Helpline")
st.sidebar.image("data/UN-Logo.png", use_column_width=True)

questions = [
    {
        'question': 'How relevevant is the "Digital Channel Launching Process"?',
        'weight': 0.077,
        'answers': {
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5
        },
        'recomendations': {
            0: "**IT Infrastructure:** <br>The digital channel launching process is poorly organized and lacks clear guidelines or procedures. Recommendation: Establish clear guidelines and procedures for launching digital channels, including documentation and training materials.",
            1: "**IT Infrastructure:** <br>The digital channel launching process is somewhat disorganized, and guidelines are not consistently followed. Recommendation: Review and refine the launching process to ensure better organization and adherence to guidelines.",
            2: "**IT Infrastructure:** <br>The digital channel launching process is average, but there is room for improvement in terms of efficiency and effectiveness. Recommendation: Identify areas of improvement and implement necessary changes to streamline the launching process.",
            3: "**IT Infrastructure:** <br>The digital channel launching process is well-defined and generally followed. Recommendation: Continuously monitor and update the launching process to maintain its effectiveness.",
            4: "**IT Infrastructure:** <br>The digital channel launching process is well-organized and documented. Recommendation: Regularly review and update the launching process to incorporate best practices and emerging technologies.",
            5: "**IT Infrastructure:** <br>The digital channel launching process is highly efficient, standardized, and continuously improved. Recommendation: Share the best practices and lessons learned with other organizations to promote excellence in digital channel launching."
        }
    },
    {
        'question': 'How relevevant is the "Technology used/ in use/ Future"?',
        'weight': 0.098,
        'answers': {
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5
        },
        'recomendations': {
            0: '**IT Infrastructure:** <br>Outdated or unreliable technology is being used, hindering the effectiveness of online protection systems. Recommendation: Invest in upgrading technology infrastructure to ensure reliable and up-to-date systems.',
            1: '**IT Infrastructure:** <br>The technology used is somewhat outdated and may have limitations in supporting online protection systems. Recommendation: Assess and prioritize technology upgrades to enhance system performance and reliability.',
            2: '**IT Infrastructure:** <br>The technology used is average but may require updates to align with emerging trends and advancements. Recommendation: Regularly evaluate and update technology solutions to meet current and future needs.',
            3: '**IT Infrastructure:** <br>The technology used is up-to-date and supports online protection systems effectively. Recommendation: Stay informed about emerging technologies to identify opportunities for enhancing system capabilities.',
            4: '**IT Infrastructure:** <br>The technology used is modern and robust, meeting the requirements of online protection systems. Recommendation: Continuously monitor and evaluate technology advancements to ensure the systems remain cutting-edge.',
            5: '**IT Infrastructure:** <br>The technology used is state-of-the-art, providing a strong foundation for online protection systems. Recommendation: Foster collaboration with technology experts and industry leaders to stay at the forefront of technological advancements.'
        }
    },
    {
        'question': 'How relevevant is the "Fundraising"?',
        'weight': 0.115,
        'answers': {
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5
        },
        'recomendations': {
            0: '**IT Infrastructure:** <br>Insufficient funds are being raised, limiting the resources available for online protection systems. Recommendation: Develop comprehensive fundraising strategies and explore diverse funding sources to secure necessary financial support.',
            1: '**IT Infrastructure:** <br>The fundraising efforts are somewhat limited, and additional funding sources should be explored. Recommendation: Expand fundraising initiatives and engage with potential donors and sponsors to increase financial support.',
            2: '**IT Infrastructure:** <br>Fundraising efforts are average, but more proactive approaches are needed to secure sustainable funding. Recommendation: Implement targeted fundraising campaigns, grant applications, and partnership opportunities to maximize financial resources.',
            3: '**IT Infrastructure:** <br>Fundraising efforts are adequate and provide a stable financial foundation for online protection systems. Recommendation: Maintain a diversified fundraising approach to sustain and grow financial support.',
            4: '**IT Infrastructure:** <br>Fundraising efforts are effective, resulting in substantial resources for online protection systems. Recommendation: Continue building strong relationships with donors and sponsors, leveraging success stories to attract more support.',
            5: '**IT Infrastructure:** <br>The fundraising efforts are exceptional, ensuring abundant resources for online protection systems. Recommendation: Share fundraising best practices and collaborate with other organizations to further strengthen financial sustainability.'
        }
    },
    {
        'question': 'How relevevant is the "Confidentiality"?',
        'weight': 0.159,
        'answers': {
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5
        },
        'recomendations': {
            0: '**IT Infrastructure:** <br>Confidentiality measures are not in place or poorly implemented, risking the privacy and safety of users. Recommendation: Implement strict confidentiality protocols and robust data protection measures to ensure user privacy and safety.',
            1: '**IT Infrastructure:** <br>Confidentiality measures are partially implemented, but there are gaps that need to be addressed. Recommendation: Conduct a thorough review of existing confidentiality measures and enhance them to meet industry standards and regulatory requirements.',
            2: '**IT Infrastructure:** <br>Confidentiality measures are average, but further improvements are necessary to ensure the privacy and confidentiality of user data. Recommendation: Regularly assess and update confidentiality measures to align with evolving data protection practices.',
            3: '**IT Infrastructure:** <br>Confidentiality measures are well-established and effectively implemented to protect user data and maintain privacy. Recommendation: Continuously monitor and update confidentiality measures to address emerging threats and vulnerabilities.',
            4: '**IT Infrastructure:** <br>Confidentiality measures are robust, meeting or exceeding industry standards for protecting user privacy. Recommendation: Share best practices and collaborate with other organizations to further enhance confidentiality measures.',
            5: '**IT Infrastructure:** <br>The highest level of confidentiality measures is in place, ensuring the utmost protection of user data and privacy. Recommendation: Conduct regular audits and security assessments to maintain the highest level of confidentiality standards.'
        }
    },
    {
        'question': 'How relevevant is the "Responsiveness"?',
        'weight': 0.093,
        'answers': {
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5
        },
        'recomendations': {
            0: '**IT Infrastructure:** <br>The online protection system is unresponsive or slow, leading to delays in providing support and assistance. Recommendation: Optimize system performance and responsiveness through technical improvements and resource allocation.',
            1: "**IT Infrastructure:** <br>The system's responsiveness is inconsistent, causing occasional delays in addressing user needs. Recommendation: Identify and address the root causes of responsiveness issues to ensure a consistent and timely response.",
            2: "**IT Infrastructure:** <br>he online protection system's responsiveness is average, but there is room for improvement in terms of speed and efficiency. Recommendation: Implement measures to enhance system responsiveness, such as optimizing server infrastructure and streamlining processes.",
            3: '**IT Infrastructure:** <br>The online protection system is generally responsive, providing timely assistance to users. Recommendation: Monitor system responsiveness and conduct regular user feedback assessments to maintain satisfactory performance.',
            4: '**IT Infrastructure:** <br>The online protection system is highly responsive, offering quick and efficient support to users. Recommendation: Continuously evaluate and optimize system performance to maintain a high level of responsiveness.',
            5: '**IT Infrastructure:** <br>The online protection system demonstrates exceptional responsiveness, ensuring immediate support and assistance to users. Recommendation: Share best practices and collaborate with other organizations to advance responsiveness standards across the industry.'
        }
    },
    {
        'question': 'How relevevant is the "User Experience"?',
        'weight': 0.089,
        'answers': {
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5
        },
        'recomendations': {
            0: '**IT Infrastructure:** <br>The user experience is extremely poor, making it difficult for users to navigate and access the necessary support. Recommendation: Conduct a comprehensive user experience assessment and redesign the system to improve usability and accessibility.',
            1: '**IT Infrastructure:** <br>',
            2: '**IT Infrastructure:** <br>',
            3: '**IT Infrastructure:** <br>',
            4: '**IT Infrastructure:** <br>',
            5: '**IT Infrastructure:** <br>'
        }
    },
    {
        'question': 'How relevevant is the "Staff expertise"?',
        'weight': 0.051,
        'answers': {
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5
        },
        'recomendations': {
            0: '**IT Infrastructure:** <br>',
            1: '**IT Infrastructure:** <br>',
            2: '**IT Infrastructure:** <br>',
            3: '**IT Infrastructure:** <br>',
            4: '**IT Infrastructure:** <br>',
            5: '**IT Infrastructure:** <br>'
        }
    },
    {
        'question': 'How relevevant is the "Cultural and Linguistic Sensitivity"?',
        'weight': 0.161,
        'answers': {
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5
        },
        'recomendations': {
            0: '**IT Infrastructure:** <br>',
            1: '**IT Infrastructure:** <br>',
            2: '**IT Infrastructure:** <br>',
            3: '**IT Infrastructure:** <br>',
            4: '**IT Infrastructure:** <br>',
            5: '**IT Infrastructure:** <br>'
        }
    },
    {
        'question': 'How relevevant is the "Age-appropriate support"?',
        'weight': 0.067,
        'answers': {
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5
        },
        'recomendations': {
            0: '**IT Infrastructure:** <br>',
            1: '**IT Infrastructure:** <br>',
            2: '**IT Infrastructure:** <br>',
            3: '**IT Infrastructure:** <br>',
            4: '**IT Infrastructure:** <br>',
            5: '**IT Infrastructure:** <br>'
        }
    },
    {
        'question': 'How relevevant is the "Accessibility"?',
        'weight': 0.09,
        'answers': {
            '0': 0,
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

st.title('UN Helpline Expert Survey')
st.markdown('_The following test aims to evaluate how well is your helpline performing, after answering these 10 questions, you will get a final score from 0 to 5, and a series of recomendations based on your answers_')

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

if answers is not None:
    answers_df = [item["answer"] for item in answers.values()]
    answers_df_new = pd.DataFrame.from_dict(answers_df).transpose()
    answers_df_new.columns = ['Digital Channel Launching Process', 'Technology– used/ in use/ future', 'Fundraise', 'Confidentiality', 'Responsiveness', 'User Experience', 'Staff expertise', 'Cultural and linguistic sensitivity', 'Age-appropriate support', 'Accessibility']
    answers_df_new.insert(0, 'ExpertID', 'my_results')
    csv = answers_df_new.to_csv(index=False)
    st.download_button("Download your results",csv,"results.csv","text/csv",key='download-csv')