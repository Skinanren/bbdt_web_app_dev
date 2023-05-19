"""Define the layout of the application"""

from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from utils.images import logo_encoded
from utils.images import logo_encoded5

# from features.layouts import features_layout

from components.navbar import navbar
from components.footer import footer
"""
def make_layout():
    layout = html.Div(
        children=[
            navbar,
            html.Div(id="page-content"),
            dcc.Location(id="url", refresh=False),
            html.Div(id="title-label", hidden=True),
        ],
        style={"margin": "0px"},
    )
    return layout


"""


def make_layout():
    layout = html.Div(
        children=[
            dcc.Location(id="url", refresh=False),
            navbar,
            html.Div(id="page-content", children=[],style={
                                                           "min-height":"600px",
                                                           "background-image": "url(/assets/ground3.png)",
                                                           }),
            footer,
        ]
    )
    return layout
