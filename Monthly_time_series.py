import pandas as pd
import numpy as np

# Load the data from Excel
file_path = 'AssignmentData.xlsx'  # Update this path if necessary
data = pd.read_excel(file_path, sheet_name='Sheet2')

# Calculate monthly carry returns by taking the difference between the InterestRate of each country and the US interest rate (USr)
# This represents the potential profit from borrowing in the US and investing in a foreign country
data['Carry_Return'] = (data['InterestRate'] - data['USr']) / 12

# Adjust carry return for the exchange rate appreciation/depreciation
# Percentage change in exchange rate (Exrate) for each month is calculated
data['Exrate_Change'] = data.groupby('country')['Exrate'].pct_change()

# Total monthly carry return includes the interest rate differential and exchange rate gain/loss
data['Total_Monthly_Carry'] = data['Carry_Return'] + data['Exrate_Change']

# Drop rows with NaN values resulting from pct_change calculation
data.dropna(inplace=True)

# Generate a time-series of monthly returns for each country
# Pivot the data to have each country as a column and the time-series as the index based on year and month
monthly_returns_time_series = data.pivot_table(
    index=['year', 'month'], 
    columns='country', 
    values='Total_Monthly_Carry'
)

# Reset index for clearer formatting in Excel output
monthly_returns_time_series.reset_index(inplace=True)

# Save the result to an Excel file for monthly returns time-series analysis
monthly_returns_path = 'Monthly_Returns_Time_Series.xlsx'
monthly_returns_time_series.to_excel(monthly_returns_path, index=False)
