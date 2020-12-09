# CPSC 471 - Group 16

## Installation:
Please make sure you have Python3 and Pip3 Installed.
### To install dependencies:
    pip3 install -r requirements.txt
## Usage:
### To setup django instance:
    cd /CPSC471_G16
    python3 manage.py makemigrations && python3 manage.py migrate
    python3 manage.py runserver
    python3 manage.py addsuperuser <-- this is just in case

### To connect to root view, use URL:
    http://127.0.0.1:<port from console>/api/v1

### When sending ```PUT``` or ```PATCH``` requests; ***use the ```id``` field as the identifier/pk***; ***NOT any fields with the suffix*** ```_id```.


## License:
[MIT](https://choosealicense.com/licenses/mit/)