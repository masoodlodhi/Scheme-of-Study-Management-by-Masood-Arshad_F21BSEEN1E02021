study_data = {"name": "Study Plan A", "description": "Description for Study Plan A", "start_date": "2022-01-01", "end_date": "2022-12-31"}

# Store the study data in the 'studies' collection
studies_collection = db["studies"]
studies_collection.insert_one(study_data)

# Retrieve the study data from the 'studies' collection
retrieved_study = studies_collection.find_one({"name": "Study Plan A"})
print(retrieved_study)