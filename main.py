import sqlite3

conn = sqlite3.connect('my_Factory.db')
cur = conn.cursor()
res = cur.execute("SELECT worker_id, name, role FROM workers_list")
print("Список всіх працівників:")
for row in res:
    print(row[0], ' - ', row[1], ' - ', row[2])

id = int(input("\nВкажіть номер працівника, оклад якого Вас цікавить: "))
res = cur.execute("SELECT workers_list.name, workers_list.role, roles_list.hourly_wage FROM workers_list, "
                  "roles_list WHERE roles_list.role = workers_list.role AND  workers_list.worker_id = ?",
                  (id,))
for row in res:
    print(row[0], ' - ', row[1], ' - ', row[2], "грн/год")

answer = input("Чи бажаєте Ви змінити оклад працівника? (Y/N): ")
if answer == 'Y' or answer == 'y':
    new_role = row[1]
    new_wage = float(input(f"Вкажіть новий оклад у гривнях для посади {new_role}: "))
    res = cur.execute('UPDATE roles_list SET hourly_wage = ? WHERE role = ?', (new_wage, str(new_role),))
    conn.commit()
    print("Зміни успішно внесені: ")
    res = cur.execute("SELECT workers_list.name, workers_list.role, roles_list.hourly_wage FROM workers_list, "
                      "roles_list WHERE roles_list.role = workers_list.role AND roles_list.role = ?",
                      (str(new_role),))
    for row in res:
        print(row[0], ' - ', row[1], ' - ', row[2], "грн/год")
print("Дякуємо за співпрацю!")
conn.commit()
conn.close()
