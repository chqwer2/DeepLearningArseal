import pandas as pd

# 360 + X
sheet_id ="1-TLqSFpxBj8mBBe4LAhq0J5_eylLeATMK_Zd4dOCTSk"
gid = 1753044556

df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?gid={gid}&format=csv")
print(df)
