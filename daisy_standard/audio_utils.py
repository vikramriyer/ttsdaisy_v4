from mutagen.mp3 import MP3
import glob, os, shutil

def get_length(audio_path):
    audio = MP3(audio_path)
    length = audio.info.length
    return "%.3f" % length

def concatenate_audio(dir_path, output_fir_path):
    os.chdir(dir_path)
    destination = open(output_fir_path + '/concat1.mp3', 'wb')
    for file in glob.glob("*.mp3"):
        shutil.copyfileobj(open(file,'rb'), destination)
    destination.close()

# print(get_length("/home/raavan/Music/Alaipaydue Kanada Adi - TamilWire.com.mp3"))
concatenate_audio("/home/raavan/Music/")
# print(os.path.dirname(os.path.realpath(__file__)))
