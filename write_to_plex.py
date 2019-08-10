from apis.plex import write_data
import argparse
import json
from tqdm import tqdm

import config

parser = argparse.ArgumentParser()
parser.add_argument('--json-path', required=True, default='movies.json',
    help='Path to JSON file containing movie data [default: movies.json]')


def get_movies_from_json(json_path):
    with open(json_path, "r") as f:
        return json.loads(f.read())


if __name__ == "__main__":
    args = parser.parse_args()
    print("✏ Writing update values from {} to Plex".format(args.json_path))
    for movie in tqdm(get_movies_from_json(args.json_path)):
        write_data(movie)

    print("✅ All done!")
