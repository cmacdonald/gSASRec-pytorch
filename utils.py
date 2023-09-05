import importlib
from config import GSASRecExperimentConfig
from dataset_utils import get_num_items
import torch
from gsasrec import GSASRec

def load_config(config_file: str) -> GSASRecExperimentConfig:
    spec = importlib.util.spec_from_file_location("config", config_file)
    config_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(config_module)
    return config_module.config

def build_model(config, device):
    num_items = get_num_items(config.dataset_name) 
    model = GSASRec(num_items, sequence_length=config.sequence_length, embedding_dim=config.embedding_dim,
                        num_heads=config.num_heads, num_blocks=config.num_blocks, dropout_rate=config.dropout_rate).to(device)

def get_device(self):
    device = "cpu"
    if torch.cuda.is_available():
        device="cuda:0"
    elif torch.backends.mps.is_available():
        device="mps"
    return device


