from views import db
from models import Task
from datetime import date

# create the database and the db table
db.create_all()

#db.session.add(Task("Finish this tutorial", date(2016,1,29),10,1))
#db.session.add(Task("Finish Real Python!",date(2016,1,30),10,1))
db.session.commit()