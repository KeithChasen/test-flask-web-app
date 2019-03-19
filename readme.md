Description
-

To run app:

```
FLASK_APP=flaskblog.py
```

```
python3 flaskblog.py
```

Create DB:

```
python3
from flaskblog import db
from flaskblog.models import User, Post
db.create_all()
User.query.all()
```

That will create site.db file inside the project root
