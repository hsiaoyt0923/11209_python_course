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

def update_data(conn:sqlite3.Connection):
    '''
    新增、更新資料
    '''
    
    sql = '''
        INSERT OR REPLACE INTO '全國各地PM2.5監測資料'(
        "測站名稱",
        "縣市名稱",
        "細懸浮微粒濃度",
        "資料建置日期",
        "測項單位"
        )
        VALUES(?,?,?,?,?)
        '''
    data = download_data()
    cursor = conn.cursor()

    for item in data['records']:
        cursor.execute(sql, item['site'], item['county'], item['pm25'], item['datacreationdate'], item['itemunit'])    
    conn.commit()



def main():
    conn = sqlite3.connect('PM2_5.db')
    update_data()


if __name__ == '__main__':
    main()