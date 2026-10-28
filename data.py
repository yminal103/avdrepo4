import pandas as pd

data = {
    'name': ['A', 'B', 'C'],
    'age': [30, 20, 20],
    'address': ['Pune', 'Mumbai', 'Nagpur']
}

print('Student Details')
df = pd.DataFrame(data)
print(df)
