from service.disco_service import DiscoService
from model.artist import Artist
from model.album import Album

class DiscoController:

    def getArtists(self):
        service = DiscoService()
        artisti = service.getAllArtists()
        output = []
        for artista in artisti:
            temp = Artist(artista.get("ArtistId", 0), artista.get("Name", 'Artista sconosciuto'))
            output.append(temp.toTuple())
        return output

    def getArtistiJson(self):
        service = DiscoService()
        return service.getAllArtists()
