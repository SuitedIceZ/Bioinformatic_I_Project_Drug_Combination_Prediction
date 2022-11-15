from DeepPurpose import utils, dataset
from DeepPurpose import DDI as DDI_models
from DeepPurpose import DTI as DTI_models
import warnings
warnings.filterwarnings("ignore")

DDI_model_1 = DDI_models.model_pretrained(path_dir='./model/DDI_model_1')
DDI_model_2 = DDI_models.model_pretrained(path_dir='./model/DDI_model_2')

def DDI_predict(Drug1, Drug2,DDI_model):
    drug_encoding, target_encoding = 'MPNN', 'CNN'
    X_pred = utils.data_process(X_drug=Drug1, y=[0.5], drug_encoding='rdkit_2d_normalized',
                                split_method='no_split', mode='DDI', X_drug_=Drug2)
    y_pred_DDI = DDI_model.predict(X_pred)
    return y_pred_DDI[0]

# load brenchmark data
bmf = open("./dataset/DDI_data_A", "r")

# write to csv
csv = open("./dataset/DDI_data_compare_1-2.csv", "w")

# write header
csv.write("Drug1,Drug2,DDI_model_1_predict,DDI_model_2_predict,answer\n")

# predict and write to csv
for line in bmf:
    line = line.strip()
    line = line.split(",")
    Drug1 = line[0]
    Drug2 = line[1]
    answer = line[2]
    DDI_model_1_predict = DDI_predict(Drug1, Drug2,DDI_model_1)
    DDI_model_2_predict = DDI_predict(Drug1, Drug2,DDI_model_2)
    csv.write(Drug1+","+Drug2+","+str(DDI_model_1_predict)+","+str(DDI_model_2_predict)+","+answer+"\n")

bmf.close()
csv.close()


