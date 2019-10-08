import  pymysql


def inquire(i):
    '''
         函数功能：数据库查询信息
         参数描述：
         i 要调用的表名
    '''
    db = pymysql.connect("39.107.126.29", "root", "459012403", "cyb",charset="utf8")
    cursor = db.cursor()
    sql = "select * from %s" % (i)
    cursor.execute(sql)
    r = cursor.fetchall()
    db.close()
    return r


def add(i,j):
    '''
        函数功能：数据库添加信息
        参数描述：
        i 要调用的表名
        j 要添加的数据
    '''
    db = pymysql.connect("39.107.126.29", "root", "459012403", "cyb",charset="utf8")
    cursor = db.cursor()
    sql = "insert into %s VALUES %s"%(i,j)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()      #出错时回滚
    db.close()

def delete(i,j):
    '''
       函数功能：数据库删除信息
       参数描述：
       i 要调用的表名
       j 要删除的数据的id
    '''
    db = pymysql.connect("39.107.126.29", "root", "459012403", "cyb",charset="utf8")
    cursor = db.cursor()
    sql = "delete from %s where id = %s"%(i,j)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()      #出错时回滚
    db.close()


def revise(i,j,c,b):
    '''
      函数功能：数据库修改信息
      参数描述：
      i 要调用的表名
      j 要修改的字段
      c 要修改内容
      b 关键字值
    '''
    db = pymysql.connect("39.107.126.29", "root", "459012403", "cyb", charset="utf8")
    cursor = db.cursor()
    sql = "update %s set %s = %s where id = %s"%(i,j,c,b)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()
    # 关闭数据库连接
    db.close()
