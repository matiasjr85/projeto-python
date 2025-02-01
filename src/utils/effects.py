import sys
import time

def type_effect(text, delay=0.02):
    """Simula efeito de digitação ao exibir texto"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()
