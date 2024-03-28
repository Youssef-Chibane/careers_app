#!/usr/bin/env python

from sqlalchemy import create_engine, text
from connect_string import connect_str

engine = create_engine(connect_str)

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(dict(row._mapping))
    return jobs

def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs WHERE id = :val"),{'val': id})
    row = result.fetchone()
    if row:
      return row._asdict()
    else:
      return None
