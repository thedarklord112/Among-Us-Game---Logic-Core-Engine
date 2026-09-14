from typing import List, Dict, Any
import random

class TaskManager:
    def __init__(self):
        # List of available tasks inspired by the Skeld map
        self.available_tasks = {
            "FIX_WIRING": {"name": "Fix Wiring", "steps": 3},
            "DOWNLOAD_DATA": {"name": "Download Data", "steps": 2},
            "SWIPE_CARD": {"name": "Swipe Card", "steps": 1},
            "DIVERT_POWER": {"name": "Divert Power", "steps": 2}
        }

    def assign_random_tasks(self, count: int = 3) -> List[Dict[str, Any]]:
        """Assigns a set of tasks to a player at the start of the match."""
        task_keys = random.sample(list(self.available_tasks.keys()), count)
        
        assigned = []
        for key in task_keys:
            task_info = self.available_tasks[key]
            assigned.append({
                "id": key,
                "name": task_info["name"],
                "total_steps": task_info["steps"],
                "current_step": 0,
                "is_completed": False
            })
        return assigned

    def check_global_progress(self, all_players: List[Any]) -> float:
        """Calculates the total game task completion percentage (0.0 to 100.0)."""
        total_tasks = 0
        completed_tasks = 0

        for player in all_players:
            if player.role == "Crewmate":
                for task in player.tasks:
                    total_tasks += 1
                    if task["is_completed"]:
                        completed_tasks += 1

        if total_tasks == 0:
            return 100.0
        return round((completed_tasks / total_tasks) * 100, 2)
