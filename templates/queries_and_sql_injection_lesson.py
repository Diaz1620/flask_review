# Including variables in our query using prepared statement to protect from security issues
query = "INSERT INTO friends (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s );"

#key names on data dictionary must be same as the variable names used in query
data = {
    "first_name": "Adrien",
    "last_name": "Dion",
    "email": "adion@testemail.com"
}