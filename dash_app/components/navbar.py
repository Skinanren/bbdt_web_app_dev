# import dash_mantine_components as dmc
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from utils.images import logo_encoded

navbar = dbc.Navbar(
    dbc.Container(

        [
            html.A(
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=logo_encoded, height="30px")),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="/",
                style={"textDecoration": "none"},
            ),
            dbc.NavItem(
                dbc.NavbarBrand(
                    "BODYBUILDING DIET APP",
                    style={"color": "#0879c9",
                           "font-size":"calc(0.5em + 2vw)",
                           "font-family":"fantasy",
                           "padding":".75rem .1rem calc(24px - .75rem)"},
                    href="/",
                )
            ),
            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
            dbc.Collapse(
                dbc.Nav(
                    [
                        
                            dbc.NavLink(
                                children="FEATURES",
                                id="features_link",
                                style={"color": "#ffffff",
                                       "padding-bottom":"0.2rem",
                                       "padding-top":"1.1rem",
                                       "border-right":"none",
                                       "border-left":"none",
                                       "font-family":"Sasita, serif"
                                       },
                                href="/features",
                            ),
                        
                            dbc.NavLink(
                                children="DOWNLOAD",
                                id="download_link",
                                style={"color": "#ffffff",
                                       "padding-bottom":"0.2rem",
                                       "padding-top":"1.1rem",
                                       "border-right":"none",
                                       "border-left":"none",
                                       "font-family":"Sasita, serif"
                                       },
                                href="/download",
                            ),
                       
                            dbc.NavLink(
                                children="TESTIMONIALS",
                                id="testimonials_link",
                                style={"color": "#ffffff",
                                       "padding-bottom":"0.2rem",
                                       "padding-top":"1.1rem",
                                       "border-right":"none",
                                       "border-left":"none",
                                       "font-family":"Sasita, serif"
                                       },
                                href="/testimonials",
                            ),
                       
                            dbc.DropdownMenu(
                                children=[
                                    dbc.DropdownMenuItem(
                                        "Summary",
                                        href="/summary",
                                        
                                    ),
                                    dbc.DropdownMenuItem(
                                        "Daily Diet",
                                        href="/daily_diet",
                                       
                                    ),
                                    dbc.DropdownMenuItem(
                                        "Macros",
                                        href="/macros",
                                      
                                    ),
                                    dbc.DropdownMenuItem(
                                        "Insights",
                                        href="/insights",
                                    
                                    ),
                                    dbc.DropdownMenuItem(
                                        "General Calculations",
                                        href="/general",
                                     
                                    ),
                                ],
                                nav=True,
                                in_navbar=True,
                                label="FAQ",
                                toggle_style={"color": "#ffffff",
                                              "padding-bottom":"0.2rem",
                                              "padding-top":"1.1rem",
                                              "border-right":"none",
                                              "border-left":"none",
                                              "font-family":"Sasita, serif"
                                              },
                              
                            )
                        
                    ]
                ),
                id="navbar-collapse",
                navbar=True,
            ),
        ],
        className="p-2"
    ),
    color="dark",
    dark=True,
)


"""

# https://dash-building-blocks.com/navbars

report_parts = {
    "/features": {
        "label": "Features",
    },
    "/download": {
        "label": "Download",
    },
    "/testimonials": {
        "label": "Testimonials",
    },
    "/summary": {
        "navbar_menu": "FAQ",
        "navbar_submenu": "App Screens",
        "label": "Summary",
    },
    "/daily_diet": {
        "navbar_menu": "FAQ",
        "navbar_submenu": "App Screens",
        "label": "Daily Diet",
    },
    "/macros": {
        "navbar_menu": "FAQ",
        "navbar_submenu": "App Screens",
        "label": "Macros",
    },
    "/insights": {
        "navbar_menu": "FAQ",
        "navbar_submenu": "App Screens",
        "label": "Insights",
    },
    "/calculations": {
        "navbar_menu": "FAQ",
        "navbar_submenu": "General Questions",
        "label": "Calculations",
    },
}


def unique_list(i_list):
    # initialize a null list
    u_list = []

    # traverse for all elements
    for x in i_list:
        # check if exists in unique_list or not
        if x not in u_list:
            u_list.append(x)
    return u_list


class Navbar:
    def __init__(
        self,
        i_report_parts,
        i_icons,
        i_report_name,
        i_report_logo,
        i_report_bug=None,
    ):
        self.i_report_parts = i_report_parts
        standalone_links = []
        for x in i_report_parts:
            try:
                i_report_parts[x]["navbar_menu"]
            except KeyError:
                standalone_links.append(x)
        self.standalone_links = standalone_links

        nav_tree = {}
        for x in unique_list(
            i_report_parts[x]["navbar_menu"]
            for x in i_report_parts
            if x not in standalone_links
        ):
            submenus = []
            for rep in i_report_parts:
                try:
                    if i_report_parts[rep]["navbar_menu"] == x:
                        try:
                            submenus.append(i_report_parts[rep]["navbar_submenu"])
                        except KeyError:
                            submenus.append("not_defined")
                            self.i_report_parts[rep]["navbar_submenu"] = "not_defined"
                except KeyError:
                    pass
            nav_tree[x] = unique_list(submenus)
        self.nav_tree = nav_tree
        self.i_icons = i_icons
        self.i_report_name = i_report_name
        self.i_report_logo = i_report_logo
        self.i_report_bug = i_report_bug

    def create_menu_target(self, name, href=None):
        try:
            if self.i_icons[name]:
                out = dmc.NavLink(
                    label=name,
                    href=href,
                    icon=DashIconify(icon=self.i_icons[name], width=17, color="grey"),
                    style={"padding": "7px", "width": "auto"},
                    styles={
                        "icon": {"margin-right": "3px"},
                        "label": {
                            "color": "grey",
                            "font-weight": "500",
                            "font-size": "16px",
                        },
                    },
                )
        except KeyError:
            out = dmc.NavLink(
                label=name,
                href=href,
                style={"padding": "7px", "width": "auto"},
                styles={
                    "icon": {"margin-right": "3px"},
                    "label": {
                        "color": "grey",
                        "font-weight": "500",
                        "font-size": "16px",
                    },
                },
            )
        return out

    def create_menu_item(self, name, href):
        try:
            if self.i_icons[name]:
                out = dmc.MenuItem(
                    name,
                    href=href,
                    icon=DashIconify(icon=self.i_icons[name]),
                )
        except KeyError:
            out = dmc.MenuItem(name, href=href)
        return out

    def create_links(self):
        links = []
        for menu in self.nav_tree:
            dropdown = []
            for submenu in self.nav_tree[menu]:
                if not ((submenu == "not_defined") & (len(self.nav_tree[menu]) == 1)):
                    try:
                        if self.i_icons[submenu]:
                            dropdown.append(
                                dmc.MenuLabel(
                                    dmc.Group(
                                        [
                                            DashIconify(
                                                icon=self.i_icons[submenu],
                                                width=13,
                                                color="grey",
                                            ),
                                            dmc.Text(
                                                "Other"
                                                if submenu == "not_defined"
                                                else submenu
                                            ),
                                        ],
                                        spacing=2,
                                    )
                                )
                            )
                    except KeyError:
                        dropdown.append(
                            dmc.MenuLabel(
                                "Other" if submenu == "not_defined" else submenu
                            )
                        )
                dropdown.extend(
                    [
                        self.create_menu_item(
                            name=self.i_report_parts[rep]["label"], href=rep
                        )
                        for rep in [
                            x
                            for x in self.i_report_parts
                            if x not in self.standalone_links
                        ]
                        if (
                            (self.i_report_parts[rep]["navbar_menu"] == menu)
                            & (self.i_report_parts[rep]["navbar_submenu"] == submenu)
                        )
                    ]
                )
            links.append(
                dmc.Menu(
                    [
                        dmc.MenuTarget(self.create_menu_target(menu)),
                        dmc.MenuDropdown(dropdown),
                    ],
                    trigger="hover",
                    offset=0,
                    transition="scale",
                    transitionDuration=150,
                )
            )
        for single in self.standalone_links:
            links.append(
                self.create_menu_target(
                    name=self.i_report_parts[single]["label"], href=single
                )
            )
        return dmc.Group(links, spacing=5)

    def create_navbar(self):
        if self.i_report_bug is not None:
            bug_report = dcc.Link(
                dmc.Tooltip(
                    dmc.ActionIcon(
                        DashIconify(
                            icon="material-symbols:bug-report-outline",
                            width=25,
                        ),
                        n_clicks=0,
                    ),
                    label="Report Issue",
                    withArrow=True,
                    arrowSize=3,
                    openDelay=500,
                    position="bottom",
                    transition="scale",
                    transitionDuration=150,
                ),
                href=self.i_report_bug,
                target="_blank",
            )
        else:
            bug_report = html.Div()
        return dmc.Header(
            height=40,
            children=[
                dmc.Grid(
                    [
                        dmc.Col(
                            [
                                dmc.Group(
                                    [
                                        dcc.Link(
                                            dmc.Avatar(
                                                DashIconify(
                                                    icon=self.i_report_logo, height=35
                                                ),
                                                radius="sm",
                                                size=30,
                                                styles={
                                                    "placeholder": {
                                                        "background-color": "#fee600"
                                                    }
                                                },
                                            ),
                                            href="/",
                                        ),
                                        dmc.Anchor(
                                            self.i_report_name,
                                            size=24,
                                            style={
                                                "margin": "0px",
                                                "padding": "0px",
                                                "font-weight": "500",
                                                "color": "black",
                                            },
                                            href="/",
                                            underline=False,
                                        ),
                                    ],
                                    spacing=5,
                                    style={"margin-left": "2vh"},
                                )
                            ],
                            style={"margin": "0px", "padding": "0px"},
                            span="content",
                        ),
                        dmc.Col([], span=1),
                        dmc.Col(
                            [self.create_links()],
                            span="content",
                            style={"margin": "0px", "padding": "0px"},
                        ),
                        dmc.Col(
                            [
                                dmc.Grid(
                                    [
                                        dmc.Col(
                                            [dmc.Group([bug_report])],
                                            span="content",
                                            style={
                                                "padding": "0px",
                                                "margin-right": "2vh",
                                            },
                                        )
                                    ],
                                    justify="flex-end",
                                )
                            ],
                            span="auto",
                        ),
                    ],
                    align="center",
                    style={"margin": "0px", "padding": "0px"},
                    columns=24,
                )
            ],
            style={"margin-bottom": "3px"},
        )


icons = {
    "Dashboards": "ps:dashboard",
    "Analytical Reports": "mdi:bar-chart",
    "Overviews": "mdi:bar-chart",
}

app_name = "Bodybuilding Diet App"
app_logo = "ph:chart-line-light"

navbar = Navbar(
    i_report_parts=report_parts,
    i_icons=icons,
    i_report_name=app_name,
    i_report_logo=app_logo,
    i_report_bug="https://developer.apple.com/bug-reporting/",
).create_navbar()
"""
