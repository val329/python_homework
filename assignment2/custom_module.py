secret = "shazam!"

def set_secret(new_secret):
   global secret
   secret = new_secret

def set_minutes(new_minutes1, new_minutes2):
    global minutes1, minutes2
    minutes1, minutes2 = new_minutes1, new_minutes2
 
def minutes_set_variable(var): 
    global minutes_set
    minutes_set = var

def minutes_list_variable(var): 
    global minutes_list
    minutes_list = var