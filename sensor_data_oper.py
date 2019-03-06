# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 01:28:28 2018

@author: Chen Zhang
"""

import mysql.connector
from mysql.connector import Error, errorcode, pooling


class SensorData:

    def insert(self, t, temperature, humidity, pm25, pm10):
        group_user = 'group5'
        group_password = 'group5'
        try:
            cnx = mysql.connector.connect(user=group_user,
                                          password=group_password,
                                          host='188.131.150.79', database='group5', use_pure=True)
            cursor = cnx.cursor(prepared=True)
            id = cursor.rowcount + 1
            query = "insert into sensordata values(?, ?, ?, ?, ?, ?)"
            cursor.execute(query, (id, t, temperature, humidity, pm25, pm10))
            cnx.commit()
        except Error as err:
            print(err)
        else:
            cnx.close()

    def select(self):
        sensor_data_list = []
        group_user = 'group5'
        group_password = 'group5'
        try:
            cnx = mysql.connector.connect(user=group_user,
                                          password=group_password,
                                          host='188.131.150.79', database='group5', use_pure=True)
            cursor = cnx.cursor(prepared=True)
            query = "select t, temperature, humidity, pm25, pm10 from sensordata"
            cursor.execute(query)
            for row in cursor:
                tmp = list(row)
                sensor_data_list.append(tmp)
            return sensor_data_list
        except Error as err:
            print(err)
        else:
            cnx.close()
        return sensor_data_list

if __name__ == '__main__':
    connstr = 'mysql+mysqlconnector://group5:group5@188.131.150.79/group5?charset=utf8'
    sensor_table = SensorData()
    # sensor_table.insert('2018-12-27 12:20:10', 20, 0.12, 12, 12)
    data = sensor_table.select()

    for i in data:
        print(i)
        print()

