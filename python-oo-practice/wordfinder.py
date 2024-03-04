"""Word Finder: finds random words from a dictionary."""

import random
class WordFinder:
    """
    >>> wf = WordFinder("3words.txt")
    3 words read

    >>> wf.random() in ["dog","cat","porcupine"]
    True

    >>> wf.random() in ["dog","cat","porcupine"]
    True

    >>> wf.random() in ["dog","cat","porcupine"]
    True

    
    """
     
    def __init__ (self, filepath):
        """Read Dict and report"""
        self.words = self._readwords(filepath)

    def _readwords (self,filepath):
        with open (filepath,"r") as file:
            words = [line.strip() for line in file]

        print(f"{len(words)} words read")
        return words    


    def random(self):
        """Return random word"""
        return random.choice(self.words)
