# Split the single column into multiple columns using semicolon as delimiter
df_split = df.iloc[:, 0].str.split(";", expand=True)
df_split.columns = ["Tanggal", "Jenis Produk", "Jumlah Order", "Harga", "Total"]

# Convert data types
df_split["Tanggal"] = pd.to_datetime(df_split["Tanggal"], dayfirst=True, errors='coerce')
df_split["Jumlah Order"] = pd.to_numeric(df_split["Jumlah Order"], errors='coerce')
df_split["Harga"] = pd.to_numeric(df_split["Harga"], errors='coerce')
df_split["Total"] = pd.to_numeric(df_split["Total"], errors='coerce')

# Check cleaned data
df_split.info(), df_split.head()
