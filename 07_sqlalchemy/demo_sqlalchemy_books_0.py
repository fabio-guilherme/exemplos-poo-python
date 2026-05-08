# import necessary packages
from sqlalchemy.engine import result
from sqlalchemy import create_engine, MetaData, Table, Column, Numeric, Integer, VARCHAR
from sqlalchemy import text

# establish connections
server_engine = create_engine(
    "mysql+mysqlconnector://root:password@localhost",
    echo=True
)

# create BD if necessary
with server_engine.connect() as conn:
    conn.execute(
        text("CREATE DATABASE IF NOT EXISTS books")
    )
    conn.commit()

# connection to the books database
engine = create_engine(
    "mysql+mysqlconnector://root:password@localhost/books",
    echo=True
)

# initialize the Metadata Object
meta = MetaData()
meta.reflect(bind=engine)

# create a table schema
books = Table(
    'books', meta,
    Column('book_id', Integer, primary_key=True),
    Column('book_price', Numeric),
    Column('genre', VARCHAR(50)),
    Column('book_name', VARCHAR(100))
)

meta.create_all(engine)

# insert records into the table
statement1 = books.insert().values(book_id=1, 
                                   book_price=12.2,
                                   genre='fiction',
                                   book_name='Old age')
statement2 = books.insert().values(book_id=2, 
                                   book_price=13.2,
                                   genre='non-fiction',
                                   book_name='Saturn rings')

statement3 = books.insert().values(book_id=3,
                                   book_price=121.6,
                                   genre='fiction',
                                   book_name='Supernova')

statement4 = books.insert().values(book_id=4,
                                   book_price=100,
                                   genre='non-fiction',
                                   book_name='History of the world')

statement5 = books.insert().values(book_id=5, 
                                   book_price=1112.2,
                                   genre='fiction', 
                                   book_name='Sun city')

# execute the insert records statement
with engine.connect() as conn:
    conn.execute(statement1)
    conn.execute(statement2)
    conn.execute(statement3)
    conn.execute(statement4)
    conn.execute(statement5)
    conn.commit()