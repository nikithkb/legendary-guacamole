# %%
import pandas as pd

# %%
# INTEGRATE
data = pd.read_csv('userData.csv')
data.drop('Timestamp', axis=1, inplace = True)
data.head(7)

# %%
df = data.copy()

# %%
for column in data:
    if column != "Username":
        data[column] = round(data[column] /data[column].abs().max(), 4)
data.head(7)

# %%
df['Score'] = ""
def calc_score (username):
    for i in range(len(data)):
        score = 1 * data.loc[i, "MVPs"] + 0.9 * data.loc[i, "Wins"] + 0.8 * data.loc[i, "Goals"] + 0.6 * data.loc[i, "Assists"] + 0.4 * data.loc[i, "Saves"] + 0.3 * data.loc[i, "Shots"]
        # max score = 4
        df.loc[i, 'Score'] = score 
    return round(score, 4)

for i in data['Username']:
    calc_score(i)
df.head(7)

# %%
df.set_index('Username', inplace = True)

# %%
df.sort_values('Score', inplace = True)
df.head(7)

# %%
# INTEGRATE
username = 'tempy'

# %%
# INTEGRATE
def find_team(username):
    idx = df.index.get_loc(username)
    if idx == 0:
        team = (df.iloc[idx : idx + 3]).copy()
    elif idx == len(df)-1:
        team = (df.iloc[idx - 2 : idx + 1]).copy()
    else:
        team = (df.iloc[idx - 1 : idx + 2]).copy()
    return team

find_team(username).to_csv('Team.csv')



