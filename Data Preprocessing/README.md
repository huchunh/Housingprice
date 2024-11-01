Here's a revised and structured version of your README:

---

# Data Preprocessing for House Price Prediction

This folder contains the data preprocessing steps for the House Price Prediction project.

### Overview of the Dataset
- **Dimensions**: 82 columns, 2930 rows
- **Data Types**:
  - `float64`: 11 columns
  - `int64`: 28 columns
  - `object`: 43 columns

The dataset includes almost half of bjective/quantitative variables (e.g., year built, number of fireplaces) and half of subjective/qualitative variables (e.g., heating quality, exterior quality).

### Data Validation
We performed data validation based on the source: [Data Documentation](http://jse.amstat.org/v19n3/decock/DataDocumentation.txt).

1. **Outlier Removal**: We excluded houses with more than 4000 square feet from the dataset.
2. **Data Correction**: Corrected a record where the garage build year was erroneously listed as 2207, changing it to 2007 (matching the house build year).

### Handling Missing Values and Duplicates
- **Duplicates**: No duplicate records were found; all data entries are unique.
- **Missing Values**:
  - Split into numerical and categorical variables for separate handling:
    - **Numerical Variables**:
      - Filled with `0` for features like basement full bathroom and total basement square feet.
      - Used the median for features like lot frontage and garage cars.
      - Filled with mode for electrical (which had only one missing value).
    - **Categorical Variables**:
      - Standardized all `NA`, empty, or `None` values to "Missing" for consistency.

### Data Saving
To ensure reproducibility and flexibility, we saved a cleaned version of the dataset (cleaned_data.csv) for potential future use with other encoding methods.

### Label Encoding
We applied label encoding to prepare categorical features for modeling. Key steps included:

1. **Missing Values Handling**: Encoded all "Missing" values as `0`.
2. **Feature Grouping**:
    - Grouped features into three categories based on their type and quality scales:
      - **Quality-related Features**: Encoded on a scale from 1 to 5, ranging from Poor to Excellent. This included 10 features.
      - **Good-to-Bad Features**: Assigned numerical values from low to high quality across 7 features.
      - **Remaining Features**: Encoded as needed for modeling purposes.

After these steps, we obtained a fully encoded dataset ready for analysis and modeling. (encoding_data.csv)


