# Huvudfil för ekonomiprogrammet
''''=== Import av moduler ==='''
import time
import matplotlib.pyplot as plt
import numpy as np
import csv # Behövs för att läsa in skattetabell
import ekonomi_funktioner as ef
"""=== Huvudprogram ==="""
def main():
# Visar välkomstext när programmet startar.
ef.welcome()
# Låt användaren välja kommun från skattetabell
# valda_rader har all data för kommun
# Skattesats är bara procentsatsen
valda_rader, skattesats = ef.val_kommun(filnamn='skattetabell.csv')
# Kollar om skattesatsen faktist hittades
# Om skattesatsen saknas (None) så används ett standardvärde på 30%
if skattesats is None:
print("Skattesatsen kunde inte hämtas. Använder standardvärde på 30 %")
skattesats = 30.0
# Starta huvudmenysystem där användaren kan välja olika funktioner
ef.meny(skattesats, valda_rader)
main() # Startar 
