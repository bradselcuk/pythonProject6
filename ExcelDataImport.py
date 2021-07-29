import pandas as pd

data = pd.read_excel(r'den.xlsx')
df = pd.DataFrame(data, columns=['Adi','Soyadi','Telefonu'])
print(df)