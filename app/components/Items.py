# import dash_bootstrap_components as dbc
# import platform
# from dash import Input, Output, State, html, callback

# placeholder_path = ""
# if platform.system() == 'Windows':
#     placeholder_path = "/assets/images/placeholder.png"  # Note the leading '/'
# else:
#     placeholder_path = "/assets/images/placeholder.png"

# modal = ""
# def get_modal():
#     return modal
 
# def set_modal(newModal):
#     modal = newModal
    
# def example_shop_item(item, cost):
#     card = dbc.Card(
#         [
#             dbc.CardImg(src=placeholder_path, top=True),
#             dbc.CardBody(
#                 [
#                     html.H4(item, className="card-title"),
#                     dbc.Button(str("Buy for "+ cost), id="open", n_clicks=0, color="primary", className="mx-auto d-block"),
#                     dbc.Modal(
#                         [
#                             dbc.ModalHeader(dbc.ModalTitle("Are you sure")),
#                             dbc.ModalBody(str("This cost " + cost)),
#                             dbc.ModalFooter(
#                                 dbc.Button(
#                                     "Pay Now", color="success", id="close", className="ms-auto", n_clicks=0
#                                 )
#                             ),
#                         ],
#                         set_modal("modal"+item),
#                         id=get_modal(),
#                         is_open=False,
#                     ),
#                 ]
#             ),
#         ],
#         className="d-grid mx-auto"
#     )
    
#     return card

# @callback(
#     Output(get_modal(), "is_open"),
#     [Input("open", "n_clicks"), Input("close", "n_clicks")],
#     [State(get_modal(), "is_open")],
#     prevent_initial_call=True  # Prevent callback from firing on page load
# )
# def toggle_modal(n1, n2, is_open):
#     if n1 or n2:
#         return not is_open
#     return is_open

from dash import Input, Output, State, html, callback
import dash_bootstrap_components as dbc
import platform

placeholder_path = ""
if platform.system() == 'Windows':
    placeholder_path = "/assets/images/placeholder.png"  # Note the leading '/'
else:
    placeholder_path = "/assets/images/placeholder.png"

def example_shop_item(item, cost, img):
    modal_id = f"modal_{item.replace(' ', '_').lower()}"
    card = dbc.Card(
        [
            dbc.CardImg(src=img, top=True),
            dbc.CardBody(
                [
                    html.H4(item, className="card-title"),
                    dbc.Button(str("Buy for "+ cost), id=f"open_{item.replace(' ', '_').lower()}", n_clicks=0, color="primary", className="mx-auto d-block"),
                    dbc.Modal(
                        [
                            dbc.ModalHeader(dbc.ModalTitle("Confirmation")),
                            dbc.ModalBody("Are you sure you want to buy this?"),
                            dbc.ModalFooter(
                                dbc.Button(
                                    "Pay Now", color="success", id=f"modal_close_{item.replace(' ', '_').lower()}", className="ms-auto", n_clicks=0
                                )
                            ),
                        ],
                        id=modal_id,
                        is_open=False,
                    ),
                ]
            ),
        ],
        className="d-grid mx-auto"
    )
    
    return card

items = ["Border 1", "Border 2", "Border 3", "Border 4", "Border 5", "Title 1", "Title 2", "Title 3", "Background 1", "Background 2", "Background 3", "10 points", "50 points", "100 points", "500 points", ]

@callback(
    [Output(f"modal_{item.replace(' ', '_').lower()}", "is_open") for item in items],
    [Input(f"open_{item.replace(' ', '_').lower()}", "n_clicks") for item in items],
    [Input(f"modal_close_{item.replace(' ', '_').lower()}", "n_clicks") for item in items],
    [State(f"modal_{item.replace(' ', '_').lower()}", "is_open") for item in items],
    prevent_initial_call=True
)
def toggle_modal(*args):
    n_clicks_indices = [i for i, n_clicks in enumerate(args) if n_clicks is not None]
    if n_clicks_indices:
        modal_index = n_clicks_indices[0]
        return [not is_open if i == modal_index else is_open for i, is_open in enumerate(args[-len(items):])]
    return [False] * len(items)
