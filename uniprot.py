import urllib2

def getSequence(code):
    response = urllib2.urlopen(urllib2.Request("http://www.uniprot.org/uniprot/%s.fasta" % code))
    result = ''
    for s in response:
        if s.startswith('>'):
            continue
        result += s.strip()
    return result