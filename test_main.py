from typer.testing import CliRunner

from main import app, __app_name__, __version__

runner = CliRunner()


def test_version():
    result = runner.invoke(app, ["-v"])
    assert result.exit_code == 0
    assert f"{__app_name__} v{__version__}\n" in result.stdout


def test_app():
    result = runner.invoke(app, ["main", "scores.txt"])
    assert result.exit_code == 0
    assert "1. Tarantulas 6 pts" in result.stdout
    assert "4. Snakes 1 pt" in result.stdout
    assert "5. Grouches 0 pts" in result.stdout
