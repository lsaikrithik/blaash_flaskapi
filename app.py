# app.py
from flask import Flask, render_template, url_for, request, redirect, jsonify
from models import db, Product, Collection, EngagementPost
from config import Config
from sqlalchemy import desc
import uuid
from sqlalchemy import BigInteger


app = Flask(__name__)
app.config.from_object(Config)


# Initialize the database
db.init_app(app)

@app.route("/")
def home():
    return render_template("base.html")

@app.route("/product/new")
def new_product():
    return render_template("createproduct.html")

# Endpoint to create a new product
@app.route('/product', methods=['POST'])
def create_product():
    
    # Get product details from the request
    name = request.form.get("name")
    image_url = request.form.get("image_url")
    sku = request.form.get("sku")

    # Create a new product instance
    new_product = Product(name=name, image_url=image_url, sku=sku)
    db.session.add(new_product)
    db.session.commit()
   
    return redirect(url_for("home"))
   

@app.route("/collection/new")
def new_collection():
    return render_template("create_collection.html")

@app.route('/collection', methods=['POST'])
def create_collection():
    
    name = request.form.get("name")
    
    new_collection = Collection(name=name )
    db.session.add(new_collection)
    db.session.commit()

    return redirect(url_for("home"))
 

# Endpoint to fetch all collections with their posts
@app.route("/collections")
def view_collections():
    collections = Collection.query.all()
    return render_template("view_collections.html", collections=collections)

@app.route("/top-posts", methods=['GET'])
def show_top_posts():
    tenant_id = request.args.get('tenant_id')
    posts = []

        # Query to get the top 5 viewed posts for the given tenant_id
    posts_query = EngagementPost.query.filter_by(tenant_id=tenant_id) \
            .order_by(desc(EngagementPost.thumbnail_title)) \
            .limit(5) \
            .all()

        # Prepare posts data for rendering
    posts = [{"thumbnail_title": post.thumbnail_title, "thumbnail_url": post.thumbnail_url} for post in posts_query]

    # Render the template with posts data
    return render_template("top_posts.html", posts=posts)

# Run the app
if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Ensure tables are created
    app.run(debug=True)

