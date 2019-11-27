def create_map(alcohol_type):
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
    
    # Load packages
    import pandas as pd
    import altair as alt
    import pandas_profiling
    from vega_datasets import data

    # Need to enable this to allow work with larger datasets (https://altair-viz.github.io/user_guide/faq.html)
    alt.data_transformers.enable('json')
    
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