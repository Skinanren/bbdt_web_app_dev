# notes
'''
This file is for creating a simple footer element.
This component will sit at the bottom of each page of the application.
'''

# package imports
from dash import html
import dash_bootstrap_components as dbc

footer = html.Footer(
    html.Div(
        dbc.Container(
            [
                 dbc.Row(
                     [
                        dbc.Col(html.Div("Copyright 2023 All right reserved"),
                                style = {"width":"30%",
                                         "float":"left",
                                         "font-weight":"bold",
                                         "color":"#a78d8d",
                                         "font-family":"fangsong"
                                         },
                                className="col-lg-2 col-sm-6"),
                        dbc.Col(html.Ul(
                                    [
                                        html.Li(html.A("Features",href="/features",
                                                style={"color":"brown",
                                                        "text-decoration":"none",
                                                        "padding":"0.3em 1.5em 0.3em 0",
                                                        "font-family":"auto"},),
                                                ),
                                        html.Li(html.A("Download",href="/download",
                                                style={"color":"brown",
                                                        "text-decoration":"none",
                                                        "padding":"0.3em 1.5em 0.3em 0",
                                                        "font-family":"auto"},),
                                                ),
                                        html.Li(html.A("Testimonials",href="/testimonials",
                                                style={"color":"brown",
                                                        "text-decoration":"none",
                                                        "padding":"0.3em 1.5em 0.3em 0",
                                                        "font-family":"auto"},),
                                                ),
                                        html.Li(html.A("Contact Us",href="/",
                                                style={"color":"brown",
                                                        "text-decoration":"none",
                                                        "padding":"0.3em 1.5em 0.3em 0",
                                                        "font-family":"auto"},),
                                                ),
                                        html.Li(html.A("Privacy Policy",href="/",
                                                style={"color":"brown",
                                                        "text-decoration":"none",
                                                        "padding":"0.3em 1.5em 0.3em 0",
                                                        "font-family":"auto"},),
                                                ),
                                        html.Li(html.A("Terms of Use",href="/",
                                                style={"color":"brown",
                                                        "text-decoration":"none",
                                                        "padding":"0.3em 1.5em 0.3em 0",
                                                        "font-family":"auto"},),
                                                ),
                                    ],
                            className="nav col-lg-10 col-sm-6",
                        )
    
                                       
                                )
                     ],
                     className="text-brown p-4 txt-green"
                 ),    
            ],
            
        ),

        style={"margin": "0","width":"100%","background-color":"rgb(16, 12, 12)"},
    )
    
)
