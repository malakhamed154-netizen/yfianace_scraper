import pandas as pd

df = pd.read_csv('Raw_Data_Company.csv')

df.columns = df.columns.str.strip()
df = df.rename(columns={
    "Comapany_Name": "Company_Name", 
    "year": "Year",
    "Total_Revenue": "Total_Revenue",
    "Gross_Profit": "Gross_Profit",
    "Net_Income": "Net_Income"
})

df.dropna(subset=['Company_Name', 'Year'], inplace=True)

financial_cols = ['Total_Revenue', 'Gross_Profit', 'Net_Income']
for col in financial_cols:
    if col in df.columns:
        df[col] = df[col].astype(str)
        df[col] = df[col].str.replace('$', '', regex=False)
        df[col] = df[col].str.replace(',', '', regex=False)
        df[col] = df[col].str.replace('B', '', regex=False)
        df[col] = df[col].str.replace('billion', '', regex=False, case=False)
        df[col] = df[col].str.strip()
        df[col] = pd.to_numeric(df[col], errors='coerce')

df = df[df['Year'] != 2026]

if 'Full_Time_Eployment' in df.columns:
    df.drop(columns=['Full_Time_Eployment'], inplace=True)

df = df.sort_values(by=['Company_Name', 'Year'])

pd.set_option('display.float_format', lambda x: '%.2f' % x)

df.to_csv('Cleaned_Data_Company.csv', index=False)

print("Data cleaning is Done")