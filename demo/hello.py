from prefect import flow, task
from prefect.blocks.system import String

string_block = String.load("future-nba-champs")

@task
def create_message():
    msg = "NBA Champs: "
    return msg

@flow
def future_nba_champs():
    team = string_block.value
    return team

@flow
def hello_world():
    nba_team = future_nba_champs()
    task_message = create_message()
    new_message = task_message + nba_team
    print(new_message)

if __name__ == "__main__":
    hello_world()
