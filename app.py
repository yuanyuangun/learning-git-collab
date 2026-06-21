from pathlib import Path


TASKS_FILE = Path("tasks.txt")


def load_tasks():
    if not TASKS_FILE.exists():
        return []

    return [
        line.strip()
        for line in TASKS_FILE.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def show_tasks(tasks):
    print("Git 协作练习任务清单")
    print("=" * 24)

    if not tasks:
        print("暂无任务。")
        return

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def main():
    tasks = load_tasks()
    show_tasks(tasks)


if __name__ == "__main__":
    main()
