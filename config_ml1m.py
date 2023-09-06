from config import GSASRecExperimentConfig

config = GSASRecExperimentConfig(
    dataset_name='ml1m',
    sequence_length=200,
    embedding_dim=256, #consider decreasing dimensionality if you have OOMs
    num_heads=1,
    max_batches_per_epoch=100,
    num_blocks=2,
    dropout_rate=0.2,
    negs_per_pos=256,
    gbce_t = 0.75,
)
