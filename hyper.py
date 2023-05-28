import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('homework2.csv')
print(df['hypertension'].mean())
cross_query = df[(df['hypertension'] == 1) ]
cross_query2 = df[(df['hypertension'] == 0) ]
count = len(cross_query)
count2= len(cross_query2)
print("Number of people who match the criteria:", count)
print("Number of people who not match the criteria:",count2)

if count > 0:
    print("IDs of people who match the criteria:")
    for id in cross_query['id']:
        print(id)


labels = ['hyper_yes', 'hyper_no']
values = [count, count2]

plt.bar(labels, values)
plt.xlabel('Criteria')
plt.ylabel('Count')
plt.title('People Matching the Criteria')
plt.show()