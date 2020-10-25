from parlai.scripts.eval_model import EvalModel 
EvalModel.main(
    task='customer_Care',
    model_file='/home/xcs224u/project/Task-Oriented-Chatbot-With-Empathy/data/test_models/pretrained_transformer_ed/model',
    metrics =  ['ppl','f1','accuracy','hits@1'],
  
    num_examples=200,    
   # optimizer='adam',

)