import requests
from models import Student

url = "https://raw.githubusercontent.com/bugbytes-io/datasets/master/students_v2.json"
response = requests.get(url=url)
data = response.json()

for student in data:
    model = Student(**student)
    print(model.model_dump_json())
