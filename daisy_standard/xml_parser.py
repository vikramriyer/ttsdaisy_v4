import xml.etree.ElementTree as ET
from django.conf import settings
from yaml import load, dump, Loader
import audio_utils
import requests

# init
with open('/data/django_u/django_projects/code_along/ttsdaisy/ttsdaisy_v4/daisy_standard/tag_config.yaml') as stream:
    tag_config = load(stream)

def build_smil():
    pass

def create_mp3(audio_list):
    # create audio for each record on audio_content and get timelines
    # concatenate and create audio per h1
    pass

def create_html():
    pass

def parse_xml(tagged_xml, language="en"):
    # tagged_xml = "/data/django_u/django_projects/code_along/ttsdaisy/ttsdaisy_v4/daisy_standard/Whats_in_the_name_2018-05-09_104006.xml"
    tagged_xml = "/data/django_u/project_files/Whats_in_the_name_2018-05-09_104006.xml"
    with open(tagged_xml) as f:
        tree = ET.parse(f)
    root = tree.getroot()

    head = root.findall(tag_config['head'])[0]
    book = root.findall(tag_config['book'])[0]
    bodymatter = book.findall(tag_config['bodymatter'])[0]
    level1 = bodymatter.findall(tag_config['level1'])[0]

    """
    counter = 1
    for x in level1.getchildren():
        if x.tag == tag_config['h1']:
            pagenum = int(x.text)
        if x.tag == tag_config['p']:
            temp_mp3 = 'tmp' + str(counter) + '.mp3'
            counter += 1

    """


    flag = False
    pagenum = -1
    audio_content = []
    for x in level1.getchildren():
        if x.tag == tag_config['pagenum']:
            # pagenum = int(x.text)
            pass
        elif x.tag == tag_config['h1'] and not flag:
            if audio_content != []:
                create_mp3(audio_content)
                audio_content = []
            flag = True
            audio_content.append(x.text)
        elif x.tag == tag_config['p'] and flag:
            audio_content.append(x.text)
        elif x.tag == tag_config['h1'] and flag:
            if audio_content != []:
                # create audio for each record on audio_content and get timelines
                # concatenate and create audio per h1
                print("odd: ",audio_content)
                audio_content = []
            flag = False
            audio_content.append(x.text)
        elif x.tag == tag_config['p'] and not flag:
            audio_content.append(x.text)
    print(audio_content)

    """
    - capture all the p from one h1 to the next one,
    - create audios for each of them and note the time
    - concatenatae all of them to create a single audio and name
    it as ```pagenum.text```.mp3
    """


parse_xml("abc")

# TODO: Information required in general to run TTS
'''
0. path of the input file
1. language (need to get this via http)
2. all the specific content from the xml (xml)
3. tagged_xml to save the results to (http or custom funtion depending on book name and language)
4. name of the book and author (xml and http, prefer http as the annotator might have done some mistake in writing)
'''

# TODO: info about imp tags
'''
From the base ones, we need only the <book> tag for now.
'''

# TODO: information required from <book> tag
'''
<book showin="blp">
    <frontmatter>
        <doctitle>Whats_in_the_name</doctitle>
        <docauthor>Vikram</docauthor>
    </frontmatter>
    <bodymatter id="bodymatter_0239">
        <level1>
            <pagenum page="normal" id="page0001">1</pagenum>
            <h1></h1>
                <p></p>
                <p></p>
            <pagenum page="normal" id="page0002">1</pagenum>
            <h1></h1>
                <p></p>
                <p></p>
        </level1>
    </bodymatter>
</book>

'''
