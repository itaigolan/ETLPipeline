from flask import Flask

app = Flask(__name__)

def etl():
    # Load CSV files
    # Process files to derive features
    # Upload processed data into a database
    pass


@app.route("/", methods=["POST"])
def trigger_etl():
    etl()
    return {"message": "ETL process started"}, 200

if __name__ == "__main__":
    app.run(debug=True)