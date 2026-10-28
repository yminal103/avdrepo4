# import pandas as pd

# data = {
#     'name': ['A', 'B', 'C'],
#     'age': [30, 20, 20],
#     'address': ['Pune', 'Mumbai', 'Nagpur']
# }

# print('Student Details')
# df = pd.DataFrame(data)
# print(df)


############# reading data from some API ####################
import pandas as pd
import requests

data = {
    'name': ['A', 'B', 'C'],
    'age': [30, 20, 20],
    'address': ['Pune', 'Mumbai', 'Nagpur']
}

print('Student Details')
df = pd.DataFrame(data)
print(df)

print('API Data')
response = requests.get('https://jsonplaceholder.typicode.com/users')
print(response.json())
