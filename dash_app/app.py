"""
This file is for housing the main dash application.
This is where we define the various css items to fetch as well as the layout of our application.
"""

import dash
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

from core_setup.main_layout import make_layout

# from core_setup.main_callbacks import add_main_layout_callbacks
from home.layouts import home_layout
from features.layouts import features_layout, card
from faq.layouts import faq_layout
from faq.summary import summary_layout
from faq.daily_diet import daily_diet_layout
from faq.general import general_layout
from faq.insights import insights_layout
from features.layouts_new import features_layout_new 
# from components.navbar import app_name, report_parts

print("hey you")

app = dash.Dash(
    __name__,
    # use_pages=True,  # turn on Dash pages
    external_stylesheets=[
        dbc.themes.SLATE,
        dbc.themes.BOOTSTRAP,
        dbc.icons.FONT_AWESOME,
        
    ],  # fetch the proper css items we want
    meta_tags=[
        {  # check if device is a mobile device. This is a must if you do any mobile styling
            "name": "viewport",
            "content": "width=device-width, initial-scale=1",
        }
    ],
    suppress_callback_exceptions=True,
    title="Bodybuilding Diet Mobile App",
    
)


app.layout = make_layout()  # set the layout to the serve_layout function


'''
@app.callback(Output("title-label", "children"), Input("url", "pathname"))
def find_label_title(pathname):
    try:
        label = app_name + " - " + report_parts[pathname]["label"]
    except KeyError:
        label = app_name
    return label


app.clientside_callback(
    """
    function(url_value) {
        document.title = url_value
    }
    """,
    Output("blank-output", "children"),
    Input("title-label", "children"),
)
'''


# app = add_main_layout_callbacks(app)
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    print("42", pathname)
    if pathname == "/":
        
        return home_layout
    if pathname == "/features":
        return features_layout
    if pathname == "/featurenew":
        return features_layout_new
    if pathname == "/summary":
        return summary_layout
    if pathname == "/daily_diet":
        return daily_diet_layout
    if pathname == "/general":
        return general_layout

    if pathname == "/insights":
        return insights_layout
    # if pathname == '/page2':
    #    return page2.layout
    else:  # if redirected to unknown link
        return "404 Page Error! Please choose a link"


# add callback for toggling the collapse on small screens
@app.callback(
    Output("navbar-collapse", "is_open"),
    Input("navbar-toggler", "n_clicks"),
    State("navbar-collapse", "is_open"),
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=int(3457), debug=True)
