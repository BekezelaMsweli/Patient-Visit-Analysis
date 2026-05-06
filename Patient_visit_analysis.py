import pandas as pd
import matplotlib.pyplot as plt

#load csv file data
df = pd.read_csv("patient_visits_dataset.csv", sep=";")

#view first 10 raws
print(df.head(10))

#view column labels
print(df.columns)

#Prepare your data first
df["visit_datetime"] = pd.to_datetime(df["visit_datetime"])

#extract useful time features
df["hour"] = df["visit_datetime"].dt.hour
df["day_of_week"] = df["visit_datetime"].dt.day_name()
df["month"] = df["visit_datetime"].dt.month

#MOST COMMON DIAGNOSES, Top 1000
top_diagnosis = df["diagnosis"].value_counts().head(10)
print(top_diagnosis)

#MOST BUSY DEPARTMENTS
top_departments = df["department"].value_counts().head(10)
print(top_departments)

#Gender distribution
gender_base = (df['gender'].value_counts(normalize=True) * 100).round(2) #print as percentage
print(gender_base)

#tital visit per day
visits_per_day = df["day_of_week"].value_counts()

#total visit per hour
visits_per_hour = df["hour"].value_counts().sort_index()

#visits over time
visits_over_time = df.groupby(df["visit_datetime"].dt.date).size()

#diagnosis per department
diag_dept = df.groupby(["department", "diagnosis"]).size().unstack().fillna(0)
print(diag_dept)

#Visualizations
#Bar char showing top diagnosis
ax = top_diagnosis.plot(kind='bar', color='orange')

plt.title("Top Diagnoses")
plt.xlabel("Diagnosis")
plt.ylabel("Number of Patients")

plt.xticks(rotation=45)
# add labels on top of bars
ax.bar_label(ax.containers[0])

plt.show()

#Top department
ax = top_departments.plot(kind='bar', color='green')

plt.title("Top Departments")
plt.xlabel("Departments")
plt.ylabel("Number of Patients")

plt.xticks(rotation=45)
# add labels on top of bars
ax.bar_label(ax.containers[0])

plt.show()

#plot for total visit per day
ax = visits_per_day.plot(kind='bar', color='skyblue')
ax.bar_label(ax.containers[0])

plt.title("Patient Visits per Day of Week")
plt.xlabel("Day")
plt.ylabel("Number of Visits")
plt.xticks(rotation=45)

plt.show()

#gender distribution
ax = gender_base.plot(kind="pie", autopct='%1.1f%%', startangle=90, figsize=(6,6))

plt.title("Gender Distribution (%)")
plt.ylabel("")
plt.show()

#visits per hour to check busiest hour
ax = visits_per_hour.plot(kind='bar', color='purple')
ax.bar_label(ax.containers[0])

plt.title("Patient Visits per Hour")
plt.xlabel("Hour of Day")
plt.ylabel("Number of Visits")

plt.show()

#visits over time (line graph)
visits_over_time.plot(kind='line', marker='o')

plt.title("Daily Patient Visits Trend")
plt.xlabel("Date")
plt.ylabel("Number of Visits")

plt.xticks(rotation=45)
plt.show()

print("######################################################################################################")
def generate_summary(df, top_diagnosis, top_departments):
    print("\n===== SUMMARY REPORT =====")
    print(f"Total Patients: {len(df)}")
    print(f"Most Common Diagnosis: {top_diagnosis.idxmax()}")
    print(f"Most Busy Department: {top_departments.idxmax()}")
    print(f"Peak Hour: {df['hour'].value_counts().idxmax()} {":00"}")
generate_summary(df, top_diagnosis, top_departments)
