##Week-05 Rubric Questions

**Algorithm Understanding</br>
How does the Gradient-Boosted Tree Algorithm work in Classification? How does Gradient Boost differ from AdaBoost and Logistic Regression?**

Answer: </br>
Gradient Boosting is an ensemble learning algorithm, which means that it uses an ensemble of “weaker” models to build a strong model for regression, classification or ranking. Gradient Boosting has three main components: the loss or cost function, the weak learner and the additive model. When the Gradient-Boosted Tree Algorithm is used for Classification, then the cost function is Log loss.

The main difference between Gradient Boosting and AdaBoost is that Gradient Boosting is a generic algorithm to find approximate solutions to the additive modeling problem. In contrast, AdaBoost is a special case with a particular loss function. So, Gradient Boosting is more flexible.

The main difference between Gradient Boosting and Logistic Regression is that Gradient Boosting uses an ensemble of weaker models to create a strong model on the given data, but logistic regression uses a generalized linear equation to describe the directed dependencies among a set of variables.

**Interview Readiness</br>
What is a Delta Lake and how does it offer a solution to building reliable data pipelines?**

Answer:</br>
Delta Lake is a storage layer that allows the storage of data (unstructured) and tables (structured) in Databricks. It is compatible with Apache Spark APIs and allows to use a single copy of data for stream and batch processing and provides incremental streaming processing at scale.

**Interview Readiness</br>
When working with Pandas, we use the class pandas.core.frame.DataFrame and when working with the pandas API in Spark, we use the class pyspark.pandas.frame.DataFrame, are these the same, explain why or why not?**

Answer:</br>
Dataframes represent a table of data with rows and columns. This never changes in any programming language. However, these two are not the same because the Spark DataFrame makes use of the distributed computing capabilities of Apache Spark including use of parallelization and use of multiple nodes, which allows to build scalable applications that can process large amounts of data.

**Interview Readiness
What is a Machine Learning Pipeline is and why it’s important? What are the steps in a Machine Learning workflow?**

Answer:</br>
A machine learning pipeline is the end-to-end construct that takes raw data input (e.g. an image) and then creates an output (e.g. a classification of content in the image). It includes the raw data input, features, outputs, the machine learning model, model parameters and prediction outputs.</br>
There are three main steps in the machine learning workflow with several sub-steps: 1 Data Engineering, 2 Model Engineering and 3 Model Deployment.

Data Engineering consists of:
1. Data Ingestion
2. Data exploration and validation
3. Data Wrangling (Cleaning)
4. Data Labeling
D5. ata Splitting


Model Engineering consists of:
1. Model Training
2. Model Evaluation
3. Model Testing
4. Model Packaging


Model Deployment consists of:
1. Model Serving
2. Model Performance Monitoring
3. Model Performance Logging
