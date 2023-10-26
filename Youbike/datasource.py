import requests
import sqlite3

def __download_youbike_data() -> list[dict]:
    
    '''
    從https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json下載Youbike2.0的即時資料
    '''

    youbike_url = 'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'
    response = requests.get(youbike_url)
    response.raise_for_status()
    print('下載成功')
    return response.json()

def __create_table(conn:sqlite3.Connection):
    
    '''
    創建名為 '台北市Youbike2.0' 的資料表
    '''

    cursor = conn.cursor()
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS "台北市Youbike2.0" (
        "ID"	INTEGER,
        "站點名稱"	TEXT NOT NULL,
        "行政區"	TEXT NOT NULL,
        "站點地址"	TEXT NOT NULL,
        "更新時間"	TEXT NOT NULL,
        "總車輛數"	INTEGER NOT NULL,
        "可借數量"	INTEGER,
        "可還數量"	INTEGER,
        PRIMARY KEY("ID" AUTOINCREMENT)
        )
        ''')
    conn.commit()

def update_data_to_sqlite():
    data = __download_youbike_data()
    conn = sqlite3.connect('Youbike.db')
    __create_table(conn)
