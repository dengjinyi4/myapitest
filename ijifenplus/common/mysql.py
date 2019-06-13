#coding:utf-8

import sys
import MySQLdb


def connectdb(host,database,user,password,port):
    try:
        global conn   
        conn=MySQLdb.connect(host=host,user=user,passwd=password,db=database,port=port)
    except Exception,e:
        print e
        print "Could not connect to MySQL server."
        sys.exit()
    global cursor
    conn.set_character_set('utf8')
    cursor=conn.cursor() 
    cursor.execute("SET NAMES utf8")  
    
    



def insertdb(sql):  
    try:
        cursor.execute("SET NAMES utf8") 
#         print sql
        cursor.execute(sql)
        conn.commit()
            
    except Exception,e:
        print e
        pass  
      

    
def deletedb(table):  
    try:
        cursor.execute("SET NAMES utf8") 
        sql="delete from %s"%(table)
#         print sql
        cursor.execute(sql)
        conn.commit()
                    
    except Exception,e:
        print e
        pass   



def deletedb1(sql):  
    try:
        cursor.execute("SET NAMES utf8") 
        cursor.execute(sql)
        conn.commit()
                    
    except Exception,e:
        print e
        pass 
    


def update(sql):  
    try:
        cursor.execute("SET NAMES utf8") 
#         print sql
        cursor.execute(sql)
        conn.commit()
            
    except Exception,e:
        print e
        pass 
    
    

def selete(sql):  
    try:
        cursor.execute("SET NAMES utf8") 
#         print sql
        cursor.execute(sql)
              
        rows = cursor.fetchall()
#        for row in rows:
#              print row
        return rows  
    except Exception,e:
        print e
        pass  





def closeconnect():
    cursor.close()
    conn.close()