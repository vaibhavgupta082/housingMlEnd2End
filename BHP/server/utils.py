import json
import pickle
import numpy as np

# global variables
__location = None
__model = None
__data_columns = None


def get_estimated_price(location, sqft, bhk, bath):
    load_saved_artifacts()
    try:
        loc_index = __location.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bhk
    x[2] = bath
    if loc_index >= 0:
        x[loc_index+3] = 1

    return round(__model.predict([x])[0], 2)


def get_location():
    load_saved_artifacts()
    return __location

# def get_model():
#     return __model
#
#
# def get_data_columns():
#     return __data_columns


def load_saved_artifacts():
    global __location
    global __model
    global __data_columns
    # Opening JSON file
    with open('artifacts/columns.json', 'r') as f:
        # Reading from json file
        __data_columns = json.load(f)['data_columns']
        __location = __data_columns[3:]

    with open('artifacts/bengaluru_house_prices_model.pickle', 'rb') as f:
        __model = pickle.load(f)


if __name__ == '__main__':
    load_saved_artifacts()
    # print(get_location())
    print(get_estimated_price('1st Block Jayanagar', 1000, 3, 3))
