from typing import Dict, List, Optional

class SabotageManager:
    def __init__(self):
        self.active_sabotage: Optional[str] = None
        self.countdown: int = 0
        self.is_critical: bool = False

    def trigger_sabotage(self, system_type: str):
        """Triggers a system crisis (O2, Reactor, or Lights)."""
        if self.active_sabotage:
            return  # One sabotage at a time!

        self.active_sabotage = system_type
        if system_type in ["O2", "REACTOR"]:
            self.countdown = 30  # 30 seconds to fix or Impostors win
            self.is_critical = True
        elif system_type == "LIGHTS":
            self.countdown = 0
            self.is_critical = False  # Lights just reduce visibility

    def resolve_sabotage(self):
        """Called when crewmates fix the system."""
        self.active_sabotage = None
        self.countdown = 0
        self.is_critical = False


class VotingSystem:
    @staticmethod
    def process_votes(votes: Dict[str, str], active_players: List[str]) -> Optional[str]:
        """
        Processes votes from an Emergency Meeting.
        Returns the ID of the ejected player, or None if it's a tie/skip.
        """
        tally: Dict[str, int] = {"SKIP": 0}
        for player in active_players:
            tally[player] = 0

        # Count votes
        for voter, voted_target in votes.items():
            if voted_target in tally:
                tally[voted_target] += 1

        # Determine winner
        # We sort by the number of votes in descending order
        sorted_votes = sorted(tally.items(), key=lambda item: item[1], reverse=True)
        
        highest_vote_target, highest_count = sorted_votes[0]
        second_highest_count = sorted_votes[1][1] if len(sorted_votes) > 1 else 0

        # If there is a tie for the most votes, no one is ejected
        if highest_count == second_highest_count:
            return None

        if highest_vote_target == "SKIP":
            return None

        return highest_vote_target
