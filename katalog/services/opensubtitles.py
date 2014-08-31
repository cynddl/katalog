import xmlrpc.client


class OpenSubtitles(object):

    SERVER_URL = "http://api.opensubtitles.org/xml-rpc"

    def __init__(self):
        self.server = xmlrpc.client.ServerProxy(self.SERVER_URL)
        self.token = None

    def login(self):
        session = self.server.LogIn("", "", "en", "OS Test User Agent")
        self.token = session["token"]

    def check_hash(self, hash):
        r = self.server.CheckMovieHash(self.token, [hash])
        if r.get('status') == '200 OK':
            data = r['data'][hash]

            if data != []:
                return data
            else:
                return None
