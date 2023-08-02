from ast import Assert
import unittest
from chess_model_impl import ChessModelImpl
from i_figure_generator_impl import FigureGeneratorImpl

class TestFigureGeneratorImpl(unittest.TestCase):
    def setUp(self):
        self.figureGenerator = FigureGeneratorImpl()

    def test_figOneGen(self):
        total_moves = 2
        self.assertEqual(self.figureGenerator.figureOneGen(total_moves), 2)
    
    if __name__ == '__main__':
        unittest.main()
