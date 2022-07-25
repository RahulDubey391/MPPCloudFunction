import os
os.environ['SNOWFLAKE_ACCOUNT_ID'] = '' 
os.environ['SNOWFLAKE_USERNAME'] = ''
os.environ['SNOWFLAKE_PASSWORD'] = ''

class Config:
    def __init__(self):
        self.username = os.environ.get('SNOWFLAKE_USERNAME')
        self.password = os.environ.get('SNOWFLAKE_PASSWORD')
        self.account_id = os.environ.get('SNOWFLAKE_ACCOUNT_ID')
        

configObj = Config()