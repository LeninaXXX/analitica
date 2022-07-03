import spotipy      # Import general, ahora veo que en particular...
import json

class Account:
    def __init__(self, username, client_id, client_secret, redirect_uri)
        self.username = username            # No tiene ningun rol en la autenticacion
        self.client_id = client_id          # Provisto por Spotify, dashboard en el que se registra la aplicacion
        self.client_secret = client_secret  # --- IDEM --- 
        self.redirect_uri = redirect_uri    # It's set en el dashboard. Req'd para *Authorization Code Flow*
        # Authorization Code Flow
        # #######################
        # This flow is suitable for long-running applications in which the user grants permission only once. It
        # provides an access token that can be refreshed. Since the token exchange involves sending your secret
        # key, perform this on a secure location, like a backend service, and not from a client such as a 
        # browser or from a mobile app. (https://spotipy.readthedocs.io/en/master/#authorization-code-flow)

    def getPlaylists(self) -> list[Playlist]:
        pass