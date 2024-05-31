import pandas as pd
import openpyxl
from openpyxl import load_workbook
import lxml
from configparser import ConfigParser
import time
import os, sys

# Import SLO Participation report
faculty_TAs_df = pd.read_csv(
    'C:/Users/fmixson/Desktop/FTEF Reporting/Fall 2023 TAs.csv', encoding='latin-1')
# C:\Users\fmixson\Desktop\FTEF Reporting\Comprehensive Teaching Assignment File - Fall 2023.csv
# faculty_TAs_df = faculty_TAs_df[faculty_TAs_df]
pd.set_option('display.max_columns', None)
faculty_TAs_df = faculty_TAs_df.fillna(0)
agg_functions = {'RG FTE%': 'sum', 'OL FTE%': 'sum' }
print(faculty_TAs_df)

faculty_TAs_df = faculty_TAs_df.groupby(faculty_TAs_df['Class#']).aggregate(agg_functions)

#create new DataFrame by combining rows with same id values
# df_new = df.groupby(df['employee_id']).aggregate(agg_functions)

#Display the new data frame
# print(df_new)

# faculty_TAs_df.groupby('Class#')
# course_sections_df = faculty_TAs_df[faculty_TAs_df['Course or Section'].str.contains('Section', na=False)]
# course_sections_df[['Course', 'Class#','Delete', 'To Be Deleted']] = course_sections_df['Course or Section'].str.split(' ', expand=True)
# course_sections_df[['Completed', 'Of', 'Total Assessments']] = course_sections_df['Completed Assessments'].str.split(' ', expand=True)
# df[['First Name', 'Last Name']] = df['Name'].str.split(' ', expand=True)
# course_sections_df = course_sections_df[course_sections_df['Class#'] != 'Totals']



# Import merged worksheets
fall_schedule_df = pd.read_csv(
    'C:/Users/fmixson/Desktop/FTEF Reporting/Copy of fte test.csv', encoding='latin-1')
pd.set_option('display.max_columns', None)

# Merge the two worksheets
# print(fall_schedule_df.dtypes, course_sections_df.dtypes)
# fall_schedule_df['Class#'] = fall_schedule_df['Class#'].astype('str')
# course_sections_df['Completed'] = course_sections_df['Completed'].astype('float')
# course_sections_df['Total Assessments'] = course_sections_df['Total Assessments'].astype('float')
merged_df = pd.merge(fall_schedule_df, faculty_TAs_df, on=['Class#'])

merged_df = merged_df[['STRM','Div', 'Dept','COURSE', 'Class#', 'FTES_TEST', 'FTEF_TEST', 'RG FTE%', 'OL FTE%']]

merged_df['Total FTE%'] = merged_df['RG FTE%'] + merged_df['OL FTE%']

#define how to aggregate various fields
# agg_functions = {'employee_name': 'first', 'sales': 'sum', }

#create new DataFrame by combining rows with same id values
# df_new = merged_df.groupby(merged_df['Class#'])


# merged_df['Completed'] = merged_df['Completed'].astype(int)
# print(merged_df.dtypes)
# merged_df['Total Assessments'] = merged_df['Total Assessments'].astype(int)
# df[["a", "b"]] = df[["a", "b"]].apply(pd.to_numeric)
merged_df.to_excel('FTES_FTEF_dataframes.xlsx')
