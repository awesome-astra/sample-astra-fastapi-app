from db_connect import get_session


INIT_CQL = '''
CREATE TABLE IF NOT EXISTS animals (
  genus           TEXT,
  species         TEXT,
  image_url       TEXT,
  size_cm         FLOAT,
  sightings       INT,
  taxonomy        LIST<TEXT>,
  PRIMARY KEY ((genus), species)
);
'''
POPULATE_CQL_0 = '''
INSERT INTO animals (
  genus,
  species,
  image_url,
  size_cm,
  sightings,
  taxonomy
) VALUES (
  'Vanessa',
  'cardui',
  'https://upload.wikimedia.org/wikipedia/commons/c/c8/0_Belle-dame_%28Vanessa_cardui%29_-_Echinacea_purpurea_-_Havr%C3%A9_%283%29.jpg',
  5.5,
  12,
  ['Arthropoda', 'Insecta', 'Lepidoptera', 'Nymphalidae']
);
'''
POPULATE_CQL_1 = '''
INSERT INTO animals (
  genus,
  species,
  image_url,
  size_cm,
  sightings,
  taxonomy
) VALUES (
  'Vanessa',
  'atalanta',
  'https://upload.wikimedia.org/wikipedia/commons/9/9d/Red_admiral_%28Vanessa_atalanta%29_Hungary.jpg',
  4.8,
  43,
  ['Arthropoda', 'Insecta', 'Lepidoptera', 'Nymphalidae']
);
'''
POPULATE_CQL_2 = '''
INSERT INTO animals (
  genus,
  species,
  image_url,
  size_cm,
  sightings,
  taxonomy
) VALUES (
  'Saitis',
  'barbipes',
  'https://upload.wikimedia.org/wikipedia/commons/f/fe/Saitis_barbipes_Barcelona_05.jpg',
  0.6,
  4,
  ['Arthropoda', 'Arachnida', 'Aranea', 'Salticidae']
);
'''


def init_db():
    session = get_session()
    print("[init_db] Running init scripts")
    session.execute(INIT_CQL)
    session.execute(POPULATE_CQL_0)
    session.execute(POPULATE_CQL_1)
    session.execute(POPULATE_CQL_2)
    print("[init_db] Init script finished")


if __name__ == '__main__':
    init_db()
