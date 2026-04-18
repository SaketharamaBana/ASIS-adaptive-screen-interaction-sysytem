import pickle, sqlite3
from sklearn.neighbors import KNeighborsClassifier

def retrain():
    conn = sqlite3.connect("gestures.db")
    c = conn.cursor()

    c.execute("SELECT gesture FROM logs")
    rows = c.fetchall()
    conn.close()

    if len(rows) < 10:
        return

    X = [[i] for i in range(len(rows))]
    y = [r[0] for r in rows]

    model = KNeighborsClassifier()
    model.fit(X, y)

    pickle.dump(model, open("model.pkl","wb"))
    print("Model auto-updated")