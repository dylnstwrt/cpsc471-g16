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
    python3 manage.py createsuperuser <-- this is just in case

### To connect to server:

Connect to the server using the URL as provided in the console when running.

### When sending ```PUT``` or ```PATCH``` requests; ***use the ```id``` field as the identifier/pk***; ***NOT any fields with the suffix*** ```_id```.

### To see Implementation Documentation, using superuser creds to login at:

    http://127.0.0.1:<port from console>/admin/doc/

## License:
[MIT](https://choosealicense.com/licenses/mit/)

## Creating and Updating Information:

The easiest way to make changes to the database is through the WebGUI. After running the server, you should see the URL in your console.
![Root List](https://i.imgur.com/x5v6E0u.png)

From that URL, you should see the root list for all models. Each link to a respective model will have a form to validate information.
At the bottom of the page you will find the form. To make a change to a single instance, use the respective "id" field as a path parameter in the URL
to see and edit the information for a single instance of a model.

![Instance View](https://i.imgur.com/rYxHkdA.png)

## Performing Transactions:

To perform a transaction:

- Create either a 'sale' or 'return'
- Create a 'basket' instance containing the 'item' you want to add to the transaction; and repeat for all items to be purchased
    ![Basket View](https://i.imgur.com/4eXx5MO.png)
    - For 'return' do not do this, since the original transaction will point to all items that will be returned
- Send a PUT request to the transaction; changing "Completed" to true.
![Complete Transaction](https://i.imgur.com/FzThE5V.png)
Following these steps should see updates to the 'financial' model/information, 'item', and 'transaction' model as soon as the completed parameter is equal to True.
![Updated Transaction](https://i.imgur.com/hIqzyIL.png)
## Postman API Documentation:

[Documentation is Here](https://documenter.getpostman.com/view/13510007/TVmV5ZSp)
