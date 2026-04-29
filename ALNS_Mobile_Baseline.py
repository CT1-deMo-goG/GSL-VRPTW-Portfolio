"""
ALNS Mobile-Edge Baseline for VRPTW
Designed for lightweight execution on Pydroid 3 environment.
Used as a stochastic baseline to benchmark against the deterministic GSL Engine.
"""

import math
import time
import random

# Lightweight Mobile Constraints
MAX_ITER = 150        
DESTRUCTION_RATE = 0.15 

def get_dist(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def is_feasible(route, nodes, capacity):
    load, t = 0, 0
    for i in range(1, len(route)):
        prev, curr = nodes[route[i-1]], nodes[route[i]]
        d = get_dist((prev[1], prev[2]), (curr[1], curr[2]))
        t = max(t + d, curr[4])
        if t > curr[5]: return False
        t += curr[6]
        load += curr[3]
        if load > capacity: return False
    return True

def initial_solution_i1(nodes, capacity):
    depot = nodes[0]
    unvisited = list(range(1, len(nodes)))
    routes = []
    while unvisited:
        route = [0]
        curr_load, curr_time, prev_node = 0, 0, depot
        while unvisited:
            best_idx = None
            for idx in unvisited:
                c = nodes[idx]
                d = get_dist((prev_node[1], prev_node[2]), (c[1], c[2]))
                arrival = max(curr_time + d, c[4])
                if curr_load + c[3] <= capacity and arrival <= c[5]:
                    best_idx = idx
                    break
            if best_idx is not None:
                c = nodes[best_idx]
                d = get_dist((prev_node[1], prev_node[2]), (c[1], c[2]))
                curr_time = max(curr_time + d, c[4]) + c[6]
                curr_load += c[3]
                route.append(best_idx)
                unvisited.remove(best_idx)
                prev_node = c
            else: break
        route.append(0)
        routes.append(route)
    return routes

def calc_cost(routes, nodes):
    td = 0.0
    for r in routes:
        for i in range(len(r)-1):
            td += get_dist((nodes[r[i]][1], nodes[r[i]][2]), (nodes[r[i+1]][1], nodes[r[i+1]][2]))
    # Cost Priority: Fleet Size (K) minimization dominates TD
    return len(routes) * 10000 + td, len(routes), td

def calculate_alns(nodes, capacity):
    start_t = time.time()
    
    current_routes = initial_solution_i1(nodes, capacity)
    best_cost, best_k, best_td = calc_cost(current_routes, nodes)
    
    num_customers = len(nodes) - 1
    num_to_remove = max(1, int(num_customers * DESTRUCTION_RATE))
    
    for iteration in range(MAX_ITER):
        # DESTROY (Random Removal for high speed)
        temp_routes = [r[:] for r in current_routes]
        removed_customers = set()
        while len(removed_customers) < num_to_remove:
            removed_customers.add(random.randint(1, num_customers))
            
        for r in temp_routes:
            r[:] = [n for n in r if n not in removed_customers]
        temp_routes = [r for r in temp_routes if len(r) > 2]
        
        # REPAIR (Greedy Insertion)
        unplanned = list(removed_customers)
        random.shuffle(unplanned) 
        
        for u in unplanned:
            best_r_idx, best_pos, min_inc = -1, -1, float('inf')
            for r_idx, r in enumerate(temp_routes):
                for i in range(1, len(r)):
                    test_r = r[:i] + [u] + r[i:]
                    if is_feasible(test_r, nodes, capacity):
                        prev_n, u_n, next_n = nodes[r[i-1]], nodes[u], nodes[r[i]]
                        inc = get_dist((prev_n[1], prev_n[2]), (u_n[1], u_n[2])) + \
                              get_dist((u_n[1], u_n[2]), (next_n[1], next_n[2])) - \
                              get_dist((prev_n[1], prev_n[2]), (next_n[1], next_n[2]))
                        if inc < min_inc:
                            min_inc, best_r_idx, best_pos = inc, r_idx, i
            
            if best_r_idx != -1:
                temp_routes[best_r_idx].insert(best_pos, u)
            else:
                temp_routes.append([0, u, 0])
                
        # ACCEPTANCE (Strict Hill Climbing)
        new_cost, new_k, new_td = calc_cost(temp_routes, nodes)
        if new_cost < best_cost:
            current_routes = [r[:] for r in temp_routes]
            best_cost, best_k, best_td = new_cost, new_k, new_td
        elif new_cost < calc_cost(current_routes, nodes)[0]:
            current_routes = [r[:] for r in temp_routes]

    return best_k, best_td, time.time() - start_t
              
