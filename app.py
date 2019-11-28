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
def create_map(alcohol_type = 'beer', region = "World"):
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

    region_dict = {"World":[140, 450, 400, 'the World'], "Asia":[400, -190, 520, 'Asia'], "Europe":[800,300, 1100, 'Europe'],
     "Africa":[400,300, 310, 'Africa'], "Americas":[275,950, 310, 'the Americas'], "Oceania":[500, -800, 50, 'Oceania']}

    # set colour scheme of map
    if alcohol_type == 'wine':
        map_color = ['#f9f9f9', '#720b18']
    elif alcohol_type == 'beer':
        map_color = ['#f9f9f9', '#DAA520']
    else:
        map_color = ['#f9f9f9', '#67b2e5', '#1f78b5']

    cols = [x for x in df.columns if alcohol_type in x]
    cols.append('country')

    # this is to select the rank column to sort
    if region == 'World':
        col_to_filter = cols[2]
    else:
        col_to_filter = cols[3]

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
            {"field": cols[4], "type": "nominal", 'title': "Country"},
            {"field": cols[1], "type": "quantitative", 'title': f'Proportion of total servings from {alcohol_type}', 'format':'.2f'},
            {"field": cols[0], "type": "quantitative", 'title': f'Total {alcohol_type} servings'},
            {"field": cols[3], "type": "quantitative", 'title': 'Continent rank'},
            {"field": cols[2], "type": "quantitative", 'title': 'Global rank'},
        ]
    ).transform_lookup(
        lookup='id',
        from_=alt.LookupData(df, 'id', fields = cols)
    ).project(
        type='mercator', scale = region_dict[region][0], translate = [region_dict[region][1], region_dict[region][2]]
    ).properties(
        width=900,
        height=600,
    )

    bar = alt.Chart(df).mark_bar().encode(
        alt.X(
            field=cols[1],
            type='quantitative',
            title = "",
            scale=alt.Scale(domain=[0, 1]),
        ),
        alt.Y(
            field='country',
            type='nominal',
            sort=alt.EncodingSortField(field=cols[1], op='max', order='descending'),
            title=''
        ),
        alt.Fill(
            field = cols[1],
            type = 'quantitative',
            scale=alt.Scale(domain=[0, 1], range=map_color),
            legend=None),
        tooltip = [
            {"field": cols[4], "type": "nominal", 'title': "Country"},
            {"field": cols[1], "type": "quantitative", 'title': f'Proportion of total servings per person from {alcohol_type}', 'format':'.2f'},
            {"field": cols[0], "type": "quantitative", 'title': f'Total {alcohol_type} servings'},
            {"field": cols[3], "type": "quantitative", 'title': 'Continent rank'},
            {"field": cols[2], "type": "quantitative", 'title': 'Global rank'},
        ]
    ).transform_filter(alt.datum.region == region if region != 'World' else alt.datum.total_servings >= 0
    ).transform_window(
        sort=[alt.SortField(cols[1], order="descending")],
        rank="rank(col_to_filter)"
    ).transform_filter(
        alt.datum.rank <= 20
    ).properties(
        title=f"Top 20 Countries that love {alcohol_type.title()} in {region_dict[region][3]}",
        width = 200,
        height = 600
    )

    return alt.hconcat(map_plot, bar).configure_legend(
        gradientLength=300,
        gradientThickness=20,
        titleLimit= 0,
        labelFontSize=15,
        titleFontSize=20
    ).configure_axis(
        labelFontSize=15,
        titleFontSize=20
    ).configure_title(
        fontSize=20
    )
header = dbc.Jumbotron(
    [
        dbc.Container(
            [

                html.H1("Which Countries are Beer-lovers, Wine-lovers, or Spirit-lovers? (2010)", className="display-3",
                        style={'color': 'red'}),
                html.P(
                    "Proportion of alcoholic drink type consumed per person in each country",
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
                    dcc.Dropdown(
                        id='dd-chart2',
                        options=[
                            {'label': 'World', 'value': 'World'},
                            {'label': 'Asia', 'value': 'Asia'},
                            {'label': 'Europe', 'value': 'Europe'},
                            {'label': 'Africa', 'value': 'Africa'},
                            {'label': 'Americas', 'value': 'Americas'},
                            {'label': 'Oceania', 'value': 'Oceania'}
                        ],
                        value='World',
                        style=dict(width='30%',
                                verticalAlign="middle")
                                )),

                    dcc.Markdown('''
                    **Source:** FiveThirtyEight ([link](https://github.com/fivethirtyeight/data/tree/master/alcohol-consumption))
                    '''),

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
    [dash.dependencies.Input('dd-chart', 'value'),
    dash.dependencies.Input('dd-chart2', 'value')])
def update_plot(alcohol_type, region):
    #Takes in an alcohol_type and calls create_map to update our Altair figure
    updated_plot = create_map(alcohol_type, region).to_html()
    return updated_plot
if __name__ == '__main__':
    app.run_server(debug=True)# Create your app here
