
from pathlib import Path

from app import add, build_site, greet


def test_greet():
    assert greet("GitHub") == "Hello, GitHub!"


def test_greet_empty():
    assert greet("") == "Hello, !"


def test_add():
    assert add(2, 3) == 5


def test_add_negative():
    assert add(-5, 2) == -3


def test_build_site(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    build_site()

    output = Path("dist/index.html")

    assert output.exists()
    assert "GitHub Actions CI/CD Success!" in (
        output.read_text(encoding="utf-8")
    )
