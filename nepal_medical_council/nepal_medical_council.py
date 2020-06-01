import requests
from bs4 import BeautifulSoup

from nepal_medical_council.conf import NMC_URL, SEARCH_PARAMETER


from nepal_medical_council.exceptions import DoctorNotFoundException

from nepal_medical_council.validators import NMCNumberValidator, FullNameValidator

from nepal_medical_council.models import Doctor


class NepalMedicalCouncil:
    def __init__(self, name=None, nmc_number=None):
        if not name and not nmc_number:
            raise TypeError('At least of attribute needed.')

        self._nmc_number = self._validate(value=nmc_number, validator=NMCNumberValidator)
        self._name = self._validate(value=name, validator=FullNameValidator)
        self._doctor = None

    def _search_doctor(self, name='', nmc_number='', degree=''):
        doctors = list()
        param_input = [name.replace(' ', '+'), nmc_number, degree]
        url = '{}?'.format(NMC_URL)
        for index, param in enumerate(SEARCH_PARAMETER.keys()):
            url = '{}{}={}&'.format(url, SEARCH_PARAMETER.get(param), param_input[index])
        url = url.rstrip('&')
        search_response = requests.get(url=url)

        soup = BeautifulSoup(markup=search_response.content, features='html.parser')
        result_tables = soup.find_all('table', {"class": "table table-bordered table-result"})
        for table in result_tables:
            response_set = {}
            table_body = table.find('tbody')
            rows = table_body.find_all('tr')
            for row in rows:
                cols = row.find_all('td')
                if cols[0].get("class") == ['text-center', 'alert-danger']:
                    raise DoctorNotFoundException('Doctor Not Found.')
                response_set[self._clean_data(cols[0].string)] = self._clean_data(cols[1].string)
            doctors.append(
                Doctor(
                    full_name=response_set.get('Full Name'),
                    address=response_set.get('Address'),
                    gender=response_set.get('Gender'),
                    degree=response_set.get('Degree'),
                    nmc_number=response_set.get('NMC No')
                )
            )
        self._doctor = doctors[0]

    def is_valid(self):
        try:
            self._search_doctor(
                name=self._name if self._name else '',
                nmc_number=self._nmc_number if self._nmc_number else ''
            )
        except DoctorNotFoundException:
            return False
        return True

    def get_doctor_detail(self):
        if self._doctor:
            return {
                'full_name': self._doctor.full_name,
                'nmc_number': self._doctor.nmc_number,
                'address': self._doctor.address,
                'gender': self._doctor.gender,
                'degree': self._doctor.degree,
            }
        return {
            'error': 'Doctor not found.'
        }

    def _clean_data(self, value):
        remove_character = ['\n', ':']
        for character in remove_character:
            value = value.replace(character, '')

        return value.lstrip().rstrip()

    def _validate(self, validator, value):
        if value:
            validate = validator()
            validate(value)
        return value


# nmc = NepalMedicalCouncil(name='amar gurung1')
# print(nmc.is_valid())
# print(nmc.get_doctor_detail())

