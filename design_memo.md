# Design memo
## High-level function Design
- Query Prompt
- Query Parser
- Query Engine
- Data loader
- Index
- Data storage

# Read Data
1. Recieved query
2. Parse query which recieved to get columns, table, filter conditions and so on
3. Get a file path of the specified table from memory
4. Read the file to load data on memory
5. Extract data which meet to the specified columns and the filter conditions
6. Show the data
