# package imports
import dash
from dash import html, dcc, Output, Input, callback
import dash_bootstrap_components as dbc
from utils.images import logo_encoded


goal_date_calculation_accordion = html.Div(
    dbc.Accordion(
        [
            dbc.AccordionItem(
                [
                    html.P(
                        "Based on your type of Goal, your current bodyfat and expected bodyfat to Goal, and pace of about 1 pound of fat loss per week."
                    ),
                    # dbc.Button("Click here"),
                ],
                title="How is Time to Goal calculated?",
            ),
        ],
        start_collapsed=True,
    ),
)

insights_layout = dbc.Container(
    [
        html.Center(html.H1("Insights FAQ"),style={"color":"white"}),
        dbc.Row(
            [
                html.Br(),
                html.Hr(),
                dbc.Col(goal_date_calculation_accordion),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(goal_date_calculation_accordion),
            ]
        ),
    ]
)
