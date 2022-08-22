from utils.models import Animal, Plant


prepared_cache = {}
def get_prepared_statement(session, stmt):
    if stmt not in prepared_cache:
        print(f'[get_prepared_statement] Preparing statement "{stmt}"')
        prepared_cache[stmt] = session.prepare(stmt)
    return prepared_cache[stmt]


def store_animal(session, animal):
    store_cql = 'INSERT INTO animals (genus,species,image_url,size_cm,sightings,taxonomy) VALUES (?,?,?,?,?,?);'
    prepared_store = get_prepared_statement(session, store_cql)
    session.execute(
        prepared_store,
        (
            animal.genus,
            animal.species,
            animal.image_url,
            animal.size_cm,
            animal.sightings,
            animal.taxonomy,
        ),
    )


def retrieve_animal(session, genus, species):
    get_one_cql = 'SELECT * FROM animals WHERE genus=? AND species=?;'
    prepared_get_one = get_prepared_statement(session, get_one_cql)
    row = session.execute(prepared_get_one, (genus, species)).one()
    if row:
        return Animal(**row._asdict())
    else:
        return row


def retrieve_animals_by_genus(session, genus):
    get_many_cql = 'SELECT * FROM animals WHERE genus=?;'
    prepared_get_many = get_prepared_statement(session, get_many_cql)
    rows = session.execute(prepared_get_many, (genus,))
    return (
        Animal(**row._asdict())
        for row in rows
    )

def generator_retrieve_plant_by_genus(session, genus):
    # Return a *generator* over all rows (there might be many, let's assume)
    get_many_cql = 'SELECT * FROM plants WHERE genus=?;'
    prepared_get_many = get_prepared_statement(session, get_many_cql)
    rows = session.execute(prepared_get_many, (genus,))
    for row in rows:
        yield Plant(**row._asdict())
