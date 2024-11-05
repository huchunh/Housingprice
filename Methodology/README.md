# Methodology for House Price Prediction

This folder contains the methodology for the House Price Prediction project. The original data set is AmesHousing.csv

### Overview of the Dataset
- **Dimensions**: 82 columns, 2930 rows
- **Data Types**:
  - `float64`: 11 columns
  - `int64`: 28 columns
  - `object`: 43 columns

The dataset includes almost half of bjective/quantitative variables (e.g., year built, number of fireplaces) and half of subjective/qualitative variables (e.g., heating quality, exterior quality).

For detailed data definitions, refer to this [Data Definition Document]
(https://docs.google.com/spreadsheets/d/1XL6LJVgLLU27yV7a_oh2zuqhGOI3Syg-jWpmr0Ekk14/edit?usp=sharing)

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


## Data Splitting

We split the encoded dataset into training and test sets with an 85/15 ratio. This allocation provides a larger portion of data for training, which is essential for model learning, especially with our limited dataset size. The larger training set also supports the accuracy and balance required for our subsequent data augmentation. 

Importantly, we only augment the training data to ensure that the test data remains purely representative of real-world cases, helping to provide an unbiased evaluation of model performance.


## Feature Selection

After splitting, we apply feature selection to identify the most relevant features for predicting SalePrice. These selected features will be used for data augmentation.

### *1. Correlation Analysis*

First, we perform a correlation analysis, focusing on features with a correlation coefficient (Pearson’s r) of at least 0.3 with SalePrice. Pearson’s r, which ranges from -1 to +1, measures the strength and direction of a linear relationship between two variables. We set the threshold at 0.3 to capture features with a moderate level of association, aiming to retain features that hold predictive potential without being overly restrictive. This method also enhances interpretability in the context of a linear model, like linear regression, which we plan to use in modeling.


### *2. Lasso Coefficients*

Next, we apply Lasso regression to further refine our feature selection. Before performing Lasso, we standardize the features since Lasso is sensitive to feature scaling. We then use LassoCV to automatically determine the optimal level of regularization. This technique penalizes less important features, potentially reducing their coefficients to zero, thereby simplifying the model and focusing on the most predictive features. We set a high threshold of 0.1 for feature importance to retain only the most impactful features. Notably, only one feature was removed by Lasso, indicating that most of the features identified in the correlation step were indeed significant.


## Data Augmentation

Finally, we use the selected features as input to the augment_data_with_perturbations function for data augmentation. This approach generates synthetic records by perturbing only the most relevant features, thereby adding meaningful diversity to the training set. By introducing controlled variability in the important features, we enable the model to generalize better to slight variations in real-world data, enhancing robustness and stability.

We set the perturbation_percentage to 0.02, limiting perturbations to within 2% of each feature’s original value. This conservative level of variation ensures that the synthetic data remains realistic, avoiding outliers that could reduce model accuracy. Adding 2000 augmented records expands the dataset in a balanced way, enhancing model performance without introducing excessive noise, while keeping computational requirements manageable.

