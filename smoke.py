import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('homework2.csv')

cross_query = df[(df['smoking_status'] == 'smokes') ]
cross_query2 = df[(df['smoking_status'] == 'never smoked') ]
cross_query3 = df[(df['smoking_status'] == 'Unknown') ]
cross_query4 = df[(df['smoking_status'] == 'formerly smoked') ]
cross_query5 = df[(df['work_type'] == 'Never_worked') ]

count = len(cross_query)
count2 = len(cross_query2)
count3 = len(cross_query3)
count4 = len(cross_query4)
count5 = len(cross_query5)
print("Number of people who match the criteria:", count)
print("Number of people who match the criteria:", count2)
print("Number of people who match the criteria:", count3)
print("Number of people who match the criteria:", count4)
print("Number of people who match the criteria:", count5)

if count > 0:
    print("IDs of people who match the criteria:")
    for id in cross_query['id']:
        print(id)

labels = ['smokes', 'never smoked','Unknown','formerly smoked']
values = [count, count2,count3,count4]

plt.bar(labels, values)
plt.xlabel('Criteria')
plt.ylabel('Count')
plt.title('People Matching the Criteria')
plt.show()