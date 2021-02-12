from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

metadata = MetaData()
engine = create_engine('mysql+pymysql://np_flask:testprzezbobra@213.222.211.156/np_jakub_6jx0')
Base = declarative_base(bind=engine, metadata=metadata)
Session = sessionmaker(bind=engine)
