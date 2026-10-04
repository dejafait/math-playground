# Degree-nine odd-prime literal-orbit calculation

The saved [SPECIALIZE assessment](literature/2026-10-04-odd-prime-literal-orbit.md) covers exactly K = Q_3(pi), pi^9 = 3, J = log(O_K^times), I = J/6, beta = 1, scalar pi and G = Aut_(Z_3)(I). This research step tests whether hull(G(pi O_K union pi J)) is contained in hull(I), without changing the packet or reviewing more literature.

The main gap remains finite B >= A at IUT III, Corollary 3.12, step (xi-f). The local test could remove the characteristic-2 qualification from the earlier literal-input obstruction. It supplies no original initial-data realization, input-pilot identification, final-container failure or normalization bridge. L007–L008 use enlarged inputs, L009 a different favorable packet, and L010–L011 a characteristic-2 packet; none answers this exact question.

The required threshold is the sharp K-ball hull(I), not a field-dependent finite enlargement. Prove a tail ideal and reduction of every unit before using finite logarithm representatives. Then test both literal branches using exact lattice coordinates. Continue only to a whole-group containment proof or a literal input point and I-preserving automorphism outside that ball; either result ends this fixed-packet diagnostic.

## Saved reasoning before proof checks

Take H = pi^5 O_K. Its minimum valuation 5/9 is above the log/exp threshold 1/2. Reduction of the four logarithms log(1+pi^j), 1 <= j <= 4, modulo H gives the following proposed exact representatives in the coordinate basis 1,pi,...,pi^8:

```text
q1 = (7/3,1,1,7/3,2,0,1/3,0,0)
q2 = (1,0,1,1,1,0,1/3,0,0)
q3 = (1,0,0,1,0,0,0,0,0)
q4 = (0,0,0,1,1,0,0,0,0)
```

The finite sums use 1 <= k < 81. For k in [3^h,3^(h+1)), h >= 4, the integer valuation of the j-th logarithm term is at least 3^h-9h >= 45, with increasing block minima. This will place every tail in H. Removing all four unit-filtration layers, together with the residue units +/-1, will identify the full log image as sum Z_3 qj + H.

The computed log minimum is -1, making the required hull(I) equal to pi^(-18) O_K, radius 9. The input pi O_K lies in I; the log branch lies in I/3 since 18pi J lies in H. An exact primitive point is w = 3pi q1. The functionals alpha(y) = 18c0/7 and beta(y) = -3c0/49+c1/7 are integral on I and satisfy alpha(q1/6)=1, beta(q1/6)=0, alpha(w)=0, beta(w)=1. The proposed involution g(y)=y+(alpha(y)-beta(y))(w-q1/6) swaps w and q1/6, taking pi q1 to q1/18, of valuation -3 and radius 27.

The preceding reasoning was saved unfinished before the proof and certificate were completed. It supplied no challenge resolution and was not treated as a substitute for the analytic, all-unit and whole-group checks.

## Completed result and decision

[L012](../lemmas/L012-odd-prime-literal-orbit-exceeds-rounded-hull.md) proves the exact log lattice, both branch enclosures and the full orbit I/3. Its functionals are named alpha and eta, reserving beta for the conductor scalar. The explicit involution takes the literal input pi q1 to q1/18, and its error on pi log(1+pi) is in I, so both attain radius 27. This exceeds the required hull(I) radius 9 by exactly three.

The [exact certificate](../scripts/tensor-hull/degree-nine-odd-orbit-result.json), reproduced by `PYTHONDONTWRITEBYTECODE=1 python3 scripts/tensor-hull/check_degree_nine_odd_orbit.py`, checks all four finite congruences independently by rational sums, both branch bounds, functional integrality, the matrix square and sharp witness. The proof supplies the infinite tails and complete group argument. No numerical approximation or orbit sampling is used.

The fixed-packet test is complete with an informative NEGATIVE. It removes the characteristic-2 restriction from the local objection without reopening the stopped universal rounded mechanism. The result is POTENTIALLY_NEW only relative to the recorded bounded source comparison; supporting setup is imported and no certified originality is claimed. The known odd-prime bounded-discrepancy theorem remains compatible with the result. Initial data, the final container, all original images and normalized B >= A are still unresolved; STATUS remains IN_PROGRESS. The reason for moving to the final-container question is to determine whether the source's quantitative conclusion survives the failed sharp intermediate transition, rather than assume essentiality from that failure.
