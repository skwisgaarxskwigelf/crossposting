from crossposting import db


#class Channel():
#    """
#    Create a channels' table
#    """
#    __tablename__ = 'channels'
#    id = db.Column(db.Integer, primary_key=True)
#    name = db.Column(db.String(50), nullable=False)
#
#
#    def __init__(self, name):
#        self.name = name
#
#
#    def __repr__(self):
#       return '<name {}>'.format(self.name)

#class Channel():
#    """
#    Create a channels' table
#    """
#    __tablename__ = 'channels'
#    #id = db.Column(db.Integer, primary_key=True)
#    id = db.relationship('Post', backref='channel', lazy='dynamic')
#    name = db.Column(db.String(50), nullable=False)
#
#
#    def __init__(self, name):
#        self.name = name
#
#
#    def __repr__(self):
#       return '<name {}>'.format(self.name)


class Post(db.Model):
    """
    Create a posts' table
    """
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True) 
    #cnannel_id =  db.Column(db.Integer, db.ForeignKey('channels.id'))
    cnannel_id =  db.relationship('Channel', backref='post', lazy='dynamic')
    header = db.Column(db.String)
    post = db.Column(db.Text)
    img_path = db.Column(db.String)
    img_date = db.Column(db.DateTime)
    post_date = db.Column(db.DateTime)
    sent = db.Column(db.Boolean, default=0)


    def __init__(self, channel_id, header, post, img_path, img_date, post_date, sent):
        self.channel_id = channel_id
        self.header = header
        self.post = post
        self.img_path = img_path
        self.img_date = img_date
        self.post_date = post_date
        self.sent = sent


    def __repr__(self):
        return '<id {}>'.format(self.id) 


class Channel(db.Model):
    """
    Create a channels' table
    """
    __tablename__ = 'channels'
    #id = db.Column(db.Integer, primary_key=True)
    #id = db.relationship('Post', backref='channel', lazy='dynamic')
    id =  db.Column(db.Integer, db.ForeignKey('posts.id'), primary_key=True)
    name = db.Column(db.String(50), nullable=False)


    def __init__(self, name):
        self.name = name


    def __repr__(self):
       return '<name {}>'.format(self.name)
