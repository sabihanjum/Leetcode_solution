class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, sentence):
        cur = self.root
        for l in sentence:
            if l not in cur:
               cur[l] = {}
            cur = cur[l]
        cur['#'] = sentence

    def search(self, prefix, cur=None):
        if cur is None:
            cur = self.root
        
        for c in prefix:
            if c not in cur:
                return []
            cur = cur[c]

        ans = []

        for k in cur:
            if k == '#':
                ans.append(cur[k])
            else:
                ans += self.search('', cur[k])
        return ans

class AutoCompleteSystem:
    def __init__(self, sentences, times):
        self.lookUp = {}
        for i, s in enumerate(sentences):
            self.lookUp[s] = times[i]

        self.trie = Trie()

        for s in sentences:
            self.trie.insert(s)
        self.keyword = ""

    def input(self, c):
        if c == '#':
            self.lookUp[self.keyword] = self.lookUp.get(self.keyword, 0) + 1
            self.trie.insert(self.keyword)
            self.keyword = ""
            return []
        else:
            self.keyword += c
            lst = self.trie.search(self.keyword)
            lst.sort(key=lambda x: (-self.lookUp[x], x))
            return lst[:3]