from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/company', methods=['GET'])
def get_company():
	company = pd.read_csv('company.csv', index_col='Id')
	#return company.to_json
	return company.to_json(orient='index')

@app.route('/company/<int:top>/top', methods=['GET'])
def get_company_top(top):
	company = pd.read_csv('company.csv', index_col='Id')
	#return company.to_json
	return company.head(top).to_json(orient='index')

@app.route('/company/<int:company_id>', methods=['GET'])
def get_company_by_id(company_id):
	company = pd.read_csv('company.csv', index_col='Id')
	#return company.to_json
	return company.loc[[company_id]].to_json(orient='index')

@app.route('/company/<company_name>', methods=['GET'])
def get_company_by_name(company_name):
	company = pd.read_csv('company.csv', index_col='Id')
	#return company.to_json
	return company[company['company_name'].str.contains(company_name)] .to_json(orient='index')

if __name__ == '__main__':
    app.run(debug=True)    