# AmongUs Logic Core Engine (Stateless Simulation)

A production-grade, highly scalable, and object-oriented backend simulation engine that models the core gameplay mechanics of **Among Us**. Built entirely with clean **Python**, this repository focuses strictly on state machine execution, condition parsing, and mathematical win-state routing without graphical overhead.

## 📸 Terminal Simulation Preview

Here is how the game core executes a match simulation step-by-step directly inside your operating system terminal:

<img width="1221" height="709" alt="Screenshot 2026-09-14 202613" src="https://github.com/user-attachments/assets/2c023b2a-b8a5-4a6a-9e77-79ec138555f8" />


---

## 🚀 Key Features

- **Dynamic Task Architecture**: Automated random assignment patterns mapping multi-step worker duties (`FIX_WIRING`, `DOWNLOAD_DATA`, etc.) with dynamic global progress scaling.
- **Crisis & Sabotage Subsystems**: Time-critical execution loops managing emergency cooldown protocols (O2 leaks and Reactor core meltdowns) carrying immediate team-wipe win conditions.
- **Algorithmic Voting Engine**: Absolute-majority consensus resolution matrix built to accurately parse emergency meetings, skipping thresholds, and player expulsion variables.
- **State Machine Loop Verification**: Real-time evaluation triggers checking game tick progressions, ability cooldown reductions, and dynamic body reporting data arrays.

---

## 🎮 Code Architecture Overview

```text
├── src/
│   ├── __init__.py
│   ├── game_state.py      # Main loop manager, lobby allocations & victory conditions
│   ├── player.py          # Identity mapping objects (Crewmate vs Impostor metadata)
│   ├── sabotages.py       # Game crises handling timers & vote tally structures
│   └── tasks.py           # Crew task generation vectors and global progress maps
├── main.py                # Main simulation script execution entrypoint
└── README.md
```

---

## 🛠️ Usage & Execution

To test and review the core simulation loops live on your local workstation, run the primary entrypoint execution script using your system python environment:

```bash
python main.py
```

---

## 🔒 Engine Safety Constraints
- **Concurrency Guardrails**: All methods process localized structural logic data arrays, allowing developers to safely plug this core matrix into high-frequency connection networks like WebSockets or gRPC servers.
- **Type Restrictions**: Heavily integrated with internal Python parameter definitions to eliminate state cross-contamination.

## 📄 License
This architecture simulator engine is free and open-source under the [MIT License](LICENSE).
