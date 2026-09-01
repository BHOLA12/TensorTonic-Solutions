import numpy as np

def target_encoding(categories: list, targets: list) -> list:
    categories = np.array(categories)
    target = np.array(targets)

    unique = np.unique(categories)
    mapping = {}

    for cat in unique:
        mapping[cat] = target[categories == cat].mean()

    result = []

    for cat in categories:
        result.append(mapping[cat])

    return result