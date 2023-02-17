# import pandas as pd
# import plotly.express as px
# import plotly.io as pio
# 
# # Load state abbreviation data
# state_abbr = pd.DataFrame({
# 	abbr: [AL, AK, AZ, AR, CA, CO, CT, DE, FL, GA, HI, ID, 
#              IL, IN, IA, KS, KY, LA, ME, MD, MA, MI, MN, MS, 
#              MO, MT, NE, NV, NH, NJ, NM, NY, NC, ND, OH, OK, 
#              OR, PA, RI, SC, SD, TN, TX, UT, VT, VA, WA, WV, WI, WY]
# })
# 
# # Load city/state data from CSV file
# # city_data = pd.read_csv("cities.csv")
# # 
# # # Extract a list of states from the city data
# # listed_states = city_data["state"].unique()
# 
# # if state unvisited, grey out
# # if state visited once, fill in white
# # if state visited more than once, fill in cyan
# # cute cyber platinum hearts or icons by home states, or gold outlines/crowns
# 
# # read the city-state data from the csv file
# df = pd.read_csv("places.csv")
# 
# # group the data by state and count the number of cities in each state
# state_counts = df.groupby("state").count().reset_index()
# 
# # create a dataframe with the state codes and the count of cities in each state
# state_data = pd.DataFrame({
#     "state": state_counts["state"],
#     "count": state_counts["city"]
# })
# 
# visitedText=0
# unvisitedText=2
# 
# # Create a choropleth map
# fig = px.choropleth(
#     state_abbr, locations="abbr", locationmode="USA-states",
#     color=state_abbr["abbr"].apply(lambda x: visitedText if x in df else unvisitedText),
# #     color=state_abbr["abbr"].apply(lambda x: visitedText if x in state_data else unvisitedText),
#     scope="usa"
# )
# 
# # Show the map
# pio.show(fig)

import pandas as pd
import plotly.graph_objects as go


# Load city-state data from csv file
df = pd.read_csv("places.csv", names=["city", "state"])

# Load state acronym data
state_data_file = pd.read_csv("us-states.csv")

# Get list of states mentioned in city-state data
visited_states = df["state"].unique()

state_visit_count_data = df.groupby("state").count().reset_index()
# state_visit_count = state_visit_count_data["city"]
# print("state count\n",state_visit_count)

state_data = pd.DataFrame({
    "state": visited_states,
    "visit_count": state_visit_count_data["city"]
})

# Map the states to colors
state_colors = [1 if state in visited_states else 0 for state in state_data_file["abbr"]]
visit_text = ["visited!" if state in visited_states else "not visited... yet" for state in state_data_file["abbr"]] # later can show # times visited or which cities, link to photos/journal, etc

# Create the figure and add the choropleth trace
fig = go.Figure(go.Choropleth(
    locations=state_data_file["abbr"],
    z=state_colors,
    locationmode="USA-states",
    colorscale=[[0, "slategrey"], [1, "forestgreen"]],
    marker_line_color="white",
    colorbar_title="",
    showscale=False,
    hovertemplate=visit_text
))

# Set the layout properties
fig.update_layout(
    title_text="The Map of Bayla :D",
    geo_scope="usa",
)

# Show the figure
fig.show()