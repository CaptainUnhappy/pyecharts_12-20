# -*- coding:utf-8 -*-
from flask import Flask, render_template, request, Response
import json
import dmPython

app = Flask(__name__)  # 定义flask


# 进入页面
@app.route('/dataset-simple')  # URL路径与下载的页面相对应（也可以不同）
@app.route('/')
def index():
    return render_template("dataset-simple1.html")  # 此时为气泡图页面


@app.route('/db', methods=['GET', 'POST'])
def my_test_db():
    connection = dmPython.connect(user='TEST', password='123456', server='192.168.95.128', port=5236)
    cur = connection.cursor()  # 游标（指针）cursor的方式操作数据
    sql = "select * from TB;"  # sql语句
    cur.execute(sql)  # execute(query, args):执行单条sql语句。
    see = cur.fetchall()  # 使结果全部可看
    li_see = list(see)  # 将元组转换为列表
    for i in range(len(see)):
        li_see[i] = list(li_see[i])  # 将每一项元组转换为列表替换
    li_see.insert(0
                  , ['年度GDP', '1999年(万亿) ', '2010年(万亿)', '2020年(万亿)']
                  )  # 在第一个元素前插入图例数据
    print(li_see)
    # 创建json数据
    jsonData = {'data1': li_see}
    # 将json格式转成str，因为如果直接将dict类型的数据写入json会发生报错，因此将数据写入时需要用到该函数。
    j = json.dumps(jsonData, ensure_ascii=False)
    cur.close()  # 关游标
    connection.close()  # 关链接
    # 渲染html模板
    return j


if __name__ == "__main__":
    """初始化,可设置参数debug=True，进入调试模式"""
    app.run(host='127.0.0.1', port=5000)
