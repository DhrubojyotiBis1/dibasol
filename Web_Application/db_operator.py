from Web_Application import db


def insert(entry):
    db.session.add(entry)
    return commit()

def remove(entry):
    db.session.delete(entry)
    return commit()

def commit():
    try:
        db.session.commit()
    except:
        return 503 
    return 200