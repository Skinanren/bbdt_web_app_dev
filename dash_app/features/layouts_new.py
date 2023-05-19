# package imports
import dash
from dash import html, dcc, Output, Input, callback
import dash_bootstrap_components as dbc
from utils.images import logo_encoded
from utils.images import logo_encoded1
from utils.images import logo_encoded2
from utils.images import logo_encoded3
from utils.images import logo_encoded4

features_layout_new = dbc.Container(
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

                dbc.Row([
                    
                    dbc.Col(
                            [
                                
                            dbc.Col([
                                html.H4("CMVG(Calories and Macros versus Goal)",
                                        style={"text-align":"right",
                                               "padding-top":"calc(0.5em + 2vw)",
                                               "font-size":"calc(0.5em + 1vw)",
                                               "font-family":"Roboto, serif",
                                               "color":"#ffffff"}),
                                html.P("Tracks, trends, and forecasts Macros in one view.",
                                       style={"text-align":"right",
                                              "padding-top":"calc(0.5em + 2vw)",
                                              "font-size":"calc(0.5em + 0.5vw)",
                                              "color":"#c76363"}),
                                html.H6("5 16 2019",
                                        style={"text-align":"right",
                                               "padding-top":"calc(0.5em + 2vw)",
                                               "font-size":"calc(0.5em + 0.5vw)",
                                               "padding-bottom":"10%",
                                               "color":"#ffffff"}),
                                
                                html.A(
                                        
                                            [
                                                html.I(className="fa fa-arrow-right"),
                                            ],
                                        
                                        href="/",
                                        style={"line-height":"38px",
                                               "text-align":"center",
                                               "textDecoration": "none",
                                               "float":"right",
                                               "border-radius":"50%",
                                               "background-color":"whitesmoke",
                                               "width":"38px","height":"38px",
                                               
                                               },
                                    ),
                                
                            ],
                                style={"width":"65%","float":"left","padding-right":"2rem"}

                            ),
                            
                            dbc.Col(
                                html.Img(src= logo_encoded1,style={"width":"100%","height":"auto","border-radius":"1rem"}),
                                style={"float":"right","width":"35%"}
                                
                            ),
                            ],
                            
                            className="col-lg-6 col-md-12 col-sm-12 col-12",
                            
                            
                            ),
                            
                    dbc.Col([
                            dbc.Col(html.Img(src= logo_encoded2,style={"max-width":"100%","height":"auto","border-radius":"1rem"}),
                                    style={"float":"left","width":"35%"}
                                    ),
                            dbc.Col([
                                html.H4("TDBD(Track Diet by Day)",
                                        style={"text-align":"left",
                                               "padding-top":"calc(0.5em + 3vw)",
                                               "font-size":"calc(0.5em + 1vw)",
                                               "font-family":"Roboto, serif",
                                               "color":"#ffffff"}),
                                html.P("Quickly add and see whats been tracked.",
                                       style={"text-align":"left",
                                              "padding-top":"calc(1em + 3vw)",
                                              "font-size":"calc(0.5em + 0.5vw)",
                                              "color":"#c76363"}),
                                html.H6("5 16 2019",
                                        style={"text-align":"left",
                                               "padding-top":"calc(0.5em + 3vw)",
                                               "font-size":"calc(0.5em + 0.5vw)",
                                               "padding-bottom":"10%",
                                               "color":"#ffffff"}),
                                
                                html.A(
                                        
                                            [
                                                html.I(className="fa fa-arrow-left"),
                                            ],
                                        
                                        href="/",
                                        style={"line-height":"38px",
                                               "text-align":"center",
                                               "textDecoration": "none",
                                               "float":"left",
                                               "border-radius":"50%",
                                               "background-color":"whitesmoke",
                                               "width":"38px","height":"38px",
                                               
                                               },
                                    ),
                                
                            ],
                                style={"width":"65%","float":"right","padding-left":"2rem"}
                                
                            ),
                                
                                ],
                            
                            className="col-lg-6 col-md-12 col-sm-12 col-12",
                            ),
                    dbc.Col(
                            [
                                
                            dbc.Col([
                                html.H4("AFL(advanced foods categorization)",
                                        style={"text-align":"right",
                                               "padding-top":"calc(0.5em + 2vw)",
                                               "font-size":"calc(0.5em + 1vw)",
                                               "font-family":"Roboto, serif",
                                               "color":"#ffffff"}),
                                html.P("Advanced foods categorization, included Bodybuiliding Diet recommended foods.",
                                       style={"text-align":"right",
                                              "padding-top":"calc(0.5em + 2vw)",
                                              "font-size":"calc(0.5em + 1vw)",
                                              "font-size":"calc(0.5em + 0.5vw)",
                                              "color":"#c76363"}),
                                html.H6("5 16 2019",
                                        style={"text-align":"right",
                                               "padding-top":"calc(1em + 2vw)",
                                               "padding-bottom":"10%",
                                               "color":"#ffffff"}),
                                
                                html.A(
                                        
                                            [
                                                html.I(className="fa fa-arrow-right"),
                                            ],
                                        
                                        href="/",
                                        style={"line-height":"38px",
                                               "text-align":"center",
                                               "textDecoration": "none",
                                               "float":"right",
                                               "border-radius":"50%",
                                               "background-color":"whitesmoke",
                                               "width":"38px","height":"38px",
                                               
                                               },
                                    ),
                                
                            ],
                                style={"width":"65%","float":"left","padding-right":"2rem"}
                                
                            ),
                            
                            dbc.Col(
                                html.Img(src= logo_encoded3,style={"width":"100%","height":"auto","border-radius":"1rem"}),
                                style={"float":"right","width":"35%","margin-top":"0.5rem"}
                                
                            ),
                            ],
                            
                            className="col-lg-6 col-md-12 col-sm-12 col-12",
                            
                            
                            ),
                    dbc.Col([
                            dbc.Col(html.Img(src= logo_encoded4,style={"max-width":"100%","height":"auto","border-radius":"1rem"}),
                                    style={"float":"left","width":"35%","margin-top":"0.5rem"}
                                    ),
                            dbc.Col([
                                html.H4("AAI(Advanced AI Insights)",
                                        style={"text-align":"left",
                                               "padding-top":"calc(1em + 2vw)",
                                               "font-size":"calc(0.5em + 1vw)",
                                               "font-family":"Roboto, serif",
                                               "color":"#ffffff"}),
                                html.P("Based on your progress and activity, generates Insights to help you make progress.",
                                       style={"text-align":"left",
                                              "padding-top":"calc(1em + 2vw)",
                                              "font-size":"calc(0.5em + 0.5vw)",
                                              "color":"#c76363"}),
                                html.H6("5 16 2019",
                                        style={"text-align":"left",
                                               "padding-top":"calc(1em + 2vw)",
                                               "font-size":"calc(0.5em + 0.5vw)",
                                               "padding-bottom":"10%",
                                               "color":"#ffffff"}),
                                
                                html.A(
                                        
                                            [
                                                html.I(className="fa fa-arrow-left"),
                                            ],
                                        
                                        href="/",
                                        style={"line-height":"38px",
                                               "text-align":"center",
                                               "textDecoration": "none",
                                               "float":"left",
                                               "border-radius":"50%",
                                               "background-color":"whitesmoke",
                                               "width":"38px","height":"38px",
                                        
                                               
                                               },
                                    ),
                                
                            ],
                                style={"width":"65%","float":"right","padding-left":"2rem"}
                                
                            ),
                                
                                ],
                            
                            className="col-lg-6 col-md-12 col-sm-12 col-12",
                            ),

                ]
    
                )
            ],
            style={"padding-bottom":"2rem"}
        ),
        
      
    ],
    
)
