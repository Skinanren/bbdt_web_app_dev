# package imports
import dash
from dash import html, dcc, Output, Input, callback
import dash_bootstrap_components as dbc
from utils.images import logo_encoded


# dash.register_page(__name__)

card = dbc.Card(
    [
        # dbc.CardImg(src="/static/images/placeholder286x180.png", top=True),
        dbc.CardImg(
            src=logo_encoded,
            top=True,
            style={"opacity": 0.3},  # lower the number, the darker
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
    style={"width": "18rem"},
)


faq_layout = dbc.Container(
    [
        dbc.Row(
            [
                html.Center(html.H1("FAQ")),
                html.Br(),
                html.Hr(),
                dbc.Col(
                    [
                        html.P("This is column 1."),
                        dbc.Button("Test Button", color="primary"),
                    ]
                ),
                dbc.Col(
                    [
                        html.P("This is column 2."),
                        html.P(
                            "You can add many cool components using the bootstrap dash components library."
                        ),
                    ]
                ),
            ]
        )
    ]
)
