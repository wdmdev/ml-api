import pandas as pd

# Load data
print(f'Loading polution and meteorological data...')
polution = pd.read_csv('hcoe.csv', sep=';')
meteo = pd.read_csv('hcoemet.csv', sep=';')

# Choose meteorological data columns
print(f'Dropping unused columns from meteorological data...')
meteo.drop(['VR (grader)', 'RH (%)', 'GS (W/m2)'], axis=1, inplace=True)

# Combine into single dataset
print(f'Combining polution data with meteorological data...')
combined = polution.join(meteo.set_index('Starttid'), on='DateTime', how='left')

# Dropping rows with missing values
combined.dropna(inplace=True)

# Replace comma with dot for decimal seperator
for c in combined.columns:
    combined[c] = combined[c].str.replace(',', '.')

# Save to new combined csv
print(f'Saving combined dataframe to csv...')
file = 'hcoe_met_combined.csv'
combined.to_csv(file, sep=';', index=False)
print(f'Saved {len(combined)} rows to {file}')