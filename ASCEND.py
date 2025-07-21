
#Make simple Q-learning with Q-table
#Note: Using only ALREADY measured data
#Q-learning with 4-step episode
#There are 3 altitude candidates: 60, 90, 120

import os
import numpy as np
import time
from scipy.io import savemat

#variables
numOfPathEdge = 4
numOfAltitudeCandidate = 3
epsilon = 1.0
linearEpsilonDecayRate = 0.01
trainingDataPath = 'data/TrainingDataSH/'
routeFolderName = 'e'
numOfState = numOfPathEdge * numOfAltitudeCandidate
numOfStatesInEpisode = numOfPathEdge
altitudeNameList = ['60','90','120']
numofEpisode = 10000
altitudeRouteList = ['11','12','13','21','22','23','31','32','33']

Q_TableSaveName = '221209_'+str(numofEpisode)+'_SH_allreward_seed0'

avgCQIList = []
stdCQIList = []
minCQIList = []
minCQIPercentile = []
longRewardList = []

#np random seed fix
np.random.seed(0)
np.set_printoptions(precision=2)
# initialize

#make Q-table
Q = np.zeros((numOfState, numOfAltitudeCandidate))

#make action array size of numOfStatesInEpisode
actionArray = np.zeros(numOfStatesInEpisode)

#make state array size of numOfStatesInEpisode+1, because has fixed initial state
stateArray = np.zeros(numOfStatesInEpisode + 1)

#make reward array size of numOfStatesInEpisode
rewardArray = np.zeros(numOfStatesInEpisode)


#define get_action function
def get_action(Q, state):
    state = int(state)
    if np.random.rand() < epsilon:
        action = np.random.randint(0, numOfAltitudeCandidate)
    else:
        action = np.argmax(Q[state, :])
    return action


#define get_next_state function
def get_next_state(state, action):
    pathEdgeNum = state // numOfAltitudeCandidate + 1
    if pathEdgeNum == numOfPathEdge:
        next_state = action
    else:
        next_state = pathEdgeNum * numOfAltitudeCandidate + action
    next_state = int(next_state)
    return next_state


#define play_episode function with 4-step
def play_episode(Q,initial_state):
    state = initial_state
    stateArray[0] = initial_state
    for i in range(numOfStatesInEpisode):
        action = get_action(Q, state)
        state = get_next_state(state, action)
        actionArray[i] = action
        stateArray[i+1] = state
    return actionArray, stateArray


#defince state and action to file name function
def state_action_to_folder_name(state, next_state):
    pathEdgeNum = state // numOfAltitudeCandidate + 1
    pathEdgeNum = int(pathEdgeNum)
    startingAltitudeName = int(state % numOfAltitudeCandidate)+1
    endingAltitudeName = int(next_state % numOfAltitudeCandidate)+1
    routeEdgeName = str(startingAltitudeName) + str(endingAltitudeName)
    #python index of routeEdgeName in altitudeRouteList
    routeEdgeIndex = altitudeRouteList.index(routeEdgeName)+1
    folderName = routeFolderName + str(pathEdgeNum) + '/' + str(routeEdgeIndex)
    return folderName


#define function for pickup data from file in folderName
def pickup_data(folderName):
    filePath = trainingDataPath + folderName
    numOfFilesInFolder = len(os.listdir(filePath)) - 1
    fileNumberTicket = filePath + '/ticketNumber.txt'
    #open fileNumberTicket and read line and convert to int
    with open(fileNumberTicket, 'r') as f:
        fileNumber = int(f.readline())
        pickedFileNumber = fileNumber
        #overwrite fileNumberTicket with fileNumber+1
        with open(fileNumberTicket, 'w') as f:
            if fileNumber == numOfFilesInFolder:
                fileNumber = 0
            f.write(str(fileNumber+1))
            #close fileNumberTicket
            f.close()
    #get file name
    fileName = filePath + '/' + str(pickedFileNumber) + '.txt'
    return fileName

    
#define get_flight_result function
def get_flight_result(state, action):
    fileName = pickup_data(state_action_to_folder_name(state, action))
    #read file, first line = average CQI, second line = variance CQI, third line = low CQI percentile, fourth line = minimum CQI
    with open(fileName, 'r') as f:
        averageCQI = float(f.readline())
        varianceCQI = float(f.readline())
        lowCQIpercentile = float(f.readline())
        minimumCQI = float(f.readline())
    return averageCQI, varianceCQI, lowCQIpercentile, minimumCQI


    #define calculate_reward function
def calculate_reward(state, next_state):
    averageCQI, varianceCQI, lowCQIpercentile, minimumCQI = get_flight_result(state, next_state)
    stdCQI = varianceCQI
    reward = minimumCQI + averageCQI - stdCQI
    #reward = minimumCQI
    avgCQIList.append(averageCQI)
    stdCQIList.append(stdCQI)
    minCQIList.append(minimumCQI)
    minCQIPercentile.append(lowCQIpercentile)
    longRewardList.append(reward)
    return reward

#define epsilon decay function
def epsilon_decay(epsilon,linearEpsilonDecayRate):
    epsilon = epsilon - linearEpsilonDecayRate
    return epsilon


#define stateArray match to altitude function
def matchToAltitude(stateArray):
    altitudeArray = np.zeros(numOfStatesInEpisode+1)
    for i in range(numOfStatesInEpisode+1):
        altitudeArray[i] = 60 + (stateArray[i] % numOfAltitudeCandidate *30)
    return altitudeArray

#define print reward and next episode function
def print_result(stateArray, episodicReward):
    print('Episode reward:', episodicReward)
    altitudeArray = matchToAltitude(stateArray)
    print('Next Recommandation Route:', altitudeArray)
    pass

#define init ticket number function
def init_ticket_number(dirFolder):
    for i in range (numOfPathEdge):
        dirFolderNum = str(i+1)
        numDirFolder = dirFolder + dirFolderNum
        for folders in os.listdir(numDirFolder):
            #make 'ticketNumber.txt' file in each folder
            ticketNumberFile = numDirFolder + '/' + folders + '/ticketNumber.txt'
            with open(ticketNumberFile, 'w') as f:
                f.write('1')
            f.close()

#main
if __name__ == "__main__":
    #check learning time
    init_ticket_number(trainingDataPath+routeFolderName)
    startTime = time.time()
    initialState = 0
    epsilon = 1
    captureRate = 1
    rewardRecord = np.zeros(numofEpisode)
    linearEpsilonDecayRate = 1/(numofEpisode*0.9 - 1)
    # linearEpsilonDecayRate = 0.1
    
    startTime = time.time()

    actionArray, stateArray = play_episode(Q, initialState)
    # print('actionArray:', actionArray, 'stateArray:', stateArray)

    #find and save maximum episodic reward
    episodicRewardMax = 0

    #start learning
    for i in range(numofEpisode):
        episodicReward = 0
        for j in range(numOfStatesInEpisode):
            state = stateArray[j]
            action = actionArray[j]
            next_state = stateArray[j + 1]
            reward = calculate_reward(state, next_state)
            episodicReward = episodicReward + reward
            #make state, action, next_state integer
            state = int(state)
            action = int(action)
            next_state = int(next_state)
            # print('state:', state, 'action:', action, 'next_state:', next_state, 'reward:', reward)
            Q[state, action] = Q[state, action] + 0.25 * (reward + 0.9 * np.max(Q[next_state, :]) - Q[state, action])
        initialState = stateArray[numOfStatesInEpisode]
        if epsilon > 0.01:
            epsilon = epsilon_decay(epsilon,linearEpsilonDecayRate)
        actionArray, stateArray = play_episode(Q, initialState)
        rewardRecord[i] = episodicReward
        


        #find and save maximum episodic reward
        # if episodicReward > episodicRewardMax:
        #     episodicRewardMax = episodicReward
        
        #print episode number every captureRate episode
        # if i % (numofEpisode/captureRate) == 0:
        #     print('---------------------------------------------------------------------------------------------------------------------')
        #     print('Episode:', i)
        #     print_result(stateArray, episodicReward)
        #     print('epsilon:', epsilon)
        #     # print(Q)
        #     print('---------------------------------------------------------------------------------------------------------------------')
        #if in last loop
        # if i == numofEpisode - 1:
        #     lastAltitudeArray = matchToAltitude(stateArray)
    
    #end learning time    
    endTime = time.time()
    print('learning time:', endTime - startTime)

    #save Q matrix in npy
    np.save('Q_matrix_' + Q_TableSaveName + '.npy', Q)
    #save reward record in txt
    np.savetxt('rewardRecord_testTemp.txt', rewardRecord)

    #some print results
    # print('Episodic Max Reward: ',episodicRewardMax)
    print(Q)
    print('Last Recommendation Route:', matchToAltitude(stateArray))
    #print last 50 average reward
    # print('Average Last 50 Reward:', np.mean(rewardRecord[-50:]))
    # print('Average Reward:', np.mean(rewardRecord))

    graphMatrix = []
    graphMatrix.append(avgCQIList)
    graphMatrix.append(stdCQIList)
    graphMatrix.append(minCQIList)
    graphMatrix.append(minCQIPercentile)
    graphMatrix.append(longRewardList)
    graphMatFile = np.matrix(graphMatrix)
    fileSaveName = 'graph_' + Q_TableSaveName + '.mat'
    savemat(fileSaveName, {'graphMatFile':graphMatFile})
    print(epsilon)
        




    # print(Q)
    # print(np.argmax(Q, axis=1))
    # print(np.argmax(Q, axis=0))
    # print(np.max(Q, axis=1))
    # print(np.max(Q, axis=0))
    # print(np.min(Q, axis=1))
    # print(np.min(Q, axis=0))
    # print(np.mean(Q, axis=1))
    # print(np.mean(Q, axis=0))
    # print(np.std(Q, axis=1))
    # print(np.std(Q, axis=0))
    # print(np.var(Q, axis=1))
    # print(np.var(Q, axis=0))
    # print(np.median(Q, axis=1))
    # print(np.median(Q, axis=0))
    # print(np.corrcoef(Q, rowvar=False))
    # print(np.corrcoef(Q, rowvar=True))
    # print(np.cov(Q, rowvar=False))
    # print(np.cov(Q, rowvar=True))