from parlai.scripts.display_model import DisplayModel
from parlai.scripts.display_model import DisplayModel
DisplayModel.main(
    task='customer_Care',
    model_file='../training/empathy_scratch/model',
   # model_file='zoo:tutorial_transformer_generator/model',
    fp16 = True,
    num_examples=10,
    skip_generation = False
)