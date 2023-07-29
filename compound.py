class Compound:
    compound_id: int
    compound_name: str
    compound_structure: str

    def __init__(self, compound_id: str, compound_name: str, compound_structure: str):
        self.compound_id = int(compound_id)
        self.compound_name = compound_name.strip()
        self.compound_structure = compound_structure.strip()