# Author       Chris Dixon
# Reference    https://dash.plotly.com/tutorial 

from dash import Dash, html, dcc, callback, Output, Input, dash_table
import pandas as pd
import plotly.express as px
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template

# Initialize the Dash app
app = Dash(__name__, external_stylesheets=[dmc.theme.DEFAULT_COLORS])

# Load data into a DataFrame from an online CSV file
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')
dg = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')


# Create a Plotly bar graph for the second page
fig = px.bar(df, x="continent", y="pop", color="continent", barmode="group")
fig1 = px.scatter(dg, x="gdp per capita", y="life expectancy",
                 size="population", color="continent", hover_name="country",
                 log_x=True, size_max=60)

# Define the layout with navigation and page content
app.layout = html.Div([
    # Navigation links
    dcc.Location(id='url', refresh=False),
    html.Nav([
        dcc.Link('Page 1 - Data and Graph', href='/'),
        html.Br(),
        dcc.Link('Page 2 - Bar Graph', href='/page-2'),
        html.Br(),
        dcc.Link('Page 3 - Scatter Plot', href='/page-3'),
        html.Br(),
        dcc.Link('Page 4 - Dash Components', href='/page-4'),
        html.Br()
    ]),
    # Content will be rendered in this element
    html.Div(id='page-content')
])

index_page = dmc.Container([
    dmc.Title('My First App with Data, Graph, and Controls', color="blue", size="h3"),
    dmc.RadioGroup(
        [dmc.Radio(i, value=i) for i in ['pop', 'lifeExp', 'gdpPercap']],
        id='my-dmc-radio-item',
        value='lifeExp',
        size="sm"
    ),
    dmc.Grid([
        dmc.Col([
            dcc.Graph(figure={}, id='graph-placeholder')
        ], span=6),
        dmc.Col([
            dash_table.DataTable(data=df.to_dict('records'), page_size=12, style_table={'overflowX': 'auto'})
        ], span=6),
    ]),
], fluid=True)

page_2_layout = html.Div([
    html.H1('Bar Graph of Population by Continent'),
    dcc.Graph(id='example-graph', figure=fig)
])

page_3_layout = html.Div([
    html.H1('Scatter Plot of Life Expectancy by Continent'),
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure=fig1
    )
])

page_4_layout = html.Div([
  html.Div(children=[
        html.Label('Dropdown'),
        dcc.Dropdown(['New York City', 'Montréal', 'San Francisco'], 'Montréal'),

        html.Br(),
        html.Label('Multi-Select Dropdown'),
        dcc.Dropdown(['New York City', 'Montréal', 'San Francisco'],
                     ['Montréal', 'San Francisco'],
                     multi=True),

        html.Br(),
        html.Label('Radio Items'),
        dcc.RadioItems(['New York City', 'Montréal', 'San Francisco'], 'Montréal'),
    ], style={'padding': 10, 'flex': 1}),

    html.Div(children=[
        html.Label('Checkboxes'),
        dcc.Checklist(['New York City', 'Montréal', 'San Francisco'],
                      ['Montréal', 'San Francisco']
        ),

        html.Br(),
        html.Label('Text Input'),
        dcc.Input(value='MTL', type='text'),

        html.Br(),
        html.Label('Slider'),
        dcc.Slider(
            min=0,
            max=9,
            marks={i: f'Label {i}' if i == 1 else str(i) for i in range(1, 6)},
            value=5,
        ),
    ], style={'padding': 10, 'flex': 1})
])


# Update the page content based on the URL
@callback(Output('page-content', 'children'),
          [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page-2':
        return page_2_layout
    if pathname == '/page-3':
        return page_3_layout
    if pathname == '/page-4':
        return page_4_layout
    else:
        # Default to index page
        return index_page

# Callback function to update the graph on the first page based on radio button selection
@callback(
    Output('graph-placeholder', 'figure'),
    Input('my-dmc-radio-item', 'value')
)
def update_graph(col_chosen):
    # Generate a histogram based on the selected data column
    fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg')
    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)