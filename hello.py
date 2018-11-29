from flask import Flask, jsonify

app = Flask(__name__)

company = [
    {
        'uid': 1,
        'company_name': u'Invest Expat',
        'company_description': u'Neque porro quisquam est qui dolorem ipsum quia dolor', 
        'company_industry': u'wealth managemen', 
		'company_address': u'21/F On Hing Building1 On Hing TerraceCentral HONG KONG', 
        'company_website': u'http://www.invest-expat.com'
    },
    {
        'uid': 2,
        'company_name': u'ABC Expat',
        'company_description': u'Neque porro quisquam est qui dolorem ipsum quia dolor', 
        'company_industry': u'wealth managemen', 
		'company_address': u'21/F On Hing Building1 On Hing TerraceCentral HONG KONG', 
        'company_website': u'http://www.invest-expat.com'
    }
]

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/company', methods=['GET'])
def get_company():
    return jsonify({'company': company})    


if __name__ == '__main__':
    app.run(debug=True)    