from django.contrib.sessions.backends.db import SessionStore as DbSessionStore

class SessionStore(DbSessionStore):
    def cycle_key(self):
        print("ttttttttttttttttttttttttt")
        print("ttttttttttttttttttttttttt")
        print(self.__dict__)
        print("ttttttttttttttttttttttttt")
        