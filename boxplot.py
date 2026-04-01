import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"D:\Sangramjit_DMV_lab\Cleaned_Students_Performance.csv")


df = df.iloc[:30, :30]


numeric_df = df.select_dtypes(include=['number'])


plt.figure()
numeric_df.boxplot()
plt.xticks(rotation=90)
plt.title("Boxplot of Dataset")
plt.show()