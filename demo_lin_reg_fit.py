import pickle
from sklearn.linear_model import LinearRegression

projects_complited = [[1], [2], [3], [4], [5]]
position = [2, 3, 5, 8, 11]

model = LinearRegression()
model.fit(projects_complited, position)

# Save the trained model using pickle
with open('modelpos.pkl', 'wb') as file:
    pickle.dump(model, file)
