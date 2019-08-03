def Schedule(team, slots):
    if slots == []:
        return {}
    for worker in team:
        if worker.shifts > 0:
            for slot in worker.slots:
                if slot in slots:
                    wcp = worker.copy()
                    new_team = [w if w != worker else wcp for w in team]
                    wcp.assign(slot)
                    assignments = Schedule(new_team, [s for s in slots if s != slot])
                    if assignments is not None:
                        assignments[slot] = worker.name
                        return assignments
    return None

