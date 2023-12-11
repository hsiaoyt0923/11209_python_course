from dash import Dash, html,dash_table,Input,Output,callback
import pandas as pd
import dash_bootstrap_components as dbc
from . import datasource

dash2 = Dash(requests_pathname_prefix="/dash/app2/",external_stylesheets=[dbc.themes.BOOTSTRAP])
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
                ],
                    className="col text-center")
            ],
                className="row",
                style={"paddingTop":'2rem'}),
            html.Div([
                html.Div([
                    dbc.Label("站點名稱"),
                    dbc.Input(id='input_value',
                              placeholder="請輸入站點名稱",
                              type="text"),
                ],
                    className='col'),
                html.Div([
                    html.Button('確定',
                                id='submit-val',
                                className="btn btn-primary",
                                n_clicks=0)
                ],
                    className="col"),
                html.Div(children='輸出內容',
                         id='output-content',
                         className="col")
            ],
                className="row row-cols-auto align-items-end",
                style={"paddingTop":'0.5rem'}),
            html.Div([
                html.Div([
                    dash_table.DataTable(
                        id='main_table',
                        data=latest_df1.to_dict('records'),
                        columns=[{'id':column,'name':column} for column in latest_df1.columns],
                        page_size=20,
                        style_table={'height': '300px', 'overflowY': 'auto'},
                        fixed_rows={'headers': True},
                        style_cell_conditional=[
                                {   'if': {'column_id': 'index'},
                                 'width': '5%'
                                },
                                {   'if': {'column_id': '站點名稱'},
                                 'width': '25%'},
                                {   'if': {'column_id': '總數'},
                                 'width': '5%'},
                                {   'if': {'column_id': '可借'},
                                 'width': '5%'},
                                {   'if': {'column_id': '可還'},
                                 'width': '5%'},
                        ],
                        row_selectable="single",
                        selected_rows=[]
                    ),
                ],className="col text-center")
            ],
            className="row",
            style={"paddingTop":'0.5rem'}),
            html.Div([
                html.H5(className="col",id='showMessage')
                ],
                    className='row',
                    style={"paddingTop":'2rem'})
        ])
    ],
    className="container-lg"
    )

@callback(
        Output('output-content','children'),
        Input('submit-val','n_clicks'),
        Input('input_value','value')
)
def clickBtn(n_clicks:None | int,inputValue:str):
        if n_clicks != 0:
        #一定先檢查有沒有按button
            print(inputValue)

@callback(
    Output('showMessage','children'),
    Input('main_table','selected_rows')  
)
def selectedRow(selected_rows:list[int]):
    #取得一個站點,series
    if len(selected_rows) != 0:
        print("執行")
        oneSite = latest_df1.iloc[selected_rows]
        oneTable =  dash_table.DataTable(oneSite.to_dict('records'), [{"name": i, "id": i} for i in oneSite.columns])
        return oneTable
    return None