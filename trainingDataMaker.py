import os
from statistics import mean, stdev

slicingPointCustom = [72,121,170,218,267]
routeNameCustom = [9,9,9,9]
routeNameCustom = [str(x) for x in routeNameCustom]

counter = 1

lowPercentileThres = -100


path_dir = str(os.getcwd()) + '/trainingDataChunk_in'
path_dir_out = str(os.getcwd()) + '/TrainingDataSH'
file_list = os.listdir(path_dir)
file_list = sorted(file_list)
for file in file_list:
    fileName = path_dir +'/'+ file
    f = open(fileName,'r', encoding='UTF8')
    rsrp_LTE = ""
    rsrp_5G = ""
    rsrp_total = []
    LTE5G_index = ""
    while True:
        line = f.readline()
        if not line:
            break;
        elif (line=='LTE(1) or 5G(2)\n'):
            LTE5G_index = f.readline().split()
            LTE5G_index = [int(x) for x in LTE5G_index]
        elif (line=='RSRP\n'):
            rsrp_LTE = f.readline().split()
            rsrp_LTE = [int(x) for x in rsrp_LTE]
        elif (line=='RSRP of 5G\n'):
            rsrp_5G = f.readline().split()
            rsrp_5G = [int(x) for x in rsrp_5G]
    for place in range(len(rsrp_LTE)):
        if rsrp_LTE[place] == 2147483647:
            rsrp_LTE[place] = rsrp_LTE[place-1]
    for place in range(len(rsrp_5G)):
        if rsrp_5G[place] == 2147483647:
            rsrp_5G[place] = rsrp_5G[place-1]
    for i in range(len(LTE5G_index)):
        if LTE5G_index[i] == 1:
            rsrp_total.append(int((rsrp_LTE[i]*0.8873-52.564)/1.244))
        else:
            rsrp_total.append(rsrp_5G[i])
    split_rsrp_1 = rsrp_total[slicingPointCustom[0]:slicingPointCustom[1]]
    split_rsrp_2 = rsrp_total[slicingPointCustom[1]:slicingPointCustom[2]]
    split_rsrp_3 = rsrp_total[slicingPointCustom[2]:slicingPointCustom[3]]
    split_rsrp_4 = rsrp_total[slicingPointCustom[3]:slicingPointCustom[4]]

    out_route_dir1 = path_dir_out+'/e1/'+routeNameCustom[0]
    if not os.path.exists(out_route_dir1):
        os.makedirs(out_route_dir1)
    fileName_w = out_route_dir1 + '/' + str(counter)  + '.txt'
    fw = open(fileName_w,'w',encoding='UTF8')
    avgTemp = mean(split_rsrp_1)
    stdTemp = stdev(split_rsrp_1)
    numLow = 0
    for k in range(len(split_rsrp_1)):
        if split_rsrp_1[k]<lowPercentileThres:
            numLow = numLow+1
    lowpTemp = float(numLow)/float(len(split_rsrp_1))*100
    minrTemp = min(split_rsrp_1)
    fw.write(str(avgTemp)+'\n')
    fw.write(str(stdTemp)+'\n')
    fw.write(str(lowpTemp)+'\n')
    fw.write(str(minrTemp)+'\n')
    fw.close()

    out_route_dir2 = path_dir_out+'/e2/'+routeNameCustom[1]
    if not os.path.exists(out_route_dir2):
        os.makedirs(out_route_dir2)
    fileName_w = out_route_dir2 + '/' + str(counter)  + '.txt'
    fw = open(fileName_w,'w',encoding='UTF8')
    avgTemp = mean(split_rsrp_2)
    stdTemp = stdev(split_rsrp_2)
    numLow = 0
    for k in range(len(split_rsrp_2)):
        if split_rsrp_2[k]<lowPercentileThres:
            numLow = numLow+1
    lowpTemp = float(numLow)/float(len(split_rsrp_2))*100
    minrTemp = min(split_rsrp_2)
    fw.write(str(avgTemp)+'\n')
    fw.write(str(stdTemp)+'\n')
    fw.write(str(lowpTemp)+'\n')
    fw.write(str(minrTemp)+'\n')
    fw.close()


    out_route_dir3 = path_dir_out+'/e3/'+routeNameCustom[2]
    if not os.path.exists(out_route_dir3):
        os.makedirs(out_route_dir3)
    fileName_w = out_route_dir3 + '/' + str(counter)  + '.txt'
    fw = open(fileName_w,'w',encoding='UTF8')
    avgTemp = mean(split_rsrp_3)
    stdTemp = stdev(split_rsrp_3)
    numLow = 0
    for k in range(len(split_rsrp_3)):
        if split_rsrp_3[k]<lowPercentileThres:
            numLow = numLow+1
    lowpTemp = float(numLow)/float(len(split_rsrp_3))*100
    minrTemp = min(split_rsrp_3)
    fw.write(str(avgTemp)+'\n')
    fw.write(str(stdTemp)+'\n')
    fw.write(str(lowpTemp)+'\n')
    fw.write(str(minrTemp)+'\n')
    fw.close()

    out_route_dir4 = path_dir_out+'/e4/'+routeNameCustom[3]
    if not os.path.exists(out_route_dir4):
        os.makedirs(out_route_dir4)
    fileName_w = out_route_dir4 + '/' + str(counter)  + '.txt'
    fw = open(fileName_w,'w',encoding='UTF8')
    avgTemp = mean(split_rsrp_4)
    stdTemp = stdev(split_rsrp_4)
    numLow = 0
    for k in range(len(split_rsrp_4)):
        if split_rsrp_4[k]<lowPercentileThres:
            numLow = numLow+1
    lowpTemp = float(numLow)/float(len(split_rsrp_4))*100
    minrTemp = min(split_rsrp_4)    
    fw.write(str(avgTemp)+'\n')
    fw.write(str(stdTemp)+'\n')
    fw.write(str(lowpTemp)+'\n')
    fw.write(str(minrTemp)+'\n')
    fw.close()
    counter = counter+1