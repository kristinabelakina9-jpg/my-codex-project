"""Первый проект для работы с OpenAI Codex."""


def greet(name: str = "мир") -> str:
    return f"Привет, {name}! Codex готов к работе."


if __name__ == "__main__":
    print(greet())
