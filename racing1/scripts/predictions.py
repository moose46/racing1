# from ast import Dict
from collections import defaultdict
from nascar.models import Driver

# Talladega = defaultdict(list)
# Talladega["Joey Logano"] = {
#     "points": 12000,
# }
# Talladega["Ryan Blaney"] = {
#     "points",
#     11000,
# }
# Talladega["Denny Hamlin"] = {
#     "points",
#     11000,
# }
# Talladega = {"Joey Logano": 12000, "Ryan Blaney": 11000, "Denny Hamlin": 9000}
# print(Talladega)
# print(Talladega["Joey Logano"])
# for x in Talladega:
#     # for y in x[0]:
#     print(f"{type(Talladega[x])} {x:12} - {Talladega[x]:,}")


total = []


def subset_sum(numbers, target, partial=[]):
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


def run():
    # if __name__ == "__main__":
    drivers = Driver.objects.all().order_by("salary")
    # create a set to add unique salaries, get rid of duplicate salaries
    salaries = set()
    for s in drivers:
        salaries.add(s.salary)
    for s in salaries:
        print(f"sal={s}")
    subset_sum(sorted(list(salaries), reverse=True), 50000)
    for s in total:
        print(s)
        # if len(s) == 5:
        #     print(s)
