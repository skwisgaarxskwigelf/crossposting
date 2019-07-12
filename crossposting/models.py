from crossposting import db


class Post(db.Model):
    """
    Create a posts' table
    """
    __tablename__ = 'posts'

    id = db.Column(db.BigInteger, primary_key=True)
    channel_id = db.Column(db.Integer, nullable=False)
    tg_id = db.Column(db.Integer, nullable=False)
    message = db.Column(db.Text, default='')
    is_photo = db.Column(db.Boolean, default=0)
    is_document = db.Column(db.Boolean, default=0)
    is_web_preview = db.Column(db.Boolean, default=0)
    is_video = db.Column(db.Boolean, default=0)
    is_gif = db.Column(db.Boolean, default=0)
    is_pole = db.Column(db.Boolean, default=0)
    grouped_id = db.Column(db.BigInteger, default=0)
    date = db.Column(db.Float)
    sent = db.Column(db.Boolean, default=False)
    db.UniqueConstraint('channel_id', 'tg_id')

    def __init__(self, channel_id, tg_id, message, is_photo, is_document, is_web_preview, is_video, is_gif, is_pole,
                 grouped_id, date, sent):
        self.channel_id = channel_id
        self.tg_id = tg_id
        self.message = message
        self.is_photo = is_photo
        self.is_document = is_document
        self.is_web_preview = is_web_preview
        self.is_video = is_video
        self.is_gif = is_gif
        self.is_pole = is_pole
        self.grouped_id = grouped_id
        self.date = date
        self.sent = sent

    def __repr__(self):
        return '<tg id {}>'.format(self.tg_id)


class Channel(db.Model):
    """
    Create a channels' table
    """
    __tablename__ = 'channels'

    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    telegram_chat_id = db.Column(db.String(50), nullable=False, unique=True)
    vk_id = db.Column(db.String(50))
    is_active = db.Column(db.Boolean, default=0)

    def __init__(self, name, telegram_chat_id, vk_id, is_active):
        self.name = name
        self.telegram_chat_id = telegram_chat_id
        self.vk_id = vk_id
        self.is_active = is_active

    def __repr__(self):
        return '<telegram chat id {}>'.format(self.telegram_chat_id)


class Photo(db.Model):
    """
    Create an photos' table
    """
    __tablename__ = 'photos'

    id = db.Column(db.BigInteger, primary_key=True)
    message_tg_id = db.Column(db.Integer)
    tg_id = db.Column(db.BigInteger, unique=True)
    grouped_id = db.Column(db.BigInteger, default=0)

    def __init__(self, message_tg_id, tg_id, grouped_id):
        self.message_tg_id = message_tg_id
        self.img_tg_id = tg_id
        self.grouped_id = grouped_id

    def __repr__(self):
        return '<tg id {}>'.format(self.tg_id)


class Document(db.Model):
    """
    Create an documents' table
    """
    __tablename__ = 'documents'

    id = db.Column(db.BigInteger, primary_key=True)
    message_tg_id = db.Column(db.Integer)
    tg_id = db.Column(db.BigInteger, unique=True)
    grouped_id = db.Column(db.BigInteger, default=0)

    def __init__(self, message_tg_id, tg_id, grouped_id):
        self.message_tg_id = message_tg_id
        self.tg_id = tg_id
        self.grouped_id = grouped_id

    def __repr__(self):
        return '<tg id {}>'.format(self.tg_id)


class WebPreview(db.Model):
    """
    Create an web previews' table
    """
    __tablename__ = 'web_previews'

    id = db.Column(db.BigInteger, primary_key=True)
    message_tg_id = db.Column(db.Integer)
    tg_id = db.Column(db.BigInteger, unique=True)
    grouped_id = db.Column(db.BigInteger, default=0)

    def __init__(self, message_tg_id, tg_id, grouped_id):
        self.message_tg_id = message_tg_id
        self.tg_id = tg_id
        self.grouped_id = grouped_id

    def __repr__(self):
        return '<tg id {}>'.format(self.tg_id)


class Video(db.Model):
    """
    Create an vieos' table
    """
    __tablename__ = 'videos'

    id = db.Column(db.BigInteger, primary_key=True)
    message_tg_id = db.Column(db.Integer)
    tg_id = db.Column(db.BigInteger, unique=True)
    grouped_id = db.Column(db.BigInteger, default=0)

    def __init__(self, message_tg_id, tg_id, grouped_id):
        self.message_tg_id = message_tg_id
        self.tg_id = tg_id
        self.grouped_id = grouped_id

    def __repr__(self):
        return '<tg id {}>'.format(self.tg_id)


class Gif(db.Model):
    """
    Create an gifs' table
    """
    __tablename__ = 'gifs'

    id = db.Column(db.BigInteger, primary_key=True)
    message_tg_id = db.Column(db.Integer)
    tg_id = db.Column(db.BigInteger, unique=True)
    grouped_id = db.Column(db.BigInteger, default=0)

    def __init__(self, message_tg_id, tg_id, grouped_id):
        self.message_tg_id = message_tg_id
        self.tg_id = tg_id
        self.grouped_id = grouped_id

    def __repr__(self):
        return '<tg id {}>'.format(self.tg_id)


class Pole(db.Model):
    """
    Create an poles' table
    """
    __tablename__ = 'poles'

    id = db.Column(db.BigInteger, primary_key=True)
    message_tg_id = db.Column(db.Integer)
    tg_id = db.Column(db.BigInteger, unique=True)
    grouped_id = db.Column(db.BigInteger, default=0)

    def __init__(self, message_tg_id, tg_id, grouped_id):
        self.message_tg_id = message_tg_id
        self.tg_id = tg_id
        self.grouped_id = grouped_id

    def __repr__(self):
        return '<tg id {}>'.format(self.tg_id)
