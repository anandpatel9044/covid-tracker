import dash
from dash import dcc, html
import plotly.express as px
from dash.dependencies import Input, Output
from data import get_global_data, get_country_data

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("COVID-19 Trend Tracker", style={"textAlign": "center"}),

    # 🌙 Dark mode toggle
    dcc.RadioItems(
        id="theme-toggle",
        options=[
            {"label": "Light", "value": "light"},
            {"label": "Dark", "value": "dark"}
        ],
        value="light",
        inline=True,
        style={"textAlign": "center", "marginBottom": "20px"}
    ),

    # 🔄 Auto refresh
    dcc.Interval(
        id="interval-component",
        interval=5*60*1000,
        n_intervals=0
    ),

    dcc.Graph(id="global-graph"),
    dcc.Graph(id="map-graph"),

    html.H2("Compare Countries"),

    dcc.Dropdown(
        id="country-dropdown",
        multi=True,
        value=["India"]
    ),

    dcc.Graph(id="comparison-graph"),

    html.Div(id="country-stats", style={"marginTop": "20px"})

], id="main-container", style={"maxWidth": "900px", "margin": "auto"})


# 🔄 Update graphs + dropdown
@app.callback(
    [
        Output("global-graph", "figure"),
        Output("map-graph", "figure"),
        Output("country-dropdown", "options")
    ],
    Input("interval-component", "n_intervals")
)
def update_dashboard(n):
    global_df = get_global_data()
    country_df = get_country_data()

    # Global trend
    line_fig = px.line(
        global_df,
        x="date",
        y=["daily_cases", "7_day_avg"],
        title="Daily Cases & 7-Day Average"
    )

    # Map fix
    country_df["iso3"] = country_df["countryInfo"].apply(
        lambda x: x["iso3"] if isinstance(x, dict) else None
    )

    map_fig = px.choropleth(
        country_df,
        locations="iso3",
        color="cases",
        title="COVID-19 Cases by Country"
    )

    options = [{"label": c, "value": c} for c in country_df["country"]]

    return line_fig, map_fig, options


# 📈 Comparison graph
@app.callback(
    Output("comparison-graph", "figure"),
    Input("country-dropdown", "value")
)
def compare_countries(selected_countries):
    country_df = get_country_data()

    df = country_df[country_df["country"].isin(selected_countries)]

    fig = px.bar(
        df,
        x="country",
        y="cases",
        color="country",
        title="Cases Comparison"
    )

    return fig


# 📊 Country stats
@app.callback(
    Output("country-stats", "children"),
    Input("country-dropdown", "value")
)
def update_country(selected_countries):
    country_df = get_country_data()

    rows = country_df[country_df["country"].isin(selected_countries)]

    return [
        html.Div([
            html.H3(row["country"]),
            html.P(f"Cases: {row['cases']:,}"),
            html.P(f"Deaths: {row['deaths']:,}"),
            html.P(f"Recovered: {row['recovered']:,}"),
            html.P(f"Tests: {row['tests']:,}")
        ], style={"border": "1px solid #ddd", "padding": "10px", "margin": "10px"})
        for _, row in rows.iterrows()
    ]


# 🌙 Theme switch
@app.callback(
    Output("main-container", "style"),
    Input("theme-toggle", "value")
)
def update_theme(theme):
    if theme == "dark":
        return {
            "backgroundColor": "#111",
            "color": "#fff",
            "maxWidth": "900px",
            "margin": "auto",
            "padding": "20px"
        }
    else:
        return {
            "backgroundColor": "#fff",
            "color": "#000",
            "maxWidth": "900px",
            "margin": "auto",
            "padding": "20px"
        }


if __name__ == "__main__":
    app.run(debug=True)