import mysql.connector
import time

# Database Connection
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="college_dbs"
)

cur = connection.cursor()

# 56. Demonstrate N+1 Query Problem

print("----- Version 1 : N+1 Queries -----")

queries = 0
start_time = time.time()

cur.execute("SELECT student_id FROM enrollments")
student_ids = cur.fetchall()
queries += 1

for sid in student_ids:
    cur.execute("SELECT first_name, last_name FROM students WHERE student_id=%s", sid)
    print(cur.fetchone())
    queries += 1

end_time = time.time()

print(f"\nTotal Queries : {queries}")
print(f"Time Taken    : {end_time-start_time:.6f} seconds")


# 57. Solve N+1 Using JOIN

print("\n----- Version 2 : JOIN -----")

queries = 0
start_time = time.time()

sql = """
SELECT s.first_name,
       s.last_name,
       c.course_name
FROM students s
JOIN enrollments e ON s.student_id=e.student_id
JOIN courses c ON e.course_id=c.course_id
"""

cur.execute(sql)
queries += 1

for record in cur.fetchall():
    print(record)

end_time = time.time()

print(f"\nTotal Queries : {queries}")
print(f"Time Taken    : {end_time-start_time:.6f} seconds")


# 58. Comparison

print("\nComparison")
print("-------------------------")
print("N+1 Version  : Multiple database calls")
print("JOIN Version : Single database call")
print("JOIN reduces unnecessary database requests.")


# 59. Observation

print("\nObservation")
print("-------------------------")
print("For 10,000 enrollments:")
print("N+1 Approach  -> 10,001 Queries")
print("JOIN Approach -> 1 Query")

cur.close()
connection.close()


"""
----- Version 1 : N+1 Queries -----

('Arjun', 'Mehta')
('Arjun', 'Mehta')
('Priya', 'Suresh')

Total Queries : 13
Time Taken    : 0.007945 seconds


----- Version 2 : JOIN -----

('Arjun', 'Mehta', 'Data Structures')
('Arjun', 'Mehta', 'Database Systems')

Total Queries : 1
Time Taken    : 0.001214 seconds


Comparison
-------------------------
N+1 Version  : Multiple database calls
JOIN Version : Single database call
JOIN reduces unnecessary database requests.


Observation
-------------------------
For 10,000 enrollments:
N+1 Approach  -> 10,001 Queries
JOIN Approach -> 1 Query
"""