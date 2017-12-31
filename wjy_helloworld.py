#coding=utf8

import json
import os
import re
print '''
***************************************************************
*                DATABASE MANAGEMENT SYSTEM
*               
*
*                   Author: Wang Jiayi
*                           201501110223
***************************************************************
'''.decode('utf-8').encode('gbk')


in_db = ''
table_name=''
f_={}
i=0
Type = ["int", "char", "smallint","string"]
def show_db():
    print("All data：").decode('utf-8').encode('gbk')
    with open("../helloworld/wjy_json.json", "r") as f:
        f_load = json.load(f)
        print(f_load)

def show_help():
    print'''
    show database
    show table
    create table table_name (type size primarykey)  (splited by ',')
    alter table table_name add column_name type size
    alter table table_name drop column column_name 
    alter table table_name modify column column_name type 
    '''.decode('utf-8').encode('gbk')

def show_table(in_db, table_name):
    return

def creat_db(db_name):
    print 'New db is %s .' % db_name

def use_db(db_name):
    global in_db
    in_db = db_name
    db_name = '../helloworld/' + db_name + '.json'
    with open(db_name, "r") as db_:
        db = json.load(db_)
        print 'Change Successed!Now db is %s .' % db_name
        # print(db)
        return db

def creat_table(in_dbs, in_db, f_, table_name):
    in_dbs[in_db][table_name]=f_
    with open(in_db + '.json', "w") as f_load:
        json.dump(in_dbs, f_load,sort_keys=True, indent=4, separators=(',', ': '))

def begin(sql):
    sql_list = sql.lower().split(' ')
    leng = len(sql_list)
    global in_db,in_dbs,f_   # DB 'name  &  all DB
    f_ = {}

    # choose data
    if sql_list[0] == 'use':
        dbs = os.listdir("../helloworld")
        db_name = sql_list[1] + '.json'
        if db_name not in dbs:
            print("Error occured:Not found!")
        else:
            in_db = sql_list[1]
            in_dbs = use_db(in_db)
    elif sql_list[0] == 'show':
        if sql_list[1] == 'database':
            show_db()
        if sql_list[1] == 'table':
            if not in_db:
                print("Please chose db first!")
                return
            else:
                print(in_dbs[in_db])
        if sql_list[1] == 'help':
            show_help()
    elif sql_list[0] == 'create':
        #build new data
        if sql_list[1] == 'database':
            # print(sql_list[2])
            creat_db(sql_list[2])
            return
        elif sql_list[1] == 'table':
            if not in_db:
                print("Please chose DATABASE first!")
                return
            else:
                if leng>=3:
                    table_name = sql_list[2]
                    if table_name in in_dbs[in_db]:
                        print 'The table is already exist. Can not be repeated!'
                    else:
                        # m = re.findall('\(?(.*?)\)$', re.findall('create table ((.*?,)*(.*)+$)', sql)[0][0])[
                        #     0].split(',')
                        m = re.findall('\(?(.*?)\)$', re.findall('create table \w+ ((.*?,)*(.*)+$)',sql)[0][0])[0].split(',')
                        m_l = len(m)  # column qneue
                        # print(m_l)
                        # print(m[0])
                        # print(m[1])
                        i = 0
                        # cycle column
                        while i < m_l:
                            m_s = re.findall('\w+\s\w+\s\d*\s?\w*', m[i])[0].split(' ')
                            m_s_l = len(m_s)
                            #bug is exist, I can not deal with it 2017/6/15 20:30
                            # with open(in_db + '.json', "r") as f_load:
                            #     _f = json.load(f_load)
                            # print(_f[in_db])
                            try:
                                if m_s[0] in in_dbs[in_db][table_name]:
                                    print 'The property is already exist. Can not be repeated!'
                            except KeyError,e:
                                if m_s[1] not in Type:
                                    print("Type Error!")
                                    return
                                else:
                                    if m_s[2] < 0:
                                        print("Size Error!")
                                        return
                                    else:
                                        f_[m_s[0]] = {}
                                        f_[m_s[0]]['*Type*'] = m_s[1]
                                        f_[m_s[0]]['*Size*'] = m_s[2]
                                        f_[m_s[0]]['DATA'] = ''
                                        i = i + 1
                                        if m_s_l == 4 and m_s[3] == 'primarykey':
                                            f_[m_s[0]]['*KEY*'] = 'Yes'
                                        else:
                                            f_[m_s[0]]['*KEY*'] = 'NO'
                        creat_table(in_dbs, in_db, f_, table_name)
                        print("Table Created Successful!")
                        f_ = {}
                else:
                    print("Tne name of table can not be blank!")
                    return

                # columns = re.search('\[(.*?)\]', sql_list[4], re.S).group(1)
                # print(columns)
                # creat_table(sql_list[2], in_dbs, in_db, columns.split('+'))
        else:
            print("Formal Error!!!")

    elif sql_list[0] == 'alter':
        if sql_list[1] == 'table':
            if not in_db:
                print("Please chose DATABASE first!")
                return
            else:
                if leng >= 3:
                    table_name = sql_list[2]

                    if table_name not in in_dbs[in_db]:
                        print'The table is not exist. Can not be altered!'
                    else:
                        if sql_list[3] == 'add':
                            if leng >= 6 and leng <= 7:
                                column_name = sql_list[4]
                                with open(in_db + '.json', "r") as f_load:
                                    f_ = json.load(f_load)
                                if column_name not in f_[in_db][table_name]:
                                    f_[in_db][table_name][column_name] = {}
                                    f_[in_db][table_name][column_name]['*Type*'] = sql_list[5]
                                    f_[in_db][table_name][column_name]['*Size*'] = ''
                                    f_[in_db][table_name][column_name]['DATA'] = ''
                                    if leng == 7:
                                        f_[in_db][table_name][column_name]['*Size*'] = sql_list[6]
                                    else:
                                        pass
                                else:
                                    print'The column is already exist. Check it first!'
                            else:
                                print'Formal Error!ReTry!'
                                return
                            # in_dbs[in_db][table_name][column_name] = f_
                            with open(in_db + '.json', "w") as f_load:
                                json.dump(f_, f_load, sort_keys=True, indent=4, separators=(',', ': '))
                            print'Alter : Add Successful!'
                            f_ = {}

                        elif sql_list[3] == 'drop':
                            if leng == 6 :
                                column_name = sql_list[5]
                                with open(in_db + '.json', "r") as f_load:
                                    f_ = json.load(f_load)
                                if column_name in f_[in_db][table_name]:
                                    f_[in_db][table_name].pop(column_name)
                                else:
                                    print'The column is not exist. Check it first!'
                                    return
                            else:
                                print'Formal Error!ReTry!'
                                return
                            with open(in_db + '.json', "w") as f_load:
                                json.dump(f_, f_load, sort_keys=True, indent=4, separators=(',', ': '))
                            print'Alter : Drop Successful!'
                            f_ = {}

                            # alter table qwe alter column qwe char
                        elif sql_list[3] == 'modify':
                            if leng == 7:
                                column_name = sql_list[5]
                                with open(in_db + '.json', "r") as f_load:
                                    f_ = json.load(f_load)
                                if column_name not in f_[in_db][table_name]:
                                    print'The column is not exist. Add it first!'
                                else:
                                    f_[in_db][table_name][column_name]['*Type*'] = sql_list[6]
                            else:
                                print'Formal Error!ReTry!'
                                return
                            with open(in_db + '.json', "w") as f_load:
                                json.dump(f_, f_load, sort_keys=True, indent=4, separators=(',', ': '))
                            print'Alter: Modify Successful!'
                        else:
                            print 'Formal Error Occured!The operation you entered is not exist!'
                else:
                    print'Tne name of table can not be blank!!'
        else:
            print 'Formal Error!'

    elif sql_list[0] == 'adduser':
        adduser()
    elif sql_list[0] == 'insert':
        if not in_db:
            print("Please chose db first!")
            return
        else:
            columns = re.search('\[(.*?)\]', sql_list[4], re.S).group(1)
            insert(sql_list[2], in_dbs, in_db, columns.split('+'))

    elif sql_list[0] == 'update':
        if not in_db:
            print("Please chose db first!")
            return
        else:
            try:
                return
            except IndexError: return

    elif sql_list[0] == 'delete':
        if not in_db:
            print("Please chose db first!")
            return
        else:
            colums = re.findall('delete from (.*?) where (.*?)$',sql,re.S)
            column_name = re.search('^(.*?)=', columns[0][1], re.S).group(1)
            column = re.search('=\'(.*?)\'', columns[0][1], re.S).group(1)
            delete(columns[0][0], in_dbs, in_db, column_name, column)

    else:
        print("Formal Error Occured at the First Step!Have a Check!")
        return

def start():
    while True:
        sql = raw_input('MYSQL>>> ')
        if sql == 'quit':
            print 'quit success.'
            exit(0)
        else:
            begin(sql)
if __name__ == '__main__':
    start()

