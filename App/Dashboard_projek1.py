import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

# Set Seaborn style
sns.set(style='darkgrid')

# Read the data
day_df = pd.read_csv("./Dashboard/final_data.csv")

# Set Streamlit header
st.title("Bike Sharing Dashboard :bike:")


st.header("Puncak Aktivitas Penyewaan Sepeeda :chart_with_upwards_trend:")

byseason_df = day_df.groupby(by="season").dteday.nunique().reset_index()
byseason_df.rename(columns={"dteday": "season_count"}, inplace=True)


colors = ["#D3D3D3", "#D3D3D3", "#72BCD4", "#D3D3D3"]


fig, ax = plt.subplots(figsize=(12, 5))
sns.barplot(
    y="season_count",
    x="season",
    data=byseason_df.sort_values(by="season_count", ascending=False),
    palette=colors
)
plt.title("Season Terbanyak pada Penyewaan Sepeda", loc="center", fontsize=15)
plt.ylabel("Jumlah Penyewa")
st.pyplot(fig)


st.header("Perbandaingan antara Penyewa Casual dan Penyewa Registered :calendar:")


num_days = st.slider("Pilih rentan hari:", min_value=1, max_value=30, value=10)

casual_df = day_df.groupby(by="dteday").casual.sum().sort_values(ascending=False).reset_index()
member_df = day_df.groupby(by="dteday").registered.sum().sort_values(ascending=False).reset_index()
total_rentals = day_df.casual.sum()


colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]


fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(24, 10))

sns.barplot(x="casual", y="dteday", data=casual_df.head(num_days), palette=colors, ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel(None)
ax[0].set_title("Casual Rentals", loc="center", fontsize=15)
ax[0].tick_params(axis='y', labelsize=12)

sns.barplot(x="registered", y="dteday", data=member_df.head(num_days), palette=colors, ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel(None)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].set_title("Registered Rentals", loc="center", fontsize=15)
ax[1].tick_params(axis='y', labelsize=12)

plt.suptitle(f"Perbandaingan antara Penyewa Casual dan Penyewa Registered {num_days} Hari", fontsize=20)
st.pyplot(fig)
