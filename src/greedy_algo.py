def greedy_algo() -> set[str]:
    states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

    stations: dict[str, set[str]] = {}
    stations["kone"] = set(["id", "nv", "ut"])
    stations["ktwo"] = set(["wa", "id", "mt"])
    stations["kthree"] = set(["or", "nv", "ca"])
    stations["kfour"] = set(["nv", "ut"])
    stations["kfive"] = set(["ca", "az"])

    final_stations: set[str] = set()

    while states_needed:
        best_station: str | None = None
        states_covered: set[str] = set()
        for station, states_cover_by_station in stations.items():
            covered = states_needed & states_cover_by_station
            if len(covered) > len(states_covered):
                best_station = station
                states_covered = covered
        states_needed -= states_covered

        if best_station is not None:
            final_stations.add(best_station)

    print(final_stations)
    return final_stations
