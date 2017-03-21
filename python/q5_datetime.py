# Hint:  use Google to find python function

####a) 
"""date_start = '01-02-2013'  
date_stop = '07-28-2015'   

####b)  
date_start = '12312013'  
date_stop = '05282015'  

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  """

date1 = datetime.strptime(date_stop,'%d-%b-%Y')
date2 = datetime.strptime(date_start,'%d-%b-%Y')

delta = date1-date2
print (delta)
