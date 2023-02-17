import pandas as pd
import plotly.graph_objects as go


# Load city-state data from csv file
df = pd.read_csv("places.csv", names=["city", "state"])

# Load state acronym data
state_data_file = pd.read_csv("us-states.csv")

# Get list of states mentioned in city-state data
visited_states = df["state"].unique()

state_visit_count_data = df.groupby("state").count().reset_index()

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