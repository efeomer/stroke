
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('homework2.csv')


cross_query = df[(df['Residence_type'] == 'Urban') ]
cross_query2 = df[(df['Residence_type'] == 'Rural') ]



count = len(cross_query)
count2= len(cross_query2)


print("Number of people who match the criteria:", count)
print("Number of people who not match the criteria:",count2)

if count > 0:
    print("IDs of people who match the criteria:")
    for id in cross_query['id']:
        print(id)

labels = ['ever_married_yes', 'ever_married_no']
values = [count, count2]

plt.bar(labels, values)
plt.xlabel('Criteria')
plt.ylabel('Count')
plt.title('People Matching the Criteria')
plt.show()