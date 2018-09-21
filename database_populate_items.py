from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_catalog_setup import Base, User, Category, Item

engine = create_engine('sqlite:///catalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# create a dummy user
User1 = User(name="Jane Doe", email='janeDoe@gmail.com')
session.add(User1)
session.commit()

User2 = User(name="Lily Potter", email='lilyPotter@gmail.com')
session.add(User2)
session.commit()


#Category of Makeup
Category1 = Category(user_id=1,name="Makeup")
session.add(Category1)
session.commit()

#Eye-liner
Item1 = Item(user_id=1,name="Eye-liner",description="Smashbox Always On Liquid Liner - Black",category=Category1)
session.add(Item1)
session.commit()

#Lipstick
Item2 = Item(user_id=1,name="Lipstick",description="Huda Beauty Contour & Strobe Lip Set - Trendsetter/Snobby",category=Category1)
session.add(Item2)
session.commit()


#Nailpolish
Item3 = Item(user_id=1,name="Nailpolish",description="Maybelline New York Color Show Nail Lacquer",category=Category1)
session.add(Item3)
session.commit()


#Category of Skin
Category2 = Category(user_id=1,name="Skin")
session.add(Category2)
session.commit()


#Facewash
Item4 = Item(user_id=1,name="Facewash",description="Lotus Herbals Whiteglow 3-in-1 Deep Cleansing Skin Whitening Facial Foam",category=Category2)
session.add(Item4)
session.commit()

#Sunscreen
Item5 = Item(user_id=1,name="Sunscreen",description="The Face Shop Natural Sun Eco Sebum Control Hydrating Sun Cream",category=Category2)
session.add(Item5)
session.commit()


#Handcream
Item6 = Item(user_id=1,name="Handcream",description="Oriflame Swedish Spa Nourishing Night-Time Hand & Nail Balm",category=Category2)
session.add(Item6)
session.commit()


#Category of Hair
Category3 = Category(user_id=1,name="Hair")
session.add(Category3)
session.commit()

#Shampoo
Item7 = Item(user_id=1,name="Shampoo",description="Sebastian Professional Hydre Shampoo For Chemically Treated Hair",category=Category3)
session.add(Item7)
session.commit()

#Conditioner
Item8 = Item(user_id=1,name="Conditioner",description="Schwarzkopf Gliss Hair Repair with Liquid Keratin Million Gloss Conditioner",category=Category3)
session.add(Item8)
session.commit()


#Hair Oil
Item9 = Item(user_id=1,name="Hair Oil",description="Kama Ayurveda Bringadi Intensive Hair Treatment Oil",category=Category3)
session.add(Item9)
session.commit()

#Category of Natural
Category4 = Category(user_id=1,name="Natural")
session.add(Category4)
session.commit()

#Essential Oils
Item10 = Item(user_id=1,name="Essential Oils",description="Nykaa Naturals Cinnamon Essential Oil",category=Category4)
session.add(Item10)
session.commit()

#Incense Sticks
Item11 = Item(user_id=1,name="Incense Sticks",description="Spa Ceylon Luxury Ayurveda Cardamom Rose Incense Sticks",category=Category4)
session.add(Item11)
session.commit()


#Candles
Item12 = Item(user_id=1,name="Candles",description="Resonance Candles Amber & Vanilla Fragrance Natural Wax Aroma Votive Candle",category=Category4)
session.add(Item12)
session.commit()

print "Added beauty products!"
