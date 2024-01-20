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
from bot_stockfish import BotStockfish, GenomeStockfish
from bot_ci_2 import BotCI2
from bot_ci_1 import BotCI1
from game_over_status import GameOverStatus
from i_figure_generator_impl import FigureGeneratorImpl
from group_win_data import GroupMatchData


def evolve(num_games_per_round = 10, num_population = 10, max_evolution_rounds = 10) -> List[GenomeBotCI3]:
    f = FigureGeneratorImpl()
    groups_data : List[GroupMatchData]= []

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
            print("Genome under test: ")
            print(genome.to_string())

            num_wins_per_genome[genome] = 0
            total_draws = 0
            
            for i in range(num_games_per_round):
                model = ChessModelImpl()
                bot = BotCI3.create_from_genome(model, genome, False)
                opponent = AIRandomMovesPlayer(model)
                view = IAsciiChessViewImpl(model, False)
                if i % 2 == 0:
                    controller = ChessControllerImpl(model, view, bot, opponent)
                else:
                    controller = ChessControllerImpl(model, view, opponent, bot)

                game_over_status = controller.run(False)
                
                if game_over_status == GameOverStatus.DRAW:
                    total_draws+=1
                elif i % 2 == 0 and game_over_status == GameOverStatus.WHITE_WIN:
                    num_wins_per_genome[genome] = num_wins_per_genome[genome] + 1
                elif i % 2 != 0 and game_over_status == GameOverStatus.BLACK_WIN:
                    num_wins_per_genome[genome] = num_wins_per_genome[genome] + 1

        total_wins_population = 0
        print("Fitness scores for population: " + str(j-1))
        for genome in num_wins_per_genome.keys():
            print(genome.to_string())
            print("Number of wins for this genom " + str(str(num_wins_per_genome[genome])))
            total_wins_population += num_wins_per_genome[genome]
        print("Total wins for this population " + str(j-1) + ": " + str(total_wins_population))

        group_data = GroupMatchData(j-1, "Generation Number", "AIRandomMovesPlayer", total_wins_population, total_draws, 
                                    (num_games_per_round * num_population) - total_wins_population - total_draws) #TODO: Auto opponent name
        groups_data.append(group_data)

        # Breeding pool?
        breeding_pool = []
        for genome in num_wins_per_genome.keys():
            for i in range(num_wins_per_genome[genome] + 1):
                breeding_pool.append(genome)
        
        print("BREEDING POOL")
        print("===============")
        for genome in breeding_pool:
            print(genome.to_string())
        print("===============")
            
        # Crossover
        parent1 : GenomeBotCI3 = breeding_pool[randint(0, len(breeding_pool) - 1)]
        # Remove parent 1 from breeding pool
        breeding_pool_parent_1_removed : List[GenomeBotCI3] = []
        for genome in breeding_pool:
            if (genome != parent1):
                breeding_pool_parent_1_removed.append(genome)

        parent2 : GenomeBotCI3 = breeding_pool_parent_1_removed[randint(0, len(breeding_pool_parent_1_removed) - 1)]

        print("Parent 1 Genome: " + parent1.to_string() + " Wins for this genome: " + str(num_wins_per_genome[parent1]))
        print("Parent 2 Genome: " + parent2.to_string() + " Wins for this genome: " + str(num_wins_per_genome[parent2]))

        child: GenomeBotCI3 = parent1.crossover(parent2)
        print("Child Genome before mutation: " + child.to_string())

        # Mutation
        child = child.mutate(0.4)

        print("Child Genome after mutation: " + child.to_string())


        # Replacement (lowest performing individual)
        lowest_genome = None
        lowest_wins = None

        for genome in num_wins_per_genome.keys():
            if lowest_genome is None:
                lowest_genome = genome
                lowest_wins = num_wins_per_genome[genome]
            elif num_wins_per_genome[genome] < lowest_wins:
                lowest_genome = genome
                lowest_wins = num_wins_per_genome[genome]

        print("Lowest performing genome: " + lowest_genome.to_string())
        population.remove(lowest_genome)
        population.append(child)

        print("Population: " + str(j))
        for genome in population:
            print(genome.to_string())
    
    f.figureGroupVWins(groups_data)
    return population


def evolveStockfish(num_games_per_round = 1, num_population = 2, max_evolution_rounds = 2) -> List[GenomeStockfish]:
    f = FigureGeneratorImpl()
    groups_data : List[GroupMatchData]= []

    # Create population
    population : List[GenomeStockfish] = []
    for i in range(num_population):
        population.append(GenomeStockfish.create_random())
    
    print("Initial Population: ")
    for genome in population:
        print(genome.to_string())

    # Evolution loop
    for j in range(max_evolution_rounds):
        # Fitness
        num_wins_per_genome = {}
        for genome in population:
            print("Genome under test: ")
            print(genome.to_string())

            num_wins_per_genome[genome] = 0
            total_draws = 0
            
            for i in range(num_games_per_round):
                print("Game " + str(i))
                model = ChessModelImpl()
                bot = BotStockfish.create_from_genome(model, genome)
                opponent = BotStockfish(model, 1000, 500)
                view = IAsciiChessViewImpl(model, False)
                if i % 2 == 0:
                    controller = ChessControllerImpl(model, view, bot, opponent)
                else:
                    controller = ChessControllerImpl(model, view, opponent, bot)

                game_over_status = controller.run(False)
                
                if game_over_status == GameOverStatus.DRAW:
                    total_draws+=1
                elif i % 2 == 0 and game_over_status == GameOverStatus.WHITE_WIN:
                    num_wins_per_genome[genome] = num_wins_per_genome[genome] + 1
                elif i % 2 != 0 and game_over_status == GameOverStatus.BLACK_WIN:
                    num_wins_per_genome[genome] = num_wins_per_genome[genome] + 1

        total_wins_population = 0
        print("Fitness scores for population: " + str(j-1))
        for genome in num_wins_per_genome.keys():
            print(genome.to_string())
            print("Number of wins for this genom " + str(str(num_wins_per_genome[genome])))
            total_wins_population += num_wins_per_genome[genome]
        print("Total wins for this population " + str(j-1) + ": " + str(total_wins_population))

        group_data = GroupMatchData(j-1, "Generation Number", "Stockish ELO 1000, time_constraint: 500", total_wins_population, total_draws, 
                                    (num_games_per_round * num_population) - total_wins_population - total_draws) #TODO: Auto opponent name
        groups_data.append(group_data)

        # Breeding pool?
        breeding_pool = []
        for genome in num_wins_per_genome.keys():
            for i in range(num_wins_per_genome[genome] + 1):
                breeding_pool.append(genome)
        
        print("BREEDING POOL")
        print("===============")
        for genome in breeding_pool:
            print(genome.to_string())
        print("===============")
            
        # Crossover
        parent1 : GenomeStockfish = breeding_pool[randint(0, len(breeding_pool) - 1)]
        # Remove parent 1 from breeding pool
        breeding_pool_parent_1_removed : List[GenomeStockfish] = []
        for genome in breeding_pool:
            if (genome != parent1):
                breeding_pool_parent_1_removed.append(genome)

        parent2 : GenomeStockfish = breeding_pool_parent_1_removed[randint(0, len(breeding_pool_parent_1_removed) - 1)]

        print("Parent 1 Genome: " + parent1.to_string() + " Wins for this genome: " + str(num_wins_per_genome[parent1]))
        print("Parent 2 Genome: " + parent2.to_string() + " Wins for this genome: " + str(num_wins_per_genome[parent2]))

        child: GenomeStockfish = parent1.crossover(parent2)
        print("Child Genome before mutation: " + child.to_string())

        # Mutation
        child = child.mutate(0.4)

        print("Child Genome after mutation: " + child.to_string())


        # Replacement (lowest performing individual)
        lowest_genome = None
        lowest_wins = None

        for genome in num_wins_per_genome.keys():
            if lowest_genome is None:
                lowest_genome = genome
                lowest_wins = num_wins_per_genome[genome]
            elif num_wins_per_genome[genome] < lowest_wins:
                lowest_genome = genome
                lowest_wins = num_wins_per_genome[genome]

        print("Lowest performing genome: " + lowest_genome.to_string())
        population.remove(lowest_genome)
        population.append(child)

        print("Population: " + str(j))
        for genome in population:
            print(genome.to_string())
    
    f.figureGroupVWins(groups_data)
    return population


if __name__ == "__main__":
    #final_pop = evolve()
    final_pop = evolveStockfish()
    print("Final Population: ")
    for genome in final_pop:
        print(genome.to_string())
