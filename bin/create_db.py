from panstora.models import Base

from sqlalchemy import create_engine

engine = create_engine("sqlite:////tmp/test.tb")

metadata = Base.metadata
metadata.create_all(engine)
