import pandas as pd
import numpy as np

StarbucksDatathon = pd.read_csv('StarbucksDatathon File.csv')
import pandas as pd
# print(StarbucksDatathon.head())
# print(StarbucksDatathon.describe())
# print(StarbucksDatathon['Beverage_category'].unique())

# Scraping data from PDF
import pdfplumber
pdf_path = "Dunkin.pdf"

# List for PDFs
dataframes = []

with pdfplumber.open(pdf_path) as pdf:
    # Iterate over each page
    for i, page in enumerate(pdf.pages):
        try:
            # Extract tables from page
            tables = page.extract_tables()
            for table in tables:
                if table:
                    print(table)
                    print(type(table))
                    # Convert table to dataframe
                    df = pd.DataFrame(table[1:], columns=table[0])
                    dataframes.append(df)
                    
                    break
                break
            break
        except Exception as e:
            print(f"Error on page {i+1}: {e}")
            continue
        
        # Convert text to dataframe

if __name__ == "__main__":
    
    print(dataframes[6].head())
    dataframes[6].to_csv('Dunkin.csv', index=False)