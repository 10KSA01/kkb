import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        dcc.Tabs(
            id="tabs",
            value="tab-1",
            children=[
                dcc.Tab(label="Page 1", value="tab-1"),
                dcc.Tab(label="Page 2", value="tab-2"),
                dcc.Tab(label="Page 3", value="tab-3"),
                dcc.Tab(label="Page 4", value="tab-4"),
                dcc.Tab(label="Page 5", value="tab-5"),
                dcc.Tab(label="Page 6", value="tab-6")
            ]
        ),
        html.Div(id="content")
    ]
)

@app.callback(
    Output("content", "children"),
    [Input("tabs", "value")]
)
def render_content(tab):
    if tab == "tab-1":
        return html.H1("Page 1")
    elif tab == "tab-2":
        return html.H1("Page 2")
    elif tab == "tab-3":
        return html.H1("Page 3")
    elif tab == "tab-4":
        return html.H1("Page 4")
    elif tab == "tab-5":
        return html.H1("Page 5")
    elif tab == "tab-6":
        return html.H1("Page 6")

if __name__ == "__main__":
    app.run_server(debug=True)


