import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import altair as alt
import pandas as pd
import pandas as pd
import altair as alt
from vega_datasets import data
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, assets_folder='assets')
server = app.server
df = pd.read_csv("data/merged_data_clean.csv")
def create_map(alcohol_type = 'beer'):
    """
    Create choropleth heatmap based on alcoholic consumption
    
    Parameters
    ----------
    alcohol_type : str {‘wine’, ‘beer’, 'spirit'}
        Type of alcohol to show on choropleth.
    
    Returns
    -------
    altair Chart object
        Choropleth of chosen alcohol type
    Examples
    --------
    >>> create_map('spirit')
    """
        
    # set colour scheme of map
    if alcohol_type == 'wine':
        map_color = ['#f9f9f9', '#720b18']
    elif alcohol_type == 'beer':
        map_color = ['#f9f9f9', '#DAA520']
    else:
        map_color = ['#f9f9f9', '#67b2e5', '#1f78b5']
    
    cols = [x for x in df.columns if alcohol_type in x]
    cols.append('country')
    
    # Create map plot
    map_plot = alt.Chart(alt.topo_feature(data.world_110m.url, 'countries')).mark_geoshape(
        stroke='white',
        strokeWidth=0.5
    ).encode(
        alt.Color(field = cols[1],
                  type = 'quantitative',
                  scale=alt.Scale(domain=[0, 1], range=map_color),
                  legend=alt.Legend(orient='top',
                                   title = f'Proportion of total servings per person from {alcohol_type}')
                 ),
        tooltip = [
            {"field": cols[3], "type": "nominal", 'title': "Country"},
            {"field": cols[1], "type": "quantitative", 'title': f'Proportion of total servings from {alcohol_type}', 'format':'.2f'},
            {"field": cols[0], "type": "quantitative", 'title': f'Total {alcohol_type} servings'},
            {"field": cols[2], "type": "quantitative", 'title': 'Global rank'},
        ]
    ).transform_lookup(
        lookup='id',
        from_=alt.LookupData(df, 'id', fields = cols)
    ).project(
        type='mercator'
    ).properties(
        width=1200,
        height=600,
    ).configure_legend(
        gradientLength=400,
        gradientThickness=30,
        titleLimit= 0
    ) 
    return map_plot
header = dbc.Jumbotron(
    [
        dbc.Container(
            [

                html.H1("Which Countries are Beer-lovers, Wine-lovers, or Spirit-lovers?", className="display-3",
                        style={'color': 'red'}),
                html.P(
                    "Proportion of alcoholic drink type consumed by each country",
                    className="lead",
                ),
            ],
            fluid=True,
        )
    ],
    fluid=True,
)
# Drop-down and Map Plot
content = dbc.Container([
    dbc.Row(
                [dbc.Col(
                    dcc.Dropdown(
                        id='dd-chart',
                        options=[
                            {'label': 'Beer', 'value': 'beer'},
                            {'label': 'Wine', 'value': 'wine'},
                            {'label': 'Spirits', 'value': 'spirit'},
                        ],
                        value='beer',
                        style=dict(width='30%',
                                verticalAlign="middle")
                                )),
                    dbc.Col(
                        html.Iframe(
                            sandbox='allow-scripts',
                            id='plot',
                            height='1000',
                            width='1500',
                            style={'border-width': '0'},
                            # need to change the category here under the create_map function
                            srcDoc= create_map().to_html()
                            )),
                    
                
                ]
    )
]
)

app.layout = html.Div([header,
                       content])
@app.callback(
    dash.dependencies.Output('plot', 'srcDoc'),
    [dash.dependencies.Input('dd-chart', 'value')])
def update_plot(alcohol_type):
    #Takes in an alcohol_type and calls create_map to update our Altair figure
    updated_plot = create_map(alcohol_type).to_html()
    return updated_plot
if __name__ == '__main__':
    app.run_server(debug=True)# Create your app here