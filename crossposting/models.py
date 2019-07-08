from crossposting import db


class Post(db.Model):
    """
    Create a posts' table
    """
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    channel_id = db.Column(db.Integer)
    post_tg_id = db.Column(db.Integer, unique=True)
    post = db.Column(db.Text, default='')
    is_img = db.Column(db.Boolean, default=0)
    is_document = db.Column(db.Boolean, default=0)
    is_web_preview = db.Column(db.Boolean, default=0)
    is_video = db.Column(db.Boolean, default=0)
    is_gif = db.Column(db.Boolean, default=0)
    is_pole = db.Column(db.Boolean, default=0)
    grouped_id = db.Column(db.Integer, default=0)
    post_date = db.Column(db.Float)
    sent = db.Column(db.Boolean, default=0)

    def __init__(self, channel_id, post_tg_id, post, is_img, is_document, is_web_preview, is_video, is_gif, is_pole,
                 grouped_id, post_date, sent):
        self.channel_id = channel_id
        self.post_tg_id = post_tg_id
        self.post = post
        self.is_img = is_img
        self.is_document = is_document
        self.is_web_preview = is_web_preview
        self.is_video = is_video
        self.is_gif = is_gif
        self.is_pole = is_pole
        self.grouped_id = grouped_id
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


class Image(db.Model):
    """
    Create an images' table
    """
    __tablename__ = 'images'

    id = db.Column(db.Integer, primary_key=True)
    post_tg_id = db.Column(db.Integer)
    img_tg_id = db.Column(db.Integer, unique=True)
    grouped_id = db.Column(db.Integer, default=0)

    def __init__(self, post_tg_id, img_tg_id, grouped_id):
        self.post_tg_id = post_tg_id
        self.img_tg_id = img_tg_id
        self.grouped_id = grouped_id

    def __repr__(self):
        return '<tg id {}>'.format(self.img_tg_id)


class Document(db.Model):
    """
    Create an documents' table
    """
    __tablename__ = 'documents'

    id = db.Column(db.Integer, primary_key=True)
    post_tg_id = db.Column(db.Integer)
    doc_tg_id = db.Column(db.Integer, unique=True)
    grouped_id = db.Column(db.Integer, default=0)

    def __init__(self, post_tg_id, doc_tg_id, grouped_id):
        self.post_tg_id = post_tg_id
        self.doc_tg_id = doc_tg_id
        self.grouped_id = grouped_id

    def __repr__(self):
        return '<tg id {}>'.format(self.doc_tg_id)


class WebPreview(db.Model):
    """
    Create an web previews' table
    """
    __tablename__ = 'web_preview'

    id = db.Column(db.Integer, primary_key=True)
    post_tg_id = db.Column(db.Integer)
    web_preview_tg_id = db.Column(db.Integer, unique=True)
    grouped_id = db.Column(db.Integer, default=0)

    def __init__(self, post_tg_id, web_preview_tg_id, grouped_id):
        self.post_tg_id = post_tg_id
        self.web_preview_tg_id = web_preview_tg_id
        self.grouped_id = grouped_id

    def __repr__(self):
        return '<tg id {}>'.format(self.web_preview_tg_id)


class Video(db.Model):
    """
    Create an vieos' table
    """
    __tablename__ = 'videos'

    id = db.Column(db.Integer, primary_key=True)
    post_tg_id = db.Column(db.Integer)
    video_tg_id = db.Column(db.Integer, unique=True)
    grouped_id = db.Column(db.Integer, default=0)

    def __init__(self, post_tg_id, video_tg_id, grouped_id):
        self.post_tg_id = post_tg_id
        self.video_tg_id = video_tg_id
        self.grouped_id = grouped_id

    def __repr__(self):
        return '<tg id {}>'.format(self.video_tg_id)


class Gif(db.Model):
    """
    Create an gifs' table
    """
    __tablename__ = 'gifs'

    id = db.Column(db.Integer, primary_key=True)
    post_tg_id = db.Column(db.Integer)
    gif_tg_id = db.Column(db.Integer, unique=True)
    grouped_id = db.Column(db.Integer, default=0)

    def __init__(self, post_tg_id, gif_tg_id, grouped_id):
        self.post_tg_id = post_tg_id
        self.gif_tg_id = gif_tg_id
        self.grouped_id = grouped_id

    def __repr__(self):
        return '<tg id {}>'.format(self.gif_tg_id)


class Pole(db.Model):
    """
    Create an poles' table
    """
    __tablename__ = 'poles'

    id = db.Column(db.Integer, primary_key=True)
    post_tg_id = db.Column(db.Integer)
    pole_tg_id = db.Column(db.Integer, unique=True)
    grouped_id = db.Column(db.Integer, default=0)

    def __init__(self, post_tg_id, pole_tg_id, grouped_id):
        self.post_tg_id = post_tg_id
        self.pole_tg_id = pole_tg_id
        self.grouped_id = grouped_id

    def __repr__(self):
        return '<tg id {}>'.format(self.pole_tg_id)