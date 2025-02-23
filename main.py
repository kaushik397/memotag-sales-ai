from flask import Flask, request, jsonify
from flasgger import Swagger, swag_from
import pandas as pd
import openai
import os
from ai_helper import sales_recommendations_agent,sales_strategies_agent,marketing_funnels_agent
app = Flask(__name__)
swagger = Swagger(app)


@app.route('/sales_recommendations', methods=['POST'])
@swag_from({
    'parameters': [
        {'name': 'file', 'in': 'formData', 'type': 'file', 'required': True, 'description': 'CSV file with sales data'},
        {'name': 'text', 'in': 'formData', 'type': 'string', 'required': True, 'description': 'Additional product description context for funnels'}
    ],
    'responses': {200: {'description': '10 sales recommendations'}}
})
def sales_recommendations():
    file = request.files['file']
    text = request.form['text']
    df = pd.read_csv(file)
    recommendations = sales_recommendations_agent(df=df,productDescription=text)
    return jsonify({'sales_recommendations': recommendations})

@app.route('/sales_strategies', methods=['POST'])
@swag_from({
    'parameters': [
        {'name': 'file', 'in': 'formData', 'type': 'file', 'required': True, 'description': 'CSV file with sales data'},
        {'name': 'text', 'in': 'formData', 'type': 'string', 'required': True, 'description': 'Additional product description context for funnels'}
    ],
    'responses': {200: {'description': '3 sales strategies'}}
})
def sales_strategies():
    file = request.files['file']
    text = request.form['text']
    df = pd.read_csv(file)
    strategies = sales_strategies_agent(df=df,productDescription=text)
    return jsonify({'sales_strategies': strategies})

@app.route('/marketing_funnels', methods=['POST'])
@swag_from({
    'parameters': [
        {'name': 'file', 'in': 'formData', 'type': 'file', 'required': True, 'description': 'CSV file with sales data'},
        {'name': 'text', 'in': 'formData', 'type': 'string', 'required': True, 'description': 'Additional product description context for funnels'}
    ],
    'responses': {200: {'description': '5 marketing funnels or strategies'}}
})
def marketing_funnels():
    file = request.files['file']
    text = request.form['text']
    df = pd.read_csv(file)
    funnels = marketing_funnels_agent(df=df,productDescription=text)
    return jsonify({'marketing_funnels': funnels})

if __name__ == "__main__":
    app.run(debug=True)
