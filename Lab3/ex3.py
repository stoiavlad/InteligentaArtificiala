import random

def normalize_data(data):
    min_val = min(data)
    max_val = max(data)

    normalized = []

    for x in data:
        val = (x - min_val) / (max_val - min_val)
        normalized.append(val)

    return normalized

random_data = [random.randint(1, 100) for _ in range(5)]
normalized_random = normalize_data(random_data)

print("\nDate:", random_data)
print("Date normalizate:", normalized_random)