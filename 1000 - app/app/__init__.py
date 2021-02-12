from app.database import Session, metadata
from app.posts.models import Post
from app.users.models import User


if __name__ == '__main__':
    session = Session()

    metadata.drop_all()
    metadata.create_all()
    print(session.query(Post).all())
    print(session.query(User).all())
