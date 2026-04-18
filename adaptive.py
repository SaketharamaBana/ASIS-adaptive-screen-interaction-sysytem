import json

def update_model(data, label):
    try:
        with open("adaptive_data.json", "r") as f:
            db = json.load(f)
    except:
        db = []

    db.append({"data": data, "label": label})

    with open("adaptive_data.json", "w") as f:
        json.dump(db, f)