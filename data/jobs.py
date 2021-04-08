import datetime
import sqlalchemy
from sqlalchemy_serializer import SerializerMixin
from .db_session import SqlAlchemyBase
from sqlalchemy import orm

from .users import User


class Jobs(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'jobs'
    # id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    id = User.id
    # team = User.id
    team_leader = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, autoincrement=True)
    job = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    work_size = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    collaborators = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    start_date = sqlalchemy.Column(
        sqlalchemy.DateTime, default=datetime.datetime.now)
    end_date = sqlalchemy.Column(
        sqlalchemy.DateTime, default=datetime.datetime.now)
    is_finished = sqlalchemy.Column(
        sqlalchemy.Boolean, nullable=True
    )

    # news = orm.relation("Jobs", back_populates='user')

    # def __repr__(self):
    #     return f'{self.id} {self.team} {self.team_leader} {self.job} {self.work_size}' \
    #            f' {self.collaborators} {self.start_date} {self.end_date} ' \
    #            f'{self.is_finished}'
