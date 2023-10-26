import requests
import threading
import sqlite3
from password import apikey


def download_data() -> dict:
    '''
    下載資料
    '''
    
    pm25_url = f"https://data.moenv.gov.tw/api/v2/aqx_p_02?language=zh&api_key={apikey}"
    response = requests.get(pm25_url)
    response.raise_for_status()
    print('下載成功')
    return response.json()


def create_table(conn:sqlite3.Connection) -> None:
    '''
    創建資料表
    '''

    sql = '''
        CREATE TABLE IF NOT EXISTS "全國各地PM2.5監測資料"(
        "ID" INTEGER
        "測站名稱" TEXT NOT NULL
        "縣市名稱" TEXT NOT NULL
        "細懸浮微粒濃度" INTEGER
        "資料建置日期" TEXT
        "測項單位" TEXT
        PRIMARY KEY('ID' AUTOINCREMENT)
        UNIQUE(測站名稱,資料建置日期) ON CONFLICT REPLACE
        )
        '''
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()


def insert_data():
    '''
    插入資料
    '''
    pass

def update_data():
    '''
    更新資料
    '''
    pass


def main():
    data = download_data()
    conn = sqlite3.connect('PM2_5.db')


if __name__ == '__main__':
    main()