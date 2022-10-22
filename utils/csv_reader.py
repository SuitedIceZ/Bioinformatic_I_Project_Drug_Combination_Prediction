import pandas as pd
import csv

# import os


def is_interaction_score_valid(interaction_score_test):
    return (interaction_score_test == "Minor" or interaction_score_test == "Moderate" or interaction_score_test == "Major")


drug_A_list = []
drug_B_list = []
interaction_score_list = []
interaction_score_dict = {"Minor": 0.9, "Moderate": 0.5, "Major": 0.1}

f = open("./dataset/ddinter_downloads_code_A.csv")
i = 0
for line_read in f:
    line_read = str(line_read)
    line_read = line_read.replace("\n", "")
    if(i > 0):
        # temp = [j for j in (line_read.split(","))[1:]]
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

DtoS = open("./dataset/drugs_to_smile.txt")

DtoS_dic = {}

i = 0
available_smile_cnt = 0
for line_read in DtoS:
    line_read = str(line_read)
    line_read = line_read.replace("\n", "")
    line_read_list = (line_read.split("\t"))
    if(len(line_read_list) != 3 or len(line_read_list[2]) == 0):
        # print("Error : " + line_read)
        continue
    # if(i % 100 == 0):
    # print("DtoS sampling : " + str(len(line_read_list)) + " , " + line_read_list[0] + " -> " + line_read_list[2])
    DtoS_dic[line_read_list[0]] = line_read_list[2]
    available_smile_cnt = available_smile_cnt + 1

    i = i + 1

print("Available smile count : " + str(available_smile_cnt))
print("smile test : " + DtoS_dic["Naltrexone"])
# print("smile test : " + DtoS_dic[drug_A_list[6]])


Output_data_list = []
for i in range(len(drug_A_list)):
    if(drug_A_list[i] in DtoS_dic and drug_B_list[i] in DtoS_dic):
        Output_data_list.append([DtoS_dic[drug_A_list[i]], DtoS_dic[drug_B_list[i]], interaction_score_dict[interaction_score_list[i]]])


print(Output_data_list[100])
print("converted count  = " + str(len(Output_data_list)))

# writing to csv file
f = open("./dataset/DDI_data_1.txt", "w")

for i in range(len(Output_data_list)):
    f.write(Output_data_list[i][0] + " " + Output_data_list[i][1] + " " + str(Output_data_list[i][2]) + "\n")

f.close()
