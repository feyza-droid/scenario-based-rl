import random
from utils.db import DB


class ReplayBuffer:
    def __init__(self, db, buffer_size, seed):
        random.seed(seed)

        self.db = db
        self.buffer_size = buffer_size
        self.id = db.get_latest_sample_id()
        self.filled_size = db.get_buffer_sample_count()

    # append experience to the replay memory
    def push(self, image_features, fused_inputs, action, reward, next_image_features, next_fused_inputs, done):
        if self.id == self.buffer_size:
            # unique db id
            self.id = 0

        self.db.insert_data_to_buffer_table(self.id, image_features, fused_inputs, action, reward, next_image_features, next_fused_inputs, done)
        self.id += 1
        self.filled_size += 1

    # get experience sample of batch size
    def sample(self, batch_size):
        high = self.filled_size if self.filled_size < self.buffer_size else self.buffer_size

        # low inclusive, high exclusive
        sample_indexes = random.sample(range(0, high), batch_size)
        
        sample_batch = self.db.read_batch_data(tuple(sample_indexes), batch_size)
        
        return sample_batch