class Compound:
    compound_id: int
    compound_name: str
    compound_structure: str

    def __init__(self, compound_id, compound_name, compound_structure):
        self.compound_id = int(compound_id)
        self.compound_name = compound_name.strip()
        self.compound_structure = compound_structure.strip()