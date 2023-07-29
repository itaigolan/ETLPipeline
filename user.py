from experiment import Experiment

class User:
    user_id: int
    name: str
    email: str
    signup_date:str
    experiments: [Experiment]

    def __init__(self, user_id, name, email, signup_date):
        self.user_id = int(user_id)
        self.name = name.strip()
        self.email = email.strip()
        self.signup_date = signup_date.strip()
        self.experiments = []

    def add_experiment(self, experiment):
        self.experiments.append(experiment)

    def total_experiments_ran(self):
        return len(self.experiments)
    
    def average_experiment_duration(self):
        total_duration = 0
        for experiment in self.experiments:
            total_duration += experiment.experiment_run_time
        
        return float(total_duration/self.total_experiments_ran())
    
    def most_common_compound(self):
        compounds = {}
        for experiment in self.experiments:
            for compound in experiment.experiment_compound_ids:
                if compound in compounds.keys():
                    compounds[compound] = compounds[compound] + 1
                else:
                    compounds[compound] = 1
        return max(compounds, key=compounds.get)