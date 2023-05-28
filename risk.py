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
