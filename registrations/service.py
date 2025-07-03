from registrations.model import ProductRegistrationModel


async def get_product_registration_detail(db):
    return db.query(ProductRegistrationModel).all()
