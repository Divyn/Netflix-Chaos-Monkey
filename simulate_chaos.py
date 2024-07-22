import random
import time


def simulate_chaos():
  # Introduce randomness in your code to simulate failures
  if random.random() < 0.2:
    print("Chaos Monkey: Simulating failure!")
    #terminate_instance

  # Simulate other chaotic events
  if random.random() > 0.8:
    # Simulate network delay by sleeping for a random amount of time
    print("Chaos Monkey: Introducing latency or disruption!")
    time.sleep(random.uniform(1, 5))

  # Continue normal operation
  print("Chaos Monkey: Everything is fine.")
  time.sleep(1)


if __name__ == "__main__":
  simulate_chaos()
