import pandas as pd
#import os


def is_interaction_score_valid(interaction_score_test):
    return (interaction_score_test == "Minor" or interaction_score_test == "Moderate" or interaction_score_test == "Major")


drug_A_list = []
drug_B_list = []
interaction_score_list = []

f = open("./dataset/ddinter_downloads_code_A.csv")
i = 0
for line_read in f:
    line_read = str(line_read)
    line_read = line_read.replace("\n", "")
    if(i > 0):
        #temp = [j for j in (line_read.split(","))[1:]]
        line_read_list = (line_read.split(","))
        drug_A = line_read_list[1]
        drug_B = line_read_list[3]
        interaction_score = line_read_list[4]

        if(not is_interaction_score_valid(interaction_score)):
            continue

        drug_A_list.append(drug_A)
        drug_B_list.append(drug_B)
        interaction_score_list.append(interaction_score)

        if(i % 1000 == 0):
            print("Test sampling : [" + drug_A + "] interact [" + drug_B + "], with score : " + interaction_score)
    i = i + 1
