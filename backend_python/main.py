if __name__ == '__main__':

    # Fill list with powers of 2, n [1..20]
    n = list(range(1, 20 + 1))


    def powers_of_two(n):
        list_of_powers = []
        for i in range(0, len(n) + 1):
            power = i ** 2
            list_of_powers.append(power)
        return list_of_powers


    print(powers_of_two(n))

    # Display sum of first ten elements starting from element 5:
    numbers = [1, 5, 2, 3, 1, 4, 1, 23, 12, 2, 3, 1, 2, 31, 23, 1, 2, 3, 1, 23, 1, 2, 3, 123]


    def sum_of_first_ten_from_five(numbers):
        for i, value in enumerate(numbers):
            if value == 5:
                summary = 0
                for item in numbers[i:i + 10]:
                    summary = summary + item
                return summary
        return 'No value 5 has been found in the list'


    print(sum_of_first_ten_from_five(numbers))

    # Create good script to create new list, which only contains users from Poland. 
    # Try to do it with List Comprehension.

    users = [
        {"name": "Kamil", "country": "Poland"},
        {"name": "John", "country": "USA"},
        {"name": "Yeti"}
    ]

    list_of_polish_users = [item['name'] for item in users if item.get('country') == 'Poland']
    print(list_of_polish_users)
