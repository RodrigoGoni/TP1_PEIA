import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.distributions.empirical_distribution import ECDF

excel_path = 'Datos_primer_TP_21Co2025_a2119.xlsx'
df = pd.read_excel(excel_path)

df.columns = ['Fecha', 'Ventas']
df['Fecha'] = pd.to_datetime(df['Fecha'], dayfirst=True)

for year in [2021, 2022, 2023]:
    df_year = df[df['Fecha'].dt.year == year]
    if df_year.empty:
        print(f"No hay datos para el año {year}")
        continue

    ecdf = ECDF(df_year['Ventas'])

    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.step(ecdf.x, ecdf.y, where='post')
    plt.xlabel('Ventas ($)')
    plt.ylabel('Probabilidad acumulada')
    plt.title(f'FEC - {year}')
    plt.grid(True)

    plt.subplot(1, 2, 2)
    sns.kdeplot(df_year['Ventas'], fill=True, color='skyblue')
    plt.xlabel('Ventas ($)')
    plt.ylabel('Densidad estimada')
    plt.title(f'Densidad (KDE) - {year}')
    plt.grid(True)

    plt.tight_layout()
    plt.savefig(f'ventas_{year}_FEC_KDE.png', dpi=300)
    plt.close()

    print(f'Graficos guardados como ventas_{year}_FEC_KDE.png')
