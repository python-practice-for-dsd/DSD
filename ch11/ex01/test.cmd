@echo off
cd %~p0
python -m unittest -v unit_test_ex1101_server.py
python -m unittest -v combined_test_ex1101.py