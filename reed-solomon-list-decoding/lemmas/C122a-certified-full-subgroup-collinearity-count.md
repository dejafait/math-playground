# C122a — Certified full-subgroup ordered collinearity count

## Hypotheses

Use exactly L122's setting: E=F_65537, H the subgroup of E* of order
1024, and P the set of unordered two-element subsets of H. For A={a,b}
put s(A)=a+b and t(A)=ab in E. Let T count ordered triples (A,B,C)
of pairwise disjoint elements of P whose three (s,t) points are collinear.
In particular all six endpoints are distinct. No core, selected support
family, received center or interleaving width is fixed.

## Conclusion

The exact finite count, obtained by the reproducible integer computation
specified below, is

\[
T=2\,298\,250\,371\,072.
\]

The vertical, horizontal and weighted nonzero-slope contributions are,
respectively,

\[
163\,243\,008,\qquad
136\,234\,398\,720,\qquad
2\,161\,852\,729\,344.
\]

This is a computational corollary of L122, classified REPRODUCTION under
the prior SPECIALIZE assessment, not a new incidence theorem. It supplies
a whole-domain diagnostic for L020. It supplies no uniform core/link bound,
supersaturation, threshold saving, RS list realization, 67/68 safety or
improvement to the 955–957 bracket. The separate 2026-10-25 critical audit
accepted this fixed-field corollary after reviewing the reduction, both
programs and all saved data. This is not a candidate complete resolution
of the grand challenge.

## Proof

**Established formula and applicability.** L122 proves the exact formula
including every vertical and antipodal case, removes precisely the shared-
endpoint star lines, and proves the weight 1024 for each of 64 nonzero-
slope representatives. Apply that formula on its unchanged field and
subgroup; no generic-domain or nonzero-sum assumption is added. No theorem
about typical cores or selected families is invoked. The computational
work evaluates that established formula; it does not reprove the reduction.
The prior assessment is
`drafts/literature/2026-10-25-l122-full-count-implementation.md`.

**Exact arithmetic and complete certificate.** Run, from the notebook,

```text
python3 scripts/finite-support/l122_full_count.py
python3 scripts/finite-support/l122_full_count_replay.py
```

The production script uses Python arbitrary-precision integer intermediates
and sums, with uint32 arrays for the two pair coordinates and occupancies.
Thus neither u*s=2^32 nor any negative modular representative is evaluated
in a narrow unsigned type. It constructs h=3^64 mod 65537=19139, verifies
h^1024=1 and h^512=-1, and lists its 1024 distinct powers. These order tests
and the root bound identify H as in L122. It scans unmarked nonzero residues
in increasing order and saves each complete coset uH, checking size 1024,
disjointness, full coverage and exactly 64 representatives, starting with 1.

For each pair of distinct power indices i<j it stores the reduced sum and
product. There are N=523776 pairs. It then computes the entire vertical
histogram, horizontal histogram, and 64 representative histograms of
t-u*s mod 65537. Every row contains all 65537 bins, including zero bins and
the star bin. Every row has mass N. Except at v=-u^2 its occupancy is checked
to be at most 512. The star occupancy is 1023 for u=1, and zero for the
other representatives and u=0, exactly as L122 prescribes. Its contribution
to T is omitted but retained in the unexcluded moments. Falling factorials
are evaluated as zero for occupancies below three.

`scripts/finite-support/l122-full-count.json` retains the complete H and
coset partition, each row's occupancy distribution, offset, digest,
unexcluded first/second/third moments and eligible third subtotal. The
complete bin arrays, in the order vertical, horizontal, increasing nonzero
representatives, are stored in
`scripts/finite-support/l122-full-count-histograms.u32`.
Each bin is a four-byte little-endian unsigned integer, each row occupies
262148 bytes, and the full file has 17301768 bytes. Its SHA-256 is

```text
4f8161677371fe052b12ead70436b92c0ceb508883a5bd658a593086043aa681
```

The exact sum of the eligible third subtotals for the 64 representative
rows is 2111184306. Consequently L122's formula evaluates to

\[
163243008+136234398720+1024(2111184306)
=2298250371072.
\]

The vertical zero-sum occupancy is 512, giving its required contribution
133432320. The horizontal rows have occupancy 511 on the 512 square elements
of H and 512 on its other 512 elements, and zero elsewhere. Both explicit
L122 contributions are checked exactly, without omitting antipodal pairs.

**Independent numerical replay.** The replay script imports no production
code, pair arrays or chosen generator. It checks primality of 65537 by all
trial divisors 2 through 256, independently lists H as all nonzero roots of
X^1024=1, and independently groups nonzero residues by x^1024. It checks the
entire resulting subgroup and ordered partition against the saved data.

For the vertical row it counts all ordered endpoints (a,b) in H^2 by a+b,
then removes the 1024 diagonal terms 2a. For each nonvertical slope u it
counts all ordered shifted products (a-u)(b-u), then removes the diagonal
(a-u)^2. Every remaining bin is checked even, divided by two, and placed
at v=(a-u)(b-u)-u^2. The equality
(a-u)(b-u)-u^2=ab-u(a+b) is precisely L122's equation (3). Distinct endpoints
occur in the two orders (a,b) and (b,a), so halving recovers the unordered
pairs counted in the production histogram; diagonals were removed first.
This replay therefore uses a different pair-generation and diagonal path.

The replay compares all 4325442 bins, checks every saved row digest, offsets
and final file length, repeats mass, star, matching-bound and moment checks,
and recomputes every eligible third subtotal. There are zero mismatches
and no reported failures in either computation. It writes the independent
complete arrays to
`scripts/finite-support/l122-full-count-replay-histograms.u32`, whose bytes
and digest equal the production artifact, and saves its exact comparisons
in `scripts/finite-support/l122-full-count-replay.json`. Both manifests also
record script hashes; the replay records the source manifest hash.

**Unexcluded moments and limits of verification.** Before removing stars,
the weighted moments, including vertical lines, are

\[
\sum r=(65537+1)523776=34327231488,
\qquad
\sum r^2=523776^2+65537(523776)=308668005888.
\]

Both actual totals equal these required values. For the second diagnostic
import Murphy and Petridis, *A Point-Line Incidence Identity in Finite Fields,
and Applications*, [arXiv:1601.03981v3](https://arxiv.org/pdf/1601.03981v3),
20 February 2016, Lemma 1, printed p.2, full Section 2 proof p.5. As already
justified in L122, the injective pair image is a subset of F_65537^2, and
that identity sums over all affine lines, including vertical lines. Its
application is only a consistency check; it does not determine the third
count or substitute for L122's endpoint and multiplicity proof.

The production pass uses 34569216 pair-bin updates and scans 4325442 bins.
Its specified main packed-array payloads total 4522245 bytes. Coset lists,
certificate objects, serialization buffers, replay arrays and interpreter
overhead are additional; no process-memory measurement or runtime bound
is claimed. The final count and all partial sums are below
N(N-1)(N-2)<2^57 as required by L122. No floating-point arithmetic or
small-field preview is used for the actual-field answer. This is an
executable finite-arithmetic certificate, not a formal proof-assistant
verification.

**Separate critical audit, 2026-10-25.** The prior SPECIALIZE assessment
`drafts/literature/2026-10-25-c122a-critical-audit-coverage.md` authorized
this review under unchanged hypotheses. Review of the complete L122 proof
checked that injectivity recovers unordered endpoints, f(r) orders only the
three distinct pairs, and unique-line counting causes no triple duplication.
On a vertical line each endpoint has one partner. On a nonvertical line
equation (3) gives one partner unless its constant is zero, when every
actual pair contains the slope endpoint. Thus removing precisely the star
lines implements six-endpoint disjointness. Multiplication by H is free
on nonzero slopes; its intercept transport is a bijection and carries the
excluded value with it. Neither a free action at slope zero nor a nonzero
sum is assumed. These checks validate the formula independently of numerical
agreement, with zero bins, antipodal pairs and horizontal lines retained.

Both complete programs were reviewed against that formula. The production
loop uses each index pair i<j once; the replay uses each ordered endpoint
pair, subtracts exactly the diagonals, tests evenness, and divides by two
before the bijective intercept translation. The subgroup reconstructed as
all roots of X^1024-1 equals the 1024 distinct powers of h. Primality is
checked through floor(sqrt(65537))=256; the order tests identify H exactly.
For nonzero x,y, x^1024=y^1024 exactly when x/y is a root, justifying the
replay's power-signature cosets. All 64 complete cosets are also checked
directly as representative times H. Python integer multiplication precedes
modular reduction and uint32 storage. Even the unreduced ordered-pair
histogram has at most 1024^2 entries in a bin, below 2^32; diagonals are
present before subtraction. The replay's current platform has four-byte
array items, as also enforced by its complete comparison with the explicit
four-byte layout. None of these checks asserts portability to a platform
whose native unsigned-int arrays have a different item size.

Run `python3 scripts/finite-support/critical_audit_c122a.py`. Its full
certificate `scripts/finite-support/c122a-critical-audit.json` stores
expected complete manifests, original hashes, 420 checks and all failures.
Every production and replay manifest field is compared with reconstructed
values, including the full subgroup/cosets, all 66 row distributions,
offsets, excluded bins, maxima, moments, weights, subtotals, schema keys,
completion flags and current program hashes. All binary bins are read as
explicit little-endian uint32; lengths and whole/row digests are checked.
The complete expected manifests are saved, not merely their previews.

The audit reruns the unchanged reviewed replay with new output destinations,
saving `scripts/finite-support/c122a-critical-audit-replay.json` and
`scripts/finite-support/c122a-critical-audit-replay-histograms.u32`.
All 4325442 bins match again and the fresh binary has the SHA-256 displayed
above. The original two programs, manifests and binary files retain their
pre-audit hashes. All 420 checks pass with no failures; the exact moments
and contributions above are recovered, and
T <= N(N-1)(N-2)=143692564770585600 < 2^57=144115188075855872.
The 4522245-byte bound remains a main-array payload bound only.

The fresh run is a rerun of the endpoint replay, not a third independent
algorithm. Production and replay independently generate pair occupancies
but share L122's line formula; the preceding mathematical review supplies
the separate endpoint/orbit check. First and second moments remain only
diagnostics. Acceptance is restricted to this exact finite count, with
no core-uniform, selected-family or list-safety inference.

## Mathlib

Full matching numerical count and certified implementation: **not checked**
in Mathlib. Supporting subgroup/coset, finite-field and finite-counting
coverage: **not checked**. The precisely cited Murphy–Petridis input is an
unexcluded moment diagnostic, not a matching theorem for this count.
