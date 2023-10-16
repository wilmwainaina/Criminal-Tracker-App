from models import Crime, Criminal, Victim, db
from app import db

def add_crime(name, description):
    crime = Crime(name=name, description=description)
    
    db.session.add(crime)
    return crime



def add_criminal(name):
    suspect = Criminal(name=name)
    db.session.add(suspect)
    return suspect

def add_victim(name):
    victim = Victim(name=name)
    db.session.add(victim)
    return victim

db.create_all()

crime1 = add_crime("Burglery", "Attempted Robbery of World Bank")


crime2 = add_crime("Violence", "Road rage with guns and knives")

crime3 = add_crime("Arson", "Setting shops and marts on fire for attempted robbery")

crime4 = add_crime("Fraud", "Deceiving of institutes and companies for money ")




crime5 = add_crime("Homicide", "Murder of 3 or more people in a club ")



suspect1 = add_suspect("Mickey Williams")


victim1 = add_victim("Adam Kelly")

suspect1.crimes.append(crime1)


victim1.crimes.append(crime1)

db.session.commit()
