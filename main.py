import time
from src.game_state import GameMatch
from src.sabotages import VotingSystem

def run_simulation():
    print("🛸 STARTING AMONG US ENGINE SIMULATION 🛸\n" + "="*40)
    
    # 1. Setup the game lobby
    match = GameMatch()
    match.add_player("p1", "RedCrew", role="Crewmate")
    match.add_player("p2", "BlueCrew", role="Crewmate")
    match.add_player("p3", "GreenImp", role="Impostor")
    
    print(f"👥 Players in Lobby: {[p.nickname for p in match.players]}")
    print(f"🎮 Initial Match Status: {match.status}")
    
    # 2. Start the game
    print("\n🚀 Shuttling players into the spacecraft...")
    match.start_match()
    print(f"🎮 Current Match Status: {match.status}")
    
    # 3. Simulating game ticks and a kill
    print("\n⏳ Game starts... Impostor is stalking...")
    match.game_tick()
    
    impostor = match.players[2] # GreenImp
    target = match.players[0]   # RedCrew
    
    print(f"🔪 {impostor.nickname} ({impostor.role}) attacks {target.nickname} ({target.role})!")
    kill_success = impostor.kill_target(target)
    
    if kill_success:
        print(f"💀 REPORT! A dead body has been found! {target.nickname} is dead.")
    
    # 4. Emergency Meeting Voting
    print("\n🚨 EMERGENCY MEETING CALLED! Voting starts...")
    # BlueCrew and GreenImp vote to eject p3 (GreenImp)
    active_votes = {"p2": "p3", "p3": "p3"}
    active_player_ids = ["p2", "p3"]
    
    ejected_id = VotingSystem.process_votes(active_votes, active_player_ids)
    
    if ejected_id:
        for p in match.players:
            if p.id == ejected_id:
                p.is_alive = False
                print(f"🌌 {p.nickname} was ejected from the spacecraft.")
    
    # 5. Check match results
    print("\n🏁 Checking structural victory conditions...")
    winner = match.check_victory_conditions()
    
    print("="*40)
    print(f"🏆 MATCH OVER! Winner Team: {winner} 🎉")
    print(f"🎮 Final Match Status: {match.status}")

if __name__ == "__main__":
    run_simulation()
