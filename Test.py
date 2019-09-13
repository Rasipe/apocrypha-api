
from repository.Connection import Connection

conn = Connection()

for user in conn.user_repository.get_all():
    print(f'{user}\n')

conn.user_repository.get(1)

conn.close_connection()
