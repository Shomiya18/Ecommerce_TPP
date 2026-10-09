from sqlalchemy import Integer, Float, Column, String, ForeignKey,Boolean
from sqlalchemy.orm import relationship
from app.db.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True)
    user_name = Column(String, nullable = False)

    email = Column(String, unique = True, nullable = False)
    password = Column(String, nullable = True)

    is_admin = Column(Boolean, default=False, nullable=False)

    products = relationship("Product", back_populates ="owner")


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key = True)
    name = Column(String, nullable = False)
    price = Column(Float, nullable = False)
    stock = Column(Integer, )
    description = Column(String, nullable = True)

    user_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates = "products")
