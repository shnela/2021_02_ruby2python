from faker import Faker

from app.database import Session
from app.posts.models import Post
from app.users.models import User

fake = Faker()


def create_users(users_number=10, *, posts_per_user=0):
    users_to_add = list()
    for _ in range(users_number):
        new_user = User(username=fake.unique.first_name())
        session.add(new_user)
        users_to_add.append(new_user)
        # we don't want to call `db.session.commit()` here,
        # to prevent many db connections
        # at the same time we can't add `Posts` here,
        # because `User.id` will be set in database after calling `db.session.commit()`
    db.session.commit()
    # now user instances have assigned `User.id`

    for new_user in users_to_add:
        create_posts(posts_per_user, user_id=new_user.id)


def delete_all(session):
    session.query(User).delete()
    session.query(Post).delete()
    session.session.commit()


def create_posts(n=10, *, user_id=None):
    for _ in range(n):
        p = Post(content=fake.unique.text(), user_id=user_id)
        db.session.add(p)
    db.session.commit()


if __name__ == '__main__':
    session = Session()
    session.create_all()
    delete_all(session)
    create_users(20, posts_per_user=10)
