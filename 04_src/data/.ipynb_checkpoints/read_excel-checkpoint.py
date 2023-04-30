import pandas as pd

path = "C:\\Users\\janwe\\OneDrive\\Dokumente\\Projekte\\Star_Wars_Legion_Rabbit\\01_data\\01_raw"

excel_pd = pd.read_excel(path+"\Liga.xlsx",index_col=0,sheet_name='Spiele')
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
print(excel_pd.columns)

all_player = excel_pd['Spieler_1'].unique()

