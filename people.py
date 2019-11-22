# This file was referenced by the 'swagger.yml' file and must contain the CRUD functions

from datetime import datetime

from flask import make_response, abort

# formatting the date
def get_timestamp():
  return datetime.now().strftime(("%Y-%m-%d  %H:%M:%S"))

# The DATA to serve with our API
PEOPLE = {
    
    "Musaku":{
        "fname": "Ben",
        "lname": "Musaku",
        "time":get_timestamp()
    },

    "Farrell":{
        "fname": "Doug",
        "lname": "Farrell",
        "time":get_timestamp()
    },


    "Jumbi":{
        "fname": "John",
        "lname": "Jjumbi",
        "time":get_timestamp()
    },

    
    "Lesner":{
        "fname": "Brock",
        "lname": "Lesner",
        "time":get_timestamp()
    }
}

# Create a function to handle the 'GET' HTTP Protocol
def read_all():
    """
    This function responds to a request for /api/people with
    the complete list of people.

    :return     sorted list of people
    """
    return [PEOPLE[key] for key in sorted(PEOPLE.keys())]

def read_one(lname):
    """
    This function responds to a request for /api/people{lname}
    with one matching person from the People list

    :param lname        last name of the person to find
    :return:            person matching last name
    """
    if lname in PEOPLE:
        person = PEOPLE.get(lname)
    else:
        abort(
            404, "Person with last name {lname} not found".format(lname=lname)
        )

    return person
