# wine_not

## Project description

The aim of the project is to explore the relationship between various independent variables and the target variable (wine quality), and build models to predict wine quality based on these variables.

## Project Goals
- To discover features that give wine a quality level
- Use Clustering to discover new features 
- Build a classifaction model to predict quality

# Initial Thoughts 
- Wine quality could be determined by several different varibles like alcohol precentage and acidity 

# Planning

## Data Acquisition
The dataset used for this project was obtained from Data.World's Wine Quality Dataset (https://data.world/data-society/wine-quality-dataset). The dataset contains separate CSV files for red and white wines, with information on several wine properties.
## Data Preparation
- Combine Red and White Wine CSVs: Merge the two separate CSV files for red and white wines into a single DataFrame, adding a new column called color to indicate whether each observation corresponds to a red or white wine.

- Check Column Data Types: Ensure that each column's data type is appropriate for the data it contains. If necessary, convert columns to appropriate data types.

- Investigate Missing Values: Identify and handle any missing values in the dataset. Possible strategies include dropping rows with missing values or filling in the missing values using appropriate methods (e.g., mean, median, or mode).

- Binned quality score into 3 categories
    - Low (3, 4, 5)
    - Medium (6)
    - High(7, 8, 9)

- Split the data into train, validate and Test


## Data Exploration
- Explore Variable Interactions: Investigate the relationship between independent variables and the target variable (wine quality) using visualization techniques (e.g., scatter plots, box plots) and statistical testing (e.g., correlation coefficients, ANOVA).

- Clustering Analysis: Use clustering techniques to explore the data and determine whether the clusters provide any meaningful insights. Perform the following steps:

- Test at least three combinations of features for clustering.
- Use statistical testing and visualization methods to support your conclusions about the usefulness of the clusters.



## Modeling

Model Evaluation: Compare the performance of the different models using appropriate evaluation metrics (e.g., accuracy, precision, recall, F1-score, mean squared error).
- Baseline: 43% on Accuracy

#### Models fit on train data and cross validated with validate
- Decision Tree
- Random Forest
- Logistic Regression
- KNN 

# Draw Conclusions
After completing these steps, and analyzing the results the Decision tree had the best results. 
- Accuracy: Train - 64% 
- Accuracy: Validate - 58%
### Test
- Accuracy: Test - 57%


# Data Dictionary

<table>
  <thead>
    <tr>
      <th>Feature</th>
      <th>Value</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Fixed Acidity</td>
      <td>Numeric</td>
      <td>The amount of fixed acids in wine (g/dm³)</td>
    </tr>
    <tr>
      <td>Volatile Acidity</td>
      <td>Numeric</td>
      <td>The amount of volatile acids in wine (g/dm³)</td>
    </tr>
    <tr>
      <td>Citric Acid</td>
      <td>Numeric</td>
      <td>The amount of citric acid in wine (g/dm³)</td>
    </tr>
    <tr>
      <td>Residual Sugar</td>
      <td>Numeric</td>
      <td>The amount of residual sugar in wine (g/dm³)</td>
    </tr>
    <tr>
      <td>Chlorides</td>
      <td>Numeric</td>
      <td>The amount of chlorides in wine (g/dm³)</td>
    </tr>
    <tr>
      <td>Free Sulfur Dioxide</td>
      <td>Numeric</td>
      <td>The amount of free sulfur dioxide in wine (mg/dm³)</td>
    </tr>
    <tr>
      <td>Total Sulfur Dioxide</td>
      <td>Numeric</td>
      <td>The amount of total sulfur dioxide in wine (mg/dm³)</td>
    </tr>
    <tr>
      <td>Density</td>
      <td>Numeric</td>
      <td>The density of wine (g/cm³)</td>
    </tr>
    <tr>
      <td>pH</td>
      <td>Numeric</td>
      <td>The pH value of wine</td>
    </tr>
    <tr>
      <td>Sulphates</td>
      <td>Numeric</td>
      <td>The amount of sulphates in wine (g/dm³)</td>
    </tr>
    <tr>
      <td>Alcohol</td>
      <td>Numeric</td>
      <td>The alcohol content of wine (% vol)</td>
    </tr>
    <tr>
      <td>Quality</td>
      <td>Numeric (0-10)</td>
      <td>The sensory quality score of wine</td>
    </tr>
  </tbody>
</table>


# Steps To Reproduce
- Clone repo
- Run Notebook


# Takeaways and Conclusions
- Could not use clustering as a feature building method
- Modeling on test data was 57% 
- 13% better then baseline
#### Features that were drivers of quality
- volatile acidity
- chlorides
- density
- alcohol

 

# Next Steps and Recommendations
- Investigate Outliers: Examine the dataset for any outliers and determine the best course of action to handle them, such as removing or replacing them.
- Re-examine clustering once outliers are removed