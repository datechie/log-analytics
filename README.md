# Udacity FSND Project - Log Analytics
The project connects to multiple tables in the news Postgresql DB to produce reports. The project contains the following files:
* **analysis.py**  - Python script to connect to the DB and print out the results.
* **README.md** -  This file specifies details about the project and how to run the script.
* **sample-output.txt** - This file contains the sample output. 

# Requirements
* Python 2.7 (Not tested with other versions of Python)
* Postgresql instance with the **news** database loaded

# Install
* Clone the repository using the command
  `git clone https://github.com/datechie/log-analytics.git`

# Setup
Run the following commands while connected to the **news** database using postgresql in the order specified below.

1. This view is for the first result 
- `create view titles as select split_part(path, '/', 3) as title, status, time, id from log where path LIKE '/article/%';`

2. This view is for the second result
- `create view author_titles as select b.author, count(*) as num from titles as a, articles as b where b.slug like a.title group by b.author order by num desc;`

3. These 3 views are for the final result
- `create view date_requests_errors as select date(time) as error_view_date, count(*) as num, status from log where status not like '200%' group by error_view_date, status order by error_view_date asc;`

- `create view date_requests_total as select date(time) as total_view_date, count(*) as num from log group by total_view_date order by total_view_date asc;`

- `create view final as select a.error_view_date as request_date, a.num as errors, b.num as total, (a.num::float * 100)/(b.num::float) as percent from date_requests_errors as a, date_requests_total as b where a.error_view_date = b.total_view_date;`


# How to run the Script
- `cd log-analytics`
- `python analysis.py` **OR** `python2.7 analyis.py`


# Output
- The included sample-output.txt file shows the example results.
# Udacity FSND Project - Log Analytics
The project connects to multiple tables in the news Postgresql DB to produce reports. The project contains the following files:
* **analysis.py**  - Python script to connect to the DB and print out the results.
* **README.md** -  This file specifies details about the project and how to run the script.
* **sample-output.txt** - This file contains the sample output. 

# Requirements
* Python 2.7 (Not tested with other versions of Python)
* Postgresql instance with the **news** database loaded

# Install
* Clone the repository using the command
  `git clone https://github.com/datechie/log-analytics.git`

# Setup
Run the following commands while connected to the **news** database using postgresql in the order specified below.

1. This view is for the first result 
- `create view titles as select split_part(path, '/', 3) as title, status, time, id from log where path LIKE '/article/%';`

2. This view is for the second result
- `create view author_titles as select b.author, count(*) as num from titles as a, articles as b where b.slug like a.title group by b.author order by num desc;`

3. These 3 views are for the final result
- `create view date_requests_errors as select date(time) as error_view_date, count(*) as num, status from log where status not like '200%' group by error_view_date, status order by error_view_date asc;`

- `create view date_requests_total as select date(time) as total_view_date, count(*) as num from log group by total_view_date order by total_view_date asc;`

- `create view final as select a.error_view_date as request_date, a.num as errors, b.num as total, (a.num::float * 100)/(b.num::float) as percent from date_requests_errors as a, date_requests_total as b where a.error_view_date = b.total_view_date;`


# How to run the Script
- `cd log-analytics`
- `python analysis.py` **OR** `python2.7 analyis.py`


# Output
- The included sample-output.txt file shows the example results.
