import sys
import psycopg2

def connect_to_db():
    conn = psycopg2.connect(
        dbname="taxonomy_db",
        user="sithukaung",
        password="KaungSithu",
        host="localhost",
        port="5432"
    )
    return conn

def find_children(node):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT subcategory FROM taxonomy WHERE category = %s", (node,))
    children = cursor.fetchall()
    cursor.close()
    conn.close()
    return [child[0] for child in children]

def count_children(node):
    return len(find_children(node))

def find_grandchildren(node):
    children = find_children(node)
    grandchildren = []
    for child in children:
        grandchildren.extend(find_children(child))
    return grandchildren

def find_parents(node):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT category FROM taxonomy WHERE subcategory = %s", (node,))
    parents = cursor.fetchall()
    cursor.close()
    conn.close()
    return [parent[0] for parent in parents]

def count_parents(node):
    return len(find_parents(node))

def find_grandparents(node):
    parents = find_parents(node)
    grandparents = []
    for parent in parents:
        grandparents.extend(find_parents(parent))
    return grandparents

def count_unique_nodes():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT category) + COUNT(DISTINCT subcategory) FROM taxonomy")
    unique_nodes = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return unique_nodes

def find_root_nodes():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT category FROM taxonomy WHERE category NOT IN (SELECT DISTINCT subcategory FROM taxonomy)")
    root_nodes = cursor.fetchall()
    cursor.close()
    conn.close()
    return [root_node[0] for root_node in root_nodes]

def find_most_children_nodes():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT category, COUNT(subcategory) as child_count FROM taxonomy GROUP BY category ORDER BY child_count DESC")
    nodes = cursor.fetchall()
    cursor.close()
    conn.close()
    max_children = nodes[0][1]
    return [node[0] for node in nodes if node[1] == max_children]

def find_least_children_nodes():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT category, COUNT(subcategory) as child_count FROM taxonomy GROUP BY category ORDER BY child_count ASC")
    nodes = cursor.fetchall()
    cursor.close()
    conn.close()
    min_children = nodes[0][1]
    return [node[0] for node in nodes if node[1] == min_children]

def rename_node(old_name, new_name):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE taxonomy SET category = %s WHERE category = %s", (new_name, old_name))
    cursor.execute("UPDATE taxonomy SET subcategory = %s WHERE subcategory = %s", (new_name, old_name))
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    operation = sys.argv[1]
    node = sys.argv[2]

    if operation == "find_children":
        print(find_children(node))
    elif operation == "count_children":
        print(count_children(node))
    elif operation == "find_grandchildren":
        print(find_grandchildren(node))
    elif operation == "find_parents":
        print(find_parents(node))
    elif operation == "count_parents":
        print(count_parents(node))
    elif operation == "find_grandparents":
        print(find_grandparents(node))
    elif operation == "count_unique_nodes":
        print(count_unique_nodes())
    elif operation == "find_root_nodes":
        print(find_root_nodes())
    elif operation == "find_most_children_nodes":
        print(find_most_children_nodes())
    elif operation == "find_least_children_nodes":
        print(find_least_children_nodes())
    elif operation == "rename_node":
        new_name = sys.argv[3]
        rename_node(node, new_name)
        print(f"Node '{node}' renamed to '{new_name}'")
    else:
        print("Invalid operation")