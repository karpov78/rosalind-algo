import urllib.request


def getSequence(code):
    response = urllib.request.urlopen(urllib.request.Request("http://www.uniprot.org/uniprot/%s.fasta" % code))
    result = ''
    for s in response:
        if s.startswith('>'):
            continue
        result += s.strip()
    return result