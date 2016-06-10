# -*- coding: utf-8 -*-

import win32com.client
import datetime as dt
import numpy as np
import time

eComCall = win32com.client.Dispatch("E3DataAccess.E3DataAccessManager.1")
print eComCall
eComCall.Server = "localhost"


#Teste

tagpath = 'bmsData.PythonValue.Value'


while True:
    Timestamp = dt.datetime.now()
    Quality = 192
    Value = int(np.random.random_integers(0,100,1))


    tagwrite = eComCall.WriteValue(tagpath,Timestamp, Quality, Value)

    tagread = eComCall.ReadValue(tagpath, Timestamp, Quality, Value)

    print tagread
    print tagwrite
    time.sleep(1)

