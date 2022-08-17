from storage.db_connect import get_session


async def g_get_session():
    yield get_session()
