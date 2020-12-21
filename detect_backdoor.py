"""
Detect Backdoor attacks
"""

import tensorflow as tf
import argparse as ap
from pathlib import Path
import keras
#rom eval import data_loader, data_preprocess
from fine_pruning import data_preprocess_and_load
import os
import numpy as np
from matplotlib import pyplot as plt
import copy

def build_parser():
    parser = ap.ArgumentParser()
    parser.add_argument('--orig', '-og', help='Path to original (backdoored) model', required=True)
    parser.add_argument('--pruned', '-pr', help='Path to Pruned model. Generate a pruned model using fine_prune.py', required=True)
    parser.add_argument('--dset', '-ds', help='Path to dataset', required=True)
    parser.add_argument('--outpath', '-o', help='File to store output labels', default='output.txt')
    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()
    args.outpath = Path(args.outpath).resolve()
    if not args.outpath.parent.exists():
        os.makedirs(args.outpath.parent)
    
    orig_model = keras.models.load_model(args.orig)
    rep_model = keras.models.load_model(args.pruned)

    test_x, test_y = data_preprocess_and_load(args.dset)
    num_labels = np.unique(test_y)
    bd_label = num_labels+1
    print('Predicting ...')
    orig_preds = orig_model.predict(test_x)
    rep_preds= rep_model.predict(test_x)

    check = (orig_preds == rep_preds)
    final_preds = copy.deep_copy(orig_preds)
    final_preds[check==False] = bd_label
    np.save('results.npy', final_preds)

