# ASCEND: Altitude Selection for High-quality Cellular Connectivity on Drones

![Publication](https://img.shields.io/badge/Publication-IEEE%20TVT-blue.svg)

## About This Repository

This repository contains the official source code, datasets, and trained models necessary to reproduce the experimental results presented in the paper "ASCEND: Altitude Selection for High-quality Cellular Connectivity on Drones," published in IEEE Transactions on Vehicular Technology (TVT). It includes the core Q-learning algorithm, scripts for data processing and analysis, and the complete datasets used in the study.

## System Requirements

*   Python 3.9+
*   NumPy
*   SciPy
*   MATLAB (optional, for running `Graph_result_drawer.m`)

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/your-username/IEEE_TVT_ASCEND_Public_Code.git
    ```
2.  Navigate to the project directory:
    ```bash
    cd IEEE_TVT_ASCEND_Public_Code
    ```
3.  Install the required Python packages:
    ```bash
    pip install numpy scipy
    ```

## Repository Structure

```
.
├── ASCEND.py
├── Confirmed_rawTxt_to_sequenceTxt.py
├── Graph_result_drawer.m
├── MATLAB_CodeGenerator_LimiationOfExhaustiveSearch.py
├── trainingDataMaker.py
├── data/
│   ├── TrainingDataSH/
│   ├── NewParsedPython/
│   ├── LOE_rawData/
│   ├── LOE_matlabCode/
│   ├── LOE_Gwan_RSRP.xlsx
│   └── LOE_Gwan_reward.xlsx
├── results/
│   ├── *.npy
│   └── *.mat
└── README.md
```

-   **`/` (root)**: Contains the main Python scripts for the simulation and data processing, along with the MATLAB script for plotting.
-   **`/data`**: Contains all the datasets used in the paper.
    -   `TrainingDataSH`: The primary training data for the Q-learning agent.
    -   `NewParsedPython`: Parsed data from the raw experimental logs.
    -   `LOE_rawData` & `LOE_matlabCode`: Data and code related to the exhaustive search comparison.
    -   `*.xlsx`: Excel files containing reward and RSRP data.
-   **`/results`**: Contains the final trained Q-tables (`.npy` files) and data for generating graphs (`.mat` files).

## Usage

### Main Simulation

To run the main Q-learning simulation, execute the `ASCEND.py` script. This will train the model using the data in `/data/TrainingDataSH` and save the output Q-table and graph data to the `/results` directory.

```bash
python ASCEND.py
```

### Data Processing

The following scripts are provided to show the data processing pipeline:

-   **`Confirmed_rawTxt_to_sequenceTxt.py`**: Parses raw log files into a structured format.
-   **`trainingDataMaker.py`**: Processes the parsed data to create the final training set used by the ASCEND algorithm.
-   **`MATLAB_CodeGenerator_LimiationOfExhaustiveSearch.py`**: Generates MATLAB code from raw data for the exhaustive search analysis.

## License

---
> **AI 사용 관련 안내**
>
> 모든 코드 및 데이터는 저자가 "직접" 수집 및 작성하였습니다. 그러나 public으로 공개하기 위한 익명화 및 레포지토리 구성은 AI의 도움을 받아 정리되었습니다.
>
> **Guidance on AI Usage**
>
> All code and data were "directly" collected and written by the author. However, the anonymization and repository organization for public release were assisted by AI.
