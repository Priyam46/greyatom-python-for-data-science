# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading the file
data=pd.read_csv(path)

#Code starts here

# Step 1 
#Reading the file


#Creating a new variable to store the value counts
loan_status=data['Loan_Status'].value_counts()
loan_status.plot(kind='bar',stacked=True, figsize=(15,10))
#Plotting bar plot
plt.show()
# Step 2
#Plotting an unstacked bar plot
property_and_loan=data.groupby('Property_Area')['Loan_Status'].size()
property_and_loan.plot(kind='bar',stacked=False, figsize=(15,10))
plt.xlabel('Property Area')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)
plt.show()

# Step 3
#Plotting a stacked bar plot
education_and_loan=data.groupby('Education')['Loan_Status'].size()
education_and_loan.plot(kind='bar',stacked=True, figsize=(15,10))
plt.xlabel('Education Status')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)
plt.show()
# Step 4 
#Subsetting the dataframe based on 'Education' column
graduate=data['Education'] == 'Graduate'

#Subsetting the dataframe based on 'Education' column
not_graduate=data['Education'] == 'Not Graduate'

#Plotting density plot for 'Graduate'
data['LoanAmount'].plot(kind='density', label='Graduate')
#Plotting density plot for 'Graduate'
data['LoanAmount'].plot(kind='density', label='Not Graduate')

#For automatic legend display


# Step 5
#Setting up the subplots
fig ,(ax_1,ax_2,ax_3)= plt.subplots(nrows = 3 , ncols = 1)

#Plotting scatter plot
ax_1.scatter(data['ApplicantIncome'],data["LoanAmount"])

#Setting the subplot axis title


#Plotting scatter plot
ax_2.scatter(data['CoapplicantIncome'],data["LoanAmount"])

#Setting the subplot axis title


#Creating a new column 'TotalIncome'
add=data['ApplicantIncome']+data['CoapplicantIncome']
data['TotalIncome']=add

#Plotting scatter plot
ax_3.scatter(data['TotalIncome'],data["LoanAmount"])


#Setting the subplot axis title



