from DeepPurpose import utils, dataset
from DeepPurpose import DDI as models
import warnings
warnings.filterwarnings("ignore")

model = models.model_pretrained(path_dir='./model/DDI_model_1')

# predict sample 1
X_drugs_a = ['NC1=NC(=O)N(C=C1)[C@@H]1CS[C@H](CO)O1']
X_drugs_b = ['OC[C@@H](O)[C@@H](O)[C@H](O)[C@H](O)CO']
y_solution = [0.5]

X_pred = utils.data_process(X_drug=X_drugs_a, y=y_solution, drug_encoding='rdkit_2d_normalized',
                            split_method='no_split', mode='DDI', X_drug_=X_drugs_b)

y_pred = model.predict(X_pred)
print('The predicted score is ' + str(y_pred) + " and the true score is " + str(y_solution))

# predict sample 2
X_drugs_a = ['CC1=CN([C@H]2C[C@H](N=[N+]=[N-])[C@@H](CO)O2)C(=O)NC1=O']
X_drugs_b = ['C\\N=C(\\NCCSCC1=C(C)NC=N1)NC#N']
y_solution = [0.9]

X_pred = utils.data_process(X_drug=X_drugs_a, y=y_solution, drug_encoding='rdkit_2d_normalized',
                            split_method='no_split', mode='DDI', X_drug_=X_drugs_b)

y_pred = model.predict(X_pred)
print('The predicted score is ' + str(y_pred) + " and the true score is " + str(y_solution))

# predict sample 3

X_drugs_a = ['[H][C@]12CC(CC3CC(C1)C(=O)CN23)OC(=O)C1=CNC2=CC=CC=C12']
X_drugs_b = ['CC(=O)O[C@H]1CC[C@]2(C)C3CC[C@@]4(C)C(CC=C4C4=CN=CC=C4)C3CC=C2C1']
y_solution = [0.1]

X_pred = utils.data_process(X_drug=X_drugs_a, y=y_solution, drug_encoding='rdkit_2d_normalized',
                            split_method='no_split', mode='DDI', X_drug_=X_drugs_b)

y_pred = model.predict(X_pred)
print('The predicted score is ' + str(y_pred) + " and the true score is " + str(y_solution))

# predict sample 4
X_drugs_a = ['C[C@H]1COC2=C3N1C=C(C(O)=O)C(=O)C3=CC(F)=C2N1CCN(C)CC1']
X_drugs_b = [
    '[H][C@]12[C@H](OC(=O)C3=CC=CC=C3)[C@]3(O)C[C@H](OC(=O)[C@H](O)[C@@H](NC(=O)C4=CC=CC=C4)C4=CC=CC=C4)C(C)=C([C@@H](OC(C)=O)C(=O)[C@]1(C)[C@@H](O)C[C@H]1OC[C@@]21OC(C)=O)C3(C)C']
y_solution = [0.9]

X_pred = utils.data_process(X_drug=X_drugs_a, y=y_solution, drug_encoding='rdkit_2d_normalized',
                            split_method='no_split', mode='DDI', X_drug_=X_drugs_b)

y_pred = model.predict(X_pred)
print('The predicted score is ' + str(y_pred) + " and the true score is " + str(y_solution))

# CC1=CN([C@H]2C[C@H](N=[N+]=[N-])[C@@H](CO)O2)C(=O)NC1=O [H][C@@]12OC3=C(O)C=CC4=C3[C@@]11CCN(CC3CC3)[C@]([H])(C4)[C@]1(O)CCC2=O 0.5

# predict sample 5
X_drugs_a = ['CC1=CN([C@H]2C[C@H](N=[N+]=[N-])[C@@H](CO)O2)C(=O)NC1=O']
X_drugs_b = ['[H][C@@]12OC3=C(O)C=CC4=C3[C@@]11CCN(CC3CC3)[C@]([H])(C4)[C@]1(O)CCC2=O']
y_solution = [0.5]

X_pred = utils.data_process(X_drug=X_drugs_a, y=y_solution, drug_encoding='rdkit_2d_normalized',
                            split_method='no_split', mode='DDI', X_drug_=X_drugs_b)

y_pred = model.predict(X_pred)
print('The predicted score is ' + str(y_pred) + " and the true score is " + str(y_solution))
