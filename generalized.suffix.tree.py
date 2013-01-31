from radixtree import RadixTree
from bitarray import bitarray

EOS_MARKER = '$'

def clip(string, startPos):
    eosPos = string.lastIndexOf(EOS_MARKER)
    if eosPos < 0: eosPos = string.length()
    return string[startPos:eosPos]

class SuffixData:
    def __init__(self, owner, stringIndex, substringStartIndex):
        self._owner = owner
        self._stringIndex = stringIndex
        self._substrStartIndex = substringStartIndex
        self._shared = None

    def replicate(self):
        replica = SuffixData(self._owner, self._stringIndex, self._substrStartIndex)
        replica.incorporateShared(self._shared)
        return replica

    def incorporateShared(self, shared):
        if not shared: return
        if not self._shared: self._shared = []
        for sharedData in shared:
            self._shared.append(sharedData)
            self.incorporateShared(sharedData.shared)

    def getSourceString(self):
        return self._owner.strings[self._stringIndex]

    def getString(self, depth):
        return self.getSourceString()[self._substrStartIndex, self._substrStartIndex + depth]

    def getSuffix(self):
        return self.getSourceString()[self._substrStartIndex:]

    def incorporate(self, other):
        if not self._shared: self._shared = []
        self._shared.append(other)
        self.incorporateShared(other._shared)

    def getShared(self):
        return self._shared

    def __str__(self):
        return "%d:%d %s" % (self._stringIndex, self._substrStartIndex, str(self._shared))

class PathElement:
    def __init__(self, node, childElement):
        self._node = node
        self._participants = bitarray()
        self.incorporate(childElement)
        self._depth = node.depth() if node else childElement._depth - 1

        suffixData = node.getData().getValue()
        if suffixData:
            self._participants[suffixData._stringIndex] = True
            shared = suffixData.getShared()
            if shared:
                for sharedData in shared:
                    self._participants[sharedData.suffixData._stringIndex] = True
        self._finalized = False
        self._key = None
        self._contribLen = 0

    def incorporate(self, childElement):
        if childElement:
            self._participants |= childElement._participants

    def finalizeElt(self, parent):
        if not self._finalized:
            if not parent:
                self._key = ''
            else:
                curKey = clip(self._node.getData().getKey(), 0)
                self._contribLen += len(curKey)
                self._key = parent._key + curKey

class Path:
    def __init__(self, leaf, node2pathElt):
        self._pathElements = []
        childElt = None
        node = leaf
        while node:
            pathElt = node2pathElt[node]
            if not pathElt:
                pathElt = PathElement()
            node = node.getParent()


class PathContainer:
    def __init__(self, suffixTree):
        self._suffixTree = suffixTree
        self._node2pathElement = {}
        self._leaves = suffixTree.getRoot().getLeaves()
        self._paths = []

        for leaf in self._leaves:
            self._paths.append(Path(leaf, self._node2pathElement))

class GeneralizedSuffixTree:
    def __init__(self, strings):
        self.strings = strings
        self.suffixTree = RadixTree()
        self.eosMarker = EOS_MARKER
        self.eosLen = len(EOS_MARKER)

        for i in range(0, len(strings)):
            for j in range(0, len(strings[i])):
                suffix = strings[i] + EOS_MARKER + i if j == 0 else strings[i][j:] + EOS_MARKER
                self.suffixTree.insert(suffix, SuffixData(self, i, j),
                    merge=lambda data, value: data.getValue().incorporate(value),
                    replicate=lambda value: value.replicate())

    def longestSubstrs(self, minSize=1):
        if minSize < 1 : minSize = 1
        pathContainer = PathContainer(suffixTree)

