from Case.面向对象案例.file_define import TextFileReader, JsonFileReader
from Case.面向对象案例.data_define import Record
from pymysql import Connect
from typing import List

text_file_reader = TextFileReader()
json_file_reader = JsonFileReader()

jan_data: List[Record] = text_file_reader.read_data(r'C:\Users\Luffy\Desktop\python_learning\Case\面向对象案例\2011年1'
                                                    r'月销售数据.txt')
feb_data: List[Record] = json_file_reader.read_data(r'C:\Users\Luffy\Desktop\python_learning\Case\面向对象案例\2011年2'
                                                    r'月销售数据JSON.txt')

# 数据合并
all_data: List[Record] = jan_data + feb_data

connect = Connect(
    host='localhost',
    port=3306,
    user='root',
    password='1027',
    autocommit=True
)
# 获取游标对象
cursor = connect.cursor()
# 选择heima数据库
connect.select_db('heima')
cursor.execute('''
    create table if not exists sales_order (
        id int auto_increment primary key,
        order_date date not null,
        order_id varchar(255) not null,
        money int not null,
        province varchar(10),
        unique key unique_order (order_id),
        index idx_date (order_date),
        index idx_province (province)
    )
''')

for record in all_data:
    # Use placeholders to safely insert values
    # 字符串类型的数据要加引号
    sql = f'''
        insert into  sales_order (order_date, order_id, money, province)
        values ('{record.date}', '{record.order_id}', {record.money}, '{record.province}')
    '''
    cursor.execute(sql)

connect.close()
