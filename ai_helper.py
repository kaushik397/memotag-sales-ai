import os
import pandas as pd
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("Missing OpenAI API Key! Set it in your environment variables.")

def read_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        raise ValueError(f"Error reading CSV: {e}")

# def analyze_sales_data(df):
#     try:
#         llm = ChatOpenAI(model_name="gpt-4", openai_api_key=OPENAI_API_KEY)
#         agent = create_pandas_dataframe_agent(llm, df, verbose=False, allow_dangerous_code=True,handle_parsing_errors=True)

#         queries = {
#             "recommendations": "Provide 10 creative ideas to increase sales based on the data.",
#             "strategies": "Suggest 3 practical sales strategies to improve revenue.",
#             "funnels": "Give 5 unique marketing funnels or strategies to sell the product."
#         }

#         results = {key: agent.run(query) for key, query in queries.items()}
#         return results

#     except Exception as e:
#         return {"error": f"Error analyzing dataset: {e}"}

def sales_recommendations_agent(df,productDescription):
    try:
        query=f"Provide 10 creative ideas to increase sales based on the data and this product description: {productDescription}"
        llm = ChatOpenAI(model_name="gpt-4", openai_api_key=OPENAI_API_KEY)
        agent = create_pandas_dataframe_agent(llm, df, verbose=False, allow_dangerous_code=True,handle_parsing_errors=True)
        result=agent.run(query)
        return result
    except Exception as e:
        return {"error": f"Error analyzing dataset: {e}"}

def sales_strategies_agent(df,productDescription):
    try:
        query=f"Suggest 3 practical sales strategies to improve revenue based on sales data and product description: {productDescription}"
        llm = ChatOpenAI(model_name="gpt-4", openai_api_key=OPENAI_API_KEY)
        agent = create_pandas_dataframe_agent(llm, df, verbose=False, allow_dangerous_code=True,handle_parsing_errors=True)
        result=agent.run(query)
        return result
    except Exception as e:
        return {"error": f"Error analyzing dataset: {e}"}


def marketing_funnels_agent(df,productDescription):
    try:
        query=f"Give 5 unique marketing funnels or strategies to sell the product based on data and this product description {productDescription}"
        llm = ChatOpenAI(model_name="gpt-4", openai_api_key=OPENAI_API_KEY)
        agent = create_pandas_dataframe_agent(llm, df, verbose=False, allow_dangerous_code=True,handle_parsing_errors=True)
        result=agent.run(query)
        return result
    except Exception as e:
        return {"error": f"Error analyzing dataset: {e}"}


















# if __name__ == "__main__":
#     file_path = "sales_report.csv"
#     if not os.path.exists(file_path):
#         print("Error: CSV file not found!")
#     else:
#         df = read_csv(file_path)
#         analysis_results = analyze_sales_data(df)
#         # Print results
#         for key, value in analysis_results.items():
#             print(f"\n### {key.upper()} ###\n{value}\n")
