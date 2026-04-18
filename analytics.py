import matplotlib.pyplot as plt
from database import get_stats

def show_chart():
    data = get_stats()

    if not data:
        print("No data")
        return

    labels = [d[0] for d in data]
    counts = [d[1] for d in data]

    plt.figure()
    plt.bar(labels, counts)
    plt.title("Gesture Usage Analytics")
    plt.xticks(rotation=45)
    plt.show()