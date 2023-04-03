"""
The file that holds the schema/classes
that will be used to create objects
and connect to data tables.
"""

from sqlalchemy import ForeignKey, Column, INTEGER, TEXT, DATETIME
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    # Columns
    username = Column("username", TEXT, primary_key=True)
    password = Column("password", TEXT, nullable=False)

    tweets = relationship("Tweet", back_populates="user")
    following = relationship("User", 
                             secondary="followers",
                             primaryjoin="User.username==Follower.follower_id",
                             secondaryjoin="User.username==Follower.following_id")
    
    followers = relationship("User", 
                             secondary="followers",
                             primaryjoin="User.username==Follower.following_id",
                             secondaryjoin="User.username==Follower.follower_id",
                             overlaps="following")
    
    def __repr__(self):
        return "@" + str(self.username)


class Follower(Base):
    __tablename__ = "followers"

    # Columns
    id = Column("id", INTEGER, primary_key=True)
    follower_id = Column('follower_id', TEXT, ForeignKey('users.username'))
    following_id = Column('following_id', TEXT, ForeignKey('users.username'))

class Tweet(Base):
    # TODO: Complete the class
    __tablename__ = "tweets"

    id = Column("id", INTEGER, primary_key=True)
    content = Column("content", TEXT, nullable=False)
    timestamp = Column("timestamp", TEXT, nullable=False)
    username = Column("username", TEXT, ForeignKey("users.username"))

    user = relationship("User", back_populates= "tweets")
    tags = relationship("Tag", secondary="tweettags", back_populates="tweets")

    def __repr__(self):
       return("@" + str(self.username) + "\n" + str(self.content) + "\n" + str(self.tags) + "\n" + str(self.timestamp))


class Tag(Base):
    # TODO: Complete the class
    __tablename__ = "tags"

    id = Column("id", INTEGER, primary_key=True)
    content = Column("content", TEXT, nullable=False)

    tweets = relationship("Tweet", secondary="tweettags", back_populates="tags")

    def __repr__(self):
        return "#" + str(self.content)

class TweetTag(Base):
    # TODO: Complete the class
    __tablename__ = "tweettags"

    tweet_id = Column(INTEGER, ForeignKey('tweets.id'), primary_key=True)
    tag_id = Column(INTEGER, ForeignKey('tags.id'), primary_key=True)
