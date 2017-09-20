class Dictionary:
    def __init__(self)
        self.words=set()

    def check(self,word)
        # is the lower of each work in self.words?  boolean
        return word.lower() in self.words
    
    
    def load(self,dictionary):
        file=open(dictionary,"r")
        for line in file:
            self.words.adds(line.rstrip("\n"))
        file.close()
        return True

    def size(self):
        return len(self.words)

    def unload(self):
        return True
