import requests
import psycopg2
import threading
import password as pw


# 須先建立password.py存放apikey，才能下載資料
# 即時資料網址:https://data.moenv.gov.tw/swagger/


def download_data() -> dict:
    '''
    下載資料
    '''

    pm25_url = f"https://data.moenv.gov.tw/api/v2/aqx_p_02?language=zh&api_key={apikey}"
    response = requests.get(pm25_url)
    response.raise_for_status()
    print('下載成功')
    return response.json()


def create_table(conn) -> None:
    '''
    創建資料表
    '''

    sql = '''
        CREATE TABLE IF NOT EXISTS "全國各地PM2.5監測資料"(
        "ID" SERIAL,
        "測站名稱" TEXT NOT NULL,
        "縣市名稱" TEXT NOT NULL,
        "細懸浮微粒濃度" INTEGER,
        "資料建置日期" TEXT,
        "測項單位" TEXT,
        PRIMARY KEY('ID'),
        UNIQUE(測站名稱,資料建置日期) 
        ON CONFLICT DO NOTHING
        )
        '''
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()


def insert_data(conn, values: list | tuple) -> None:
    '''
    新增資料
    '''

    sql = '''
        INSERT INTO '全國各地PM2.5監測資料'(
        "測站名稱",
        "縣市名稱",
        "細懸浮微粒濃度",
        "資料建置日期",
        "測項單位"
        )
        VALUES(%s,%s,%s,%s,%s)
        '''

    cursor = conn.cursor()
    cursor.execute(sql, values)
    conn.commit()


def update_data():
    '''
    下載並更新資料
    '''

    conn = psycopg2.connect(database=pw.DATABASE,
                            user=pw.USER,
                            password=pw.PASSWORD,
                            host=pw.HOST,
                            port=pw.PORT)
    create_table(conn)    
    try:    
        data = download_data()
    except:
        print('網路發生錯誤，請稍後再試')
    else:    
        for item in data['records']:
            insert_data(conn, (item['site'], item['county'], item['pm25'], item['datacreationdate'], item['itemunit']))
        timer = threading.Timer(10, update_data)
        timer.start()
        print('資料更新完畢')
        conn.close()


if __name__ == '__main__':
    update_data()
