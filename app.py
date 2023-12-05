import streamlit as st
import json
import numpy as np

answer_options = ["It is more than I expected.", "It seems fair.", "It is lower than I expected.", "I would never want to share this data, regardless of the earning amount."]

options = ["Basic demographic data", "Online Engagement", "Financial Transactions", "Locations"]

def main():
    st.title("Cross-Cultural Privacy-Scenario Assessment App")

    with st.sidebar:
        st.image('privacy_IB.png')
        st.write("""
Imagine an institution, much like a bank, where you can securely deposit your information. This institution will facilitate the sharing of your information with other organizations, or "buyers," for their marketing and sales efforts. As a result, you may receive targeted ads or communications from these buyers, and in return, you will receive compensation for utilizing this service. For instance, the information you deposit could encompass your basic demographic, contact information, and/or online browsing history.

Please Answer Questions with respect to the different scenarios given, whether you'll be willing to sell your data for said price.
            """)

    with st.form("my_form"):
        with st.expander("Scenario 1: Basic demographic data", expanded=True):
            question_1 = """
    ### Package: Basic demographic data
    The following information will be shared with the buyers:
            """
            st.write(question_1)
            col1, col2, col3 = st.columns(3)
            with col1:
                st.write("- Name")
                st.write("- Date of Birth (Age)")

            with col2:
                st.write("- Gender")
                st.write("- Marital Status")

            with col3:
                st.write("- Hometown")
                st.write("- Occupation")
            response_1 = st.selectbox("You will receive $6/month. Would you be willing to sell your data for this price?", answer_options)
        with st.expander("Scenario 2: Online Engagement", expanded=True):
            question_2 = """
    ### Package: Online Engagement
    Your online browsing history i.e. the urls of the websites you visited. You may be asked to install a tool, such as a web browser extension, that allows the bank to track your online browsing history.

            """
            st.write(question_2)
            response_2 = st.selectbox("You will receive $5/month. Would you be willing to sell your data for this price?", answer_options)
        with st.expander("Scenario 3: Financial Transactions", expanded=True):
            question_3 = """
    ### Package: Financial Transactions

    Your bank transactions and the category of your spending. To access your bank transaction data, the information bank may require your permission. A similar real-world example is a budgeting app that requests read access to your bank account to categorize your transactions and assist you in tracking your spending. Consider using a frequently used bank account for this question, rather than an inactive one.
            """
            st.write(question_3)
            response_3 = st.selectbox("You will receive $10/month. Would you be willing to sell your data for this price?", answer_options)
        with st.expander("Scenario 4: Locations", expanded=True):
            question_4 = """
    ### Package: Locations

    You location data of the places you went to in the past 3-6 months (not real-time). You install a mobile app that collects and shares your GPS location with potential buyers.
            """
            st.write(question_4)
            response_4 = st.selectbox("You will receive $10/month. Would you be willing to sell your data for this much?", answer_options)
        submitted = st.form_submit_button("Submit")
        if submitted:
            with open("counts.json", "r") as f:
                counts = json.load(f)
            outputs_allowed = []
            for country, country_counts in counts.items():
                total = sum(value for value in country_counts[0].values())
                count_1 = round(100*country_counts[0].get(response_1, 0)/total)
                count_2 = round(100*country_counts[1].get(response_2, 0)/total)
                count_3 = round(100*country_counts[2].get(response_3, 0)/total)
                count_4 = round(100*country_counts[3].get(response_4, 0)/total)
                ps = [count_1, count_2, count_3, count_4]
                # largest percentage:
                scenario_best_suited = np.argmax(ps)
                largest_output = str(ps[scenario_best_suited])+"\% of people from "+country+" responded the same as you for the "+options[scenario_best_suited]+" Scenario!"
                # smallest percentage:
                scenario_least_suited = np.argmin([count_1, count_2, count_3, count_4])
                smallest_output = str(ps[scenario_least_suited])+"\% of people from "+country+" responded the same as you for the "+options[scenario_least_suited]+" Scenario!"
                outputs_allowed.append((largest_output, smallest_output))
            cal1, cal2 = st.columns(2)
            with cal1:
                if np.random.random()>0.5:
                    st.info(outputs_allowed[0][0])
                else:
                    st.warning(outputs_allowed[0][1])
                if np.random.random()>0.5:
                    st.info(outputs_allowed[1][0])
                else:
                    st.warning(outputs_allowed[1][1])
            with cal2:
                if np.random.random()>0.5:
                    st.info(outputs_allowed[2][0])
                else:
                    st.warning(outputs_allowed[2][1])
                if np.random.random()>0.5:
                    st.info(outputs_allowed[3][0])
                else:
                    st.warning(outputs_allowed[3][1])
            cal__1, cal__2, cal__3 = st.columns(3)
            with cal__2:
                if np.random.random()>0.5:
                    st.info(outputs_allowed[4][0])
                else:
                    st.warning(outputs_allowed[4][1])       
    st.markdown("**Team:** Hsin-Li (Cindy) Kan, Oravee Smithiphol, Aman Priyanshu, and Chisaki Nakaizumi")
    st.markdown("**Under Supervision of:** Professor Lujo Bauer & TA Jenny Tang")

if __name__ == "__main__":
    main()
