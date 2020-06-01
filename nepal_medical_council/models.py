class Doctor:
    def __init__(self, full_name: str, nmc_number: str, address: str, gender: str, degree: str):
        self.degree = degree
        self.gender = gender
        self.address = address
        self.nmc_number = nmc_number
        self.full_name = full_name

    def __repr__(self):
        return self.full_name

    def __str__(self):
        return self.full_name
