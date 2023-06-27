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
            0: '**Technology in the future:** <br>Outdated or unreliable technology is being used, hindering the effectiveness of online protection systems. Recommendation: Invest in upgrading technology infrastructure to ensure reliable and up-to-date systems.',
            1: '**Technology in the future:** <br>The technology used is somewhat outdated and may have limitations in supporting online protection systems. Recommendation: Assess and prioritize technology upgrades to enhance system performance and reliability.',
            2: '**Technology in the future:** <br>The technology used is average but may require updates to align with emerging trends and advancements. Recommendation: Regularly evaluate and update technology solutions to meet current and future needs.',
            3: '**Technology in the future:** <br>The technology used is up-to-date and supports online protection systems effectively. Recommendation: Stay informed about emerging technologies to identify opportunities for enhancing system capabilities.',
            4: '**Technology in the future:** <br>The technology used is modern and robust, meeting the requirements of online protection systems. Recommendation: Continuously monitor and evaluate technology advancements to ensure the systems remain cutting-edge.',
            5: '**Technology in the future:** <br>The technology used is state-of-the-art, providing a strong foundation for online protection systems. Recommendation: Foster collaboration with technology experts and industry leaders to stay at the forefront of technological advancements.'
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
            0: '**Fundraising:** <br>Insufficient funds are being raised, limiting the resources available for online protection systems. Recommendation: Develop comprehensive fundraising strategies and explore diverse funding sources to secure necessary financial support.',
            1: '**Fundraising:** <br>The fundraising efforts are somewhat limited, and additional funding sources should be explored. Recommendation: Expand fundraising initiatives and engage with potential donors and sponsors to increase financial support.',
            2: '**Fundraising:** <br>Fundraising efforts are average, but more proactive approaches are needed to secure sustainable funding. Recommendation: Implement targeted fundraising campaigns, grant applications, and partnership opportunities to maximize financial resources.',
            3: '**Fundraising:** <br>Fundraising efforts are adequate and provide a stable financial foundation for online protection systems. Recommendation: Maintain a diversified fundraising approach to sustain and grow financial support.',
            4: '**Fundraising:** <br>Fundraising efforts are effective, resulting in substantial resources for online protection systems. Recommendation: Continue building strong relationships with donors and sponsors, leveraging success stories to attract more support.',
            5: '**Fundraising:** <br>The fundraising efforts are exceptional, ensuring abundant resources for online protection systems. Recommendation: Share fundraising best practices and collaborate with other organizations to further strengthen financial sustainability.'
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
            0: '**Confidentiality:** <br>Confidentiality measures are not in place or poorly implemented, risking the privacy and safety of users. Recommendation: Implement strict confidentiality protocols and robust data protection measures to ensure user privacy and safety.',
            1: '**Confidentiality:** <br>Confidentiality measures are partially implemented, but there are gaps that need to be addressed. Recommendation: Conduct a thorough review of existing confidentiality measures and enhance them to meet industry standards and regulatory requirements.',
            2: '**Confidentiality:** <br>Confidentiality measures are average, but further improvements are necessary to ensure the privacy and confidentiality of user data. Recommendation: Regularly assess and update confidentiality measures to align with evolving data protection practices.',
            3: '**Confidentiality:** <br>Confidentiality measures are well-established and effectively implemented to protect user data and maintain privacy. Recommendation: Continuously monitor and update confidentiality measures to address emerging threats and vulnerabilities.',
            4: '**Confidentiality:** <br>Confidentiality measures are robust, meeting or exceeding industry standards for protecting user privacy. Recommendation: Share best practices and collaborate with other organizations to further enhance confidentiality measures.',
            5: '**Confidentiality:** <br>The highest level of confidentiality measures is in place, ensuring the utmost protection of user data and privacy. Recommendation: Conduct regular audits and security assessments to maintain the highest level of confidentiality standards.'
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
            0: '**Responsiveness:** <br>The online protection system is unresponsive or slow, leading to delays in providing support and assistance. Recommendation: Optimize system performance and responsiveness through technical improvements and resource allocation.',
            1: "**Responsiveness:** <br>The system's responsiveness is inconsistent, causing occasional delays in addressing user needs. Recommendation: Identify and address the root causes of responsiveness issues to ensure a consistent and timely response.",
            2: "**Responsiveness:** <br>he online protection system's responsiveness is average, but there is room for improvement in terms of speed and efficiency. Recommendation: Implement measures to enhance system responsiveness, such as optimizing server infrastructure and streamlining processes.",
            3: '**Responsiveness:** <br>The online protection system is generally responsive, providing timely assistance to users. Recommendation: Monitor system responsiveness and conduct regular user feedback assessments to maintain satisfactory performance.',
            4: '**Responsiveness:** <br>The online protection system is highly responsive, offering quick and efficient support to users. Recommendation: Continuously evaluate and optimize system performance to maintain a high level of responsiveness.',
            5: '**Responsiveness:** <br>The online protection system demonstrates exceptional responsiveness, ensuring immediate support and assistance to users. Recommendation: Share best practices and collaborate with other organizations to advance responsiveness standards across the industry.'
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
            0: '**User Experience:** <br>The user experience is extremely poor, making it difficult for users to navigate and access the necessary support. Recommendation: Conduct a comprehensive user experience assessment and redesign the system to improve usability and accessibility.',
            1: '**User Experience:** <br>The user experience is below average, requiring users to overcome significant challenges to access and utilize the online protection system. Recommendation: Identify pain points in the user journey and implement iterative improvements to enhance the overall user experience.',
            2: '**User Experience:** <br>The user experience is average, but there are areas that can be enhanced to provide a smoother and more intuitive user interface. Recommendation: Gather user feedback and make incremental adjustments to optimize the user experience.',
            3: '**User Experience:** <br>The user experience is generally satisfactory, with an interface and features that facilitate easy access to support and resources. Recommendation: Continuously monitor user feedback and make necessary refinements to maintain a positive user experience.',
            4: "**User Experience:** <br>The user experience is good, with intuitive navigation and efficient access to the online protection system's features and services. Recommendation: Conduct periodic usability testing and incorporate user feedback to further enhance the user experience.",
            5: '**User Experience:** <br>The user experience is excellent, offering a seamless and engaging interface that enables users to access support effortlessly. Recommendation: Share best practices in user experience design and leverage user feedback to continue refining and innovating the user interface.'
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
            0: '**Staff Expertise:** <br>The staff lacks the necessary expertise and training to effectively support users through the online protection system. Recommendation: Provide comprehensive training and professional development opportunities to enhance staff expertise.',
            1: '**Staff Expertise:** <br>Staff expertise is limited, requiring additional training and resources to ensure effective support provision. Recommendation: Implement a continuous learning program to upskill staff members and stay updated with emerging trends and best practices.',
            2: '**Staff Expertise:** <br>Staff members possess average expertise, but there is room for improvement in certain areas to deliver optimal support. Recommendation: Conduct regular assessments of staff skills and knowledge gaps and provide targeted training to address specific areas of improvement.',
            3: '**Staff Expertise:** <br>Staff members exhibit satisfactory expertise, enabling them to provide quality support to users. Recommendation: Establish a knowledge-sharing system and foster a learning culture to continuously enhance staff expertise.',
            4: '**Staff Expertise:** <br>Staff members demonstrate advanced expertise, equipped with the necessary skills and knowledge to address a wide range of user needs effectively. Recommendation: Encourage staff members to participate in industry events and training programs to stay at the forefront of online protection practices.',
            5: '**Staff Expertise:** <br>Staff members possess exceptional expertise, representing industry leaders in providing support through the online protection system. Recommendation: Recognize and reward staff achievements and expertise while fostering a collaborative environment for knowledge sharing.'
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
            0: '**Cultural and Linguistic Sensitivity:** <br>The online protection system lacks cultural and linguistic sensitivity, failing to address the diverse needs of users from different backgrounds. Recommendation: Incorporate cultural competency training for staff members and ensure the availability of multilingual resources and support.',
            1: '**Cultural and Linguistic Sensitivity:** <br>There is limited cultural and linguistic sensitivity in the online protection system, requiring improvements to ensure inclusivity. Recommendation: Conduct a cultural assessment and collaborate with diverse communities to incorporate their perspectives and address cultural and linguistic barriers.',
            2: "**Cultural and Linguistic Sensitivity:** <br>The online protection system demonstrates average cultural and linguistic sensitivity but can benefit from further enhancements. Recommendation: Engage with multicultural organizations and language experts to review and improve the system's cultural responsiveness.",
            3: "**Cultural and Linguistic Sensitivity:** <br>The online protection system shows satisfactory cultural and linguistic sensitivity, considering the diverse needs and backgrounds of users. Recommendation: Regularly assess and update the system's cultural responsiveness based on user feedback and changing demographics.",
            4: '**Cultural and Linguistic Sensitivity:** <br>The online protection system exhibits good cultural and linguistic sensitivity, effectively catering to users from different cultures and language groups. Recommendation: Collaborate with cultural advisors and language experts to continuously improve and expand cultural and linguistic support.',
            5: '**Cultural and Linguistic Sensitivity:** <br>The online protection system excels in cultural and linguistic sensitivity, providing a highly inclusive and accessible environment for all users. Recommendation: Share best practices in cultural responsiveness and regularly engage with communities to ensure ongoing alignment with their needs.'
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
            0: '**Age-appropriate Support:** <br>The online protection system does not offer age-appropriate support, neglecting the unique needs and vulnerabilities of different age groups. Recommendation: Develop age-specific resources, guidelines, and support mechanisms to ensure appropriate assistance for users of all ages.',
            1: '**Age-appropriate Support:** <br>The online protection system provides limited age-appropriate support, requiring additional measures to address the specific challenges faced by different age groups. Recommendation: Conduct research and consult child development experts to develop targeted interventions and tailored resources for each age group.',
            2: '**Age-appropriate Support:** <br>The online protection system includes some age-appropriate support, but there is room for improvement in addressing the varying needs of users across different age groups. Recommendation: Continuously update and expand age-specific resources and ensure that user feedback informs ongoing enhancements.',
            3: '**Age-appropriate Support:** <br>The online protection system offers satisfactory age-appropriate support, recognizing and addressing the distinct requirements of users at different stages of development. Recommendation: Regularly evaluate and update age-specific resources to ensure they remain relevant and effective.',
            4: "**Age-appropriate Support:** <br>The online protection system provides good age-appropriate support, catering well to the specific needs and vulnerabilities of users across various age groups. Recommendation: Share best practices in age-specific support and collaborate with child development experts to further enhance the system's offerings.",
            5: '**Age-appropriate Support:** <br>The online protection system excels in providing age-appropriate support, employing evidence-based approaches that effectively meet the unique requirements of users at different ages. Recommendation: Continue to lead in the field of age-specific support by conducting research, piloting innovative interventions, and sharing knowledge with other organizations.'
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
            0: '**How relevevant is the "Accessibility:** <br> The online protection system lacks accessibility features, making it difficult for users with disabilities to access and utilize the system. Recommendation: Conduct an accessibility audit and implement necessary accommodations, such as alternative text, keyboard navigation, and compatibility with assistive technologies.',
            1: '**How relevevant is the "Accessibility:** <br>The online protection system has limited accessibility features, requiring further improvements to ensure equal access for users with disabilities. Recommendation: Engage with accessibility experts and organizations to identify and address accessibility barriers across the system.',
            2: '**How relevevant is the "Accessibility:** <br>The online protection system includes some accessibility features but can benefit from additional enhancements to improve usability for users with disabilities. Recommendation: Conduct user testing with individuals with disabilities to gather feedback and prioritize accessibility updates based on their needs.',
            3: '**How relevevant is the "Accessibility:** <br>The online protection system demonstrates satisfactory accessibility, ensuring that users with disabilities can navigate and utilize the system with relative ease. Recommendation: Establish an accessibility feedback mechanism and regularly update accessibility features based on user input and evolving accessibility standards.',
            4: '**How relevevant is the "Accessibility:** <br>The online protection system provides good accessibility, incorporating a range of features and accommodations to enable users with disabilities to fully participate. Recommendation: Seek recognition and certifications for accessibility compliance and collaborate with disability advocacy groups to continuously enhance accessibility.',
            5: '**How relevevant is the "Accessibility:** <br>The online protection system excels in accessibility, implementing best practices and innovative solutions to ensure seamless access for users with disabilities. Recommendation: Share knowledge and expertise in accessible design to contribute to industry-wide advancements in digital accessibility.'
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

if csv is not None:
    data = pd.read_csv(csv)
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