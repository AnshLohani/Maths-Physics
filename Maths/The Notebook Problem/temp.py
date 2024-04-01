import time
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from itertools import cycle, product
from queue import Queue
from typing import Union

NUMBER_OF_NOTEBOOKS = 20
NUMBER_OF_QUEUES = 4
NUMBER_OF_THREADS = NUMBER_OF_QUEUES


@dataclass
class Notebook:
    id: int
    name: str
    processed: bool = False


def make_distribution(ids_to_distribute, group: list, parsed: bool = False) -> list:
    if not group:
        group = [[] for _ in range(NUMBER_OF_QUEUES)]
    if parsed:
        for i in cycle(group):
            if not ids_to_distribute:
                return group
            num = ids_to_distribute.pop(0)
            i.append(num)

    for g in cycle(group):
        while len(g) < NUMBER_OF_NOTEBOOKS:
            if not ids_to_distribute:
                break
            num = ids_to_distribute.pop(0)
            g.append(num)
        if ids_to_distribute and sum([len(i) for i in group]) == len(group) * NUMBER_OF_NOTEBOOKS or not ids_to_distribute:
            return make_distribution(ids_to_distribute, group, True)
    else:
        return group


def iter_distribution(values_to_distribute, group, parsed=False):
    for i in make_distribution(values_to_distribute, group, parsed):
        yield i


def populate_notebooks(_queue: Union[Queue, list]):
    """
    Populates the queues with given number of notebooks
    :param _queue:
    :return:
    """

    if isinstance(_queue, list):
        for i in range(_queue):
            n = Notebook(id=i+1, name=f"Notebook {i}")
            _queue[i].put(n)
        return
    for i in range(NUMBER_OF_NOTEBOOKS):
        n = Notebook(id=i+1, name=f"Notebook {i}")
        _queue.put(n)


def process_notebook(n: Notebook) -> Notebook:
    time.sleep(1)
    n.processed = True
    print(f"Notebook {n.id} processed")
    return n


def main():
    # test for 1 queue, 2 queues, and NUMBER_OF_NOTEBOOKS queues
    # for i in range(NUMBER_OF_NOTEBOOKS):
    #     q1.put(i)
    #
    # while not q1.empty():
    #     notebook = q1.get()
    #     process_notebook(notebook)

    # test 2: with 2 queues and 2 workers
    # with ThreadPoolExecutor(max_workers=2) as executor:
    #     while not q1.empty():
    #         notebook = q1.get()
    #         executor.submit(process_notebook, notebook)

    # test 3: Using a dynamic number of NUMBER_OF_NOTEBOOKS and NUMBER_OF_QUEUES
    comb = product(range(1, NUMBER_OF_NOTEBOOKS+1), range(1, NUMBER_OF_QUEUES+1), range(1, NUMBER_OF_THREADS+1))
    for ix, c in enumerate(comb):
        notebook_no, queue_no, executors_no = c
        notebooks = [Notebook(id=i, name=f"Notebook {i}") for i in range(notebook_no)]
        groups = make_distribution([i for i in range(notebook_no)], [], True)

        with ThreadPoolExecutor(max_workers=executors_no) as executor:
            for i in groups:
                executor.submit(process_notebook, notebooks[i])
                ...
    # TODO:
    # 1: Get every element from c variable and:
    # 2: Create notebooks_no, queues_no based on the variables
    # 3: pass as an argument this variables to ThreadPoolExecutor using max_workers=executors_no
    # 4: Save the result time for each combination on a dict {(x, y, z): time}
    # 5: tabulate the dict and print the best 10 results


if __name__ == "__main__":
    # queues_list = [Queue() for _ in range(NUMBER_OF_QUEUES)]
    # distribution_groups = make_distribution([i for i in range(NUMBER_OF_NOTEBOOKS)], [], True)
    # # [[0, 4, 8, 12, 16], [1, 5, 9, 13, 17], [2, 6, 10, 14, 18], [3, 7, 11, 15, 19]]
    # print(distribution_groups)
    # populate_notebooks()
    # main()

    # comb = product(range(1, NUMBER_OF_NOTEBOOKS+1), range(1, NUMBER_OF_QUEUES+1), range(1, NUMBER_OF_THREADS+1))
    # for ix, c in enumerate(comb):
    #     print(f'Combination: {c}')
    #     if ix == 100:
    #         break

    main()
