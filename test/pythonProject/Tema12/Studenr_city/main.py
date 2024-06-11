import csv
import re
def write_holiday_cities(first_letter):
    travel_notes = []
    visited_set = set()
    wish_set = set()
    with (open('travel-notes.csv', 'r', newline='', encoding='utf8') as file_read):
        reader = csv.reader(file_read)
        for row in reader:
            if row[0].startswith(first_letter):
                pattern = r"\w+(?:(?:[^;]*\[[^][]*])+[^;]*|[^;']+)"
                travel_notes.append(row)
                cities = re.findall(pattern, row[1])
                for city in cities:
                    visited_set.add(city)

                cities = re.findall(pattern, row[2])
                for city in cities:
                    wish_set.add(city)

    all_cities = visited_set.union(wish_set)
    not_been = (all_cities.difference(visited_set))
    next_city = sorted(not_been)[0] if not_been else ''
    with (open('holiday.csv', 'w', newline='', encoding='utf8') as file_out):
        writer = csv.writer(file_out)
        writer.writerow([f'Информация о городах людей, имена которых начинаются на: {first_letter} '])
        writer.writerow(['Уже были в: ', ', '.join(sorted(visited_set))])
        writer.writerow(['Хотят побывать в: ', ', '.join(sorted(wish_set))])
        writer.writerow(['Еще не были в: ', ', '.join(sorted(not_been))])
        writer.writerow(['Следующий город: ', next_city])

letter = "L"
find_cities_by_letter_name = write_holiday_cities(letter)