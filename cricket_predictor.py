import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier 

df = pd.read_csv("match_data.csv")

X=df.drop("WINNER",axis=1)
y=df["WINNER"]

X=pd.get_dummies(X)

X_train,X_test,y_train,y_test = train_test_split(
    X,y,
    test_size=0.2,
    random_state=42)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train,y_train)

accuracy = model.score(X_test,y_test)

print("\nEncoded Columns:")
print(X.columns)

print("Model traained successfully with accuracy:", accuracy)
print(f"Model accuracy: {accuracy:.2f}")

team1 = input("\nEnter Home Team : ").upper()
team2 = input("Enter Away Team: ").upper()
city = input("Enter City: ").capitalize()
toss_winner = input("Enter Toss Winner: ").upper()
toss_decision = input("Enter Toss Decision (bat/field): ").capitalize()

new_match = pd.DataFrame(0, index=[0], columns=X.columns)

col=f"TEAM1_HOME_{team1}"
if col in new_match.columns:
    new_match[col]=1

col=f"TEAM2_AWAY_{team2}"
if col in new_match.columns:
    new_match[col]=1    
    
col=f"CITY_{city}"
if col in new_match.columns:
    new_match[col]=1
    
col=f"TOSS_WINNER_{toss_winner}"
if col in new_match.columns:
    new_match[col]=1
    
col=f"TOSS_DECISION_{toss_decision}"
if col in new_match.columns:
    new_match[col]=1
    
predicted_winner = model.predict(new_match)

probabilities = model.predict_proba(new_match)

print("\nPredicted Winner: ",predicted_winner[0])


print("\nWinning Probabilities:")

for team, prob in zip(model.classes_, probabilities[0]):
    print(f"{team}: {prob:.2f}")