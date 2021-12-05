# Task 30
import statistics
import math
import json


# 1.
# or we could do from package_name import function
data = [11, 21, 11, 19, 46, 21, 19, 29, 21, 18, 3, 11, 11]
x = statistics.mean(data)
print(x)


y = 5
print(math.factorial(y))


my_dict = {"1": "Hello", "2": "World", "3": "I'm", "4": "Here!"}
json_string = json.dumps(my_dict)
print(type(json_string))

z = '{ "name":"John", "age":30, "city":"New York"}'
j = json.loads(z)
print(type(j))


# 2.

katerynakovalchuk@katerynakovalchuk-FVFC436JL414 ~ % pip install Jinja2==2.9.3
DEPRECATION: Configuring installation scheme with distutils config files is deprecated and will no longer work in the near future. If you are using a Homebrew or Linuxbrew Python, please see discussion at https://github.com/Homebrew/homebrew-core/issues/76621
Collecting Jinja2==2.9.3
  Downloading Jinja2-2.9.3-py2.py3-none-any.whl (274 kB)
     |████████████████████████████████| 274 kB 2.1 MB/s
Requirement already satisfied: MarkupSafe>=0.23 in /usr/local/lib/python3.9/site-packages (from Jinja2==2.9.3) (1.1.1)
Installing collected packages: Jinja2
DEPRECATION: Configuring installation scheme with distutils config files is deprecated and will no longer work in the near future. If you are using a Homebrew or Linuxbrew Python, please see discussion at https://github.com/Homebrew/homebrew-core/issues/76621
ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
flask 1.0 requires Jinja2>=2.10, but you have jinja2 2.9.3 which is incompatible.
Successfully installed Jinja2-2.9.3
katerynakovalchuk@katerynakovalchuk-FVFC436JL414 ~ % pip show jinja2
Name: Jinja2
Version: 2.9.3
Summary: A small but fast and easy to use stand-alone template engine written in pure python.
Home-page: http://jinja.pocoo.org/
Author: Armin Ronacher
Author-email: armin.ronacher@active-4.com
License: BSD
Location: /usr/local/lib/python3.9/site-packages
Requires: MarkupSafe
Required-by: Flask


# 3.
katerynakovalchuk@katerynakovalchuk-FVFC436JL414 ~ % python3 -m venv old_django
katerynakovalchuk@katerynakovalchuk-FVFC436JL414 ~ % source old_django/bin/activate
(old_django) katerynakovalchuk@katerynakovalchuk-FVFC436JL414 ~ % pip install Django==1.6
Collecting Django==1.6
  Downloading Django-1.6-py2.py3-none-any.whl (6.7 MB)
     |████████████████████████████████| 6.7 MB 2.0 MB/s
Installing collected packages: Django
Successfully installed Django-1.6
(old_django) katerynakovalchuk@katerynakovalchuk-FVFC436JL414 ~ % deactivate

katerynakovalchuk@katerynakovalchuk-FVFC436JL414 ~ % python3 -m venv new_django
katerynakovalchuk@katerynakovalchuk-FVFC436JL414 ~ % source new_django/bin/activate
(new_django) katerynakovalchuk@katerynakovalchuk-FVFC436JL414 ~ % pip install Django==2.0
Collecting Django==2.0
  Downloading Django-2.0-py3-none-any.whl (7.1 MB)
     |████████████████████████████████| 7.1 MB 1.1 MB/s
Collecting pytz
  Downloading pytz-2021.3-py2.py3-none-any.whl (503 kB)
     |████████████████████████████████| 503 kB 11.5 MB/s
Installing collected packages: pytz, Django
Successfully installed Django-2.0 pytz-2021.3
(new_django) katerynakovalchuk@katerynakovalchuk-FVFC436JL414 ~ % deactivate