# GSL-TW V111: High-Performance Deterministic VRPTW Solver

[อ่านภาษาไทยคลิกที่นี่](README_TH.md)

**GSL-TW V111** is a proprietary computational engine specifically engineered for the Vehicle Routing Problem with Time Windows (VRPTW). The solver focuses on extreme computational efficiency and deterministic reliability.

Unlike standard stochastic metaheuristics, GSL-TW utilizes an advanced structural framework to pinpoint near-optimal solutions (BKS) with ultra-low latency, making it a "Production-Ready" solution for large-scale industrial logistics.

## Key Characteristics
* **Unified Scalability:** A single-script architecture solving all scales from 100 to 1,000 customer nodes.
* **Mobile-Optimized Efficiency:** Developed and verified entirely on a mobile edge environment (Pydroid 3), demonstrating superior algorithmic efficiency without relying on heavy computational hardware.
* **Deterministic Reliability:** Zero stochastic variance; every execution on the same dataset yields consistent, auditable results.
* **Real-World Speed:** 1,000-node instances solved within ~38 seconds, suitable for dynamic and real-time operational planning.

---

## 1. Benchmark Portfolio (BKS Match Rate)
The engine has been verified against the complete Solomon and Homberger benchmark spectrum (100 to 1,000 nodes). All solutions are Audit Verified (100% feasibility).

| Dataset Series | Problem Scale | BKS Match Rate | Avg. Runtime (Mobile Edge) |
| :--- | :--- | :--- | :--- |
| **Solomon-100** | Small (100 nodes) | 46.4% | ~2.78 s |
| **Solomon-200** | Mid (200 nodes) | 51.7% | ~7.57 s |
| **Homberger-400** | Large (400 nodes) | 35.0% | ~20.0 s |
| **Homberger-600** | Large (600 nodes) | 30.0% | ~29.20 s |
| **Homberger-800** | Massive (800 nodes) | 35.0% | ~31.15 s |
| **Homberger-1000** | Massive (1,000 nodes) | 21.6% | ~38.22 s |

---

## 2. Algorithm Baseline Comparison
To demonstrate real-time efficiency, GSL-TW V111 was benchmarked against widely recognized algorithms under **equal computational time budgets** on the same mobile environment. 

* **GSL vs. Solomon I1 (Insertion Heuristic):**
  * **100 Nodes:** GSL Wins 45/56. (Avg Time: GSL 2.77s vs I1 1.49s)
  * **200 Nodes:** GSL Wins 53/60. (Avg Time: GSL 7.43s vs I1 9.83s)
  * **800 Nodes:** GSL Wins 57/60. (Avg Time: GSL 30.57s vs I1 181.06s)
  * *Result:* GSL perfectly scales linearly, completely outperforming standard heuristics in large datasets.

* **GSL vs. ALNS (Adaptive Large Neighborhood Search):**
  * **100 Nodes:** GSL Wins 53/56.
  * **800 Nodes:** GSL Wins 60/60. (Avg Time: GSL 30.57s vs ALNS 380.43s)
  * *Result:* Under real-time operational constraints, GSL processes data over 12x faster while delivering vastly superior routing efficiency compared to stochastic metaheuristics.

* **GSL vs. Tabu Search (TS):**
  * **100 Nodes:** GSL Wins 54/56. (Avg Time: GSL 2.77s vs TS 139.90s)
  * *Result:* Trajectory-based methods like TS are proven to be too computationally heavy ($O(N^3)$) for edge deployment, operating 50x slower than GSL.

📂 **[Click here to view detailed CSV reports for all comparative benchmarks](./Comparative_Benchmarks)**

---

## Technical Strategy & Architecture
The GSL engine replaces exhaustive brute-force search with:
1. **Geometric Sensing:** Pinpointing high-quality initial clusters based on spatial rules.
2. **Deterministic Vehicle Minimization:** Prioritizing fleet reduction before distance refinement.
3. **Temporal Constraint Synchronization:** Precision handling of tight time windows without exponential complexity growth.

## GSL-Solver Platform

**The Enterprise Route Optimization Portal**
Access the production-ready deterministic engine here:  
[**https://gsl-solver.com**](https://gsl-solver.com)

---

## Professional Contact

**Independent Researcher:** Chonmapoohm Thamsuwan (CTSuwan)  
**Email:** [ctsuwan@proton.me](mailto:ctsuwan@proton.me)  

---

## Services & Collaboration

Open to professional engagement in the following areas:

- **Logistics-as-a-Service (LaaS):** Real-time route optimization for enterprise fleets.
- **High-Precision Modeling:** Custom algorithmic solutions for complex supply chain constraints.
- **Technical Consultancy:** Large-scale network stress-testing and optimization audits.

