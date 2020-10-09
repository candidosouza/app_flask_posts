from settings.settings import setting

app = setting.app
db = setting.db

class Post(db.Model):
    __tablename__ = 'posts'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    body = db.Column(db.Text)
    
    def __init__(self, title=None, body=None):
        self.__title: str = title
        self.__body: str = body
    
    def __repr__(self) -> str:
        return '<Post %s>' % (self.title)
    
    @property
    def title(self) -> str:
        return self.__title
    
    @property
    def body(self) -> str:
        return self.__body
