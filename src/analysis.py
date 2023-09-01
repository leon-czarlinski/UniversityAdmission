#Leon Czarlinski, n01541167
import pandas as pd
df = pd.read_csv("../data/Customers.csv")

#Give average income of all customers

average_income = df['annual_income'].mean()
average_income = round(average_income,2)
print(f"Average income is $ {average_income:.2f}")

#Give highest in come of all females
female_customers = df[df['gender'] == 'Female']
highest_income = female_customers['annual_income'].max()
highest_income = round(highest_income,2)
print(f"Highest female income is $ {highest_income:.2f}")

#Give lowest income of all males
male_customers = df[df['gender'] == 'Male']
lowest_income = male_customers['annual_income'].min()
lowest_income = round(lowest_income,2)
print(f"Lowest male income is $ {lowest_income:.2f}")

#What is the average age of all artists
artists = df[df['profession'] == 'Artist']
average_age = artists['age'].mean()
average_age = round(average_age,2)
print(f"the average age of all artists is {average_age:.2f}")

#How many male lawyers are there in the database
male_lawyers = df[(df['gender'] == 'Male') & (df['profession'] == 'Lawyer')]
count_male_lawyers = male_lawyers['custm_id'].count()
print(f"The number of male lawyers are: {count_male_lawyers}")

#find all males who have work experience more than 5 years and are lawyers
lawyers_exp = df[(df['profession'] == 'Lawyer') & (df['work_exp'].astype(float) >= 5) & (df['gender'] == 'Male')]
print(lawyers_exp)

#find correlation between age and income
corr_age_income = df['age'].corr(df['annual_income'])
corr_age_income = abs(corr_age_income)
print(f"The correlation between age and income is {corr_age_income:.5f}")

#find correlation between spending scores and all revelant features. 
#Which is the feature with the highest correlation 
corr_spend_score_work_exp = abs(df['spend_score'].corr(df['work_exp']))
corr_spend_score_fam_size = abs(df['spend_score'].corr(df['fam_size']))
corr_spend_score_annual_income = abs(df['spend_score'].corr(df['annual_income']))
corr_spend_score_age = abs(df['spend_score'].corr(df['age']))

find_max = [corr_spend_score_work_exp, corr_spend_score_fam_size, corr_spend_score_annual_income, corr_spend_score_age]
max_correlation = max(find_max)

print(f"Absolute correlation between Spend Score and WorkExperience is: {corr_spend_score_work_exp:.5f}")
print(f"Absolute correlation between Spend Score and Family Size is: {corr_spend_score_fam_size:.5f}")
print(f"Absolute correlation between Spend Score and Annual Income is: {corr_spend_score_annual_income:.5f}")
print(f"Absolute correlation between Spend Score and Age is: {corr_spend_score_age:.5f}")
print(f"Maximum correlation: {max_correlation:.5f}")