import csv

import numpy as np


def get_jester_data(path):
    data = []
    with open(path) as File:
        reader = csv.reader(File, delimiter=',')
        for row in reader:
            data_row = []
            for _item in row[1:]:
                if _item in {'99', ''} or float(
                        _item) < 7.0:  # Rates above or equal to 7 are considered positive i.e. 1. Otherwise 0.0.
                    data_row.append(0.0)
                else:
                    data_row.append(1.0)
            data.append(data_row)

    jester_data = np.asarray(data)
    filtered_data = []
    for _row in jester_data:
        if sum(_row) > 1:  # Keep only the rows where a user has rated at least one 1 joke
            filtered_data.append(_row.tolist())

    return np.asarray(filtered_data)
