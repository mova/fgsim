"""Console script for fgsim."""
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--tag", default="default", required=False)

subparsers = parser.add_subparsers(help="Available Commands", dest="command")

train_parser = subparsers.add_parser("train")
train_parser = subparsers.add_parser("generate")
geo_parser = subparsers.add_parser("geo")

args = parser.parse_args()
