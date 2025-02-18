import requests
from enum import Enum

# fetch the raw JSON data from Github
url = 'https://raw.githubusercontent.com/bugbytes-io/datasets/master/students_v2.json'
data = requests.get(url).json()


# define an Enum of acceptable Department values
class DepartmentEnum(Enum):
    ARTS_AND_HUMANITIES = 'Arts and Humanities'
    LIFE_SCIENCES = 'Life Sciences'
    SCIENCE_AND_ENGINEERING = 'Science and Engineering'