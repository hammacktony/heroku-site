from typing import List

def get_data(table: str, database) -> List:
    """Retrieves data from PostgresDB. DB Uri depends on production environment.

    Arguments:
        table {str} -- [source of comic data]

    Keyword Arguments:
        database {orator database object} -- [Postgres db Orator ORM connection]

    Returns:
        List -- [list of comic titles and links in table]
    """

    results = database.table(table).get()
    return results
