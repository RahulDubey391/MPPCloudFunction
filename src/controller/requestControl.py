from ..utilities import SnowflakeConnector
import pandas as pd
from multiprocessing import Process, Pool

class DataController:
    def __init__(self,database,schema,table):
        self.database = database
        self.schema = schema
        self.table = table

    def requestExecutor(self,query,filename):
        con = SnowflakeConnector()
        cur = con.get_con().cursor()
        df = cur.execute(query).fetch_pandas_all()
        self.fileWriter(df,filename)
        return 'Done'
    
    def pullQueries(self):
        querylist = []
        q1 = '''SELECT * FROM %s.%s.%s;'''%(self.database,self.schema,self.table)
        q2 = '''SELECT * FROM %s.%s.%s;'''%(self.database,self.schema,self.table)
        querylist.append([q1,'1'])
        querylist.append([q2,'2'])
        return querylist
    
    def fileWriter(self,df,filename):
        df.to_csv(filename,index=False,header=True)
    
    def leecher(self):
        queries = self.pullQueries()
        print(queries)

        pool = Pool(processes=5)
        results = pool.starmap(self.requestExecutor, queries)
        for result in results:
            print(result)

    def poster(self):
        return None