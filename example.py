from dash import Dash, html, dash_table, dcc, Output, Input
import plotly.express as px
import dash_stylish_header_footer_hook

# Register header and footer hooks with header custom gradient adn footer text
dash_stylish_header_footer_hook.add_header(
   gradient="linear-gradient(90deg, black, red)"
)
dash_stylish_header_footer_hook.add_footer_hook("© 2025 My Dash App")

# Data
df = px.data.gapminder()

app = Dash()

app.layout = html.Div([
    html.Div(
        className="row",
        children=[
            dcc.RadioItems(
                options=["pop", "lifeExp", "gdpPercap"],
                value="lifeExp",
                inline=True,
                id="my-radio-buttons-final",
            )
        ],
    ),
    html.Div(
        className="row",
        children=[
            html.Div(
                className="six columns",
                children=[
                    dash_table.DataTable(
                        data=df.to_dict("records"),
                        page_size=11,
                        style_table={"overflowX": "auto"},
                        id="datatable",
                    )
                ],
            ),
            html.Div(
                className="six columns",
                children=[dcc.Graph(figure={}, id="histo-chart-final")],
            ),
        ],
    ),
])

@app.callback(
    Output("histo-chart-final", "figure"),
    Input("my-radio-buttons-final", "value"),
)
def update_graph(col_chosen):
    fig = px.histogram(df, x="continent", y=col_chosen, histfunc="avg")
    return fig

if __name__ == "__main__":
    app.run(debug=True, port=8051)