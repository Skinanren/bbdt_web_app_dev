# package imports
import dash
from dash import html, dcc, Output, Input, callback
import dash_bootstrap_components as dbc
from utils.images import logo_encoded
from utils.images import logo_encoded1
from utils.images import logo_encoded2
from utils.images import logo_encoded3
from utils.images import logo_encoded4

home_layout = dbc.Container(
    [
        dbc.Row(
            [
                html.Center(html.H1("WELCOME TO BODYBUILDING DIET APP"),
                            style={"color":"#ffffff","margin":"2rem auto","font-family":"Georgia, serif"}),
                html.Br(),
             
            ],
            style={"padding-top":"6rem"}
        ),
        
      
    ],
    
)
