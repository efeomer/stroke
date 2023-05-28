import pandas as pd
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.impute import SimpleImputer

train_data = pd.read_csv("train.csv")
homework_data = pd.read_csv("homework.csv")
test_data = pd.read_csv("test.csv")

merged_data = pd.concat([train_data, homework_data], ignore_index=True)

imputer = SimpleImputer(strategy="most_frequent")
merged_data_filled = imputer.fit_transform(merged_data)

merged_df = pd.DataFrame(merged_data_filled, columns=merged_data.columns)

X = pd.concat([merged_df, test_data], ignore_index=True)

X_encoded = pd.get_dummies(X, columns=["gender", "ever_married", "work_type", "Residence_type", "smoking_status"])

train_X = X_encoded[X_encoded["stroke"].notnull()]
train_y = train_X["stroke"].astype(int)
train_X = train_X.drop("stroke", axis=1)

test_X = X_encoded[X_encoded["stroke"].isnull()]
test_X = test_X.drop("stroke", axis=1)

clf = HistGradientBoostingClassifier()

clf.fit(train_X, train_y)

predictions = clf.predict_proba(test_X)[:, 1]

output = pd.DataFrame({
    "id": test_data["id"],
    "stroke": predictions
})

output.to_csv("predictions.csv", index=False)
import pandas as pd

predictions = pd.read_csv("predictions.csv")

threshold = predictions["stroke"].mean()

risk_persons = predictions[predictions["stroke"] > threshold]

risk_analysis = pd.DataFrame({
    "id": risk_persons["id"],
    "Risk Probability": risk_persons["stroke"]
})

risk_analysis.insert(0, "Threshold", threshold)

risk_analysis.to_csv("risk_analysis.csv", index=False)
