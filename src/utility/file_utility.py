import pickle
import pandas as pd


class PickleObjectGenerator:

    def __init__(self, filename):
        self.filename = filename

    def __iter__(self):
        with open(self.filename, "rb") as f:
            while True:
                try:
                    file_object = pickle.load(f)
                    yield file_object
                except EOFError:
                    break


def file_lines_to_list(file_name):
    with open(file_name, 'r', encoding='utf-8') as f: # Set encoding to prevent errors
        result = list(f.readlines())
    return [sentence[:-1] for sentence in result] # [:-1] to remove newline; input file must end with empty line


# PANDAS file utility
def read_tsv_to_pd(file_tsv: str):
    cur_df = pd.read_csv(file_tsv, sep='\t')
    return cur_df
