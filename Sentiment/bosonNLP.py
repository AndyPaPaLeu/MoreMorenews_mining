

import requests
import time
from bosonnlp import BosonNLP
import pymysql
import random

# Open database connection
conn = pymysql.connect(host='192.168.35.168'
                       ,port=3306
                       ,user='andy'
                       ,passwd='andy'
                       ,db='news')
# prepare a cursor object using cursor() method
cursor = conn.cursor()
sql = "SELECT * FROM newtalk WHERE time LIKE '%2017%'"
#Sentiment not 'x'

try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()


   counter=0
   stop_contral=0
   resolt_list = []
   for row in results:
      time.sleep(random.randint(1,2))
      title = row[0]
      text = row[3]
      content = title+text
      print(f'title = {title}')
      if counter > 24:
            counter=0
            stop_contral += 1 #改成SQL updata
            print(stop_contral)

      token = ['KtOHze9c.34347.8GdWMiJRjCoi','YROpExWd.34345.-X4HFZOXDw1D','HDalUMrF.34350.e1zsznOmMyiX','BfqAZDEX.34351.nkUXSYLCCiqC','kaXBe5Y_.34352.UfILlmyxWkWB',
               'WwaBjRiI.34354.1upEzAZyEr6J','9VtwMcBG.34355.GuGRxvM2ljxP','bqaTUNuF.34357.8XRb2cMe6ZmF','6fJWGaB3.34359.0Q3ofBgkgch7','Mshj6ROM.34362.7lpXqlrc3WSP',
               'GHhLzuPM.34364.q0LjAlOd90mH','C7DKUyJt.34366.iIcRjetIpGsm','_Sm1poAy.34369.xTgEcK7_QQB5','-tu9o8X_.34371.UWsibP_xWIXb','Sk9pHqGr.34372.E7atgOZBbm3j',
               'x35CKIJf.34373.sEfA7p69Sm9T','tf3ornL4.34374.H74Yp4Rx9c6n','sVRIZcvC.34375.XkDW26mUPXu4','ZBAa5U-p.34376.f5quJmgi9MjV','h6sjAsGv.34378.txeNWPJgrcoU',
               'g2f4CmD9.34380.cMzFBC_W8BEQ','TYUre4Y6.34382.LoQo-__GTihX','N09l8vC-.34389.qfp3W7qRd0sb','kN6Rh57B.34391.xlKfN5EyWMJs','dC5oWMVw.34394.v_iZp5RNkvH_']

      nlp = BosonNLP(token[counter])

      semti_resolt = nlp.sentiment(content)
      tuple_result = (title,semti_resolt[0][0],semti_resolt[0][1])
      # print(tuple_result)
      resolt_list.append(tuple_result)     #title / posi / neg
      counter += 1
      print(counter)

   print(resolt_list)

except:
   # Rollback in case there is any error
   print ('unable to fetch data')