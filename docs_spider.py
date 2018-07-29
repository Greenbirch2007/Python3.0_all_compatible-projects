
import requests
import re
import pymysql
from multiprocessing import Pool
import pymongo
# 发生异常的处理


def get_one_page(url):
    repseonse = requests.get(url)
    if repseonse.status_code == 200:
        return repseonse.text
    else:
        return None

# 存储到mysql中的解析方式
# def parse_one_page(html):
#     patt = re.compile('<span class="package-snippet__name">(.*?)</span>' +
#                       '.*?<p class="package-snippet__description">(.*?)</p>',re.S)
#     items = re.findall(patt,html)
#     content =[]
#     for item in items:
#         content.append(item)
#     return content

# mysql插入数据终于搞定了！
# def insertDB(content):
#     connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='python3_packages',
#                                  charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
#     cursor = connection.cursor()
#     try:
#
#         cursor.executemany("insert into docs (Da,Des) values (%s,%s)", content)
#         connection.commit()
#     except Exception:    # 把异常给放过去了
#         pass
#
#     connection.close()
#


# 存储到mongoDB中的解析方式
def parse_one_page(html):
    patt = re.compile('<span class="package-snippet__name">(.*?)</span>' +
                      '.*?<p class="package-snippet__description">(.*?)</p>',re.S)
    items = re.findall(patt,html)
    for item in items:
        yield {
            'name':item[0],
            'description':item[1]
        }


# 存入到MongoDB中 ，要改写成结构化数据,也就是Json格式～

def insertDB(content):
    client = pymongo.MongoClient('localhost', 27017)
    db = client.Python3_docs
    collection = db.themes
    collection.insert(content)





if __name__ == '__main__':
    pool = Pool(4)
    for num in range(1,501):
        url = 'https://pypi.org/search/?c=Programming+Language+%3A%3A+Python+%3A%3A+3&page=' + str(num)
        html = get_one_page(url)
        content = parse_one_page(html)
        insertDB(content)
        print(url)









# insert into docs (Da,Des)  values ('tensorflowonspark', 'Deep learning with TensorFlow on Apache Spark clusters'),('tensorflow-probability-gpu', 'Probabilistic modeling and statistical inference in TensorFlow');
# create table docs (
# id int  primary key auto_increment,
# Da varchar(255) ,
# Des varchar(255) );
#

