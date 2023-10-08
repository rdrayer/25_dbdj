"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    __tablename__ = 'playlists'
    """Playlist."""
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.String,
                     nullable=False,
                     unique=True)
    description = db.Column(db.String)
    songs = db.relationship('Song',
                            secondary='playlists_songs',
                            backref='playlists')


class Song(db.Model):
    __tablename__ = 'songs'
    """Song."""
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    title = db.Column(db.String,
                      nullable=False)
    artist = db.Column(db.String,
                        nullable=False)


class PlaylistSong(db.Model):
    __tablename__ = 'playlists_songs'
    """Mapping of a playlist to a song."""
    id = db.Column(db.Integer,
                primary_key=True,
                autoincrement=True)
    playlist_id = db.Column(db.Integer,
                            db.ForeignKey("playlists.id"),
                            primary_key=True)
    song_id = db.Column(db.Integer,
                        db.ForeignKey("songs.id"),
                        primary_key=True)


# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
