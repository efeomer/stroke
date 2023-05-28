import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('homework2.csv')
print(df['avg_glucose_level'].mean())
cross_query = df[(df['avg_glucose_level'] > 95.57500662251657) ]
cross_query2 = df[(df['avg_glucose_level'] < 95.57500662251657) ]
count = len(cross_query)
count2= len(cross_query2)
print("Number of people who match the criteria:", count)
print("Number of people who not match the criteria:",count2)

if count > 0:
    print("IDs of people who match the criteria:")
    for id in cross_query['id']:
        print(id)


labels = ['age>65', 'age<65']
values = [count, count2]

plt.bar(labels, values)
plt.xlabel('Criteria')
plt.ylabel('Count')
plt.title('People Matching the Criteria')
plt.show()