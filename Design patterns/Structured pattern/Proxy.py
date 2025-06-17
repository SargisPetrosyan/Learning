'''
Proxy Design Pattern

The Proxy pattern acts as an intermediary, controlling access to a real object.  
It improves performance, enforces security, and enables lazy loading.  

### Benefits:
- **Lazy Initialization**: Creates objects only when needed.  
- **Access Control**: Restricts unauthorized access.  
- **Caching & Logging**: Optimizes performance and tracks usage.  
- **Remote Access**: Handles communication with remote objects.  

Used in authentication, database connections, and resource-heavy operations.  
'''

class Database:
    def connect_database(self):
        print(f"you connected to database")
        

class DatabaseProxy:
    def __init__(self,user):
        self._user = user
        self._database_connection = Database()
        
    def request_database(self):
        if self._user == 'admin':
            self._database_connection.connect_database()
        else:
            print("Access denied. You need admin privileges.")
            
            
proxy_admin = DatabaseProxy(user='admin')
proxy_admin.request_database()
# it will print 'you connected to database'

proxy_admin = DatabaseProxy(user='user')
proxy_admin.request_database()
# Proxy: Access denied. You need admin privileges.'
