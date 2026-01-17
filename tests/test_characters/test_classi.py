# tests/test_characters/test_classi.py

import random

def test_mago_attacco(sample_personaggi):
    mago = sample_personaggi["mago"]
    danno = mago.attacca()
    assert isinstance(danno, int)

def test_guerriero_attacco(sample_personaggi):
    guerriero = sample_personaggi["guerriero"]
    danno = guerriero.attacca()
    assert isinstance(danno, int)

def test_ladro_attacco(sample_personaggi):
    ladro = sample_personaggi["ladro"]
    danno = ladro.attacca()
    assert isinstance(danno, int) or danno == 0
