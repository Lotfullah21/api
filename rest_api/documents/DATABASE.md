```sh
# to connect to postgres
pip install psycopg2-binary
# to install debut toolbar
pip install django-debug-toolbar
# to install drf
pip install djangorestframework
```

# Database

A **database** is an organized collection of data that is stored and accessed electronically. Databases are designed to manage, store, and retrieve data efficiently, allowing users to perform various operations on that data. Here are some key aspects of databases:

## Key Components of a Database

1. **Data**: The actual information stored in the database, which can include text, numbers, images, and more.

2. **Database Management System (DBMS)**: Software that facilitates the creation, manipulation, and administration of the database.  
   **Examples**: MySQL, Oracle, MongoDB.

3. **Schema**: The structure that defines how data is organized within the database, including tables, fields, data types, and relationships.

4. **Tables**: In relational databases, data is organized into tables, which consist of rows and columns. Each row represents a record, and each column represents an attribute of that record.

5. **Queries**: Commands used to retrieve, insert, update, or delete data from the database, often written in SQL (Structured Query Language) for relational databases.

# Database Management System

A Database Management System (DBMS) is software that allows users to create, manage, and manipulate databases. It serves as an interface between the end users and the database

# Types of DBMS

## 1. Relational DBMS (RDBMS)

Organizes data in tables with rows and columns, using Structured Query Language (SQL) for data manipulation.

**Examples**: MySQL, PostgreSQL, Oracle Database.

## 2. NoSQL DBMS

Designed for unstructured data and supports various data models.  
**Examples**: MongoDB, Cassandra.

## 3. Network DBMS

## 4. Hierarchical DBMS

Organizes data in a tree-like structure with parent-child relationships.  
**Examples**: IBM Information Management System.

Uses a graph structure to allow more complex relationships among data entities.  
**Examples**: Integrated Data Store.

## 5. Object-Oriented DBMS

Integrates object-oriented programming principles with database capabilities.  
**Examples**: db4o.

# Relational Database

Relational databases models data by storing them in columns and rows in tables.
If there are multiple tables, we can create relationships between them and that relationships can be involved in our queries.

# Three major databases in use

- Postgres
- Oracle
- MySql

# SQL

Structured Query Language is the language we use to issue commands to the database.

- Create/insert data
- Read/Select data
- Update data
- Delete Data

| Feature                          | PostgreSQL                                                                   | MySQL                                                                                     |
| -------------------------------- | ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| **ACID Compliance**              | Fully ACID-compliant in all cases                                            | ACID-compliant with InnoDB; limited with other engines (e.g., MyISAM)                     |
| **Data Types and Extensibility** | Wide range of native types (JSON, XML, custom types); highly extensible      | Limited types (added JSON support recently); less extensible                              |
| **Performance and Speed**        | Efficient with complex queries and joins                                     | Generally faster for simple read-heavy operations                                         |
| **Concurrency Support**          | Multi-Version Concurrency Control (MVCC) for high concurrency                | InnoDB supports similar control, but less optimized for high concurrency                  |
| **Replication and Scaling**      | Synchronous and asynchronous replication, supports advanced clustering       | Asynchronous replication by default, supports read replicas and clustering (e.g., Galera) |
| **SQL Standards Compliance**     | High SQL standards compliance, advanced features like window functions, CTEs | Less strict with SQL standards, looser data validation by default                         |
| **Community and Ecosystem**      | Strong open-source community, enterprise-grade focus                         | Large ecosystem, both open-source and commercial support under Oracle                     |
| **Best Use Cases**               | Complex, write-intensive, analytical applications                            | Simple, read-heavy web applications                                                       |

# Database model

A database model or database schema is the structure or format of a database, described in a formal language supported by a database management system.

## Queryset

A queryset is a Django object that represents a collection of data from the database
It allows us to perform database queries, such as fetching, filtering, updating, or deleting records, all through Python code without writing raw SQL.

### Key Points:

Represents Data: A queryset holds database records (rows) as Python objects.
Lazy Execution: Queries are not executed until needed, improving performance.
Chainable: We can build complex queries step by step.
