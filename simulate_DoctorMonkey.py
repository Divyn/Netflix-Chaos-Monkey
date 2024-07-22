import random
import time
import requests


def simulate_doctor():
  if random.random() < 0.5:
    print("Doctor Monkey: Checking Replit Health!")
    response = requests.get("https://replit.com/@DShree/")
    if response.status_code == 200:
      print("Doctor Monkey: Everything is fine.")

  time.sleep(1)


if __name__ == "__main__":
  simulate_doctor()
