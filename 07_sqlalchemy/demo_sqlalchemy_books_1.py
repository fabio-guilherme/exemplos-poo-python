from sqlalchemy import create_engine
from sqlalchemy import text

engine = create_engine(
    "mysql+mysqlconnector://root:password@localhost/books",
    echo=True
)

sql = text(
    'SELECT * FROM books WHERE books.book_price > 100'
)

with engine.connect() as conn:

    result = conn.execute(sql).fetchall()

    for record in result:
        print("\n", record)

from sqlalchemy import text

# define os dados
data = (
    {
        "book_id": 6,
        "book_price": 400,
        "genre": "fiction",
        "book_name": "yoga is science"
    },

    {
        "book_id": 7,
        "book_price": 800,
        "genre": "non-fiction",
        "book_name": "alchemy tutorials"
    },
)

# query INSERT
statement = text("""
    INSERT INTO books
    (book_id, book_price, genre, book_name)
    VALUES
    (:book_id, :book_price, :genre, :book_name)
""")

# query SELECT
sql = text("SELECT * FROM books")

with engine.connect() as conn:

    # inserir os dados
    for line in data:
        conn.execute(statement, line)

    # guardar alterações
    conn.commit()

    # obter resultados
    results = conn.execute(sql)

    # mostrar resultados
    for record in results:
        print("\n", record)