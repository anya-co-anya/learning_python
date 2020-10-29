import sqlite3


staff_data = [("William", "Shakespeare", "m", "1961-10-25"),
               ("Frank", "Schiller", "m", "1955-08-17"),
               ("Jane", "Wall", "f", "1989-03-14")]


create_table = '''
    CREATE TABLE worker
    (id integer primary key,
    first_name integer varchar(30),
    last_name integer varchar(30),
    gender CHAR(1),
    birth_date DATE)
    '''
rename_table = '''ALTER TABLE worker RENAME TO employee'''
add_col = '''ALTER TABLE employee ADD email VARCHAR(100)'''

def add_people(data_list):
    commands = []
    for person in data_list:
        commands.append(f'''INSERT INTO employee (first_name, last_name, gender, birth_date)
        VALUES ('{person[0]}', '{person[1]}', '{person[2]}', '{person[3]}')''')
    return commands

update_table = '''
    UPDATE employee
    SET email = 'jane.wall@gmail.com'
    WHERE first_name = 'Jane' AND last_name = "Wall"
    '''
delete_worker = '''
    delete from employee
    where first_name = 'William' AND last_name = "Shakespeare"
    '''

if __name__ == '__main__':
    connection = sqlite3.connect('staff.db')
    cur = connection.cursor()

    cur.execute(create_table)
    cur.execute(rename_table)
    cur.execute(add_col)

    for command in add_people(staff_data):
        cur.execute(command)

    cur.execute(update_table)
    cur.execute(delete_worker)

    connection.commit()
    connection.close()
