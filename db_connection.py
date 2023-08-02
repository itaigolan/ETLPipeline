import psycopg2

from user import User

class PostgresConnection():
    def __init__(self):
        # When run on docker the host is postgres
        self.conn = psycopg2.connect(host="postgres", dbname="postgres", user="postgres", password="12345", port=5432)
        self.cursor = self.conn.cursor()
        # Initialize users table
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users(
                            user_id INT PRIMARY KEY,
                            name VARCHAR(255),
                            email VARCHAR(255),
                            signup_date DATE,
                            total_experiments INT,
                            average_experiment_duration FLOAT,
                            most_common_compound VARCHAR(255)
                            );
        """)
        self.conn.commit()


    def populate_results(self, usersList, compoundsList):
        user: User
        for user in usersList.values():
            self.cursor.execute("""INSERT INTO users (
                                user_id,
                                name,
                                email,
                                signup_date,
                                total_experiments,
                                average_experiment_duration,
                                most_common_compound) VALUES
                                ({},'{}','{}',TO_DATE('{}', 'YYYY-MM-DD'),{},{},'{}')
                                ON CONFLICT (user_id) DO NOTHING;
                                """
                                .format(
                                    user.user_id,
                                    user.name,
                                    user.email,
                                    user.signup_date,
                                    user.total_experiments_ran(),
                                    user.average_experiment_duration(),
                                    compoundsList[user.most_common_compound()].compound_structure
                                )
                            )

        self.conn.commit()

    def query_results(self):
        self.cursor.execute("SELECT * FROM users")

        return self.cursor.fetchall()

    def close_db(self):
        self.cursor.close()
        self.conn.close()
