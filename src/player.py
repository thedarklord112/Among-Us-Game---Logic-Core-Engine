from typing import List, Dict, Any
from src.tasks import TaskManager

class Player:
    def __init__(self, player_id: str, nickname: str, role: str):
        """
        Initializes a player in the match.
        role can be either 'Crewmate' or 'Impostor'.
        """
        self.id = player_id
        self.nickname = nickname
        self.role = role  
        self.is_alive = True
        self.kill_cooldown = 0  # Only changes for Impostors
        self.tasks: List[Dict[str, Any]] = []

        # Automatically assign tasks if the player is a Crewmate
        if self.role == "Crewmate":
            manager = TaskManager()
            self.tasks = manager.assign_random_tasks()

    def reduce_cooldown(self):
        """Reduces the kill cooldown by 1 second (simulating a game tick)."""
        if self.kill_cooldown > 0:
            self.kill_cooldown -= 1

    def kill_target(self, target_player: 'Player') -> bool:
        """
        Executes an elimination target if the player is an active Impostor 
        and the cooldown counter has hit zero.
        """
        if self.role != "Impostor" or not self.is_alive:
            return False
        if self.kill_cooldown > 0 or not target_player.is_alive or target_player.role == "Impostor":
            return False

        target_player.is_alive = False
        self.kill_cooldown = 25  # Reset kill cooldown to 25 seconds
        return True
