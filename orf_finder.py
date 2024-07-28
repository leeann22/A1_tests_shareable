"""
Trie - Open Reading Frame Finder
Author: Choong Lee Ann
Version: 1.0
"""

class Vertex:
    """
    Vertex class that represents a Vertex in the trie
    """

    def __init__(self):
        """
        This function initializes the Vertex with link and index
        Written by Choong Lee Ann

        Precondition: None
        Postcondition: a Vertex is created with link and index

        Input:
            None
        Return:
            None

        Time complexity: 
            Best case analysis: O(1)
            Worst case analysis: O(1)
        Space complexity: 
            Input space analysis: O(1)
            Aux space analysis: O(1)
        """
        # time complexity: O(1)
        # terminal $ and 4 letters A-D
        self.link = [None] * 4
        self.index = []

class Trie:
    """
    Trie class that represents a trie data structure
    """

    def __init__(self):
        """
        This function initializes the trie with a root node
        Written by Choong Lee Ann

        Precondition: None
        Postcondition: a trie is created with a root node

        Input:
            None
        Return:
            None

        Time complexity: 
            Best case analysis: O(1)
            Worst case analysis: O(1)
        Space complexity: 
            Input space analysis: O(1)
            Aux space analysis: O(1)
        """
        self.root = Vertex()

    def insert(self, genome):
        """
        This function inserts the genome into the trie
        Written by Choong Lee Ann

        Precondition: genome is a non-empty string consisting of only A-D uppercase
        Postcondition: the genome is inserted into the trie

        Input:
            genome: a non-empty string consisting of only A-D uppercase
        Return:
            None

        Time complexity: 
            Best case analysis: O(N^2) where N is the length of the genome
            Worst case analysis: O(N^2)
        Space complexity: 
            Input space analysis: O(N)
            Aux space analysis: O(N^2)
        """
        for i in range(len(genome)):
            # begin from the root
            current = self.root
            for char in range(i, len(genome)):
                index = ord(genome[char]) - ord('A')
                # if the letter has not been inserted, create a new node
                if current.link[index] is None:
                    current.link[index] = Vertex()

                current = current.link[index]
                current.index.append(i)

    def search(self, key):
        """
        This function searches for the key in the trie
        Written by Choong Lee Ann

        Precondition: key is a non-empty string consisting of only A-D uppercase
        Postcondition: the indexes where the key is found in the trie is returned

        Input:
            key: a non-empty string consisting of only A-D uppercase
        Return:
            current.index: a list of indexes where the key is found in the trie

        Time complexity: 
            Best case analysis: O(N) where N is the length of the key
            Worst case analysis: O(N)
        Space complexity: 
            Input space analysis: O(N)
            Aux space analysis: O(1)
        """
        current = self.root
        for char in key:
            index = ord(char) - ord('A')
            # if the letter exists, move to the next node
            if not current.link[index] is None:
                current = current.link[index]
            else: 
                return []
            
        return current.index

class OrfFinder:
    """
    OrfFinder class that finds the open reading frames in a genome
    """

    def __init__(self, genome):
        """
        This function initializes the OrfFinder by creating a forward and reverse trie
        Written by Choong Lee Ann

        Precondition: genome is a non-empty string consisting of only A-D uppercase
        Postcondition: the forward and reverse trie is created

        Input:
            genome: a non-empty string consisting of only A-D uppercase
        Return:
            None

        Time complexity: 
            Best case analysis: O(N^2) where N is the length of the genome 
            Worst case analysis: O(N^2) 
        Space complexity: 
            Input space analysis: O(N)
            Aux space analysis: O(N^2)
        """
        # forward trie
        self.trie = Trie()
        self.genome = genome
        self.trie.insert(genome)

        # reverse trie
        self.reverse_trie = Trie()
        reverse_genome = ''.join(reversed(genome))
        self.reverse_trie.insert(reverse_genome)

    def find(self, start, end):
        """
        This function finds the open reading frames in the genome that starts with start and ends with end
        Written by Choong Lee Ann

        Precondition: start and end are non-empty strings consisting of only A-D uppercase
        Postcondition: the substrings that start with start and end with end are returned

        Input:
            start: a non-empty string consisting of only A-D uppercase
            end: a non-empty string consisting of only A-D uppercase
        Return:
            output: list of substrings which begin with start and end with end

        Time complexity: 
            Best case analysis: O(T + U + V) where T is the length of start, U is the length of end, and V is the number of characters in the output list
            Worst case analysis: O(T + U + V) 
        Space complexity: 
            Input space analysis: O(T + U)
            Aux space analysis: O(V)
        """
        # will return list of indexes which has start
        output = []
        # time complexity: O(T)
        start_indexes = self.trie.search(start) 

        rev_end = ''.join(reversed(end))
        # will return list of indexes which has end
        # time complexity: O(U)
        end_indexes = self.reverse_trie.search(rev_end)

        # if either returns [], return
        if not start_indexes or not end_indexes:
            return output
        
        # get the indexes of the end in the ori trie
        endings = [len(self.genome) - end_index - len(end) for end_index in end_indexes]

        # get the substrings
        for starting in start_indexes:
            for ending in endings:
                if starting + len(start) <= ending:
                    substr = self.genome[starting:ending + len(end)]
                    output.append(substr)

        return output