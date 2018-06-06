import xml.etree.ElementTree as ET

# init
ns = {
"ns":"http://www.daisy.org/z3986/2005/dtbook/",
}

def parse_xml(filepath, language="en"):
    filepath = "/data/django_u/django_projects/code_along/ttsdaisy/ttsdaisy_v4/daisy_standard/Whats_in_the_name_2018-05-09_104006.xml"
    with open(filepath) as f:
        tree = ET.parse(f)
    root = tree.getroot()

    head = root.findall("ns:head",ns)[0]
    book = root.findall("ns:book",ns)[0]
    bodymatter = book.findall("ns:bodymatter",ns)[0]
    level1 = bodymatter.findall("ns:level1",ns)[0]
    ps = level1.findall("ns:p",ns)

    is_page_num = False
    for x in level1.getchildren():
        if x.tag.split("}")[-1] == "pagenum":
            print(x.tag)

parse_xml("abc")


def create_smil():
    pass

def create_mp3():
    pass

def create_html():
    pass

# TODO: Information required in general to run TTS
'''
0. path of the input file
1. language (need to get this via http)
2. all the specific content from the xml (xml)
3. filepath to save the results to (http or custom funtion depending on book name and language)
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
