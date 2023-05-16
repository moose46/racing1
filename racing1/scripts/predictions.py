# from ast import Dict
import logging
from collections import Counter, defaultdict
from pathlib import Path

from nascar.models import Driver

log_file = Path.cwd() / "predictions_log.txt"
print(log_file)

logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="w",
)
total = []


def subset_sum(numbers, target, partial=[]):
    # sourcery skip: default-mutable-arg
    s = sum(partial)

    # check if the partial sum is equals to target
    if s == target and len(partial) == 5:
        # print("sum(%s)=%s" % (partial, target))
        total.append(partial)
    if s >= target:
        return  # if we reach the number why bother to continue
    # if len(partial) == 5 and s <= target:
    #     return
    # for i in range(len(numbers)):
    # print(f"len of numbers = {len(numbers)}")
    for i in range(len(numbers)):
        n = numbers[i]
        # print(f"n = {n}")
        remaining = numbers[i + 1 :]
        # print(f"remaining = {remaining}")
        # print(f"partial = {partial + [n]}")
        subset_sum(remaining, target, partial + [n])


from itertools import combinations, combinations_with_replacement, product


def special_permutation(lst, rno, suma):
    return [c for c in product(lst, repeat=rno) if sum(c) == suma]


def run():
    # if __name__ == "__main__":
    # drivers = Driver.objects.all().order_by("salary")
    drivers = Driver.objects.raw(
        "select 1 id, salary from nascar_driver group by salary order by salary"
    )
    # drivers = Driver.objects.raw(
    #     "select 1 id,salary from nascar_driver group by salary order by salary"
    # )

    # exit()
    # get the count of each salary for all the drivers
    db_count_of_salaries = {}
    for driver in drivers:
        if driver.salary not in db_count_of_salaries:
            db_count_of_salaries[driver.salary] = 0
        db_count_of_salaries[driver.salary] += 1
    # create a dictionary with number of times each salary occurs
    salaries = [s.salary for s in drivers]
    logging.info(f"salaries= {salaries}")

    # for s in salaries:
    #     print(f"sal={s}")
    # get picks for salaries rangiong from 40,000 to 50,000
    for x in range(40000, 50000, 10000):
        subset_sum(sorted(list(salaries), reverse=True), x)
    # for s in total:
    # print(s)
    # if len(s) == 5:
    #     print(s)
    # print(sorted(salaries))

    combo = combinations(special_permutation(list(salaries), 5, 50000), 1)
    combo = combinations(sorted(list(salaries), reverse=True), 5)
    salaries = [12000, 11000, 10000, 9000, 8000]
    combo = combinations_with_replacement(sorted(list(salaries), reverse=True), 5)
    for x in combo:
        if sum(x) == 50000:
            logging.info(x)
    exit()
    i = 0
    final_set = set()
    count_of_each_possible_salary = Counter()
    for list_of_possible_salaries in combo:
        if sum(list_of_possible_salaries) != 50000:
            continue
        logging.info(
            f"list_of_possible_salaries={list(list_of_possible_salaries)} type={type(list_of_possible_salaries)}"
        )
        # create a dictionary of all possible salaries
        count_of_each_possible_salary = Counter(list_of_possible_salaries)
        logging.info(f"count_of_each_possible_salary{count_of_each_possible_salary}")
        # loop through drivers salary and make sure it does not exceed the number of drivers with that
        # salary available
        # logging.info(f"db_count_of_salaries={db_count_of_salaries}")
        for s, value in db_count_of_salaries.items():
            if (
                count_of_each_possible_salary[s] <= value
                and sum(list_of_possible_salaries) == 50000
            ):
                i += 1
                # print(
                #     f"db_count_of_salaries[{s}] = {value} t={count_of_each_possible_salary} list_of_possible_salaries={list_of_possible_salaries} #{i} value={value}"
                # )
                final_set.add(list_of_possible_salaries)
            # print(f"{sum(c)} {c} #{i}")
    # print(f"dict of driver salaries {db_count_of_salaries}")
    for x in final_set:
        logging.info(f"final_set={x}")
    for pick_number, s in enumerate(list(final_set), start=2):
        s = set(s)
        # print(f"s={s}")
        possible_picks = {}
        for value in s:
            list_of_drivers_with_the_salary = Driver.objects.filter(salary=value)
            # print(
            #     f"salary={value} ---> list_of_drivers_with_salary={list_of_drivers_with_the_salary}"
            # )
            x = {
                f"{the_driver.name} {the_driver.salary}"
                for the_driver in list_of_drivers_with_the_salary
            }
            for y in list_of_drivers_with_the_salary:
                possible_picks[y.name] = y.salary
            # print(
            #     f"pick - {count_of_each_possible_salary[value]} ---> {x} type(x)={type(x)}"
            # )
            # print(f"s={s} ---> x={x}")

            # print(f"{d} {d.salary}")
        # print(f"1 - possible_picks={combinations_with_replacement(possible_picks, 5)}")
        # if sum(possible_picks[item] for item in possible_picks) > 50000:
        #     print(f"{pick_number} ===========================")
        logging.info(f"\n\npossible_picks={possible_picks}\n")
        for i, value_ in possible_picks.items():
            logging.info(f"{i:24} {value_}")
