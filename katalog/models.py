import guessit
import katalog.sync

class File(object):
    def __init__(self, path):
        self.path = path


class Movie(File):
    def __init__(self, path):
        super(Movie, self).__init__(path)
        self._hash = None
        self.imdb_id = None
        self.metadata = {}

    @property
    def hash(self):
        if self._hash is None:
            self._hash = guessit.guess_file_info(self.path, 'hash_mpc')['hash_mpc']
        return self._hash

    def identify(self, opensub, imdb_client=None):
        data = opensub.check_hash(self.hash)

        if data is not None:
            self.imdb_id = 'tt' + data['MovieImdbID']

            if imdb_client is not None:
                m = imdb_client.find_movie_by_id(self.imdb_id)

                if m != False:
                    new_m = {
                        'rating': m.rating,
                        'title': m.title,
                        'poster_url': m.poster_url,
                        'date': m.release_date,
                        'genres': m.genres
                    }

                    self.metadata.update(new_m)
