# Project DVC

This project uses Data Version Control (DVC) to manage datasets and track changes efficiently. Below is the directory structure and description of each component in this project.

## Directory Structure

```plaintext
project_dvc/                  # Root folder for the DVC project
├── .dvc/                      # DVC configuration folder
│   ├── config.txt             # DVC configuration file
│   └── gitignore.txt          # Git ignore settings for DVC files
├── data/                      # Data folder containing datasets and version files
│   ├── AmesHousing.csv.dvc    # DVC-tracked file for the Ames Housing dataset
│   ├── cleaned_data.csv.dvc   # DVC-tracked file for the cleaned dataset
│   ├── encoding_data.csv.dvc  # DVC-tracked file for the encoded dataset
│   ├── gitignore.txt          # Git ignore file specific to the data folder
│   └── dvcignore.txt          # DVC ignore file for excluding certain files from DVC tracking
```

## Description of Files and Folders

- **project_dvc/**: The main directory of the project where all DVC-related files are stored.
  
- **.dvc/**: Contains DVC configuration and settings files.
  - **config.txt**: Configuration file that includes the settings for DVC in this project.
  - **gitignore.txt**: Specifies files and directories that Git should ignore in the `.dvc` folder.
  
- **data/**: This folder contains the datasets used in the project, all tracked by DVC.
  - **AmesHousing.csv.dvc**: DVC-tracked file for the original Ames Housing dataset.
  - **cleaned_data.csv.dvc**: DVC-tracked file for the cleaned version of the dataset after preprocessing.
  - **encoding_data.csv.dvc**: DVC-tracked file for the dataset after encoding categorical variables.
  - **gitignore.txt**: File to specify files in the `data` folder that Git should ignore.
  - **dvcignore.txt**: File to specify files in the `data` folder that DVC should ignore.

## Usage

1. **Setting Up DVC**:
   - Ensure DVC is installed by running `pip install dvc`.
   - Initialize DVC in the project (if not already done) using `dvc init`.

2. **Adding Data Files**:
   - Place raw and processed datasets in the `data/` folder.
   - Track each dataset with DVC by running `dvc add data/<filename>`.
   - This creates `.dvc` files (e.g., `AmesHousing.csv.dvc`) that reference the version-controlled data.

3. **Using gitignore.txt and dvcignore.txt**:
   - `gitignore.txt` is used to prevent specific files in `data/` from being tracked by Git.
   - `dvcignore.txt` helps DVC to ignore files or directories in `data/` that you do not want to track.

4. **Pushing Data to Remote Storage**:
   - Configure a remote storage for DVC using `dvc remote add -d <remote-name> <remote-url>`.
   - Push the data to the remote storage with `dvc push` to back up your datasets.

5. **Pulling Data**:
   - To retrieve data from the remote storage, use `dvc pull`.

## Notes

- Ensure that both `gitignore.txt` and `dvcignore.txt` are properly configured to exclude unnecessary files from version control.
- For collaborative projects, share `.dvc` files and configuration, allowing others to reproduce your work by using `dvc pull` to fetch the data.
