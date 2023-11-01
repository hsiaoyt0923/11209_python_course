import requests
import sqlite3


__all__ = ['update_sqlite_data']

def __download_youbike_data() -> list[dict]:
    
    '''
    從https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json下載Youbike2.0的即時資料
    '''

    youbike_url = 'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'
    response = requests.get(youbike_url)
    response.raise_for_status()
    print('下載成功')
    return response.json()

def __create_table(conn:sqlite3.Connection) -> None:
    
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
        UNIQUE(站點名稱,更新時間) ON CONFLICT REPLACE
        )
        ''')
    conn.commit()
    cursor.close()

def __insert_data(conn, values) -> None:
    sql = '''
        REPLACE  INTO "台北市Youbike2.0" 
        (站點名稱,行政區,站點地址,更新時間,總車輛數,可借數量,可還數量)
        VALUES(?,?,?,?,?,?,?)        
        '''
    cursor = conn.cursor()
    cursor.execute(sql, values)
    conn.commit()
    cursor.close()


def update_sqlite_data() -> None:

    '''
    下載並更新資料庫
    '''

    data = __download_youbike_data()
    conn = sqlite3.connect('Youbike.db')
    __create_table(conn)
    for item in data:
        __insert_data(conn, [item['sna'], item['sarea'], item['ar'], item['mday'], item['tot'], item['sbi'], item['bemp']])
    conn.close()

def lastest_datetime_data():
    conn = sqlite3.connect("youbike.db")

    sql = '''
    SELECT 站點名稱, MAX(更新時間) AS 更新時間, 行政區,站點地址,總車輛數,可借數量,可還數量
    FROM '台北市Youbike2.0'
    GROUP BY 站點名稱
    '''

    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows
