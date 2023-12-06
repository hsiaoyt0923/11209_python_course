from dash import Dash, html,dash_table
import pandas as pd
import dash_bootstrap_components as dbc
import datasource

dash2 = Dash(requests_pathname_prefix="/dash/app2/",external_stylesheets=[dbc.themes.FLATLY])
dash2.title = "台北市youbike及時資料"

latest_data = datasource.lastest_datetime_data()
latest_df = pd.DataFrame(latest_data, columns=['站點名稱','更新時間','行政區','地址','總數','可借','可還'])
latest_df1 = latest_df.reset_index()
latest_df1['站點名稱'] = latest_df1['站點名稱'].map(lambda name:name[11:])

dash2.layout = html.Div(
    [
        dbc.Container([
            html.Div([
                html.Div([
                    html.H1("台北市youbike即時資料")
                ],className="col text-center")
            ],
            className="row",
            style={"paddingTop":'2rem'}),
            html.Div([
                html.Div([
                    dash_table.DataTable(
                        style_data={
                                'whiteSpace': 'normal',
                                'height': 'auto',
                            },
                        data=latest_df1.to_dict('records'),
                        columns=[{'id':column,'name':column} for column in latest_df1.columns],
                        page_size=20)
                ],
                className="col text-center")
            ],
            className="row",
            style={"paddingTop":'2rem'})
        ])
    ],
    className="container-lg"
    )