from argparse import ArgumentError
from bot_ci_3 import BotCI3
from i_player import IPlayer
from typing import List
from bot_ci_3 import GenomeBotCI3
from chess_model_impl import ChessModelImpl
from ai_random_moves_player import AIRandomMovesPlayer
from chess_controller_impl import ChessControllerImpl
from i_ascii_chess_view_impl import IAsciiChessViewImpl
from random import randint
from bot_stockfish import BotStockfish
from bot_ci_2 import BotCI2
from bot_ci_1 import BotCI1
from game_over_status import GameOverStatus


def evolve(num_games_per_round = 20, num_population = 20, max_evolution_rounds = 20) -> List[GenomeBotCI3]:
    # Create population
    population : List[GenomeBotCI3] = []
    for i in range(num_population):
        population.append(GenomeBotCI3.create_random())
    
    print("Initial Population: ")
    for genome in population:
        print(genome.to_string())

    # Evolution loop
    for j in range(max_evolution_rounds):
        # Fitness
        num_wins_per_genome = {}
        for genome in population:
            num_wins_per_genome[genome] = 0
            
            for i in range(num_games_per_round):
                model = ChessModelImpl()
                bot = BotCI3.create_from_genome(model, genome, False)
                opponent = BotCI1(model, False)
                view = IAsciiChessViewImpl(model, False)
                if i % 2 == 0:
                    controller = ChessControllerImpl(model, view, bot, opponent)
                else:
                    controller = ChessControllerImpl(model, view, opponent, bot)

                game_over_status = controller.run(False)
                
                if i % 2 == 0 and game_over_status == GameOverStatus.WHITE_WIN:
                    num_wins_per_genome[genome] = num_wins_per_genome[genome] + 1
                elif i % 2 != 0 and game_over_status == GameOverStatus.BLACK_WIN:
                    num_wins_per_genome[genome] = num_wins_per_genome[genome] + 1

        # Breeding pool?
        breeding_pool = []
        for genome in num_wins_per_genome.keys():
            for i in range(num_wins_per_genome[genome] + 1):
                breeding_pool.append(genome)
            
        # Crossover
        parent1 : GenomeBotCI3 = breeding_pool[randint(0, len(breeding_pool) - 1)]
        parent2 : GenomeBotCI3 = breeding_pool[randint(0, len(breeding_pool) - 1)]

        child: GenomeBotCI3 = parent1.crossover(parent2)

        # Mutation
        child = child.mutate()

        # Replacement (lowest performing individual)
        lowest_genome = None
        lowest_wins = 0

        for genome in num_wins_per_genome.keys():
            if lowest_genome is None:
                lowest_genome = genome
            elif num_wins_per_genome[genome] < lowest_wins:
                lowest_genome = genome

        population.remove(lowest_genome)
        population.append(child)

        total_wins_population = 0
        print("Fitness scores for population: " + str(j-1))
        for genome in num_wins_per_genome.keys():
            print(genome.to_string())
            print("Number of wins for this genom " + str(num_wins_per_genome[genome]))
            total_wins_population += num_wins_per_genome[genome]
        print("Total wins for this population " + str(j-1) + ": " + str(total_wins_population))

        print("Population: " + str(j))
        for genome in population:
            print(genome.to_string())
    
    return population


if __name__ == "__main__":
    final_pop = evolve()
    print("Final Population: ")
    for genome in final_pop:
        print(genome.to_string())
