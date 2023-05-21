import heapq


class Process:
    def __init__(self, pid, priority, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.remaining_time = burst_time
        self.waiting_time = 0

    def __lt__(self, other):
        if self.arrival_time == other.arrival_time:
            return self.pid < other.pid
        return self.arrival_time < other.arrival_time


class Scheduler:
    def __init__(self):
        self.current_time = 0
        self.quantum = 2
        self.highest_priority_queue = []
        self.lowest_priority_queue = []
        self.processes = []

    def add_process(self, process):
        heapq.heappush(self.processes, (process.arrival_time, process))

    def process_arrived(self):
        while self.processes and self.processes[0][0] <= self.current_time:
            _, process = heapq.heappop(self.processes)
            if process.priority == 1:
                heapq.heappush(self.highest_priority_queue, process)
            else:
                heapq.heappush(self.lowest_priority_queue, (process.remaining_time, process.pid, process))

    def notify_waiting(self, process, waiting_time):
        for process_ in self.highest_priority_queue:
            if process != process_:
                process_.waiting_time += waiting_time
                if process_.arrival_time == self.current_time-1:
                    process_.waiting_time = 1
                elif process_.arrival_time == self.current_time:
                    process_.waiting_time = 0
        for _, _, process_ in self.lowest_priority_queue:
            if process != process_:
                process_.waiting_time += waiting_time
                if process_.arrival_time == self.current_time-1:
                    process_.waiting_time = 1
                elif process_.arrival_time == self.current_time:
                    process_.waiting_time = 0

    def run(self):
        finished_processes = []
        seq = []
        while self.processes or self.highest_priority_queue or self.lowest_priority_queue:
            self.process_arrived()

            if self.highest_priority_queue:
                process = self.highest_priority_queue[0]
                if len(seq) == 0 or seq[-1] != process.pid:
                    seq.append(process.pid)
                if process.remaining_time <= self.quantum:
                    self.current_time += process.remaining_time
                    self.highest_priority_queue.pop(0)
                    heapq.heappush(finished_processes, process)
                    self.process_arrived()
                    self.notify_waiting(process, process.remaining_time)
                    process.remaining_time = 0

                else:
                    self.current_time += self.quantum
                    process.remaining_time -= self.quantum
                    self.process_arrived()
                    self.highest_priority_queue.pop(0)
                    self.highest_priority_queue.append(process)
                    self.notify_waiting(process, self.quantum)

            elif self.lowest_priority_queue:
                _, _, process = self.lowest_priority_queue[0]
                if len(seq) == 0 or seq[-1] != process.pid:
                    seq.append(process.pid)
                self.current_time += 1
                process.remaining_time -= 1
                self.lowest_priority_queue[0] = (process.remaining_time, process.pid, process)

                if process.remaining_time <= 0:
                    process.remaining_time = 0
                    self.lowest_priority_queue.pop(0)
                    heapq.heappush(finished_processes,  process)
                    self.lowest_priority_queue.sort(key=lambda x: x[0])

                self.notify_waiting(process, 1)

            else:
                self.current_time += 1
                for process in self.highest_priority_queue:
                    process.waiting_time += 1
                for _, _, process in self.lowest_priority_queue:
                    process.waiting_time += 1

        print("".join(seq))
        finished_processes.sort()
        print(",".join([f"{process.pid}:{process.waiting_time}" for process in finished_processes]))


if __name__ == "__main__":
    # read the console continiously input while not eof and skip \n
    scheduler = Scheduler()
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line == "":
            continue
        newProcess = line.split(",")
        scheduler.add_process(Process(newProcess[0], int(newProcess[1]), int(newProcess[2]), int(newProcess[3])))
    scheduler.run()
