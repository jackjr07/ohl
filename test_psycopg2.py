import psycopg2
connection = psycopg2.connect(
			user = "sysadmin",	
			password = "Jax07",
			host = "localhost",
			port = "5432",
			database = "test.db")

try:
	cursor = connection.cursor()
	print(connection.get_dsn_paramaters(),"\n")

	cursor.execute("SELECT versions();")
	record = cursor.fethone()
	print("You are connected to =", record, "\n")

except(Exception, psycopg2.Error) as error:
	print("FUCKING ERROR")
finally:
	if(connection):
		cursor.close()
		connection.close()
		print("PSY connection is closed")

