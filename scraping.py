import pandas as pd
import os
import pdfplumber
pdf_path = "Dunkin.pdf"

# Scraping data from PDF

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
                    # Clean up table
                    for index, item in enumerate(table[0][1:]):
                        tmp_item = item.replace("\n", " ")
                        table[0][index+1] = tmp_item[::-1]
                    
                    for row in table[1:]:
                        row[0] = row[0].replace("\n", " ")
                    
                    # Convert to dataframe
                    df = pd.DataFrame(table[1:], columns=table[0])
                    dataframes.append(df)
                    
        except Exception as e:
            print(f"Error on page {i+1}: {e}")
            continue
        

# Functions on dataframes

def print_dataframe(number):
    print(dataframes[number].head())
    
def save_dataframe(number):
    dataframes[number].to_csv(f"table{number:02d}.csv", index=False)
        
# function to find the first nonempty header
def first_nonempty_header(df):
    for header in df.columns:
        if header.strip():
            return header.strip()
    return None

# group DataFrames by their first nonempty header
grouped_dfs = {}
for df in dataframes:
    header = first_nonempty_header(df)
    if header:
        if header not in grouped_dfs:
            grouped_dfs[header] = []
        grouped_dfs[header].append(df)

# Concatenate DataFrames within each group
concatenated_dfs = []
for header, group in grouped_dfs.items():
    # concatenate the group. ignore_index will reset the index and discard the old index
    concatenated_df = pd.concat(group, ignore_index=True)
    concatenated_dfs.append(concatenated_df)


tmp_dataframes = []

for ind, df in enumerate(concatenated_dfs):
    if df.empty:
        print(f"Warning: DataFrame in {index+1} is empty. Skipping.")
        continue

    first_column_name = df.columns[0]

    if first_column_name is None:
        print(f"Warning: First column name is None in {index+1}. Skipping.")
        continue

    tmpdf = df.copy()
    tmpdf.rename(columns={first_column_name: 'Item Name'}, inplace=True)
    tmpdf['Item Category'] = first_column_name
    tmpdf = tmpdf[['Item Category'] + [col for col in tmpdf.columns if col != 'Item Category']]
    tmp_dataframes.append(tmpdf)
    
dataframes = tmp_dataframes
    
print(tmp_dataframes[9])

# Now you have a list of DataFrames in 'dataframes'
# You can process them further or concatenate them into a single DataFrame
# For example, to concatenate them into one DataFrame:
all_tables_df = pd.concat(dataframes, ignore_index=True)
all_tables_df.to_csv("Dunkin.csv", index=False)

def print_dataframe(number):
    print(dataframes[number])

def dataframe_to_csv(number, dataframes_folder="tables"):
    # Create the output folder if it doesn't exist
    if not os.path.exists(dataframes_folder):
        os.makedirs(dataframes_folder)

    dataframes[number].to_csv(os.path.join(dataframes_folder, f"table{number:02d} {dataframes[number].columns[0]}.csv"), index=False)

# for i in range(len(dataframes)):
#     dataframe_to_csv(i)


if __name__ == "__main__":
    
    print(type(dataframes[7]))
    
    print_dataframe(10)
    
    dataframes[7]["Item Category"] = "Beverages"
    print(dataframes[7])
