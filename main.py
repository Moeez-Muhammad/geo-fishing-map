import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

fp = "gpr\\gpr_000a11a_e.shp"
map_df = gpd.read_file(fp)
print(map_df)
map_df.plot()
map_df

df = pd.read_csv("Canada_Provinical_boundaries_generalized_0.csv")
print(df)

merged = map_df.set_index('PRENAME').join(df.set_index('Name_EN'))
merged = merged[merged['Percentage of Fisheries'] == merged['Percentage of Fisheries']]
print(merged.head())


variable = 'Percentage of Fisheries'
vmin, vmax = 0, 50
fig, ax = plt.subplots(1, figsize=(10, 6))

merged.plot(column=variable, cmap='Blues', linewidth=0.8, ax=ax, edgecolor='0.8')
ax.axis('off')

ax.set_title('Percentage of fisheries in the Atlantic', fontdict={'fontsize': '25', 'fontweight': '3'})
ax.annotate('Source: Canadian Government, 2019',xy=(0.1, .08),  xycoords='figure fraction', horizontalalignment='left', verticalalignment='top', fontsize=12, color='#555555')
fig.show()

sm = plt.cm.ScalarMappable(cmap='Blues', norm=plt.Normalize(vmin=vmin, vmax=vmax))
sm._A = []
cbar = fig.colorbar(sm)

fig.savefig('temp.png', dpi=300)
