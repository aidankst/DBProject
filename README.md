# DBProject
Project for Database (Fourth Semester - AGH UST)

Prepared by Min Khant Soe Oke, Kaung Sithu

- Min Khant Soe Oke
- oke@student.agh.edu.pl
- 414176

- Kaung Sithu
- sithu@student.agh.edu.pl
- 414175

Preparation for Tasks

1. Install PostgreSQL: Depending on your operating system, you can download and install PostgreSQL from the official website (https://www.postgresql.org/download/). Follow the instructions provided for your specific platform.

2. Create a new database: After installing PostgreSQL, open the terminal or command prompt and run the following command to create a new database called `taxonomy_db`:

   ```
   createdb taxonomy_db
   ```

3. To import the CSV data into our PostgreSQL database, we first need to create a table to store the data. We will create a table called `taxonomy` with two columns: `category` and `subcategory`. Both columns will be of type `VARCHAR`.

    ```sql
    CREATE TABLE taxonomy (
        category VARCHAR(255),
        subcategory VARCHAR(255)
    );
    ```

4. Now that we have our table set up, we can import the CSV data into the `taxonomy` table. We will use the `COPY` command in PostgreSQL to import the data from the CSV file. Make sure to decompress the `taxonomy_iw.csv.gz` file before importing it.

    ```sql
    COPY taxonomy (category, subcategory)
    FROM '/path/to/your/file/taxonomy_iw.csv'
    DELIMITER ',' CSV HEADER;
    ```
5. You can also create a python file to copy the data from csv file. Run the python script to import the CSV data into the database: 

    ```
    python import_data.py --csv taxonomy_iw.csv.gz --db <database_name> --user <username> --password <password>
    ```

6. **Using the utility:**

The utility can be run using the following command: `python taxonomy_utility.py --db <database_name> --user <username> --password <password> <action> <node_name>`.

Replace `<action>` with one of the following options:

- `find_children`: Find all children of a given node.
- `count_children`: Count all children of a given node.
- `find_grandchildren`: Find all grandchildren of a given node.
- `find_parents`: Find all parents of a given node.
- `count_parents`: Count all parents of a given node.
- `find_grandparents`: Find all grandparents of a given node.
- `count_unique_nodes`: Count how many uniquely named nodes there are.
- `find_root_nodes`: Find a root node, one which is not a subcategory of any other node.
- `find_most_children`: Find nodes with the most children.
- `find_least_children`: Find nodes with the least children.
- `rename_node`: Rename a given node. Provide the new name as an additional argument.

Replace `<node_name>` with the name of the node you want to perform the action on.

**Examples:**

- To find all children of the "1880s_films" node: `python utility.py --db <database_name> --user <username> --password <password> find_children 1880s_films`.
- To count all parents of the "1889_films" node: `python utility.py --db <database_name> --user <username> --password <password> count_parents 1889_films`.
- To rename the "1880s_films" node to "1880s_movies": `python utility.py --db <database_name> --user <username> --password <password> rename_node 1880s_films 1880s_movies`.


