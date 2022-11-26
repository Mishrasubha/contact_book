import sys
import click

@click.command
@click.option("--add","-a",nargs=2,help="Adds the name and number")
@click.option("--find","-f",nargs=1,help="Finds a contact number using name")
@click.option("--list","-l",nargs=0,help="Lists all contact")
@click.option("--edit","-e",nargs=1,help="Edits the name or number")
@click.option("--remove","-rm",nargs=1,help="Deletes the number")
@click.option("--clear","-cl",nargs=0,help="Deletes all numbers")
@click.option("--export","ex",nargs=0,help="exports the list to csv")
def main():
    pass
