# Data Analysis | Programming Challenge 

Create a virtualenv and activate it:

    $ python3 -m venv venv
    $ . venv/bin/activate

Or on Windows cmd:

    $ py -3 -m venv venv
    $ venv\Scripts\activate.bat

### Install:
    pip install -r requirements.txt

### Run the crawler:
    python crawler.py

### Run Flask
    $ export FLASK_APP=hello.py
    $ flask run
     * Running on http://127.0.0.1:5000/
     
If you are on Windows, the environment variable syntax depends on command line interpreter. 

On Command Prompt:

    C:\path\to\app>set FLASK_APP=hello.py

And on PowerShell:

    PS C:\path\to\app> $env:FLASK_APP = "hello.py"
    
Alternatively you can use python -m flask:

    $ export FLASK_APP=hello.py
    $ python -m flask run
     * Running on http://127.0.0.1:5000/ 
 
## Task-01: 

*Be sure to run the crawler.py before hittting below api*

#### API List:
##### 1. Get all companies  http://127.0.0.1:5000/company
##### 2. Get top n companies http://127.0.0.1:5000/company/<int:top>/top
##### 3. Get company by id http://127.0.0.1:5000/company/<int:company_id>
##### 4. Get company by name http://127.0.0.1:5000/company/<company_name>

## Task-02: 
Jupyter Notebook: company.ipynb (company.html)
