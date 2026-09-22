base_checks = ["Проверить затяжку винтов", "Проверить заряд батареи (не менее 95%)", "Проверить связь с пультом"]
camera_checks = ["Снять защитную крышку с объектива", "Проверить флешку в камере", "Сделать тестовый снимок"]
night_checks = ["Включить габаритные огни", "Проверить работу маяка"]
final_checklist = base_checks.copy()
has_camera = input('На дроне установлена камера? (да/нет:)')
if has_camera == 'да':
    final_checklist += camera_checks
night_mode = input('Этот дрон рассчитан на использование в темное время суток? (да/нет):')
if night_mode == 'да':
    final_checklist += night_checks
number = 0
with open('checklist.txt', "w", encoding="utf-8") as checklist:
    for item in final_checklist:
        number += 1
        checklist.write(f"{number}. {item}\n")


print(f'Итоговый список действий: {final_checklist}')