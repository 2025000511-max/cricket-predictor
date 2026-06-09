import pandas as pd
import numpy as np  # Set a seed for reproduci np.ran num_students = 100
 # Generate synthetic data
data = { 
     'student_id': range(1, num_students + 1),
     'discipline': np.random.choice(['Good', 'Average', 'Poor'], size=num_students),
     'attendance': np.random.randint(80, 100, size=num_students),       
     'homework_completion': np.random.choice([True, False], size=num_students),
     'exam_score': np.random.normal(loc=50, scale=15, size=num_students)
 }
 
 # Create DataFrame
df = pd.DataFrame(data)

 # Calculate marks based on discipline and attendance
def calculate_marks(row):
     base_mark = 60  # Base mark for each student
     if row['discipline'] == 'Good':
         base_mark += 10
     elif row['discipline'] == 'Average':
         base_mark += 5
         attend_factor = row['attendance'] / 100.
         homework_factor = 1.5 if row['homework_completion'] else 0.5
     else:
         attend_factor = row['attendance'] / 100.
         homework_factor = 1.5 if row['homework_completion'] else 0.5

     return int(base_mark * (attend_factor + homework_factor))
df['marks'] = df.apply(calculate_marks, axis=1)
df.to_csv('student_marks.csv', index=False)