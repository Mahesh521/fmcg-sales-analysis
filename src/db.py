
import os
from sqlalchemy import create_engine
password=os.getenv('DB_PASSWORD')
engine = create_engine('postgresql+psycopg2://postgres:{password}@localhost:5432/fmcg_sales')


