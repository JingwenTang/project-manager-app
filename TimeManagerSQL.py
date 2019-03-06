# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 01:28:28 2018

@author: Jony
"""

from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

connstr = 'mysql+mysqlconnector://group5:group5@188.131.150.79/group51?charset=utf8'
engine = create_engine(connstr, encoding='utf8')

# result = engine.execute("select * from project where projectID = 2")
# for i in result:
#     print(i)
# query = session.query(Project)

Base = declarative_base()


class Project(Base):
    __tablename__ = 'project'

    project_id = Column(Integer, primary_key=True)
    project_name = Column(String(20))

    projectJobs = relationship("ProjectJob", back_populates='project')
    userPerformances = relationship('UserPerformance', back_populates='project')

    def __repr__(self):
        return "<Project(project_id = '%d', project_name = '%s') % (self.project_id, self.project_name)>" % (
        self.project_id, self.project_name)


class ProjectJob(Base):
    __tablename__ = 'projectJob'

    job_id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('project.project_id'))  # foreign key

    job_name = Column(String(20))
    job_number = Column(Integer)
    job_description = Column(String(20))

    project = relationship("Project", back_populates='projectJob')
    userPerformances = relationship("UserPerformance", back_populates='projectJob')

    def __repr__(self):
        return "<ProjectJob(project_id = '%d',job_id = '%d', job_name = '%s', job_number = '%d', job_description = '%s')\
                % (self.project_id, self.job_id, self.job_name, self.job_number, self.job_description)>" \
               % (self.project_id, self.job_id, self.job_name, self.job_number, self.job_description)


class SensorData(Base):
    __tablename__ = 'sensorData'

    time = Column(DateTime, primary_key=True)
    temperature = Column(Integer)
    humidity = Column(Float)
    HCHO = Column(Float)
    PM25 = Column(Float)

    def __repr__(self):
        return "<SensorData(time = '%Y-%m-%d %H:%i:%s',temperature = '%d', humidity = '%f', HCHO = '%f', PM25 = '%f')\
                % (self.time, self.temperature, self.temperature, self.HCHO, self.PM25)>" \
               % (self.time, self.temperature, self.temperature, self.HCHO, self.PM25)


class User(Base):
    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(20))
    user_password = Column(String(20))
    user_identity = Column(String(20))
    user_level = Column(String(20))

    userPerformances = relationship('UserPerformance', back_populates='user')

    def __repr__(self):
        return "<User(user_id = '%d',user_name = '%s', user_password = '%s', user_password = '%s', user_level = '%s')\
                % (self.user_id, self.user_name, self.user_password, self.user_password, self.user_level)>" \
               % (self.user_id, self.user_name, self.user_password, self.user_password, self.user_level)


class UserPerformance(Base):
    __tablename__ = 'userPerformanceer'

    project_id = Column(Integer, ForeignKey('project.project_id'), primary_key=True)  # foreign key
    job_id = Column(Integer, ForeignKey('projectJob.job_id'), primary_key=True)  # foreign key
    user_id = Column(Integer, ForeignKey('user.user_id'), primary_key=True)  # foreign key
    user_grade = Column(Float)

    user = relationship('User', back_populates='userPerformance')
    project = relationship('Project', back_populates='userPerformance')
    job = relationship('Job', back_populates='userPerformance')

    def __repr__(self):
        return "<UserPerformance(user_id = '%d',project_id = '%d', job_id = '%d', user_grade = '%f')\
                % (self.user_id, self.project_id, self.job_id, self.user_grade)>" \
               % (self.user_id, self.project_id, self.job_id, self.user_grade)


Base.metadata.create_all(engine)







