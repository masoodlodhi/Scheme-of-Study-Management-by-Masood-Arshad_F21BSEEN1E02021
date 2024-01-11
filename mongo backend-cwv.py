from pymongo import MongoClient

def create_study(study_name, study_description, start_date, end_date):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['study_db']
    collection = db['studies']

    study = {
        "name": study_name,
        "description": study_description,
        "start_date": start_date,
        "end_date": end_date
    }

    result = collection.insert_one(study)
    return result.inserted_id