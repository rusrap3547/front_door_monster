import os
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GAME = ROOT / "game.py"


def run_game(commands, monster_name="Vampire"):
    env = os.environ.copy()
    env["FDM_MONSTER"] = monster_name

    payload = "\n".join(commands) + "\n"
    result = subprocess.run(
        [sys.executable, str(GAME)],
        input=payload,
        capture_output=True,
        text=True,
        env=env,
        cwd=ROOT,
    )
    return result.stdout


class GameSmokeTests(unittest.TestCase):
    def test_quit_command_ends_game(self):
        output = run_game(["quit"])
        self.assertIn("RPG Game", output)
        self.assertIn("Game over. Thanks for playing.", output)

    def test_balcony_reveals_hint(self):
        # Vampire starts in Master Bedroom.
        output = run_game(
            [
                "go east",
                "go north",
                "go south",
                "go west",
                "go south",
                "go south",
                "get balcony key",
                "go north",
                "go north",
                "go east",
                "go north",
                "quit",
            ],
            monster_name="Vampire",
        )

        self.assertIn("You are currently in the Balcony.", output)
        self.assertIn("A torn note catches in the wind...", output)
        self.assertIn("You see a vampire guarding something in the Green House.", output)
        self.assertIn("The lights snap out for a heartbeat.", output)


if __name__ == "__main__":
    unittest.main()
