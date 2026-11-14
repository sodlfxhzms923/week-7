
from pathlib import Path


def greet(name: str) -> str:
    return f"Hello, {name}!"


def add(a: int, b: int) -> int:
    return a + b


def build_site() -> None:
    output = Path("dist")
    output.mkdir(exist_ok=True)

    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Python CI/CD</title>
    </head>
    <body>
        <h1>GitHub Actions CI/CD Success!</h1>
        <p>Build, Test, Deploy completed.</p>
    </body>
    </html>
    """

    (output / "index.html").write_text(
        html, encoding="utf-8"
    )


if __name__ == "__main__":
    build_site()
    print(greet("GitHub Actions"))
