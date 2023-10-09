import pandas as pd


def get_coordinate(file_name='coordinate.csv'):
    # Read the csv file
    df = pd.read_csv(file_name).values.tolist()
    # print("coordinates size: ", len(df))
    return df


def project_coordinates(coordinates, scale):

    projected_coordinates = []

    for coord in coordinates:
        new_x = int(coord[0] * scale)
        new_y = int(coord[1] * scale)
        projected_coordinates.append((new_x, new_y))

    return projected_coordinates