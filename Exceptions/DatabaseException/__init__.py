class DatabaseException:

    @staticmethod
    def db_connect_error(e):
        print("Error occurred while connect to the database: ", e)

    @staticmethod
    def query_execution_error(e):
        print("Error occurred while executing query: ", e)