import os
import sys


path_dir = str(os.getcwd()) + '/NewUnparsed'
path_dir_out = 'NewParsedPython'
if not os.path.exists(path_dir_out):
    os.makedirs(path_dir_out)
#print(path_dir)    
file_list = os.listdir(path_dir)

for files in file_list:
    fileName = path_dir +'/'+ files
    f = open(fileName,'r', encoding='UTF8')

    fileName_r = path_dir_out + '/' + files
    fr = open(fileName_r,'w',encoding='UTF8')

    SNR = ""
    LTE_5G = ""
    this_data = ""
    SNR_5G = ""
    RSSI = ""
    RSRP = ""
    CID = ""
    RSRP_5G = ""
    Indicator = ""
    Altitude = ""
    while True:
        line = f.readline()
        if not line:
            break;
        elif(line[0]=='N'):
            curr_data = line[line.find('[')+1:line.find(']')]
            SNR = SNR + curr_data + " "
        elif(line[0]=='T'):
            curr_data = line[line.find('[')+1:line.find(']')]
            if curr_data == "LTE":
                this_data = "1"
            else:
                this_data = "2"
            LTE_5G = LTE_5G + this_data + " "
        elif(line[0]=='F'):
            curr_data = line[line.find('[')+1:line.find(']')]
            SNR_5G = SNR_5G + curr_data + " "
        elif (line[0] == 'S'):
            curr_data = line[line.find('[') + 1:line.find(']')]
            RSSI = RSSI + curr_data + " "
        elif (line[0] == 'R'):
            curr_data = line[line.find('[') + 1:line.find(']')]
            RSRP = RSRP + curr_data + " "
        elif (line[0] == 'C'):
            curr_data = line[line.find('[') + 1:line.find(']')]
            CID = CID + curr_data + " "
        elif (line[0] == 'D'):
            curr_data = line[line.find('[') + 1:line.find(']')]
            RSRP_5G = RSRP_5G + curr_data + " "
        elif (line[0] == 'I'):
            curr_data = line[line.find('[') + 1:line.find(']')]
            Indicator = Indicator + curr_data + " "
        elif (line[0] == 'A'):
            curr_data = line[line.find('[') + 1:line.find(']')]
            Altitude = Altitude + curr_data + " "


    
    
    fr.write("LTE(1) or 5G(2)\n")
    fr.write(LTE_5G)
    fr.write("\nSNR of LTE\n")
    fr.write(SNR)
    fr.write("\nSNR of 5G\n")
    fr.write(SNR_5G)
    fr.write("\nRSSI\n")
    fr.write(RSSI)
    fr.write("\nRSRP\n")
    fr.write(RSRP)  
    fr.write("\nCID\n")
    fr.write(CID)
    fr.write("\nRSRP of 5G\n")
    fr.write(RSRP_5G)
    fr.write("\nCQI\n")
    fr.write(Indicator)
    fr.write("\nAltitude\n")
    fr.write(Altitude)




    f.close()
    fr.close()