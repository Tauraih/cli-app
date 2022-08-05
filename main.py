from typing import Optional

import typer

__app_name__ = "cli app"
__version__ = "0.1.0"


app = typer.Typer()


@app.command()
def main(name: str):
    with open(name, 'r') as f:
        team_dict = dict()
        for line in f:
            teams = line.split(",")
            team_1 = teams[0].strip(" ")
            team_2 = teams[1].strip(" ").strip("\n")
            team_1_name = team_1[:-1]
            team_2_name = team_2[:-1]
            team_1_score = int(team_1[-1])
            team_2_score = int(team_2[-1])
            if team_1_score > team_2_score:
                if team_dict.get(team_1_name):
                    team_dict[team_1_name] = 3 + team_dict.get(team_1_name)
                else:
                    team_dict[team_1_name] = 3
                if team_dict.get(team_2_name) is None:
                    team_dict[team_2_name] = 0
            elif team_1_score == team_2_score:
                if team_dict.get(team_1_name):
                    team_dict[team_1_name] = 1 + team_dict.get(team_1_name)
                else:
                    team_dict[team_1_name] = 1
                if team_dict.get(team_2_name):
                    team_dict[team_2_name] = 1 + team_dict.get(team_2_name)
                else:
                    team_dict[team_2_name] = 1
            elif team_1_score < team_2_score:
                if team_dict.get(team_2_name):
                    team_dict[team_2_name] = 3 + team_dict.get(team_2_name)
                else:
                    team_dict[team_2_name] = 3
                if team_dict.get(team_1_name) is None:
                    team_dict[team_1_name] = 0
        f.close()
        sorted_teams = sorted(team_dict.items(), key=lambda x: (-x[1], x[0]))
        for i,x in enumerate(sorted_teams, start=1):
            if x[1] != 1:
                print(f"{i}. {x[0]}{x[1]} pts")
            else:
                print(f"{i}. {x[0]}{x[1]} pt")


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


@app.callback()
def version(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version",
        callback = _version_callback,
        is_eager=True,
    )
) -> None:
    return


if __name__ == "__main__":
    app()
