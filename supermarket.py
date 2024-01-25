import random

def main():
    num_cashiers = 5
    processing_time = 150
    num_simulations = 1000
    current_time = 0
    total_work_time = 24*60*60

    total_customers_served = [0] * num_cashiers
    total_customers_lost = 0
    status_customers = [False] * num_cashiers
    service_time_customers = [0] * num_cashiers

    for _ in range(num_simulations):
        current_time = 0
        while current_time < total_work_time:
            arrival_rate = random.randint(1, 50)

            if arrival_rate > total_work_time - current_time:
                break

            current_time += arrival_rate

            for i in range(num_cashiers):
                if service_time_customers[i] != 0:
                    if service_time_customers[i] <= arrival_rate:
                        service_time_customers[i] = 0
                        status_customers[i] = False
                        total_customers_served[i] += 1
                    else:
                        service_time_customers[i] -= arrival_rate

            if False not in status_customers:
                total_customers_lost += 1
            else:
                for i in range(num_cashiers):
                    if status_customers[i] == False:
                        status_customers[i] = True
                        service_time_customers[i] = processing_time
                        break

    average_customers_served = [int(s / num_simulations) for s in total_customers_served]
    print(f'Количество обслуженных клиентов каждой кассой: {average_customers_served}')
    print(f'Количество необслуженных клиентов: {int(total_customers_lost / num_simulations)}')

if __name__ == "__main__":
    main()
