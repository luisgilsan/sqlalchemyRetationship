import db
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship


class Repository(db.Base):
    __tablename__ = 'repository'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

class Branch(db.Base):
    __tablename__ = 'branch'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    repository_id = Column(Integer, ForeignKey('repository.id'))
    repository = relationship("Repository")

class Commit(db.Base):
    __tablename__ = 'commit'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    user = Column(Integer, nullable=False)
    message = Column(String, nullable=False)
    date = Column(DateTime, nullable=False)
    hash = Column(String, nullable=False)
    branch_id = Column(Integer, ForeignKey('branch.id'))
    branch = relationship("Branch")

class Pullrequest(db.Base):
    __tablename__ = 'pullrequest'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    branch_origin_id = Column(Integer, ForeignKey('branch.id'))
    branch_origin = relationship("Branch")
    branch_dest_id = Column(Integer, ForeignKey('branch.id'))
    branch_dest = relationship("Branch")
