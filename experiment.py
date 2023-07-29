class Experiment:
    experiment_id: int
    user_id: int
    experiment_compound_ids: [int]
    experiment_run_time: int

    def __init__(self, experiment_id, user_id, experiment_compound_ids, experiment_run_time):
        self.experiment_id = int(experiment_id)
        self.user_id = int(user_id)
        self.experiment_run_time = int(experiment_run_time)

        self.experiment_compound_ids = []
        compounds = experiment_compound_ids.strip().split(';')
        for compound in compounds:
            self.experiment_compound_ids.append(int(compound))
