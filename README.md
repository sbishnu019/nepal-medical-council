# Nepal Medical Council

Nepal Medical Council is a Python library for dealing with Doctor's registered in Nepal Medical Council.


## Usage
Nepal Medical Council

```python
from nepali_company_registrar import NepalCompanyRegistrar

nepali_company_registrar = NepalCompanyRegistrar(company_name_input='AGRICULTURAL DEVELOPMENT BANK') # for company input

nepali_company_registrar.is_valid()   # returns "True" if it is registered company name
                                      # returns "False" if it is not registered in company registrar

nepali_company_registrar.get_company_detail()      # returns company detail eg. {'name': 'AGRICULTURAL DEVELOPMENT BANK', 'name_in_nepali': 'कृषि विकास बैंक', 'registration_number': '928', 'registration_date': '2062-3-30', 'company_type': 'Public', 'share_holder': None, 'address': 'का.म.न.पा.-११,काठमाण्डौ,बाग्मती'}

nepali_company_registrar.list_similar_companies()    # returns list of similar companies registered in company registrar
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
