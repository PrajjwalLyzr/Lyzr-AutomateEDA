# Welcome to the Automate EDA by Lyzr!

![Lyzr Logo](./logo/lyzr-logo.png)

This application will automate the Exploratory data analysis with help of Lyzr Agent, this agent will perform all the analysis operations on top the data which was provided by user.
Operations are:

- Get Analysis: This operation enables you to ask questions directly related to the data at hand.
- Get Visualization: It generates one or more visualizations, on top of the user query.
- Dataset Description: It provides an automatically generated summary of the dataset.
- Queries for Analysis: This method generates queries tailored to the dataset.
- Recommendations for Analysis: It guides user on the types of analysis that would be most valuable to perform on their DataFrame based on the data provided.
- Recommendations: It returns various categories of queries, such as exploratory, regression, correlation, clustering, and time series analyses.


*Note: For this application to function properly in your local system, ensure that the required dependencies are installed and configured correctly, and make sure that you have your OpenAI API Key.*

### Create Virtual Environment 
- `python3 -m venv venv` - Ubuntu/MacOs
- `python -m venv venv` - Windows

### Activate the environment
- `source venv/bin/activate`  - Ubuntu/MaOS
- `venv/Script/acitvate` - Windows

### Installing Dependencies
- `pip3 install -r requirements.txt`- Ubuntu/MacOs
- `pip install -r requirements.txt` - Windows


### Run the application on local server
`streamlit run app.py`

# About Lyzr
Lyzr is a low-code agent framework that follows an **‘agentic’** way to build LLM apps, contrary to Langchain’s ‘functions and chains’ way and DSPy’s ‘programmatic’ way of building LLM apps. 

- [Lyzr](https://www.lyzr.ai/)
- [Book a Demo](https://www.lyzr.ai/book-demo/)
- [Discord](https://discord.gg/nm7zSyEFA2)
