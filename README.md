# Carry Trade Analysis Using Python

This repository contains Python code for analyzing carry trades, focusing on monthly returns for various currencies against the US Dollar. Carry trades involve borrowing in a low-interest currency (e.g., USD) and investing in a high-interest currency to capitalize on interest rate differentials. This analysis calculates potential returns based on interest rate spreads and exchange rate fluctuations over time.

## Project Overview

The goal of this project is to:
- Calculate monthly carry trade returns for multiple countries.
- Assess the impact of exchange rate changes on carry trade profitability.
- Provide a time-series analysis of carry trade returns that can be exported to Excel for further analysis.

This project is aimed at finance students, data analysts, and anyone interested in foreign exchange (FX) markets and international finance.

## Key Features

- **Interest Rate Differential Calculation**: Computes the monthly carry return based on the difference between US and foreign interest rates.
- **Exchange Rate Adjustment**: Incorporates monthly percentage changes in exchange rates to reflect currency appreciation or depreciation impacts.
- **Export to Excel**: Saves the time-series data for each country’s carry trade returns in an Excel format for easy visualization.

## Getting Started

### Prerequisites

- **Python 3.7+**
- **Pandas**: `pip install pandas`
- **Matplotlib**: `pip install matplotlib` (optional, for graph generation)

### Files

- `AssignmentData.xlsx`: Excel file containing interest rates, exchange rates, and market data for various countries.
- `carry_trade_analysis.py`: Python script to calculate carry trade returns and save output to an Excel file.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Carry-Trade-Analysis.git
   cd Carry-Trade-Analysis

2. Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ### Usage
   
### Usage

1. **Run the Script**: Open `carry_trade_analysis.py` and modify the file path if necessary. Then, execute the script:
   ```bash
   python carry_trade_analysis.py
2. **View Results**: The script will generate an Excel file with the monthly carry returns for each country.

3. **Generate Graphs (optional)**: The script includes code to plot the carry trade returns for specific country pairs (e.g., Yen-USD, CHF-EUR).

### Example Output

- Excel File: `Monthly_Returns_Time_Series.xlsx` containing time-series data of carry returns.
- Graph: Visualization of monthly carry returns for selected country pairs.

### Repository Structure

```plaintext
Carry-Trade-Analysis/
│
├── AssignmentData.xlsx             # Input data file with interest and exchange rates
├── carry_trade_analysis.py          # Python script for carry trade calculation
├── Monthly_Returns_Time_Series.xlsx # Output Excel file (auto-generated)
└── README.md                        # Repository instructions and overview
