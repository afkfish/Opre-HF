def find_victim(frozen, second, fifo, frames, itera):
    if itera >= 6:
        return None
    ite = itera % 3
    if (frame := len(fifo)) < 3:
        fifo.append(frame)
        return frame - 1
    frame = fifo.pop(ite)
    if frozen[frame] <= 0:  # if not frozen
        fifo.append(frame)  # put it back
        if not second[frame]:  # if it does not have second chance
            return frame
        second[frame] = False  # remove second chance
    else:  # if frozen
        fifo.insert(ite, frame)  # put it back where it was
        itera += 1  # increase iteration index
    return find_victim(frozen, second, fifo, frames, itera)


def simulate(inp):
    frames: [int] = [None, None, None]
    fifo = []
    second_chance = {
        0: False,
        1: False,
        2: False
    }
    frozen_frames = {
        0: 0,
        1: 0,
        2: 0
    }
    faults = 0
    output = ""

    for reference in inp:
        if abs(reference) in frames:
            output += "-"
            second_chance[frames.index(abs(reference))] = reference > 0

            for item in frozen_frames:
                frozen_frames[item] -= 1

        else:
            victim_index = find_victim(frozen_frames, second_chance, fifo, frames, 0)
            for item in frozen_frames:
                frozen_frames[item] -= 1

            if victim_index is None:
                output += "*"
                faults += 1
                continue

            output += chr(ord("A") + victim_index)
            frames[victim_index] = abs(reference)
            frozen_frames[victim_index] = 3
            faults += 1

    print(output)
    print(faults)


references = input().strip().split(",")
references = [int(reference) for reference in references]
simulate(references)
