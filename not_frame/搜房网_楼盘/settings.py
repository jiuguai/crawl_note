USER_AGENT = [
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36",
    "Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50",
    "Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11",
    "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Maxthon2.0)",
    "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TencentTraveler4.0)",
    "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1)",
    "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TheWorld)",
    "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Trident/4.0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727;SE2.XMetaSr1.0)",
    "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;360SE)",
    ]


# 存储数据 数据类型

# mongoDB MySQL
DB_TYPE = 'mongoDB'

MYSQL_CON_INFO = dict(
        host="localhost",user="root",
        password="root",database="soufang",
        port=3306,
)

MSQL_INSET_STR = """
            INSERT INTO new_house_t(
            city ,province ,lp_name ,rooms ,area ,addr ,district ,sale_state ,house_type ,sale,origin_url
            ) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """

MONGO_CON = {"host":"127.0.0.1","port":27017}






