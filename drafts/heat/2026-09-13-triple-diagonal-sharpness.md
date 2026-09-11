# Triple diagonal sharpness checkpoint — 2026-09-13

Existing L163 is complete. Candidate lower bound: choose four integer
logarithmic displacements in [-h,h], h=floor(log2(N)/100), complete a
3-by-3 displacement matrix with all row/column sums zero, and place
entry ij in [N^(1/3)2^dij, (1+eta)N^(1/3)2^dij]. All six margins then
lie in [N,(1+eta)^3 N], and each box has volume comparable to N^3.
There are order (log N)^4 disjoint boxes.

Unproved checkpoint: establish a uniform positive fraction of pairwise
coprime entries in every box. First restrict all entries to 1 modulo
the product of primes up to a fixed P. Conditional union bounds for
larger shared primes should cost O(1/P)+o(1), because all side scales
are between N^(1/3-0.04) and N^(1/3+0.04), so maximum scale divided
by minimum scale squared tends to zero. Pairwise coprimality gives
xij=gcd(row_i,column_j), hence injectivity. Resume by making this sieve
bound explicit before promoting any sharpness statement.

Completed as L164. The uniform residue-class union bound and gcd recovery
prove the matching fourth-power lower bound for every sufficiently large
real N. No cutoff-weighted conclusion is asserted.
