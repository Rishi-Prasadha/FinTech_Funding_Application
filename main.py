import fire
import questionary
import sys
from pathlib import Path
import pandas as pd


from utils.calculators import (
    avg,
    std
)


def run():
    zip = enter_zip()
    bath = get_bath()
    bed = get_bed()
