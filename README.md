# Calculator
Django web app for vision algorithm demo.

Tested under: <br/>
Python version: 3.8.3 <br/>
Django version: 3.0.7

---

**Usage:**

`git clone https://github.com/fullstacksuiit/calculator.git` <br/>
`cd calculator` <br/>

*[Optional]* <br/>
`virtualenv -p <python3_path> venv` <br/>
`source venv/bin/activate` <br/>
`pip install -r requirements.txt` <br/>

---

*[To start backend]* <br/>
`python manage.py runserver` <br/>

*[To run tests]* <br/>
`python manage.py test` <br/>

----

####Endpoints<br/>
`base_url = "localhost:8000/calculate"`

**Addition**
URL: base_url + '/addition'
Request Method: GET

**Subtraction**
URL: base_url + '/subtraction'
Request Method: GET
<br>

**Multiplication**
URL: base_url + '/multiplication'
Request Method: GET


**Division**
URL: base_url + '/division'
Request Method: GET


Parameters to all the above mentioned endpoints: `a, b`
The value to these parameters should be a numerical value(integer & float)

> These parameter keys are not needed to be strictly `a` & `b` and also there APIs accept more than two values, i.e there can also be a third parameter, eg - `c`

*Evaluate Expression (Bonus)*
URL: base_url + '/evaluate'
Request Method: GET

Parameters: key-`a`, value should be mathematical expression.
Eg - `a = 5+9-4`

> The key does not strictly need to be `a` and it can accept more expressions in the same format.
There can another parameter such as `b = 9-8+0*6`

---

Postman Collection: https://www.getpostman.com/collections/836562b1ce1105976df3

For any further information, please contact: `rahmantanshit@gmail.com`