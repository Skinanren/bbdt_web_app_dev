# package imports
import dash
from dash import html, dcc, Output, Input, callback
import dash_bootstrap_components as dbc
from utils.images import logo_encoded


accordion = html.Div(
    dbc.Accordion(
        [
            dbc.AccordionItem(
                [
                    html.P(
                        "You can update last week as needed.  The Summary screen displays past seven days and next seven days.  You can still track foods before and after that week in the DailyDiet screen"
                    ),
                    dbc.Button("Click here"),
                ],
                title="Why can't I pick older weeks to change?",
            ),
            dbc.AccordionItem(
                [
                    html.P("This is the content of the second section"),
                    dbc.Button("Don't click me!", color="danger"),
                ],
                title="Item 2",
            ),
            dbc.AccordionItem(
                "This is the content of the third section",
                title="Item 3",
            ),
        ],
    )
)


summary_layout = dbc.Container(
    [
        dbc.Row(
            [
                html.Center(html.H1("Summary FAQ"),style={"color":"white"}),
                html.Br(),
                html.Hr(),
                dbc.Row(accordion),
            ]
        ),
    ]
)
