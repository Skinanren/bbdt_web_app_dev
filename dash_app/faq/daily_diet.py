# package imports
import dash
from dash import html, dcc, Output, Input, callback
import dash_bootstrap_components as dbc
from utils.images import logo_encoded


total_calories_accordion = html.Div(
    dbc.Accordion(
        [
            dbc.AccordionItem(
                [
                    html.P(
                        "The formulas of BBDT leverage carb cycling and as your macros change, the total calories will fluctuate"
                    ),
                    # dbc.Button("Click here"),
                ],
                title="Why is my Calories Goal different from one day to the next?",
            ),
        ],
        start_collapsed=True,
    ),
)
arrows_up_down_accordion = html.Div(
    dbc.Accordion(
        [
            dbc.AccordionItem(
                [
                    html.P(
                        "If arrows are up, that means you have tracked food for that meal.  If down, no food is tracked for that meal."
                    ),
                    # dbc.Button("Click here"),
                ],
                title="On DailyDiet screen, why are some arrows up and some down?",
            ),
        ],
        start_collapsed=True,
    ),
)
daily_diet_layout = dbc.Container(
    [
        html.Center(html.H1("Daily Diet FAQ"),style={"color":"white"}),
        dbc.Row(
            [
                html.Br(),
                html.Hr(),
                dbc.Col(total_calories_accordion),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(arrows_up_down_accordion),
            ]
        ),
    ]
)
