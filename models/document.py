from extensions import db


class Document(db.Model):

    __tablename__ = "documents"

    id = db.Column(

        db.Integer,

        primary_key=True

    )

    filename = db.Column(

        db.String(255),

        unique=True,

        nullable=False

    )

    file_type = db.Column(

        db.String(20)

    )

    chunks = db.Column(

        db.Integer,

        default=0

    )

    file_size = db.Column(

        db.Float,

        default=0

    )

    uploaded_at = db.Column(

        db.DateTime,

        server_default=db.func.now()

    )

    def __repr__(self):

        return f"<Document {self.filename}>"