import unittest
from Node import Node

class TestClass(unittest.TestCase):

    def testing_class_node(self):
        result = Node('Lanche', None, Node('Pizza'))
        self.assertEqual(result.value, 'Lanche', "Valor inserido difere do retorno")
        self.assertEqual(result.left, None, "Valor inserido difere do retorno")
        self.assertEqual(result.right.value, 'Pizza', "Valor inserido difere do retorno")
        Node.set_left(self, 'Banana')
        self.assertEqual(Node.get_left(self), 'Banana', "Função get_left retornando errado")
    
if __name__ == "__main__":
    unittest.main()