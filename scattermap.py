import dash
from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

# Figure 1 (for 2023)
df2023 = pd.read_csv('eBird_data_acquisition/cleaned_eBird_data/eBird2023_cleaned.csv')
fig2023 = go.Figure(go.Scattermapbox(
    lat=list(df2023['lat']),
    lon=list(df2023['lng']),
    mode='markers',
    marker=dict(size=9), # change markers to birds eventually, maybe add opacity=__
    text=list(df2023['comName'])))
fig2023.update_layout(
    autosize=True,
    hovermode='closest',
    mapbox=dict( 
        bearing=0,
        center=dict(lat=39.2398155, lon=-119.270401),
        pitch=0,
        zoom=10,
        style="open-street-map"),
    margin=dict(l=25, r=25, t=25, b=25))
fig2023.update_traces(marker=dict(color='blue')) 

# Figure 2 (for 2021)
df2021 = pd.read_csv('eBird_data_acquisition/cleaned_eBird_data/eBird2021_cleaned.csv')
fig2021 = go.Figure(go.Scattermapbox(
    lat=list(df2021['lat']),
    lon=list(df2021['lng']),
    mode='markers',
    marker=dict(size=9), 
    text=list(df2021['comName'])))
fig2021.update_layout(
    autosize=True,
    hovermode='closest',
    mapbox=dict( 
        bearing=0,
        center=dict(lat=39.2398155, lon=-119.270401),
        pitch=0,
        zoom=10,
        style="open-street-map"),
    margin=dict(l=25, r=25, t=25, b=25))
fig2021.update_traces(marker=dict(color='blue'))

# Figure 3 (for 2020)
df2020 = pd.read_csv('eBird_data_acquisition/cleaned_eBird_data/eBird2020_cleaned.csv')
fig2020 = go.Figure(go.Scattermapbox(
    lat=list(df2020['lat']),
    lon=list(df2020['lng']),
    mode='markers',
    marker=dict(size=9), 
    text=list(df2020['comName'])))
fig2020.update_layout(
    autosize=True,
    hovermode='closest',
    mapbox=dict( 
        bearing=0,
        center=dict(lat=39.2398155, lon=-119.270401),
        pitch=0,
        zoom=10,
        style="open-street-map"),
    margin=dict(l=25, r=25, t=25, b=25))
fig2020.update_traces(marker=dict(color='blue'))

# Figure 4 (for 2018)
df2018 = pd.read_csv('eBird_data_acquisition/cleaned_eBird_data/eBird2018_cleaned.csv')
fig2018 = go.Figure(go.Scattermapbox(
    lat=list(df2018['lat']),
    lon=list(df2018['lng']),
    mode='markers',
    marker=dict(size=9), 
    text=list(df2018['comName'])))
fig2018.update_layout(
    autosize=True,
    hovermode='closest',
    mapbox=dict( 
        bearing=0,
        center=dict(lat=39.2398155, lon=-119.270401),
        pitch=0,
        zoom=10,
        style="open-street-map"),
    margin=dict(l=25, r=25, t=25, b=25))
fig2018.update_traces(marker=dict(color='blue'))

# Figire 5 (for 2017)
df2017 = pd.read_csv('eBird_data_acquisition/cleaned_eBird_data/eBird2017_cleaned.csv')
fig2017 = go.Figure(go.Scattermapbox(
    lat=list(df2017['lat']),
    lon=list(df2017['lng']),
    mode='markers',
    marker=dict(size=9), 
    text=list(df2017['comName'])))
fig2017.update_layout(
    autosize=True,
    hovermode='closest',
    mapbox=dict( 
        bearing=0,
        center=dict(lat=39.2398155, lon=-119.270401),
        pitch=0,
        zoom=10,
        style="open-street-map"),
    margin=dict(l=25, r=25, t=25, b=25))
fig2017.update_traces(marker=dict(color='blue'))

# format the website
app.layout = html.Div([

    html.Div([
        html.Br(),
        html.H1('Bird Sightings in Northern California and Nevada', style={'textAlign': 'center'}),
        html.H4('Data Source: eBird', style={'textAlign': 'center'}),
        html.Br()
    ], style={'backgroundColor': 'white'}),

    html.H2('2023 Bird Sightings', style={'textAlign': 'center'}),
    dcc.Graph(figure=fig2023),

    html.H2('2021 Bird Sightings', style={'textAlign': 'center'}),
    dcc.Graph(figure=fig2021),

    html.H2('2020 Bird Sightings', style={'textAlign': 'center'}),
    dcc.Graph(figure=fig2020),

    html.H2('2018 Bird Sightings', style={'textAlign': 'center'}),
    dcc.Graph(figure=fig2018),

    html.H2('2017 Bird Sightings', style={'textAlign': 'center'}),
    dcc.Graph(figure=fig2017)
    
], style={'backgroundColor': '#1155ccff'})

if __name__ == '__main__':
    app.run_server(debug=True) 

# Resources: https://plotly.com/python/tile-scatter-maps/ 


# import dash
# from dash import Dash, dcc, html
# import plotly.graph_objects as go
# import pandas as pd
# import gdown

# # Download CSVs dynamically
# file_ids = {
#     "eBird2023_cleaned.csv": "1MHwX5PYzHa7UGs6n15fo-4KQT5mx99T_",
#     "eBird2021_cleaned.csv": "1V18U-C-bA1Fwy4PIfxIkJWX96JlqcDiQ",
#     "eBird2020_cleaned.csv": "1gxA-w3-Z8XDSJ5hwl-9tMyRtA-Rfe8GB",
#     "eBird2018_cleaned.csv": "1eraBW6ljZaUGpDtGL4AFkee7hWz3IKES",
#     "eBird2017_cleaned.csv": "1sORx3iEYjcX3DFu_jZYd2v5L3wCMhpfb"
# }

# for filename, file_id in file_ids.items():
#     url = f"https://drive.google.com/uc?id={file_id}"
#     gdown.download(url, filename, quiet=False)

# # Load the datasets
# df2023 = pd.read_csv("eBird2023_cleaned.csv")
# df2021 = pd.read_csv("eBird2021_cleaned.csv")
# df2020 = pd.read_csv("eBird2020_cleaned.csv")
# df2018 = pd.read_csv("eBird2018_cleaned.csv")
# df2017 = pd.read_csv("eBird2017_cleaned.csv")

# # Create scatter maps for each dataset
# def create_scatter_map(df):
#     fig = go.Figure(go.Scattermapbox(
#         lat=df['lat'],
#         lon=df['lng'],
#         mode='markers',
#         marker=dict(size=9, color='blue'),
#         text=df['comName']
#     ))
#     fig.update_layout(
#         autosize=True,
#         hovermode='closest',
#         mapbox=dict(
#             bearing=0,
#             center=dict(lat=39.2398155, lon=-119.270401),
#             pitch=0,
#             zoom=10,
#             style="open-street-map"
#         ),
#         margin=dict(l=25, r=25, t=25, b=25)
#     )
#     return fig

# # Build Dash app
# app = Dash(__name__)

# # App layout
# app.layout = html.Div([
#     html.H1('Bird Sightings in Northern California and Nevada', style={'textAlign': 'center'}),
#     html.H4('Data Source: eBird', style={'textAlign': 'center'}),

#     html.H2('2023 Bird Sightings', style={'textAlign': 'center'}),
#     dcc.Graph(figure=create_scatter_map(df2023)),

#     html.H2('2021 Bird Sightings', style={'textAlign': 'center'}),
#     dcc.Graph(figure=create_scatter_map(df2021)),

#     html.H2('2020 Bird Sightings', style={'textAlign': 'center'}),
#     dcc.Graph(figure=create_scatter_map(df2020)),

#     html.H2('2018 Bird Sightings', style={'textAlign': 'center'}),
#     dcc.Graph(figure=create_scatter_map(df2018)),

#     html.H2('2017 Bird Sightings', style={'textAlign': 'center'}),
#     dcc.Graph(figure=create_scatter_map(df2017)),
# ], style={'backgroundColor': '#1155ccff'})

# if __name__ == '__main__':
#     app.run_server(debug=True)
