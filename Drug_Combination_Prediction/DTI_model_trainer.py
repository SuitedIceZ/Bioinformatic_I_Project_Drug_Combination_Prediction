from DeepPurpose import utils, dataset
from DeepPurpose import DTI as models
import warnings
warnings.filterwarnings("ignore")

X_drugs, X_targets, y = dataset.load_process_DAVIS(path='./data', binary=False, convert_to_log=True, threshold=30)

drug_encoding, target_encoding = 'MPNN', 'CNN'
train, val, test = utils.data_process(X_drugs, X_targets, y,
                                      drug_encoding, target_encoding,
                                      split_method='random', frac=[0.7, 0.1, 0.2],
                                      random_seed=1)

config = utils.generate_config(drug_encoding=drug_encoding,
                               target_encoding=target_encoding,
                               cls_hidden_dims=[1024, 1024, 512],
                               train_epoch=5,
                               LR=0.001,
                               batch_size=128,
                               hidden_dim_drug=128,
                               mpnn_hidden_size=128,
                               mpnn_depth=3,
                               cnn_target_filters=[32, 64, 96],
                               cnn_target_kernels=[4, 8, 12]
                               )

model = models.model_initialize(**config)
model.train(train, val, test)

model.save_model('./model/DTI_model_1')
