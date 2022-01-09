from bot.chat.chat_interface import ChatInterface
from bot.logic.army_micro_manager.army_micro_manager_interface import \
    ArmyMicroManagerInterface
from bot.logic.army_strategy_manager.army_strategy_manager_interface import \
    ArmyStrategyManagerInterface
from bot.logic.army_tactics_manager.army_tactics_manager_interface import \
    ArmyTacticsManagerInterface
from bot.logic.logic_interface import LogicInterface
from bot.logic.queen_manager.default_queen_manager import DefaultQueenManager
from bot.logic.queen_manager.queen_manager_interface import \
    QueenManagerInterface
#from bot.logic.resource_manager.default_resource_manager import DefaultResourceManager
from bot.logic.resource_manager.resource_manager import ResourceManager
from bot.logic.resource_manager.resource_manager_interface import \
    ResourceManagerInterface
from bot.logic.spending.spending_interface import SpendingInterface
from bot.logic.spending.spending_v2 import Spendingv2
from bot.logic.spending.supply_mechanic.supply_mechanic_interface import \
    SupplyMechanicInterface
from bot.logic.spending_actions.spending_actions_interface import \
    SpendingActionsInterface

from ..chat.basic_chat import BasicChat
from ..logic.default_logic import DefaultLogic
from ..logic.spending.default_spending import DefaultSpending
from ..logic.spending.supply_mechanic.basic_supply import BasicSupply
from ..logic.spending_actions.default_spending_actions import \
    DefaultSpendingActions
from .configuration_interface import ConfigurationInterface


class BasicConfiguration(ConfigurationInterface):
    def __init__(self):
        self.d = {
            ChatInterface: BasicChat,
            LogicInterface: DefaultLogic,
            SpendingInterface: Spendingv2,
            SpendingActionsInterface: DefaultSpendingActions,
            SupplyMechanicInterface: BasicSupply,
            ResourceManagerInterface: ResourceManager,
            QueenManagerInterface: DefaultQueenManager
        }
    def get(self, injectable):
        return self.d[injectable]
