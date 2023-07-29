import csv
from db_connection import PostgresConnection
from flask import Flask
from compound import Compound
from experiment import Experiment
from user import User

app = Flask(__name__)

def etl():
    # Load CSV files and parse data
    user_table = parse_users("data/users.csv")
    experiment_list = parse_experiments("data/user_experiments.csv")
    compound_table = parse_compounds("data/compounds.csv")

    # Associate each experiment with the user that ran it
    for experiment in experiment_list:
       user_table[experiment.user_id].add_experiment(experiment)

    # Process files to derive features
    # Upload processed data into a database
    conn = PostgresConnection()
    conn.populate_results(user_table, compound_table)
    conn.close_db()
    pass

def parse_users(data_source: str):
    users_file = open(data_source, newline='')
    users_reader = csv.reader(users_file, delimiter=',')
    next(users_reader)
    user_table= {}
    for row in users_reader:
        user_table[int(row[0])] =  User(
                user_id=row[0],
                name=row[1],
                email=row[2],
                signup_date=row[3]
            )
    return user_table

def parse_experiments(data_source: str):
    experiments_file = open(data_source, newline='')
    experiments_reader = csv.reader(experiments_file, delimiter=',')
    next(experiments_reader)
    experiment_list = []
    for row in experiments_reader:
        experiment_list.append(
            Experiment(
                experiment_id=row[0],
                user_id=row[1],
                experiment_compound_ids=row[2],
                experiment_run_time=row[3]
            )
        )
    return experiment_list

def parse_compounds(data_source: str):
    compound_file = open(data_source, newline='')
    compound_reader = csv.reader(compound_file, delimiter=',')
    next(compound_reader)
    compound_table = {}
    for row in compound_reader:
        compound_table[int(row[0])] = Compound(
                compound_id=row[0],
                compound_name=row[1],
                compound_structure=row[2]
            )
    return compound_table

@app.route("/", methods=["POST"])
def trigger_etl():
    etl()
    return {"message": "ETL process started"}, 200

if __name__ == "__main__":
    app.run(debug=True)