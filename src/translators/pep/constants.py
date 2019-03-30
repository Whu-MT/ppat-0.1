import os
import string

# All constants and Configurations should be listed in this file

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# CMU Origin Dictionary Path
CMU_DICT_PATH = os.path.join(BASE_DIR, 'dataset', 'cmudict-0.7b')
CMU_SYMBOLS_PATH = os.path.join(BASE_DIR, 'dataset', 'cmudict-0.7b.symbols')
ABBREV_CSV_PATH = os.path.join(BASE_DIR, 'dataset', 'abbreviations.csv')
QTY_ABBREV_CSV_PATH = os.path.join(BASE_DIR, 'dataset', 'quantity_abbreviations.csv')
# Output from pickle
ABBREV_DICT_PATH = os.path.join(BASE_DIR, 'output', 'bp-abbrev-dict.pkl')
QTY_ABBREV_DICT_PATH = os.path.join(BASE_DIR, 'output', 'bp-qty-abbrev-dict.pkl')
PHONETIC_DICT_PATH = os.path.join(BASE_DIR, 'output', 'bp-phonetic-dict.pkl')
PHONETIC_SYMBOLS_PATH = os.path.join(BASE_DIR, 'output', 'bp-phonetic-symbols.pkl')
# Model Savings
PREDICTION_MODEL_WEIGHTS_PATH = os.path.join(BASE_DIR, 'output', 'prediction_model_weights.hdf5')
# Utils
ALLOWED_SYMBOLS = [".", "-", "'"]
ALLOWED_CHARS = ALLOWED_SYMBOLS + list(string.ascii_uppercase)
START_PHONE_SYM = '\t'
END_PHONE_SYM = '\n'
MIN_CHAR_SEQ_LEN = 2
MAX_CHAR_SEQ_LEN = 20
MAX_PHONE_SEQ_LEN = 19
# Phone Sequences are padded with Start/End tokens
MAX_PADDED_PHONE_SEQ_LEN = MAX_PHONE_SEQ_LEN + 2

# Model Config