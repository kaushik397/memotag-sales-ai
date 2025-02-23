# AI/ML Sales Analysis API

## Overview
This project consists of a set of Flask APIs designed to analyze sales data and product features to generate actionable insights for MemoTag. The APIs provide:

1. **Sales Recommendations**
        - 10 creative ways to increase sales.
2. **Sales Strategies**
       - 3 practical sales strategies.
3. **Marketing Funnels/Strategies**
       - 5 unique marketing funnels/strategies.
    The APIs use **OpenAI's GPT-4** via LangChain to generate intelligent, data-driven responses.
    
    ---
    ## Features
    ✅ **AI-powered Sales Insights** – Provides unique, actionable strategies.
    ✅ **Flask REST API** – Lightweight and fast for seamless integration.
    ✅ **CSV Upload Support** – Processes sales data dynamically.
    ✅ **Swagger Documentation** – For easy testing and integration.
    ✅ **Live Deployment** – Accessible via an online endpoint.
    ✅ **Frontend Integration Ready** – API can be called from a web interface.
    
    ---
    ## API Endpoints
    ### 1. **Sales Recommendations**
    - **Endpoint:** `POST /sales_recommendations`
    - **Description:** Returns 10 out-of-the-box ideas to boost sales.
    - **Inputs:**
      - `file` (CSV) – Sales data
      - `additional_info` (Optional String) – Contextual information
    - **Response:** JSON with 10 creative sales ideas.
    
    ### 2. **Sales Strategies**
    - **Endpoint:** `POST /sales_strategies`
    - **Description:** Returns 3 practical sales strategies.
    - **Inputs:**
      - `file` (CSV) – Sales data
      - `additional_info` (Optional String) – Contextual information
    - **Response:** JSON with 3 sales strategies.
    
    ### 3. **Marketing Funnels**
    - **Endpoint:** `POST /marketing_funnels`
    - **Description:** Returns 5 unique marketing funnels.
    - **Inputs:**
      - `file` (CSV) – Sales data
      - `additional_info` (Optional String) – Contextual information
    - **Response:** JSON with 5 marketing funnel ideas.
    
    ---
    ## Installation & Setup
    ### 1. **Clone the Repository**
    ```sh
    git clone [https://github.com/yourusername/memotag-ai-api.git](https://github.com/kaushik397/memotag-sales-ai.git)
    cd memotag-ai-api
    ```
    
    ### 2. **Install Dependencies**
    ```sh
    pip install -r requirements.txt
    ```
    
    ### 3. **Set Up API Key**
    Replace `your-api-key-here` in the script with your **OpenAI API Key**.
    
    ### 4. **Run the Flask Application**
    ```sh
    python app.py
    ```
    - The API will be available at: `http://127.0.0.1:5000/`
    - Swagger Docs: `http://127.0.0.1:5000/apidocs`
    
    ---
    ## Deployment
    The API is deployed at: **[Live API Endpoint](https://memotag-sales-ai.onrender.com/apidocs/)**
    
    You can use **Render, Heroku, or Google Cloud** to deploy the API.
    
    ---
    ## Example API Call
    ### Using `cURL`
    ```sh
    curl -X POST "https://your-deployment-url.com/sales_recommendations" \
      -F "file=@sales_report.csv" \
      -F "additional_info=Focus on digital sales"
    ```
    
    ### Using Python Requests
    ```python
    import requests
    files = {'file': open('sales_report.csv', 'rb')}
    data = {'additional_info': 'Focus on digital sales'}
    response = requests.post("https://your-deployment-url.com/sales_recommendations", files=files, data=data)
    print(response.json())
    ```
    
    ---
    ## Project Structure
    ```
    memotag-ai-api/
    │── main.py                 # Main Flask application
    │── requirements.txt        # Dependencies
    │── README.md               # Documentation
    │── ai_helper.py            # Helper functions to process data
    │── .env                    # Environment variables (API keys, etc.)
    ```
    
    ---
    ## Technologies Used
    - **Flask** – Web framework
    - **OpenAI GPT-4** – AI for generating insights
    - **LangChain** – AI data analysis
    - **Pandas** – Data processing
    - **Swagger (Flasgger)** – API documentation
    
    ---
    ## Submission Details
    - **Live API:** [Deployed API Link](https://memotag-sales-ai.onrender.com/apidocs/)
    - **GitHub Repo:** [Repository Link](https://github.com/kaushik397/memotag-sales-ai.git)
    
    ---
    ## Contact
    For any issues or queries, please contact **kaushikgupta911@gmail.com**
    
    ---    
