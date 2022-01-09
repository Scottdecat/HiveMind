import json

from bot import MyBot
from bot.configuration.basic_configuration import BasicConfiguration
from sc2 import Difficulty, Race, maps, run_game
from sc2.player import AIBuild, Bot, Computer, Human


def main():
    with open("botinfo.json") as f:
        info = json.load(f)

    race = Race[info["race"]]

    run_game(maps.get("OdysseyLE"), [
        Bot(race, MyBot()),
        Computer(Race.Terran, Difficulty.VeryHard, ai_build=AIBuild.Timing)
    ], realtime=False, step_time_limit=2.0, game_time_limit=(60*20), save_replay_as="test.SC2Replay")

    #Code for playing against yoru own bot
    # run_game(maps.get("OdysseyLE"), [
    #     #Human(Race.Terran),
    #     Human(Race.Zerg),
    #     Bot(race, MyBot()),
    #     # Computer(Race.Terran, Difficulty.CheatInsane, ai_build=AIBuild.Timing)
    # ], realtime=True, game_time_limit=(60*20), save_replay_as="test.SC2Replay")

if __name__ == '__main__':
    main()
