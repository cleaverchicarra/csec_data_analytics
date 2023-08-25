# Project 1: Database Indexing

## Overview

In this assignment, you will establish your application and database environment to be used throughout the semester. 
The main objective is to understand and analyze database performance variations with and without the use of indexing.

## Prerequisites
Ensure that the following tools are downloaded and installed on your machine:

- **Python 3.11**: [Download here](https://www.python.org/downloads/)
- **PyCharm**: [Download here](https://www.jetbrains.com/pycharm/)
  - *Note*: Students have a free offer for the professional license. More details [here](https://www.jetbrains.com/pycharm/buy/?var=1#students).
- **MongoDB and Compass**: [Download here](https://www.mongodb.com/try/download/community)
- **GitHub Desktop**: [Download here](https://desktop.github.com/)

While a Cyber Arena server will be made available for those who require it, local installations are recommended if 
possible.

## Setup Steps

1. **Clone the Repository**: Use the following link to clone the repository to your local development setup:
   - [csec_data_analytics Repository](https://github.com/pdhuff/csec_data_analytics.git)
   - For those using GitHub Desktop: [Open in GitHub Desktop](x-github-client://openRepo/https://github.com/pdhuff/csec_data_analytics)

2. **Environment Configuration**: Carefully review the README file in the cloned repository to configure your Django 
and MongoDB environments.

3. **Database Initialization**:
   - After successfully setting up Django and MongoDB, execute the management command `project1_init_database`. This will populate your MongoDB with 100,000 user documents.
   - Utilize MongoDB Compass to inspect these records.

4. **Performance Analysis**:
   - Execute the management command `project1_get --field last_name --value <YOUR_CHOSEN_LAST_NAME>`. Take note of the runtime.
   - Now, implement an index for the `last_name` field and re-run the above command. Observe any changes in the runtime.

## Assignment Questions

1. Explain the performance difference observed before and after the index creation.
2. Detail the size of the index and describe the content being stored.
3. Accurately denote the correct Landeau symbol for the provided relations.

## Submission Guidelines

Prepare a comprehensive report containing:

- A cover page with your:
  - Name
  - Date
  - Course number
- Detailed responses to each of the assignment questions.
- Relevant screenshots showcasing the execution tests and the configured indices in MongoDB Compass.