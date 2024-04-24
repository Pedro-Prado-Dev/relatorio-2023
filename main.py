import pandas as pd


results = pd.read_excel('data/Results.xlsx')
site_list = pd.read_excel('data/SiteList.xlsx')

rel = results[results['Year'] == 2023]
site_list = site_list[site_list['Year'] == 2023]

rel = rel[rel['Site ID'].isin(site_list['Site ID'])]
rel = rel.sort_values(['State'])

alert_atives = rel[rel['Alerts'] == 'Yes']
sum_qualities = rel['Quality (0-10)'].sum()
len_qualities = len(rel) 
sites_mbps = rel[rel['Mbps'] < 10]

print(f'Sites com alertas ativos: {alert_atives}')
print(f'Media da qualidade dos sites: {sum_qualities/len_qualities}')
print(f'Sites com menos de 10Mbps: {sites_mbps}')


rel = rel.drop(["Alerts"], axis= 1)

rel.to_excel('result/quaity-report-2023.xlsx', index=False)

