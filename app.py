import time
import random


def greedy_algorithm(jobs):
    sorted_jobs = sorted(jobs, key=lambda x: x[0])
    schedule = []
    total_penalty = 0

    for job in sorted_jobs:
        deadline, penalty, duration = job
        if deadline >= len(schedule) + 1:
            schedule.append(job)
            total_penalty += penalty

    return schedule, total_penalty


def branch_and_bound_algorithm(jobs):
    def branch_and_bound_recursive(current_schedule, remaining_jobs, current_penalty):
        nonlocal best_schedule, best_penalty

        # Verifica se a solução atual é viável
        if current_penalty < best_penalty:
            best_schedule = current_schedule.copy()
            best_penalty = current_penalty

        # Verifica se é possível adicionar mais trabalhos
        if remaining_jobs:
            for i, job in enumerate(remaining_jobs):
                deadline, penalty, duration = job
                new_schedule = current_schedule + [job]
                new_penalty = current_penalty + penalty

                # Verifica se a solução parcial é viável
                if deadline >= len(new_schedule):
                    branch_and_bound_recursive(new_schedule, remaining_jobs[i + 1:], new_penalty)

    best_schedule = []
    best_penalty = float('inf')

     # Inicia a busca recursiva com uma solução vazia
    branch_and_bound_recursive([], jobs, 0)
    
    # Retorna a melhor solução encontrada e sua penalidade
    return best_schedule, best_penalty


def generate_data(size, global_deadline):
    jobs = []
    for _ in range(size):
        penalty = random.randint(1, 10)
        duration = random.randint(1, 15)
        jobs.append((global_deadline, penalty, duration))
    return jobs




def run_algorithm_and_measure_time(algorithm, jobs):
    start_time = time.time()
    result = algorithm(jobs)
    execution_time = time.time() - start_time
    return result, execution_time


def main():
    dataset_sizes = [15, 20, 30]
    global_deadline = 10

    for size in dataset_sizes:
        jobs = generate_data(size, global_deadline)

        greedy_solution, greedy_time = run_algorithm_and_measure_time(greedy_algorithm, jobs)
        bb_solution, bb_time = run_algorithm_and_measure_time(branch_and_bound_algorithm, jobs)

        print(f"Dataset Size: {size}")
        print(f"Greedy Solution: {greedy_solution[0]}, Greedy Penalty: {greedy_solution[1]}")
        print(f"Greedy Execution Time: {greedy_time} seconds")

        print(f"Branch and Bound Solution: {bb_solution[0]}, Branch and Bound Penalty: {bb_solution[1]}")
        print(f"Branch and Bound Execution Time: {bb_time} seconds")

        print("\n")

if __name__ == "__main__":
    main()
