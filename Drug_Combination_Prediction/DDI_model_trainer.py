from DeepPurpose import DDI as models
from DeepPurpose.utils import *
from DeepPurpose.dataset import *

# load DB Binary Data
X_drugs, X_drugs_, y = read_file_training_dataset_drug_drug_pairs("./dataset/DDI_data_A.txt")

drug_encoding = 'rdkit_2d_normalized'
train, val, test = data_process(X_drug=X_drugs, X_drug_=X_drugs_, y=y,
                                drug_encoding=drug_encoding,
                                split_method='random',
                                random_seed=1)

config = generate_config(drug_encoding=drug_encoding,
                         cls_hidden_dims=[512],
                         train_epoch=20,
                         LR=0.001,
                         batch_size=128,
                         )

model = models.model_initialize(**config)
model.train(train, val, test)

model.save_model('./model/DDI_model_1')
