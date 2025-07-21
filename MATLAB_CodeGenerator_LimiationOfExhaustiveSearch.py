import os
thisPath = os.getcwd()
fileWriteDir = str(thisPath) + '/LOE_matlabCode'
fileReadDir = str(thisPath) + '/LOE_rawData'

fileList = os.listdir(fileReadDir)
for files in fileList:
    fileName = fileReadDir +'/'+ files
    f = open(fileName,'r', encoding='UTF8')
    LTE_5G = []
    RSRP = []
    RSRP_5G = []
    Altitude = ""
    RSRP_total = []
    while True:
        line = f.readline()
        if not line:
            break;
        elif(line[0]=='T'):
            curr_data = line[line.find('[')+1:line.find(']')]
            if curr_data == "LTE":
                LTE_5G.append(1)
            else:
                LTE_5G.append(2)
        elif (line[0] == 'R'):
            curr_data = line[line.find('[') + 1:line.find(']')]
            RSRP.append(int(curr_data))
        elif (line[0] == 'D'):
            curr_data = line[line.find('[') + 1:line.find(']')]
            RSRP_5G.append(int(curr_data))
        elif (line[0] == 'A'):
            curr_data = line[line.find('[') + 1:line.find(']')]
            Altitude = Altitude + curr_data + " "
    for i in range(len(LTE_5G)):
        if(LTE_5G[i]==1):
            RSRP_total.append(int((RSRP[i]*0.8873-52.564)/1.244))
        else:
            RSRP_total.append(RSRP_5G[i])
    fileName_w = fileWriteDir + '/' + files  + '_matlabCode.txt'
    fw = open(fileName_w,'w',encoding='UTF8')
    fw.write("%%\n")
    # size = len(Altitude)
    # Altitude = Altitude[:size-2]
    # size = len(CID)
    # CID = CID[:size-2]
    # size = len(RSRP_5G)
    # RSRP_5G = RSRP_5G[:size-2]
    RSRP_total_str = [str(i) for i in RSRP_total]
    fw.write("altitude_loe"  + '= [' + Altitude + '];\n')
    fw.write("rsrp" + '= [' + ' '.join(RSRP_total_str) + '];\n')
    fw.write("%%\n")
    fw.write('figure();\nplot(altitude_loe);\n')
    fw.write("%%\n")
    fw.write('slicingIndex = [];\n')
    f.close()
    fw.close()