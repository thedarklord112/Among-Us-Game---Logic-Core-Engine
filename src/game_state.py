from typing import List, Dict, Any, Optional
from src.player import Player
from src.sabotages import SabotageManager, VotingSystem

class GameMatch:
    def __init__(self):
        self.players: List[Player] = []
        self.status: str = "LOBBY"  # LOBBY, IN_GAME, END_GAME
        self.winner_role: Optional[str] = None
        self.sabotage_manager = SabotageManager()

    def add_player(self, player_id: str, nickname: str, role: str) -> bool:
        """Adds a player to the lobby before the match starts."""
        if self.status != "LOBBY":
            return False
        self.players.append(Player(player_id, nickname, role))
        return True

    def start_match(self):
        """Transitions the match status from the lobby to the active game state."""
        if len(self.players) >= 3:  # Minimum required players to start
            self.status = "IN_GAME"

    def game_tick(self):
        """Simulates one second of game time, updating cooldowns and critical events."""
        if self.status != "IN_GAME":
            return

        # 1. Update sabotage counts
        if self.sabotage_manager.is_critical:
            self.sabotage_manager.countdown -= 1
            if self.sabotage_manager.countdown <= 0:
                self.status = "END_GAME"
                self.winner_role = "Impostor"
                return

        # 2. Update player abilities countdown
        for player in self.players:
            player.reduce_cooldown()

    def check_victory_conditions(self) -> Optional[str]:
        """
        Evaluates the current state to check if any team met a win condition.
        Returns 'Crewmate', 'Impostor', or None.
        """
        if self.status == "END_GAME":
            return self.winner_role

        alive_crewmates = 0
        alive_impostors = 0
        total_crew_tasks_done = True

        for p in self.players:
            if p.is_alive:
                if p.role == "Crewmate":
                    alive_crewmates += 1
                    # Check if this crewmate still has pending tasks
                    if any(not t["is_completed"] for t in p.tasks):
                        total_crew_tasks_done = False
                elif p.role == "Impostor":
                    alive_impostors += 1

        # Condition A: Impostors wiped out or all tasks completed
        if alive_impostors == 0 or (alive_crewmates > 0 and total_crew_tasks_done):
            self.status = "END_GAME"
            self.winner_role = "Crewmate"
            return "Crewmate"

        # Condition B: Impostors outnumber or equal alive crewmates
        if alive_impostors >= alive_crewmates:
            self.status = "END_GAME"
            self.winner_role = "Impostor"
            return "Impostor"

        return None
