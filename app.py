import csv
from flask import Flask
from compound import Compound
from experiment import Experiment
from user import User

app = Flask(__name__)

def etl():
    # Load CSV files and parse data
    user_list = parse_users("data/users.csv")
    experiment_list = parse_experiments("data/user_experiments.csv")
    compound_list = parse_compounds("data/compounds.csv")

    # Process files to derive features
    # Upload processed data into a database
    pass

def parse_users(data_source):
    user_list = []
    users_file = open(data_source, newline='')
    users_reader = csv.reader(users_file, delimiter=',')
    next(users_reader)
    for row in users_reader:
        user_list.append(
            User(
                user_id=row[0],
                name=row[1],
                email=row[2],
                signup_date=row[3]
            )
        )
    return user_list

def parse_experiments(data_source):
    experiment_list = []
    experiments_file = open(data_source, newline='')
    experiments_reader = csv.reader(experiments_file, delimiter=',')
    next(experiments_reader)
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

def parse_compounds(data_source):
    compound_list = []
    compound_file = open(data_source, newline='')
    compound_reader = csv.reader(compound_file, delimiter=',')
    next(compound_reader)
    for row in compound_reader:
        compound_list.append(
            Compound(
                compound_id=row[0],
                compound_name=row[1],
                compound_structure=row[2]
            )
        )
    return compound_list

@app.route("/", methods=["POST"])
def trigger_etl():
    etl()
    return {"message": "ETL process started"}, 200

if __name__ == "__main__":
    app.run(debug=True)