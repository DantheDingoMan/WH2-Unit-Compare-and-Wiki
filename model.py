from os import name
from config import db, mm

class faction(db.Model):
    __tablename__ = "FACTION"

    factionname = db.Column(db.String, primary_key = True)
    description = db.Column(db.String)

    
    
class darkelves(db.Model):
    __tablename__ = "DARKELVES"
    faction = db.Column(db.String)
    unitname = db.Column(db.String, primary_key = True)
    cost = db.Column(db.Integer)
    unitscale = db.Column(db.String)
    unitsize = db.Column(db.Integer)
    health = db.Column(db.Integer)
    meleeattack = db.Column(db.Integer)
    meleedefense = db.Column(db.Integer)
    physicalresistance = db.Column(db.Integer)
    chargebonus = db.Column(db.Integer)
    leadership = db.Column(db.Integer)
    weapondamage = db.Column(db.Integer)
    armorpiercing = db.Column(db.Integer)
    meleeinterval = db.Column(db.Integer)
    bonusvslarge = db.Column(db.Integer)
    bonusvsinfantry = db.Column(db.Integer)
    armor = db.Column(db.Integer)
    
class highelves(db.Model):
    __tablename__ = "HIGHELVES"
    faction = db.Column(db.String)
    unitname = db.Column(db.String, primary_key = True)
    cost = db.Column(db.Integer)
    unitscale = db.Column(db.String)
    unitsize = db.Column(db.Integer)
    health = db.Column(db.Integer)
    meleeattack = db.Column(db.Integer)
    meleedefense = db.Column(db.Integer)
    physicalresistance = db.Column(db.Integer)
    chargebonus = db.Column(db.Integer)
    leadership = db.Column(db.Integer)
    weapondamage = db.Column(db.Integer)
    armorpiercing = db.Column(db.Integer)
    meleeinterval = db.Column(db.Integer)
    bonusvslarge = db.Column(db.Integer)
    bonusvsinfantry = db.Column(db.Integer)
    armor = db.Column(db.Integer)

class unitinformation(db.Model):
    __tablename__ = "UNITINFO"
    faction = db.Column(db.String)
    unitname = db.Column(db.String, primary_key = True)
    description = db.Column(db.String)

class unitinformationSchema(mm.SQLAlchemyAutoSchema):
    class Meta:
        model = unitinformation
        load_instance = True

class factionSchema(mm.SQLAlchemyAutoSchema):
    class Meta:
        model = faction
        load_instance = True


class highelvesSchema(mm.SQLAlchemyAutoSchema):
    class Meta:
        model = highelves
        load_instance = True


class darkelvesSchema(mm.SQLAlchemyAutoSchema):
    class Meta:
        model = darkelves
        load_instance = True
