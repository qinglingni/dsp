# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

Both lists and tuples are ordered collections of values. Of course, the Python sytax is different as well. You use [] for list and () for tuples. The difference between the two are: 1. tuples are immutable, meaning you cannot change tupple, for example, you cannot replace element in tuples. Lists are mutable. 2. Tuples have structure, while lists have order. Tuples can be used as keys in dictionaries, because you cannot change the keys

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

Sets are a list of unique items and they are not ordered.The performance will be much better finding and element in lists because they are ordered.

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

Lambda is a rewrite of an function to a single line. Example: sorted(student_objects, key=lambda student: student.age)
---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

List comprehension is basically a for loop. 

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

937 days
"""
from datetime import datetime

date_start ='01-02-2013'
date_stop = '07-28-2015'

date1 = datetime.strptime(date_stop,'%m-%d-%Y')
date2 = datetime.strptime(date_start,'%m-%d-%Y')

delta = date1-date2
print (delta)
"""
b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```
513 days """change the date format to without dash"""

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

7850 days """change the format of month to %b"""

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Write a script as indicated (using the football data) in [q8_parsing.py](python/q8_parsing.py)





