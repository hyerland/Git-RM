from typer.testing import CliRunner

from src.gitrm.cli import app

runner = CliRunner()


def test_app():
    result = runner.invoke(app, ["https://github.com/hyerland/Git-RM"])
    assert result.exit_code == 0
    assert "Successfully cloned, [green][dim]'{url}'[/dim][/green] and stored within cache." in result.stdout