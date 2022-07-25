from ..config import configObj
import snowflake.connector

class SnowflakeConnector:
    def get_con(self):
        con = snowflake.connector.connect(
            user=configObj.username,
            password=configObj.password,
            account=configObj.account_id
        )
        return con
