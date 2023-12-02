import pytest
from main.py import simulate_fitting_room

# Output expected
# When a blue thread is the first to enter an empty fitting room, the thread should print the string “Blue only.”
# When a green thread is the first to enter an empty fitting room, the thread should print the string “Green only.”
# When a thread enters the fitting room, the thread should print its thread ID and color (i.e., blue or green).
# When a thread is the last to exit the fitting room, the thread should print the string “Empty fitting room.”

def capture_fitting_room(capsys, n, b, g):
    simulate_fitting_room(n, b, g)
    captured = capsys.readouterr()

    return captured

def test_blue_only(capsys):
    captured = capture_fitting_room(capsys, 1, 1, 0)
    assert "Blue only." in captured.out

def test_green_only(capsys):
    captured = capture_fitting_room(capsys, 1, 0, 1)
    assert "Green only." in captured.out

