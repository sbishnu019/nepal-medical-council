import re


class FullNameValidator:
    message = 'Invalid Full Name'
    full_name_regex = re.compile("^[a-zA-Z]+(\s[a-zA-Z]+)+$")

    def __init__(self, message=None):
        if message is not None:
            self.message = message

    def __call__(self, value):
        if not value:
            raise TypeError(self.message)

        if not self.full_name_regex.match(value):
            raise TypeError(self.message)

    def __eq__(self, other):
        return (
                isinstance(other, FullNameValidator) and
                (self.message == other.message)
        )


class NMCNumberValidator:
    message = 'Invalid NMC Number'
    nmc_number_regex = re.compile("^[0-9]+$")

    def __init__(self, message=None):
        if message is not None:
            self.message = message

    def __call__(self, value):
        if not value:
            raise TypeError(self.message)

        if not self.nmc_number_regex.match(value):
            raise TypeError(self.message)

    def __eq__(self, other):
        return (
                isinstance(other, FullNameValidator) and
                (self.message == other.message)
        )

