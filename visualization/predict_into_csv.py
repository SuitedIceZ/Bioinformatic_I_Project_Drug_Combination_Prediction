from DeepPurpose import utils, dataset
from DeepPurpose import DDI as DDI_models
from DeepPurpose import DTI as DTI_models
import warnings
warnings.filterwarnings("ignore")

DDI_model_1 = DDI_models.model_pretrained(path_dir='./model/DDI_model_1')
DDI_model_2 = DDI_models.model_pretrained(path_dir='./model/DDI_model_2')

def DDI_predict(Drug1, Drug2,y_expected,DDI_model):
    #print(y_expected)
    X_pred = utils.data_process(X_drug=Drug1, y=y_expected, drug_encoding='rdkit_2d_normalized',
                                split_method='no_split', mode='DDI', X_drug_=Drug2)
    y_pred_DDI = DDI_model.predict(X_pred)
    return y_pred_DDI[0]


# load brenchmark data
bmf = open("./dataset/DDI_data_P.txt", "r")

# write to csv
csv = open("data/DDI_data_P_compare_1-2_withY_v4.csv", "w")

# write header
csv.write("Drug1,Drug2,DDI_model_1_predict,DDI_model_2_predict,answer\n")

cnt = 0
# predict and write to csv
for line in bmf:
    line = line.replace("\n", "")
    line = line.split(" ")
    Drug1 = [line[0]]
    Drug2 = [line[1]]
    answer = line[2]
    y_expected = [float(answer)]
    y_pred_DDI_1 = DDI_predict(Drug1, Drug2,y_expected,DDI_model_1)
    y_pred_DDI_2 = DDI_predict(Drug1, Drug2,y_expected,DDI_model_2)
    csv.write(Drug1[0] + "," + Drug2[0] + "," + str(y_pred_DDI_1) + "," + str(y_pred_DDI_2) + "," + str(answer) + "\n")

    cnt += 1
    if(cnt%100 == 0):
        print("***************cnt: ", cnt)
        # break
    # if(cnt == 200):
    #     break

bmf.close()
csv.close()


