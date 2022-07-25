from src import DataController
#"TAST_API"."TPCDS_SF100TCL"."CALL_CENTER"

database = ''
schema = ''
table = ''

runner = DataController(database,schema,table)

runner.leecher()