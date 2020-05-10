from pymongo import MongoClient


class PythonMongoClient():
    """
    Python Class for Python Mongp Connection
    """

    def __init__(self, user_name: str, password: str, db: str):
        """

        Args:
            user_name:
            password:
            db:
        """
        self.user_name = user_name
        self.password = password
        self.db = db

    def connect_mongo(self):
        """

        Returns:

        """
        mongo_client = MongoClient("172.16.3.1:27017",
                                   username=self.user_name,
                                   password=self.password,
                                   authSource=self.db)
        print(mongo_client)
        return mongo_client


if __name__ == '__main__':
    mc = PythonMongoClient('xprdb_admin', 'xprdb@Abz00ba', 'xprdb')
    mc.connect_mongo()
