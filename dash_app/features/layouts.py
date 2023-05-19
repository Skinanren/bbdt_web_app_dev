# package imports
import dash
from dash import html, dcc, Output, Input, callback
import dash_bootstrap_components as dbc
from utils.images import logo_encoded
from utils.images import logo_encoded1

# dash.register_page(__name__)

card = dbc.Card(
    [
        # dbc.CardImg(src="/static/images/placeholder286x180.png", top=True),
        dbc.CardImg(
            src=logo_encoded1,
            top=True,
            style={"opacity": 1},  # lower the number, the darker
        ),
        dbc.CardBody(
            [
                html.H4("Card title", className="card-title"),
                html.P(
                    "Some quick example text to build on the card title and "
                    "make up the bulk of the card's content.",
                    className="card-text",
                ),
                dbc.Button("Go somewhere", color="primary"),
            ]
        ),
    ],
    style={"width": "18rem","margin-bottom":"2rem"},
)


features_layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col([
                    # html.Center(html.H1("Features")),
                    dbc.DropdownMenu(
                            label="SETTING",
                            children=[
                                dbc.DropdownMenuItem("Item 1",href="/features"),
                                dbc.DropdownMenuItem("Item 2",href = "/featurenew"),
                            ],
                            style={"float":"right"}
                        ),

                ]),
                
                html.Br(),
                html.Hr(),
                dbc.Col(card),
                dbc.Col(card),
                dbc.Col(card),
            ]
        ),
    ]
)
