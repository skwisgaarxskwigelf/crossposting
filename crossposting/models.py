from crossposting import db


class Post(db.Model):
    """
    Create a posts' table
    """
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True) 
    post_tg_id = db.Column(db.Integer)
    channel_id =  db.Column(db.Integer)
    post = db.Column(db.Text)
    is_img = db.Column(db.Boolean) 
    post_date = db.Column(db.Float)
    sent = db.Column(db.Boolean, default=0)


    def __init__(self, post_tg_id, channel_id, post, is_img, post_date, sent):
        self.post_tg_id = post_tg_id
        self.channel_id = channel_id
        self.post = post
        self.is_img = is_img
        self.post_date = post_date
        self.sent = sent


    def __repr__(self):
        return '<tg id {}>'.format(self.post_tg_id) 


class Channel(db.Model):
    """
    Create a channels' table
    """
    __tablename__ = 'channels'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    telegram_chat_id = db.Column(db.String(50), nullable=False, unique=True)
    is_active = db.Column(db.Boolean, default=0)


    def __init__(self, name, telegram_chat_id, is_active):
        self.name = name
        self.telegram_chat_id = telegram_chat_id
        self.is_active = is_active


    def __repr__(self):
       return '<name {}>'.format(self.name)


class Image(db.Model):
    """
    Create an images' table
    """
    __tablename__ = 'images'
    id = db.Column(db.Integer, primary_key=True)
    img_tg_id = db.Column(db.Integer)
    post_tg_id = db.Column(db.Integer) 


    def __init__(self, img_tg_id, post_tg_id):
        self.img_tg_id = img_tg_id
        self.post_tg_id = post_tg_id


    def __repr__(self):
        return '<tg id {}>'.format(self.img_tg_id)
