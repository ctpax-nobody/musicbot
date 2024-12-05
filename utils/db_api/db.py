import pymysql


class Database:
    def __init__(self, db_name, db_password, db_user, db_port, db_host):
        self.db_name = db_name
        self.db_password = db_password
        self.db_user = db_user
        self.db_port = db_port
        self.db_host = db_host

    def connect(self):
        return pymysql.Connection(
                host="${{RAILWAY_PRIVATE_DOMAIN}}",
                user="root",  # MySQL foydalanuvchi nomi
                password="MbEGoeFOApAJVFPYrYxECXJfLSqJErDt",  # MySQL paroli
                database="railway",  # Ma'lumotlar bazasi nomi
                port=3306  # MySQL server porti
            )


    def execute(self, sql: str, params: tuple = (), commit=False, fetchone=False, fetchall=False) -> dict | list:
        database = self.connect()
        cursor = database.cursor()

        cursor.execute(sql, params)
        data = None

        if fetchone:
            data = cursor.fetchone()

        elif fetchall:
            data = cursor.fetchall()

        if commit:
            database.commit()

        return data

    def create_users_table(self) -> None:
        """
        Creates users table
        :return: None
        """
        sql = """
            CREATE TABLE IF NOT EXISTS users(
                id BIGINT PRIMARY KEY AUTO_INCREMENT,
                telegram_id INT NOT NULL UNIQUE,
                fullname VARCHAR(100),
                username VARCHAR(100)
            )
        """
        self.execute(sql)

    def register_user(self, telegram_id: int, fullname: str, username: str):
        sql="""
        INSERT INTO users (telegram_id, fullname, username)
        VALUES(%s, %s, %s)
    """

        self.execute(sql, (telegram_id, fullname, username), commit=True)


    # def create_categories_table(self) -> None:
    #     """
    #     Creates categories table
    #     :return: None
    #     """
    #     sql = """
    #         CREATE TABLE IF NOT EXISTS categories(
    #             id INT PRIMARY KEY AUTO_INCREMENT,
    #             name VARCHAR(100) NOT NULL UNIQUE
    #         )
    #     """
    #     self.execute(sql)

    # def get_categories(self) -> list:
    #     """
    #     Returns all categories from categories table
    #     :return: list
    #     """
    #     sql = """
    #         SELECT * FROM categories
    #     """
    #     return self.execute(sql, fetchall=True)

 