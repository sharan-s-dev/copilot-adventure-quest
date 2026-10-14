"""
Unit tests for Chrono-Hacker's Quest game mechanics.
"""

import pytest
from adventure import Player


def test_player_initialization():
    player = Player("Neo")
    assert player.name == "Neo"
    assert player.health == 100
    assert player.is_alive() is True
    assert player.has_item("Cyberdeck") is True
    assert player.has_item("Quantum Key") is True


def test_player_damage_and_healing():
    player = Player("Trinity")
    player.take_damage(40)
    assert player.health == 60
    assert player.is_alive() is True

    player.heal(20)
    assert player.health == 80

    player.heal(100)  # Should cap at max_health
    assert player.health == 100

    player.take_damage(150)
    assert player.health == 0
    assert player.is_alive() is False


def test_inventory_management():
    player = Player("Morpheus")
    assert player.has_item("Plasma Overclocker") is False
    player.add_item("Plasma Overclocker")
    assert player.has_item("Plasma Overclocker") is True
