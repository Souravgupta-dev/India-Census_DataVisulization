from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd
# Load dashboard data
DATA_PATH = "data/cleaned/census_dashboard_data.csv"
df = pd.read_csv(DATA_PATH)

# Calculate summary metrics
total_population = df["TOT_P"].sum()
total_male = df["TOT_M"].sum()
total_female = df["TOT_F"].sum()
average_literacy = df["Literacy_Rate"].mean()
average_sex_ratio = df["Sex_Ratio"].mean()


# Day 16: Validate dashboard calculations
print("\n--- DASHBOARD DATA VALIDATION ---")

print("Number of regions:", df["Name"].nunique())
print("Total population:", int(df["TOT_P"].sum()))
print("Male population:", int(df["TOT_M"].sum()))
print("Female population:", int(df["TOT_F"].sum()))

print(
    "Average calculated literacy rate:",
    round(df["Literacy_Rate"].mean(), 2), "%"
)

print(
    "Average sex ratio:",
    round(df["Sex_Ratio"].mean(), 2)
)

print(
    "Missing values in key columns:",
    df[
        [
            "Name",
            "TOT_P",
            "TOT_M",
            "TOT_F",
            "Literacy_Rate",
            "Sex_Ratio",
            "Population_Density",
        ]
    ].isnull().sum().sum()
)

print(
    "Duplicate region names:",
    df["Name"].duplicated().sum()
)


# Population chart: Top 10 most populated regions
top_population = df.nlargest(10, "TOT_P").sort_values("TOT_P")

population_fig = px.bar(
    top_population,
    x="TOT_P",
    y="Name",
    orientation="h",
    title="Top 10 Most Populated States/UTs — Census 2011",
    labels={
        "TOT_P": "Population",
        "Name": "State/Union Territory"
    },
    color="TOT_P",
    color_continuous_scale="Blues"
)


population_fig.update_layout(
    height=500,
    margin=dict(l=100, r=30, t=80, b=60),
    title_x=0.5,
    font=dict(size=12),
)

population_fig.update_traces(
    hovertemplate=(
        "Region: %{y}<br>"
        "Population: %{x:,.0f}"
        "<extra></extra>"
    )
)


# Literacy chart: Top 10 regions by calculated literacy rate
top_literacy = df.nlargest(10, "Literacy_Rate").sort_values(
    "Literacy_Rate"
)

literacy_fig = px.bar(
    top_literacy,
    x="Literacy_Rate",
    y="Name",
    orientation="h",
    title="Top 10 States/UTs by Calculated Literacy Rate — Census 2011",
    labels={
        "Literacy_Rate": "Calculated Literacy Rate (%)",
        "Name": "State/Union Territory",
    },
    color="Literacy_Rate",
    color_continuous_scale="Greens",
)

literacy_fig.update_layout(
    template="plotly_white",
    coloraxis_showscale=False,
)

# Sex ratio chart: Top 10 regions
top_sex_ratio = df.nlargest(10, "Sex_Ratio").sort_values(
    "Sex_Ratio"
)

sex_ratio_fig = px.bar(
    top_sex_ratio,
    x="Sex_Ratio",
    y="Name",
    orientation="h",
    title="Top 10 States/UTs by Sex Ratio — Census 2011",
    labels={
        "Sex_Ratio": "Females per 1,000 Males",
        "Name": "State/Union Territory",
    },
    color="Sex_Ratio",
    color_continuous_scale="Purples",
)

sex_ratio_fig.update_layout(
    template="plotly_white",
    coloraxis_showscale=False,
)

# Population density chart: Top 10 regions
top_density = df.nlargest(10, "Population_Density").sort_values(
    "Population_Density"
)

density_fig = px.bar(
    top_density,
    x="Population_Density",
    y="Name",
    orientation="h",
    title="Top 10 Most Densely Populated States/UTs — Census 2011",
    labels={
        "Population_Density": "People per Square Kilometre",
        "Name": "State/Union Territory",
    },
    color="Population_Density",
    color_continuous_scale="Oranges",
)

density_fig.update_layout(
    template="plotly_white",
    coloraxis_showscale=False,
)



# Consistent layout for all dashboard charts
for fig in [population_fig, literacy_fig, sex_ratio_fig, density_fig]:
    fig.update_layout(
        height=480,
        autosize=True,
        margin=dict(l=120, r=40, t=100, b=80),
        title_x=0.5,
        title_font=dict(size=18),
        font=dict(size=12),
        template="plotly_white",
        coloraxis_showscale=False,
    )

    fig.update_traces(
        hoverlabel=dict(font_size=13)
    )



app = Dash(__name__)
app.title = "India Census Data Dashboard"

# Reusable KPI card

def create_card(title, value, color):
    return html.Div(
        [
            html.H4(
                title,
                style={
                    "fontSize": "16px",
                    "marginBottom": "10px",
                    "color": "#333333",
                },
            ),
            html.H2(
                value,
                style={
                    "fontSize": "25px",
                    "margin": "0",
                    "color": "#111827",
                },
            ),
            html.Hr(style={"marginTop": "18px"}),
        ],
        style={
             "display": "flex",
            "flexWrap": "wrap",
            "gap": "18px",
            "width": "100%",
            "alignItems": "stretch",
            "backgroundColor": "#FFFFFF",
            "padding": "20px",
            "borderRadius": "12px",
            "boxShadow": "0 3px 8px rgba(0, 0, 0, 0.12)",
            "borderTop": f"5px solid {color}",
            "flex": "1 1 180px",
            "minWidth": "180px",
            "textAlign": "center",
            "boxSizing": "border-box",
        },
    )


app.layout = html.Div(
    [
        html.H1(
            "India Census 2011 Dashboard",
            style={"textAlign": "center", "color": "#17365D"},
        ),
        html.P(
            "Explore population and demographic indicators across "
            "Indian states and union territories.",
            style={"textAlign": "center", "fontSize": "17px"},
        ),
        html.Hr(),

        html.H2("Key Statistics"),

        
# KPI cards
html.Div(
    [
        create_card("Total Population", f"{total_population:,}", "#2563EB"),
        create_card("Male Population", f"{total_male:,}", "#0891B2"),
        create_card("Female Population", f"{total_female:,}", "#DB2777"),
        create_card("Average Literacy Rate", f"{average_literacy:.2f}%", "#16A34A"),
        create_card("Average Sex Ratio", f"{average_sex_ratio:.2f}", "#D97706"),
    ],
    style={
        "display": "flex",
        "flexWrap": "wrap",
        "gap": "18px",
    },
),

html.Hr(),

# Population chart — separate from the KPI cards
html.H2("Population Analysis"),

dcc.Graph(
    id="population-chart",
    figure=population_fig,
    style={"width": "100%"},
),

dcc.Graph(
    id="literacy-chart",
    figure=literacy_fig,
    style={"width": "100%"},
),

dcc.Graph(
    id="sex-ratio-chart",
    figure=sex_ratio_fig,
    style={"width": "100%"},
),

dcc.Graph(
    id="density-chart",
    figure=density_fig,
    style={"width": "100%"},
),


html.Hr(),

html.H2("Explore a State or Union Territory"),

dcc.Dropdown(
    id="region-dropdown",
    options=[
        {"label": name, "value": name}
        for name in sorted(df["Name"].unique())
    ],
    value="UTTAR PRADESH",
    clearable=False,
    placeholder="Select a state or union territory",
    style={"color": "#222", "maxWidth": "600px"},
),

html.Div(
    id="region-details",
    style={
        "backgroundColor": "white",
        "padding": "20px",
        "marginTop": "15px",
        "borderRadius": "10px",
    },
),

html.H3("Dataset Overview"),
html.P(f"Number of regions: {df['Name'].nunique()}"),
html.P(f"Total records: {len(df)}"),

    ],
    style={
        "fontFamily": "Arial, sans-serif",
        "backgroundColor": "#F3F6FA",
        "minHeight": "100vh",
        "padding": "30px",
    },
)

@app.callback(
    Output("region-details", "children"),
    Input("region-dropdown", "value")
)
def update_region_details(selected_region):
    region = df[df["Name"] == selected_region].iloc[0]

    return html.Div([
        html.H3(selected_region),
        html.P(f"Population: {int(region['TOT_P']):,}"),
        html.P(f"Male population: {int(region['TOT_M']):,}"),
        html.P(f"Female population: {int(region['TOT_F']):,}"),
        html.P(
            f"Calculated literacy rate: "
            f"{region['Literacy_Rate']:.2f}%"
        ),
        html.P(
            f"Sex ratio: {region['Sex_Ratio']:.2f} "
            "females per 1,000 males"
        ),
        html.P(
            f"Population density: "
            f"{region['Population_Density']:.2f} people/km²"
        ),
    ])

if __name__ == "__main__":
    app.run(debug=True)
