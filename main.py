import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import dash_core_components as dcc
import dash_html_components as html
from dash import Dash


# Import data
path = './data/Airbnb/Airbnb_Open_Data.csv'
df = pd.read_csv(path, low_memory=False)
data_df = pd.DataFrame(df)
# headers = list(data_df.columns)
headers = {'id', 'host_name', 'neighbourhood', 'neighbourhood_group', 'room_type', 'country', 'instant_bookable',
           'cancellation_policy', 'Construction year', 'price', 'service fee', 'minimum nights', 'number of reviews',
           'last review', 'reviews per month', 'review rate number'}
worksheet_df = pd.DataFrame(data_df, columns=headers)

fig = plt.figure(figsize=(12, 8))
plt.subplots()


def flask_interface():
    app = Dash(__name__)

    fig = px.bar(worksheet_df, x='neighbourhood', y='price', color='room_type', barmode='group')
    app.layout = html.Div([
        html.H1('Preço por Bairro'),
        dcc.Graph(figure=fig)
    ])


'''
if __name__ == '__main__':
    flask_interface()
    app.run_server(debug=True)

'''