#This is my mad libs program

person = input("What is your name? ")
subject = input("What is your favorite subject? ")

def fix_name(person):
    return person

def make_madlib(person, subject):
    fixed_name = fix_name(person)
    madlib = print("Your name is %s and your favorite subject is %s" %(fixed_name, subject))
    return madlib


make_madlib(person, subject)