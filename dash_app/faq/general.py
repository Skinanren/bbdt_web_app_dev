# package imports
import dash
from dash import html, dcc, Output, Input, callback
import dash_bootstrap_components as dbc
from utils.images import logo_encoded


bodyfat_override_accordion = html.Div(
    dbc.Accordion(
        [
            dbc.AccordionItem(
                [
                    html.P(
                        "Check to ensure that Bodyfat Override is not select in the Profile Tab under Settings."
                    ),
                    # dbc.Button("Click here"),
                ],
                title="My bodyfat does not change even when I change my weight?",
            ),
        ],
        start_collapsed=True,
    ),
)

another_accordion = html.Div(
    dbc.Accordion(
        [
            dbc.AccordionItem(
                [
                    html.P(
                        "Check to ensure that Bodyfat Override is not select in the Profile Tab under Settings."
                    ),
                    # dbc.Button("Click here"),
                ],
                title="My bodyfat does not change even when I change my weight?",
            ),
        ],
        start_collapsed=True,
    ),
)

general_layout = dbc.Container(
    [
        html.Center(html.H1("Gereral Calculations FAQ"),style={"color":"white"}),
        dbc.Row(
            [
                html.Br(),
                html.Hr(),
                dbc.Col(bodyfat_override_accordion),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(another_accordion),
            ]
        ),
    ]
)
