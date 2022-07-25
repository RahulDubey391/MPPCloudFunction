from ..utilities import SnowflakeConnector
import pandas as pd

class DataController:
    def __init__(self,database,schema,table):
        self.database = database
        self.schema = schema
        self.table = table
        self.sflkConnector = SnowflakeConnector()

    def pullQueries(self):
        querylist = []
        query = '''SELECT * FROM %s.%s.%s;'''%(self.database,self.schema,self.table)
        querylist.append(query)
        return querylist
    
    def fileWriter(self,df,filename):
        df.to_csv(filename,index=False,header=True)
    
    def leecher(self):
        con = self.sflkConnector.get_con()
        queries = self.pullQueries()
        for i in queries:
            df = con.cursor().execute(i).fetch_pandas_all()
            filename = 'samplefile.csv'
            self.fileWriter(df,filename)

    def poster(self):
        return None