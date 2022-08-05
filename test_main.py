from typer.testing import CliRunner

from main import app 

runner = CliRunner()


def test_app():
    result = runner.invoke(app, ["scores.txt"])
    assert result.exit_code == 0
    assert "1. Tarantulas 6 pts" in result.stdout
    assert "4. Snakes 1 pt" in result.stdout
    assert "5. Grouches 0 pts" in result.stdout
