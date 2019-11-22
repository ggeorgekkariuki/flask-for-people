# This file was referenced by the 'swagger.yml' file and must contain the CRUD functions

from datetime import datetime

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
