import random as rd 
import threading
import time


# Agent function table
agent_table = {
    ('Clean', 'A'): 'MoveRight',
    ('Clean', 'B'): 'MoveLeft',
    ('Dirty', 'A'): 'Suck',
    ('Dirty', 'B'): 'Suck',
}

env = {
    'A' : [],
    'B' : []
}
# Vacuum cleaner class
class VacuumCleaner:
    def __init__(self, location='A', status='Clean'):
        self.location = location
        self.status = status

    def percept(self):
        return self.status

    def act(self, action):
        if action == 'MoveRight':
            self.location = 'B'
        elif action == 'MoveLeft':
            self.location = 'A'
        elif action == 'Suck':
            self.status = 'Clean'
            env['A'] = "Clean"
            env['B'] = "Clean"

# Table-driven agent function
def table_driven_agent(percept):
    return agent_table.get(percept, 'NoOp')



def evilMan(interval,vacuum):

    for _ in range(5):
        for key in env:
            if vacuum.location != key:
                env['A'] = 'dirty'
                vacuum.status = "Dirty"
            else:
                env['B'] = 'dirty'
                vacuum.status = "Dirty"
        time.sleep(interval)


# Main simulation loop
if __name__ == "__main__":
    vacuum = VacuumCleaner()

    #running the thread of evilman to add dirt to env and vacuum status.
    run_bg = threading.Thread(target = evilMan, args = (3,vacuum), daemon = True)
    run_bg.start()

    for _ in range(10):  # Run for 10 time steps
        current_percept = vacuum.percept()
        action = table_driven_agent((current_percept, vacuum.location))
        print(f"Percept: {current_percept}, Action: {action}")

        if action != 'NoOp':
            vacuum.act(action)
            time.sleep(1)

        print(f"Location: {vacuum.location}, Status: {vacuum.status}\n")

   #Check room status at end     
    for k in range(1):
        print(env.get('A'))
        print(env.get('B')) 
