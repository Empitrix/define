from src.visual import prt
import subprocess, os

# Check for less
if os.system("less --version") == 1:
	prt('[red]"Less" is NOT installed!')

