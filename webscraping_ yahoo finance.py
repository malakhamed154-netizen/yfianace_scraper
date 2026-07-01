import yfinance as yf 
import pandas as pd 
import time
companies = {
    'AAPL': 'Apple',
    'GOOGL': 'Google',
    'AMZN': 'Amazon',
    'META': 'Meta',
    'MSFT': 'Microsoft',
    'NVDA': 'NVIDIA'
}
empty_List =[]
for ticker, name in companies.items():
   try:
      company_data = yf.Ticker(ticker)
      financials = company_data.financials
      if financials.empty or len(financials.columns) == 0:
        print(f"There is no data {name}")
        continue
      available_column = financials.columns[:4]
   except Exception as e:
      print("Error")
      continue
   #Employee Count
   try:
      employee_count = company_data.info.get("fullTimeEmployees",'N/A')
   except:
      employee_count = 'N/A'

   for latest_col in available_column:
       actual_year = str(latest_col)[:4]
       print("Year found successfully")
       total_revenue = financials.loc["Total Revenue", latest_col] if "Total Revenue" in financials.index else 'N/A'
       gross_profit = financials.loc["Gross Profit", latest_col] if "Gross Profit" in financials.index else 'N/A'
       operating_income = financials.loc["Operating Income", latest_col] if "Operating Income" in financials.index else 'N/A'
       net_income = financials.loc["Net Income", latest_col] if "Net Income" in financials.index else 'N/A'

       all_data= { 
            "Comapany_Name":ticker,
           "year":actual_year,
           "Full_Time_Eployment":employee_count,
           "Total_Revenue":total_revenue,
           "Gross_Profit":gross_profit,
           "Net_Income":net_income}

       empty_List.append(all_data)
time.sleep(1.5)
print("Scrap Done")
if len(empty_List) > 0:  
   df_raw = pd.DataFrame(empty_List)
   df_raw.to_csv("Raw_Data_Company.csv", index=False, encoding='utf-8')
   print("Done")






    
