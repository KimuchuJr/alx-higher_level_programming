In SQL, granting access involves using the `GRANT` statement to provide specific permissions to users or roles on various database objects. The exact syntax can vary slightly depending on the specific database management system you're using, but the general idea remains similar across different systems.

Here's a general example:

### Granting SELECT access on a table

```sql
GRANT SELECT ON table_name TO user_name;
```

This grants the `SELECT` permission on a specific table (`table_name`) to a user (`user_name`). Replace `table_name` with the actual name of the table and `user_name` with the username or role to which you want to grant access.

### Granting multiple permissions

You can grant multiple permissions at once:

```sql
GRANT SELECT, INSERT, UPDATE ON table_name TO user_name;
```

### Granting access to all tables in a database

```sql
GRANT SELECT ON DATABASE database_name TO user_name;
```

Replace `database_name` with the actual name of the database.

### Granting access to all tables in a schema

```sql
GRANT SELECT ON ALL TABLES IN SCHEMA schema_name TO user_name;
```

Replace `schema_name` with the actual name of the schema.

### Granting administrative privileges

Some database systems allow granting administrative privileges like `CREATE`, `DROP`, `ALTER`, etc. These should be used carefully, as they give significant control over the database.

```sql
GRANT CREATE, DROP ON DATABASE database_name TO user_name;
```

### Granting access to specific columns

```sql
GRANT SELECT (column1, column2) ON table_name TO user_name;
```

This grants `SELECT` permission only on specific columns (`column1` and `column2`) of the table (`table_name`).

### Revoking access

To revoke previously granted access, you can use the `REVOKE` statement:

```sql
REVOKE SELECT ON table_name FROM user_name;
```

Always ensure that you grant the minimum necessary permissions to users or roles to follow the principle of least privilege and enhance database security.
