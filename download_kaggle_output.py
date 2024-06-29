import os
from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()

# Replace 'revanthonteddu/treasury-bills-with-cmb' with your actual Kaggle username and kernel name
api.kernels_output_download('revanthonteddu/treasury-bills-with-cmb', path='./output')
