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


create .bash_profile

```
touch ~/.bash_profile
```

put config vars there

export SECRET_KEY="27526d42886bf80c026c9e2838b62f7a"
export SQLALCHEMY_DATABASE_URI="sqlite:///site.db"

apply changes

```
source ~/.bash_profile
```