import os
from PIL import Image
from pathlib import Path
import streamlit as st
from utils import utils
from dotenv import load_dotenv; load_dotenv()
from lyzr import DataConnector, DataAnalyzr

apikey = os.getenv('apikey') #replace this with your openai api key or create an environment variable for storing the key.

# create directory if it doesn't exist
data = "data"
plot = 'plot'
os.makedirs(data, exist_ok=True)
os.makedirs(plot, exist_ok=True)


# Setup your config
st.set_page_config(
    page_title="Automate EDA",
    layout="centered",  # or "wide" 
    initial_sidebar_state="auto",
    page_icon="./logo/lyzr-logo-cut.png"
)

# Load and display the logo
image = Image.open("./logo/lyzr-logo.png")
st.image(image, width=150)

# App title and introduction
st.title("Automate EDA by Lyzr")
st.markdown("### Welcome to the Automate EDA!")
st.markdown("Automate EDA by Lyzr will analysis through a conversational interface to derive actionable insights and intuitive visualizations")

# Custom function to style the app
def style_app():
    # You can put your CSS styles here
    st.markdown("""
    <style>
    .app-header { visibility: hidden; }
    .css-18e3th9 { padding-top: 0; padding-bottom: 0; }
    .css-1d391kg { padding-top: 1rem; padding-right: 1rem; padding-bottom: 1rem; padding-left: 1rem; }
    </style>
    """, unsafe_allow_html=True)

# Automate EDA Application
    
def data_uploader():
    st.title("Data")
    st.subheader("Upload CSV file for analysis")
    # Upload csv file
    uploaded_file = st.file_uploader("Choose csv file", type=["csv"])
    if uploaded_file is not None:
        utils.save_uploaded_file(uploaded_file)
    else:
        utils.remove_existing_files(data)
        utils.remove_existing_files(plot)


def analyzr():
    path = utils.get_files_in_directory(data)
    path = path[0]

    datafiles = {
		"dataset": path,
    }

   

    analyzr = DataAnalyzr(analysis_type='ml', api_key=apikey)
     # Call the get_data method
    analyzr.get_data(
            db_type = "files",
            config = {
                    "datasets": datafiles,
                    
            },
            vector_store_config = {
				"pass": "password", 
				"remake": False
		}
           
    )

    return analyzr


def file_checker():
    file = []
    for filename in os.listdir(data):
        file_path = os.path.join(data, filename)
        file.append(file_path)

    return file

# Function to display the dataset description
def display_description(analyzr):
    # deprecated in future versions
    description = analyzr.dataset_description()
    if description is not None:
        st.subheader("Dataset Description:")
        st.write(description)
 

   

# Function to display queries
def display_queries(analyzr):
    # deprecated in future verions
    queries = analyzr.ai_queries_df()
    if queries is not None:
        st.subheader("These Queries you can run on the data:")
        st.write(queries)
    


# Function to display insights
def display_insights(analyzr):
    query =  st.text_input("Write your query")
    if st.button("Submit"):
        insights = analyzr.ask(
           
            user_input = query,
            outputs = ["insights"]

        )
        # analysis = analyzr.analysis_insights(user_input=query)
        if insights is not None:
            st.subheader("Insights according to your query:")
            st.write(insights['insights'])




# Function to display recommendations
def display_recommendation(analyzr):
    query =  st.text_input("Write your query")
    if st.button("Submit"):
        # recommendation = analyzr.analysis_insights(user_input=query)
        recommendation = analyzr.ask(
            user_input = query,
            outputs = ["recommendations"]
        )
        if recommendation is not None:
            st.subheader("Recommendations based on the analysis insights:")
            st.write(recommendation['recommendations'])



# # Function to display Visualization
# def visualization_for_analysis(analyzr):
#     query =  st.text_input("Write your analysis query")

#     if st.button("Submit"):
#         utils.remove_existing_files(plot)
#         visualiation = analyzr.ask(
#                 query,
#                 outputs = ["visualisation"],
#                 plot_path = Path(f'./plot/{query[:12]}.png')
#         )
#         # visualiation = analyzr.visualisation(user_input=query, plot_path=Path('./plot'))
#         plot_files = os.listdir("./plot")
#         for plot_file in plot_files:
#             st.subheader(f'Visualization: {query}')
#             st.image(f"./plot/{plot_file}")
       

if __name__ == "__main__":
    style_app()
    st.sidebar.title("Automate EDA")
    selection = st.sidebar.radio("Go to", ["Data", "Analysis"])

    if selection == "Data":
        data_uploader()
    elif selection == "Analysis":
        file = file_checker()
        if len(file) > 0:
            analyzr = analyzr()
            # create buttons
            st.header("Select an Action")
            options = ['None',"Description", "Queries", "Insights", "Recommendation"]
            selected_option = st.radio("Select an option", options)

            if selected_option == "Description":
                display_description(analyzr)
            elif selected_option == "Queries":
                display_queries(analyzr)
            elif selected_option == "Insights":
                display_insights(analyzr)
            elif selected_option == "Recommendation":
                display_recommendation(analyzr)
            # elif selected_option == "Visualization":
            #     visualization_for_analysis(analyzr)

        else:
            st.error("Please upload csv file")

    with st.expander("ℹ️ - About this App"):
        st.markdown("""
        This app uses Lyzr DataAnalyzr agent to generate analysis on data. With DataAnalyzr, you can streamline the complexity of data analytics into a powerful, intuitive, and conversational interface that lets you command data with ease. For any inquiries or issues, please contact Lyzr.
        
        """)
        st.link_button("Lyzr", url='https://www.lyzr.ai/', use_container_width = True)
        st.link_button("Book a Demo", url='https://www.lyzr.ai/book-demo/', use_container_width = True)
        st.link_button("Discord", url='https://discord.gg/nm7zSyEFA2', use_container_width = True)
        st.link_button("Slack", url='https://join.slack.com/t/genaiforenterprise/shared_invite/zt-2a7fr38f7-_QDOY1W1WSlSiYNAEncLGw', use_container_width = True)
