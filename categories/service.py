from categories.model import CategoryModel


async def get_all_categories(db):
    return db.query(CategoryModel).all()
