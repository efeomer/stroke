import pandas as pd
risk_analysis = pd.read_csv("risk_analysis.csv")
homework = pd.read_csv("test.csv")
merged_data = pd.merge(risk_analysis, homework, on="id", how="inner")
merged_data.to_csv("homework2.csv", index=False)
