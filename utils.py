import plotly.express as px
import plotly.graph_objects as go

# by: cego669 (https://github.com/cego669)
# credits: https://stackoverflow.com/questions/76431672/using-plotly-i-want-to-plot-a-chart-with-filters
# the only work i had was to generalize the code for any melted dataframe

def plot_time_series_by_category(df, col_x, col_y, col_to_filter, time_series_name, template, normalize=False):
    
    if normalize:
        y_min, y_max = (-3, 3)
    else:
        y_min, y_max = (df[col_y].min(), df[col_y].max())

    fig = go.Figure(layout_yaxis_range=[y_min, y_max])

    for s in df[col_to_filter].unique():
        dff = df[df[col_to_filter] == s]
        for n in dff[time_series_name].unique():
            dfn = dff[dff[time_series_name] == n]
            if normalize:
                y = (dfn[col_y] - dfn[col_y].median())/(dfn[col_y].quantile(.9) - dfn[col_y].quantile(.1))
            else:
                y = dfn[col_y]
            fig.add_trace(go.Scatter(
                    mode='lines',
                    x=dfn[col_x],
                    y=y,
                    name=n,
                    visible=False,
                ))
    
    total_time_series_names = len(df[time_series_name].unique())
    for k in range(total_time_series_names):
        fig.update_traces(visible=True, selector=k)

    buttons = []
    for i,s in enumerate(df[col_to_filter].sort_values().unique()):
        button=dict(
            label=s,
            method='update',
            args=[{'visible': [False] * len(fig.data)}, {'title': s, 'showlegend': True}]
            )
        for j in range(total_time_series_names):
            button['args'][0]['visible'][i*total_time_series_names + j] = True
        buttons.append(button)

    fig.layout.updatemenus = [{'buttons': buttons}]
    fig.update_layout(xaxis_title=col_x, yaxis_title=col_y, template=template)

    fig.show()