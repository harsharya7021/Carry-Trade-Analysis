import pandas as pd
import numpy as np


file_path = 'AssignmentData.xlsx'  
data = pd.read_excel(file_path, sheet_name='Sheet2')


data['Carry_Return'] = (data['InterestRate'] - data['USr']) / 12


data['Exrate_Change'] = data.groupby('country')['Exrate'].pct_change()


data['Total_Monthly_Carry'] = data['Carry_Return'] + data['Exrate_Change']


data.dropna(inplace=True)


monthly_returns_time_series = data.pivot_table(
    index=['year', 'month'], 
    columns='country', 
    values='Total_Monthly_Carry'
)

monthly_returns_time_series.reset_index(inplace=True)

# Save the result to an Excel file for monthly returns time-series analysis
monthly_returns_path = 'Monthly_Returns_Time_Series.xlsx'
monthly_returns_time_series.to_excel(monthly_returns_path, index=False)
