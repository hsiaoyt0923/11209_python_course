SELECT 站點名稱, 行政區, 地址, 總車輛數, 可借, 可還, MAX(更新時間) 
FROM 台北市youbike
GROUP BY 站點名稱


