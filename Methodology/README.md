# Methodology for House Price Prediction

This folder documents the methodology used in the House Price Prediction project, detailing the steps taken to process data, select features, and develop a robust model. The dataset used is **AmesHousing.csv**.

---

## 1. Introduction

The methodology outlined here serves as a guide to understanding the reasoning behind data processing, feature selection, and model preparation for predicting house prices. Each decision was made with the goal of improving model accuracy, interpretability, and robustness. 

For detailed data definitions, refer to this [Data Definition Document](https://docs.google.com/spreadsheets/d/1XL6LJVgLLU27yV7a_oh2zuqhGOI3Syg-jWpmr0Ekk14/edit?usp=sharing).

---

## 2. Data Processing Methods

### Overview of the Dataset
- **Dimensions**: 82 columns, 2930 rows
- **Data Types**:
  - `float64`: 11 columns
  - `int64`: 28 columns
  - `object`: 43 columns

The dataset includes a balanced mix of quantitative variables (e.g., year built, number of fireplaces) and qualitative variables (e.g., heating quality, exterior quality).

### Data Validation
We validated the dataset using information from the [Data Documentation](http://jse.amstat.org/v19n3/decock/DataDocumentation.txt). Key steps included:
1. **Outlier Removal**: Houses with over 4000 square feet were excluded to avoid skewing the model.
2. **Data Correction**: Corrected a record where the garage build year was incorrectly listed as 2207, changing it to 2007.

### Handling Missing Values and Duplicates
- **Duplicates**: No duplicate records were identified in the dataset.
- **Missing Values**:
   - **Numerical Variables**: Handled based on variable type:
      - Filled with `0` for features like basement full bathroom and total basement square feet.
      - Used the median for continuous features like lot frontage and garage cars.
   - **Categorical Variables**: Standardized all `NA`, empty, or `None` values to "Missing" for consistency.

### Data Saving
The cleaned dataset was saved as `cleaned_data.csv` to ensure reproducibility and facilitate alternative encoding methods if needed.

---

## 3. Feature Engineering

To prepare categorical features for modeling, we applied label encoding. The encoding was customized based on feature types and scales:

1. **Handling Missing Values**: Encoded all "Missing" values as `0`.
2. **Feature Grouping and Encoding**:
   - **Quality-related Features**: Encoded on a scale from 1 to 5, ranging from Poor to Excellent, covering 10 features.
   - **Good-to-Bad Features**: Assigned values from low to high quality across 7 features.
   - **Other Features**: Encoded appropriately based on their role in modeling.

After encoding, we saved the transformed dataset as `encoding_data.csv` for modeling use.

---

## 4. Data Splitting

The processed data was split into training and test sets with an 85/15 ratio. This larger training set size enhances model learning, particularly given the limited dataset size. To maintain an unbiased evaluation, we applied data augmentation only to the training data, leaving the test set untouched as a representative sample for real-world cases.

---

## 5. Feature Selection

After data splitting, we identified relevant features for predicting SalePrice using two methods:

### *1. Correlation Analysis*
   - We focused on features with a Pearson’s r correlation coefficient of at least 0.3 with SalePrice. This threshold balances relevance with simplicity, retaining features with moderate associations without over-complicating the model.

### *2. Lasso Regression*
   - To refine feature selection further, we applied Lasso regression, using LassoCV to find the optimal regularization level. Standardized features were used to ensure consistent scaling. We set a high importance threshold of 0.1, and only one feature was removed, reinforcing the relevance of those identified in the correlation analysis.

---

## 6. Data Augmentation

The selected features were passed through the `augment_data_with_perturbations` function for data augmentation, which introduces slight variations in key features. This approach is intended to enhance model generalization by simulating small real-world changes in the data. Key augmentation parameters:

- **Perturbation Percentage**: Set at 0.02 to ensure variations remain within 2% of original feature values, maintaining data realism.
- **Augmented Records**: Generated 2000 synthetic records, balancing data diversity with computational efficiency.

---

## 7. Model Selection and Training

For model selection, we experimented with regression, tree-based models, and neural networks. **Lasso regression** and **tree-based models** were chosen for their interpretability and performance. Hyperparameters were fine-tuned to optimize performance while avoiding overfitting.

---

## 8. Evaluation Metrics

To assess model performance, we used **Root Mean Squared Error (RMSE)** and **Mean Absolute Error (MAE)**, as both metrics provide insight into prediction accuracy and error magnitudes. These metrics help in evaluating model generalization and guiding further tuning.

---

## 9. Experimentation and Results

Several experiments were conducted to evaluate feature impact and model configurations. Through these, we achieved:
- An optimal balance between accuracy and complexity.
- Improved performance using data augmentation, which increased model robustness.

---

## 10. References and Resources

- **[Data Definition Document](https://docs.google.com/spreadsheets/d/1XL6LJVgLLU27yV7a_oh2zuqhGOI3Syg-jWpmr0Ekk14/edit?usp=sharing)**
- **[Data Documentation](http://jse.amstat.org/v19n3/decock/DataDocumentation.txt)**
- **Research Papers and Resources on Data Augmentation and Feature Selection Techniques**

