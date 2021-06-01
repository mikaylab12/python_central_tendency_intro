import matplotlib.pyplot as plt
cities = ["East London", "Cape Town", "Kimberley", "Durban"]
rainfall = [140, 200, 120, 157]
# bar graph placing and details
x_pos = [i for i, _ in enumerate(cities)]
plt.bar(x_pos, rainfall, color='purple')
plt.xlabel("Cities")
plt.ylabel("Rainfall")
plt.title("Rainfall for 4 cities in South Africa")
plt.xticks(x_pos, cities)
# to display bar graph
plt.show()
