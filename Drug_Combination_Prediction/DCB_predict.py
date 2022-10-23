from DeepPurpose import utils, dataset
from DeepPurpose import DDI as DDI_models
from DeepPurpose import DTI as DTI_models
import warnings
warnings.filterwarnings("ignore")

DDI_model = DDI_models.model_pretrained(path_dir='./model/DDI_model_1')
DTI_model = DTI_models.model_pretrained(path_dir='./model/DTI_model_1')

drug_encoding, target_encoding = 'MPNN', 'CNN'


def DCB_predict(Drug1, Drug2, Target):
    X_drug1 = utils.data_process(Drug1, Target, [5.5],
                                 drug_encoding, target_encoding,
                                 split_method='no_split')

    X_drug2 = utils.data_process(Drug2, Target, [5.5],
                                 drug_encoding, target_encoding,
                                 split_method='no_split')

    y_pred_DTI_1 = DTI_model.predict(X_drug1)
    y_pred_DTI_2 = DTI_model.predict(X_drug2)

    X_pred = utils.data_process(X_drug=Drug1, y=[0.5], drug_encoding='rdkit_2d_normalized',
                                split_method='no_split', mode='DDI', X_drug_=Drug2)

    y_pred_DDI = DDI_model.predict(X_pred)
    y_pred = y_pred_DDI[0] * (y_pred_DTI_1[0] + y_pred_DTI_2[0])
    return y_pred


# predict sample 1
Drug1 = ['CC1=C2C=C(C=CC2=NN1)C3=CC(=CN=C3)OCC(CC4=CC=CC=C4)N']
Drug2 = ['C1CC1NC2=C3C(=NC(=N2)N)N(C=N3)C4CC(C=C4)CO']
Target = ['MKKFFDSRREQGGSGLGSGSSGGGGSTSGLGSGYIGRVFGIGRQQVTVDEVLAEGGFAIVFLVRTSNGMKCALKRMFVNNEHDLQVCKREIQIMRDLSGHKNIVGYIDSSINNVSSGDVWEVLILMDFCRGGQVVNLMNQRLQTGFTENEVLQIFCDTCEAVARLHQCKTPIIHRDLKVENILLHDRGHYVLCDFGSATNKFQNPQTEGVNAVEDEIKKYTTLSYRAPEMVNLYSGKIITTKADIWALGCLLYKLCYFTLPFGESQVAICDGNFTIPDNSRYSQDMHCLIRYMLEPDPDKRPDIYQVSYFSFKLLKKECPIPNVQNSPIPAKLPEPVKASEAAAKKTQPKARLTDPIPTTETSIAPRQRPKAGQTQPNPGILPIQPALTPRKRATVQPPPQAAGSSNQPGLLASVPQPKPQAPPSQPLPQTQAKQPQAPPTPQQTPSTQAQGLPAQAQATPQHQQQLFLKQQQQQQQPPPAQQQPAGTFYQQQQAQTQQFQAVHPATQKPAIAQFPVVSQGGSQQQLMQNFYQQQQQQQQQQQQQQLATALHQQQLMTQQAALQQKPTMAAGQQPQPQPAAAPQPAPAQEPAIQAPVRQQPKVQTTPPPAVQGQKVGSLTPPSSPKTQRAGHRRILSDVTHSAVFGVPASKSTQLLQAAAAEASLNKSKSATTTPSGSPRTSQQNVYNPSEGSTWNPFDDDNFSKLTAEELLNKDFAKLGEGKHPEKLGGSAESLIPGFQSTQGDAFATTSFSAGTAEKRKGGQTVDSGLPLLSVSDPFIPLQVPDAPEKLIEGLKSPDTSLLLPDLLPMTDPFGSTSDAVIEKADVAVESLIPGLEPPVPQRLPSQTESVTSNRTDSLTGEDSLLDCSLLSNPTTDLLEEFAPTAISAPVHKAAEDSNLISGFDVPEGSDKVAEDEFDPIPVLITKNPQGGHSRNSSGSSESSLPNLARSLLLVDQLIDL']


y_pred = DCB_predict(Drug1, Drug2, Target)
print('The predicted score is ' + str(y_pred) + ' and the true score is ' + 'Unknown')
