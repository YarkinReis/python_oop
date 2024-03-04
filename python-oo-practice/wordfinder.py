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


class RandomWordFinder(WordFinder):
    """Word finder but special => excludes blanks
    
    >>> rwf = RandomWordFinder("newtxt.txt)
    3 words read
    >>> rwf.random() in ["apple","mango", "kale"]
    True
    >>> rwf.random() in ["apple","mango", "kale"]
    True
    >>> rwf.random() in ["apple","mango", "kale"]
    True
    """ 
    def _readwords(self, filepath):
        with open(filepath,"r") as file:
            words =[line.strip() for line in file if line.strip() and not line.startswith("#")]
        print(f"{len(words)} words read")
        return words