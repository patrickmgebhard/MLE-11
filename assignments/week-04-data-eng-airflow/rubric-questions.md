## Week-04 Rubric Questions

**Algorithm Understanding</br>
Feature selection methods are intended to reduce the number of input variables to those that are believed to be most useful to a model in order to predict the target variable. What algorithms can be used to automatically select the most important features (regression, etc..)? Describe at least 3?**

Answer:</br>
There are three common feature selection strategies: filter methods, wrapper methods and embedded methods.</br>
In filter methods features are selected based on their scores in various statistical tests (e.g. Pearson’s correlation, Spearman’s rank, etc.) for their correlation with the outcome variable.</br>
In wrapper methods, we use a subset of features and train a model with them. Then we decide to remove or add features from the subset based on the results and repeat the cycle. This is computationally very expensive.</br>
Embedded methods combine the qualities of filter and wrapper methods. They are implemented as algorithms that have their own built-in feature selection methods e.g. LASSO and RIDGE.</br>


**Interview Readiness</br>
Explain data leakage and overfitting (define each)?
Explain the effect of data leakage and overfitting on the performance of an ML model.**

Answer:</br>
Data leakage is when information about the target variable is leaking into the input of the model during training. So, the model will rely on data that will not be available in the ongoing data that we want to predict on.</br>
Overfitting means that the model models the training data too well.</br>

Data leakage inflates the model performance estimates. The model will not perform as expected because the actual that we’ll make predictions on does not have the same information about the target variable as the training data.</br>
Overfitting will cause the model to not generalize to other data points outside the test data very well and hence perform poorly.</br>

**Interview Readiness</br>
Explain what our outliers in your data?
Explain at least two methods to deal/treat outliers in your data?**

Answer:</br>
An outlier is a data point that differs a lot from the other data points.</br>
You can remove outliers from the data set or change the variable into a categorical variable and then put the outliers in one of the categories.</br>

**Interview Readiness</br>
What is feature scaling and why is it important to our model?</br>
Explain the difference between Normalization and Standardization?**

Answer:</br>
Feature scaling is a technique that involves transforming the features into a common range or scale. This is necessary because some models are sensitive to the scale of input features such as neural networks. Feature scaling can improve model performance and model interpretability.</br>

Normalization means to rescale the values into a range of [0,1]. Standardization means to rescale data to have a mean of 0 and a standard variation of 1.</br>
