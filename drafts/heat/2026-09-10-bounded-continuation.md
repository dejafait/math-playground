# Bounded forward continuation checkpoint — 2026-09-10

Completed as Lemma 61 in this step; this draft retains the initial reasoning.

Proposed scope: the exact family on a compact interval [a,b] and a bounded open domain D with no boundary zeros at any parameter. Assume all zeros in D at a are real. Do not assume a smooth boundary or a global zero count theorem on D.

Proof plan: at each fixed parameter isolate its finitely many zeros in the compact closure of D by discs compactly inside D. The remainder of the closure is compact and zero-free, hence stays zero-free for nearby parameters. Rouché on the finitely many discs gives local constancy of the total count. Reality is closed by persistence of any hypothetical nonreal zero in a disc disjoint from the real axis. At a real configuration the local results for multiplicities one, two, and higher give a uniform right interval of reality. A supremum of initial intervals then proves forward reality on [a,b]. A multiple zero at any parameter greater than a would force nonreal zeros just to its left, contradicting the established reality.

Check especially: emptiness of the zero set; arbitrary bounded boundary; right persistence plus closedness needs an initial-interval argument, not a claim of two-sided openness; endpoint b simplicity follows from left splitting. Downward continuation fails at collisions, even with a boundary-free bounded disc (polynomial illustration in Lemma 58).
