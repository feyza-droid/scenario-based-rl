from datetime import datetime

today = datetime.today() # month - date - year
now = datetime.now() # hours - minutes - seconds

current_date = str(today.strftime("%b_%d_%Y"))
current_time = str(now.strftime("%H_%M_%S"))

# month_date_year-hour_minute_second
time_info = current_date + "-" + current_time

# path of main repository
base_path = "/home/resul/Research/Codes/Carla/scenario-based-rl" # Local
# base_path = "/cta/eatron/CarlaChallenge/ea202101001_platooning_demo/carla_ws" # WorkStation

# dataset for imitation learning (training)
training_data_path = base_path + "/checkpoint/dataset/dataset_4_workstation/" # Local
# training_data_path = "/cta/eatron/CarlaChallenge/TransFuser/data/14_weathers_data/" # WorkStation

# dataset for imitation learning (validation)
validation_data_path = base_path + "/checkpoint/dataset/dataset_4_workstation/" # Local
# validation_data_path = "/cta/eatron/CarlaChallenge/TransFuser/data/14_weathers_data/" # WorkStation

best_model_date = "Nov_07_2021-15_32_09"
best_model_name = "epoch_290.pth"

# whether to train a pre-trained model
pretrained = False

# location of all trained and saved models
model_save_path = base_path + "/checkpoint/results/" + time_info + "/"

# latest trained model
trained_model_path = base_path + "/checkpoint/" + best_model_date + "/" + best_model_name

# aggregated data path. will be concatenated with training dataset
dagger_data_path = base_path + "/dataset/dagger/"

# training hyperparameters
batch_size = 32
learning_rate = 1e-2
momentum = 0.9
gamma = 0.1
min_milestone = 10
max_milestone = 20
max_number_of_epochs = 50
loss_print_interval = 32
speed_input_size = 120

# model saving frequency
save_every_n_epoch = 1

# test on validation set every epoch
validate_per_n = 1

train_towns = [ "town01_long", "town01_short", "town01_tiny",
                "town05_long", "town05_short", "town05_tiny",
                "town03_short"]

validation_towns = ["town03_long"]
