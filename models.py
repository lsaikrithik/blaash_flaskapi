# models.py
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy import BigInteger


db = SQLAlchemy()

class Product(db.Model):
    __tablename__ = 'engagement_post_product'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(100), nullable=False)
    image_url = db.Column(db.String(200), nullable=True)
    sku = db.Column(db.String(50), unique=True, nullable=False)

    def __init__(self, name, image_url, sku):
        self.name = name
        self.image_url = image_url
        self.sku = sku

class Collection(db.Model):
    __tablename__ = 'collection'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(100), nullable=False)
    
class EngagementPost(db.Model):
    __tablename__ = 'engagement_post'

    engagement_post_id = db.Column(db.BigInteger, primary_key=True)
    tenant_id = db.Column(db.BigInteger, nullable=False)
    thumbnail_title = db.Column(db.String(200), nullable=True)
    thumbnail_url = db.Column(db.String(200), nullable=True)
    
