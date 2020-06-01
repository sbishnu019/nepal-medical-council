# Nepal Medical Council

Nepal Medical Council is a Python library for dealing with Doctor's registered in Nepal Medical Council.


## Usage
Nepal Medical Council

```python
from nepal_medical_council import NepalMedicalCouncil

nepal_medical_council = NepalMedicalCouncil(name='amar gurung') # for doctor input

nepal_medical_council.is_valid()   # returns "True" if it is registered doctor
                                      # returns "False" if it is not registered in nepal medical council

nepal_medical_council.get_doctor_detail()      # returns doctor detail eg. {'full_name': 'Dr. Niraj Regmi', 'nmc_number': '5480', 'address': 'Ratopul, Gaushala , Kathmandu', 'gender': 'Male', 'degree': 'MBBS'}

```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
