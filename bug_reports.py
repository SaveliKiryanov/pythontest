bug_reports = [
    "Ошибка 1 — High",
    "Ошибка 2 — Low",
    "Ошибка 3 — Medium",
    "Ошибка 4 — Low",
	"Ошибка 5 — High"
]
def add_bug(description, priority):
    bug_reports.append(f"{description} — {priority}")
    print(f"✅ Баг '{description} — {priority}' добавлен.")

def remove_low_priority():
    global bug_reports
    bug_reports = [bug for bug in bug_reports if "Low" not in bug]
    print("🗑 Все баги с низким приоритетом удалены.")

def sort_bugs():
    priority_order = {"High": 1, "Medium": 2, "Low": 3}
    bug_reports.sort(key=lambda bug: priority_order.get(bug.split(" — ")[1], 99))
    print("📋 Баги отсортированы по приоритету.")

print("📌 Исходный список багов:")
print(bug_reports)

add_bug("Ошибка 6", "Medium")
remove_low_priority()
sort_bugs()

print("\n📌 Итоговый список багов:")
for bug in bug_reports:
    print(bug)