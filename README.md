# cc98-tornado
A tornado version forum of cc98 for ZJU

1. install all required modules:
	
	```
	shell> pip install -r requirements.txt
	```

2. create database and then exec sql file in the dbstrucutre directory

  ```
  shell> mysql -u USERNAME -p

  mysql> create databases DBNAME;
  mysql> exit

  shell> mysql -u USERNAME -p --database=DBNAME < dbstructure/SQL.sql
  ```

