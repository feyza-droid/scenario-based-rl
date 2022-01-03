import os
import sys
import argparse

# to add the parent "agents" folder to sys path and import models
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from utils.db import DB
from utils import base_utils

#TODO: also add seeds for all random generators
parser = argparse.ArgumentParser(description='initialize parameters')
parser.add_argument('--evaluate', action="store_true", help='RL Model Evaluate(True) Train(False)')
parser.add_argument('--model_name', type=str, default=None, help='model_name')
parser.add_argument('--load_episode_number', type=int, default=None, help='episode number of the model to be loaded for evaluation')
parser.add_argument('--is_cpu', type=bool, default=False, help='CPU(True) GPU(False) (Default is False)')
parser.add_argument('--debug', type=bool, default=False, help='debug(True) no_debug(False) (Default is False)')
parser.add_argument('--n_actions', type=int, default=2, help='number of actions')
parser.add_argument('--state_size', type=int, default=1000, help='resnet output size (state_size))')
parser.add_argument('--random_seed', type=int, default=100, help='random package seed')
parser.add_argument('--buffer_size', type=int, default=200_000, help='buffer size')
parser.add_argument('--lrpolicy', type=float, default=0.0001, help='learning rate of policy network') #actor
parser.add_argument('--lrvalue', type=float, default=0.0005, help='learning rate of value network') #critic
parser.add_argument('--tau', type=float, default=0.001, help='tau for target network')
parser.add_argument('--alpha', type=float, default=0.2, help='alpha')
parser.add_argument('--gamma', type=float, default=0.97, help='gamma')
parser.add_argument('--batch_size', type=int, default=64, help='batch size')
parser.add_argument('--xml_file', type=str, help='xml file contains routes')
parser.add_argument('--json_file', type=str, help='json_file contains scenarios')

args = parser.parse_args()

for arg in vars(args):
    print(f"{arg} : {getattr(args, arg)}")

db = DB()

db.create_training_table()
db.create_evaluation_table()
db.create_buffer_table()

if not args.evaluate:
    args.model_name = base_utils.get_time_info() #create new model name with current time
    print(f"Train will start with {args.model_name}")
    db.insert_data_to_training_table(args)
else:
    print(f"Evaluate will start with {args.model_name} models with ep num {args.load_episode_number}")
    db.insert_data_to_evaluation_table(args)

db.close()