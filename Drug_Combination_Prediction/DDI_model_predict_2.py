from DeepPurpose import utils, dataset
from DeepPurpose import DDI as models
import warnings
warnings.filterwarnings("ignore")

model = models.model_pretrained(path_dir='./model/DDI_model_1')

# predict sample 1
X_drugs_a = ['ClC1=CC=C2N=C3NC(=O)CN3CC2=C1Cl']
X_drugs_b = ['CCN(CC)CCCC(C)NC1=C2C=CC(Cl)=CC2=NC=C1']
y_solution = [0.1]

# X_pred = utils.data_process(X_drug=X_drugs_a, y=y_solution, drug_encoding='rdkit_2d_normalized',
#                             split_method='no_split', mode='DDI', X_drug_=X_drugs_b)
X_pred = utils.data_process(X_drug=X_drugs_a, y=y_solution,drug_encoding='rdkit_2d_normalized',
                            split_method='no_split', mode='DDI', X_drug_=X_drugs_b)

y_pred = model.predict(X_pred)
print('The predicted score is ' + str(y_pred) + " and the true score is " + str(y_solution))