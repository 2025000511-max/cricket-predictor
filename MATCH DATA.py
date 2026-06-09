import pandas as pd

data = {
    'TEAM1_HOME': ['CSK', 'MI', 'RR', 'DC','LSG'],
    'TEAM2_AWAY': ['RCB', 'KKR', 'GT', 'LSG','SRH'],
    'CITY': ['Chennai', 'Mumbai', 'Jaipur', 'Delhi','Lucknow'],
    'TOSS_WINNER': ['CSK', 'KKR', 'RR', 'DC','SRH'],
    'TOSS_DECISION': ['Field', 'Bat', 'Field', 'Bat','Field'],
    'WINNER':['CSK', 'MI', 'RR', 'DC','LSG']
}

df=pd.DataFrame(data)
df.to_csv('match_data.csv', index=False)
print("DataFrame created and saved to 'match_data.csv'")
