# c't uplink - The Video Podcast Kodi Plug-in
# by Achim Barczok, Heise Medien
#

#Use the Youtube-Plugin and open the c't uplink Playlist in there
import xbmc
if __name__ == '__main__':
    xbmc.executebuiltin("ActivateWindow(10028,plugin://plugin.video.youtube/play/?playlist_id=PLUoWfXKEShjdcawz_wBJVqkv0pVIakmSP&order=default)")