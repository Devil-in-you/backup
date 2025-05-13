import pandas as pd

# Creating the data dictionary
data = {
    "Parameter": [
        "Filling Hours", "Reaction Hours", "Retention Hours", "Total Time",
        "Rs (Initial)", "Rst (Initial)", "Alcohol (Initial)",
        "Transfer Rs", "Transfer Rst", "Transfer Alcohol", "VFA"
    ],
    "Value": [
        "20 hrs", "24 hrs", "20 hrs", "64 hrs",
        "0.50%", "1.11%", "12.20%",
        "0.28%", "1.11%", "12.49%", "702 ppm"
    ]
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Saving to an Excel file
file_path = "//home/vedansh/Desktop/Batch_Data_Analysis.xlsx"
df.to_excel(file_path, index=False)

file_path
