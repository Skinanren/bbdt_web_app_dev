# package imports
import dash
from dash import html, dcc, callback, Input, Output

dash.register_page(
    __name__,
    path="/",
    redirect_from=["/home"],
    title="Bodybuilding Diet App",
    description="lose fat, gain muscle",
)

layout = html.Div(
    [
        html.H1("Bodybuiling Diet App"),
        html.Div(html.A("Checkout the not so complex page here.", href="/complex")),
        html.A("/page2", href="/page2"),
        dcc.RadioItems(
            id="radios",
            options=[{"label": i, "value": i} for i in ["Orange", "Blue", "Red"]],
            value="Orange",
        ),
        html.Div(id="content"),
    ]
)


@callback(Output("content", "children"), Input("radios", "value"))
def home_radios(value):
    return f"You have selected {value}"
