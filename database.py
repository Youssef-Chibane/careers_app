from sqlalchemy import create_engine, text

engine = create_engine("mysql+pymysql://root:root@localhost:3306/joviancareers")

with engine.connect() as conn:
    result = conn.execute(text("SHOW DATABASES"))
    print(result.all())