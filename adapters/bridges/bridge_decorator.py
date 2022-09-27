from adapters.connectors.db_connection import DatabaseConnection


def db_setup(call_func):
    def decorator_func(*args, **kwargs):
        # Pre
        db_conn = DatabaseConnection()
        db_conn.connect()
        result = call_func(db_conn)
        # Post
        db_conn.disconnect()
        print(result)
        return result
    return decorator_func
