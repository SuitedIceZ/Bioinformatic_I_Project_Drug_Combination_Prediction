
# A B D H L P R V
file_sub_name = ["A", "B", "D", "H", "L", "P", "R", "V"]

# create output file that concatenate all the files
fw = open("./dataset/DDI_data_all.txt", "w")

# read all the files
for i in range(len(file_sub_name)):
    path_name = "./dataset/DDI_data_" + file_sub_name[i] + ".txt"
    fr = open(path_name)
    for line_read in fr:
        fw.write(line_read)
    fr.close()

fw.close()




