# L124 — Cyclic spectral core-deletion bound

## Hypotheses

Use exactly L123's finite configuration space: E=F_65537, H the
order-1024 multiplicative subgroup, and Omega the ordered triples of
pairwise disjoint unordered endpoint pairs whose sum/product images
are collinear. Put n=1024 and T=|Omega|=2298250371072. For distinct
a,b in H, d(a,b) counts configurations containing both endpoints,
including both same-pair and different-pair placements. Use L123's
complete audited ratio table, its scaling and inverse symmetries, and
singleton count s=13466310768. Let K be any 61-element subset of H and
U(K) the number of configurations avoiding K. No selected support family,
received center, or equivalence of different cores is assumed.

## Conclusion

The finite spectral certificate and exact arithmetic below give uniformly

\[
\sum_{\{a,b\}\subset K}d(a,b)\le120815550367,
\qquad U(K)\le1597620964591.
\]

The survivor upper bound improves L123's 1600876449624 by 3255485033.
It is a diagnostic for the full configuration space, not an exact core
optimum, selected-family transfer, RS realization or safety theorem.
The 955–957 bracket is unchanged. This is REPRODUCTION of a known
finite spectral method under the prior SPECIALIZE assessment
`drafts/literature/2026-10-25-ratio-weighted-core-energy-calculation.md`.
No new general spectral theorem or mathematical originality is claimed.
The separate 2026-10-25 critical audit below accepts this specialization
and complete finite certificate. It is not a complete challenge candidate.

## Proof

**Imported inputs and specialization.** Use Robert M. Gray, *Toeplitz and
Circulant Matrices: A Review*, 2005–2006 author revision, §3.1,
(3.5)–(3.13), printed pp.32–34, and Theorem 3.1, pp.34–35
([author PDF](https://ee.stanford.edu/~gray/toeplitz.pdf)), for complete
finite Fourier diagonalization. Use A. E. Brouwer and W. H. Haemers,
*Spectra of Graphs*, §2.4, printed p.33's orthonormal-eigenvector
expansion and subspace Rayleigh bounds
([author preprint](https://homepages.cwi.nl/~aeb/math/ipm/ipm.pdf)).
Both were inspected in the reused source assessment. These apply to
finite real symmetric matrices, allowing repeated and negative
eigenvalues. No asymptotic or unweighted-graph restriction is imported.
The generic theorems are cited, not reproved. What follows checks the
particular cyclic indexing, indicator, and normalization.

Let h=3^64 mod 65537=19139, H={h^i:0<=i<n}, and
w_0=0, w_j=d(1,h^j) for 1<=j<n. L123 gives
d(h^i,h^j)=w_(j-i mod n) for i!=j, and w_j=w_(-j mod n).
Thus A_ij=w_(j-i mod n) is a real symmetric circulant, with zero
diagonal and constant row sum R=sum_j w_j=67331553840=5s.
This is Gray's first-row convention: advancing the row rotates the
first row one position to the right. With Fourier vectors having
i-th entry n^(-1/2) exp(-2 pi i m i/n), its eigenvalues are

\[
\lambda_m=\sum_{j=0}^{n-1}w_j\exp(-2\pi\mathrm{i}mj/n)
          =\sum_{j=0}^{n-1}w_j\cos(2\pi mj/n),\quad0\le m<n.
\]

Inverse symmetry cancels the imaginary terms, including the
self-inverse j=512 term (whose sine is zero). The constant mode is
lambda_0=R. The other n-1 Fourier vectors span the orthogonal complement
of the constants; every such mode is retained, including m=512 and
repeated eigenvalues. Put lambda_* = max_(1<=m<n) lambda_m, using the
largest algebraic value rather than its absolute value.

For z=1_K, k=61, and x=z-(k/n)1, we have 1^T x=0,
||x||^2=k-k^2/n=58743/1024. Since A1=R1, both cross terms vanish and
the cited symmetric Rayleigh bound gives

\[
z^TAz=Rk^2/n+x^TAx
 \le Rk^2/n+\lambda_* k(1-k/n).
\]

The zero diagonal and symmetry imply
z^TAz=2 sum_{{a,b} subset K}d(a,b). The factor two counts endpoint
orders; it does not change the already ordered configuration triples.
No assumption that a maximizing real eigenvector is a core is needed.
This centered-indicator application is also consistent with Jakob
Hansen, *Expansion in Matrix-Weighted Graphs*, 2020-10-14 preprint,
Lemma 3.1, (5), pp.12–13
([author PDF](https://www.jakobhansen.org/publications/mwgraphs.pdf)).
Its problematic display (4) and subsequent one-sided operator-norm
wording are not used.

**Exact trigonometric enclosure.** Import the addition, product and
half-angle identities in NIST DLMF §4.21, (4.21.2)–(4.21.3),
(4.21.16), (4.21.21)–(4.21.22)
([primary formulas](https://dlmf.nist.gov/4.21)), inspected in the
prior assessment. Enclosing expression evaluation is the standard
method described by S. M. Rump, *Verification methods: Rigorous results
using floating-point arithmetic*, Acta Numerica 19 (2010), 287–449,
§5.3–5.5, (5.14)–(5.17), author pp.27–28
([corrected author PDF](https://www.tuhh.de/ti3/rump/intlab/ActaNumerica2010.pdf)).
Here all endpoints and checks use arbitrary-precision integers;
no floating-point assumption or root-box theorem is used.

Set B=2^128, theta=2 pi/1024=pi/512. Intervals below store integer
endpoints [l,u] meaning [l/B,u/B]. Starting from cos(pi/2)=0, perform
eight positive half-angle steps. If the input endpoints are l,u,
the new endpoints L,U are certified by the exact inequalities

\[
2L^2\le(B+l)B<2(L+1)^2,\qquad
2(U-1)^2<(B+u)B\le2U^2.
\]

These enclose sqrt((1+cos(t))/2). At every step 0<t/2<pi/2,
so the positive root is the correct cosine branch. All eight inputs,
radicands, endpoints and inequalities are retained; all endpoints lie
between 0 and B. The final interval encloses cos(theta).

Construct cos(r theta) for 2<=r<256 in increasing order. For even
r=2a use 2 cos(a theta)^2-1; for odd r=2a+1 use
2 cos((a+1)theta)cos(a theta)-cos(theta). All referenced indices
are smaller than r. The factors are nonnegative because their angles
lie in [0,pi/2]. Hence endpoint multiplication followed by downward
and upward division by B encloses each product. Subtract the opposite
endpoints of the subtracted interval. Intersect with [0,B], valid
because r theta lies in [0,pi/2]; record both raw and intersected
intervals. The exact endpoints cos(0)=1 and cos(256 theta)=0 are set
directly. The product identity is specialized, not reproved.

For every residue r modulo 1024, reduce to t=min(r,1024-r).
If t<=256 use the computed interval; otherwise negate the interval
for 512-t, exchanging its endpoints. Evenness and cos(pi-u)=-cos(u)
justify these reflections. This retains cos(pi)=-1 and all residues.
For each m=0,...,1023, sum the intervals for cos(mj theta) weighted
by the nonnegative integers w_j. This gives a complete rational
enclosure [l_m/B,u_m/B] for every lambda_m. Repeated angles and dependence
between intervals affect sharpness, not enclosure validity.

The largest cosine interval width in units of 1/B is 97339. Since
sum_j w_j=R, every spectral interval width is at most
R*97339/B=6553986119231760/B < 2^(-75). The actual largest spectral
width is 3012990786359568/B. These bounds are computed over the entire
tables, not inferred from the preset precision. The 128-bit precision
already decides the comparison; the allowed 256-bit retry is unused.

**Complete finite evidence and numerical comparison.** Run from the
notebook:

```text
python3 scripts/finite-support/ratio_spectral_bound.py
python3 scripts/finite-support/verify_ratio_spectral_bound.py
```

The first program saves `scripts/finite-support/ratio-spectral-bound.json`.
It checks the current hashes of every original artifact recorded in
L123's audit and C122a's audit, both audit scripts, and C122a's fresh
replay artifacts. All saved audit checks pass and completion flags have
no failures. The full endpoint manifest equals the audited expected
manifest; both full histogram manifests equal C122a's audited values.
No enumeration rerun is needed because linkage to the accepted inputs
passes. The certificate saves all checked hashes and its producer hash.

The generator has h^1024=1, h^512=-1; its 1024 powers are distinct and
equal all nonzero roots of X^1024=1. All cyclic successor identities
are checked. The text ratio table has exactly 1023 distinct rows in
the order h,...,h^1023, covers exactly H minus {1}, and agrees in every
same-pair, different-pair and total count with the accepted manifest.
Every inverse symmetry, the zero diagonal, nonnegativity, row sum and
antipodal value are checked. All weights and the cyclic order are saved.

The complete certificate retains eight half-angle records, 254
recurrence records, all 1024 cosine intervals and all 1024 modes.
The largest upper endpoint among nonconstant modes occurs at 426 and
598. Without asserting that an endpoint is an exact eigenvalue, it gives

\[
\lambda_*\le
\Lambda=\frac{-18018083607067510117209940640903437490413147824}{2^{128}}<0.
\]

The certificate also retains the lower enclosure endpoint for lambda_*;
this is not a lower bound on any core's pair energy. Using the upper
endpoint and the positive squared norm, the exact rational pair bound is

\[
\frac12\left(\frac{R61^2}{1024}
        +\Lambda\frac{58743}{1024}\right)
=\frac{5262259384323702554445122878822311364591458658052163}
       {43556142965880123323311949751266331066368}
<120815550368.
\]

Since pair energies are integers, this proves the first conclusion.
The old pairwise-maximum bound was 1830*67798380=124071035400.
Thus this is a strict improvement, not a rounding straddle.

The second program imports no producer code. It reads the entire saved
certificate, rechecks all hashes and input weights, verifies every root
inequality and recurrence using Fraction arithmetic, checks each cosine
reflection, and recomputes every mode by first grouping weights by angle
residue. It compares the exact full maximum, error data and rational
bounds. It saves `scripts/finite-support/ratio-spectral-verification.json`,
including the verified certificate hash, its own hash and all checks.
There are 2386 passing production checks and 2355 passing verification
checks, with no failures; 1023 nonconstant modes are verified. The readback
of the production artifact also matches every saved field. This is
executable finite-arithmetic evidence, not proof-assistant verification.
The separate critical audit below also reviews the mathematics and code.

**Survivor direction.** Reuse L123's finite endpoint-event model and
the standard Bonferroni second truncation: *Probability inequalities*,
§15.1, Proposition 15.2, printed pp.196–197
([UConn-hosted primary chapter](https://probability.oer.math.uconn.edu/wp-content/uploads/sites/2187/2020/08/ch15M.pdf)).
For E_a={omega in Omega:a occurs}, |E_a|=s and
|E_a intersect E_b|=d(a,b). No independence is required. The union is
bounded below by 61s minus the unordered intersection sum. Complementing
in Omega and inserting the proved integer upper bound therefore yields

\[
U(K)\le T-61s+120815550367=1597620964591.
\]

All substitutions and comparisons are exact. This improves the tested
diagnostic by 3255485033, satisfying the approved continuation test.
It proves neither sharpness for cores nor that any selected support
family contains one of these configurations. The transfer obstructions
and antipodal configurations in ATTEMPTS/010 and /019 remain intact;
threshold saving, RS realization, 67/68 safety and qualified ABF
equivalence remain unresolved. No unfinished L121/root work is used.

**Separate critical audit, 2026-10-25.** The prior SPECIALIZE assessment
`drafts/literature/2026-10-25-l124-critical-audit-coverage.md` authorizes
this unchanged audit, classified REPRODUCTION. Full L124, both spectral
programs, L123, L122, C122a and the accepted upstream audit records were
reviewed. The source coverage above is reused; no new general theorem
or broader set of hypotheses is introduced.

The scaling map on endpoints is a bijection of the ordered configuration
space and induces the invertible plane map (s,t) -> (hs,h^2 t). Therefore
L123's ratio counts are applicable to every matrix entry. Interchanging
the two queried endpoints and scaling gives inverse symmetry; this does
not divide by orbit sizes and includes the self-inverse antipodal ratio.
Each configuration containing a fixed endpoint contains exactly five
other endpoints, so the row sum is 5s. The diagonal is deliberately zero:
the singleton count s must not be inserted there. The singleton value
6T/1024 follows from six distinct endpoints and the transitive scaling
action, with no transitivity on cores required.

For row i and column i+j, the negative-exponent Fourier vector contributes
its i-th component times exp(-2 pi i m j/1024), giving the stated
first-row convention. Inverse symmetry cancels imaginary parts. The
complete Fourier basis supplies all 1023 nonconstant modes, even with
repeated eigenvalues; the real symmetric Rayleigh theorem applies to
the real centered indicator in this invariant subspace. A negative
algebraic maximum remains an upper bound on its quadratic form. The
cross terms vanish since A1=R1, and direct expansion gives
||1_K-(61/1024)1||^2=61-61^2/1024. Dividing by two is necessary because
each unordered endpoint pair occurs in both off-diagonal orders; the
configuration ordering is already included in d. This verifies every
normalization in the spectral inequality independently of numerical replay.

The eight positive half-angle steps take pi/2 to pi/512. Their root
inequalities have the correct scale: after division by 2B^2 the radicand
is (1+c)/2. The producer's isqrt(floor(rad/2)) gives the floor of the
root, and its upper correction gives the ceiling, also when rad is odd
or a root is exact. For every recurrence the two referenced indices are
strictly smaller than r; their cosine intervals are nonnegative. Thus
endpoint multiplication is monotone, subtraction reverses endpoints,
and floor/ceiling division encloses the value. Intersection with [0,B]
is valid for the target angle, not an assumption about its approximation.
All four reflected quadrants, including the exact values at 0, pi/2,
pi and 3pi/2, were checked. Weight signs are nonnegative, so interval
sums enclose every mode even when that eigenvalue is negative. Reusing
a cosine interval in different summands cannot invalidate an enclosure.

Run `python3 scripts/finite-support/critical_audit_l124.py`. Its complete
report is `scripts/finite-support/l124-critical-audit.json`. It constructs
the entire required input-hash dictionary from the two accepted upstream
audits and checks equality, preventing omission of a required input.
Every current hash, every field of the endpoint and two histogram
manifests, all 1023 same/different/total ratio entries, and the five saved
endpoint replay outputs are checked. Upstream enumeration is reused
through its accepted unchanged evidence, not rerun or newly proved here.

The audit replays the reviewed producer to
`scripts/finite-support/l124-audit-production-replay.json` and the reviewed
verifier to `scripts/finite-support/l124-audit-verification-replay.json`.
The complete serialized artifacts equal their originals, including all
2386 production and 2355 verification checks. Neither original is
overwritten. The verifier imports no producer code and uses Fraction
arithmetic for recurrence rounding and angle-residue grouping for modes.
The audit separately checks every root inequality and recurrence record,
uses four explicit quadrant cases for all 1024 cosines, and recomputes
each of the 1024 mode intervals by pairing indices j and -j for
1<=j<=511 while retaining index 512 once, with value w_512*(-1)^m.
This differs from the producer's ungrouped sum and verifier's residue
buckets, but shares the justified trigonometric identities; it is not
an independent transcendental approximation method. Complete evidence
is checked programmatically, not inferred from previews or check totals.

All 4958 final audit checks pass, with no failures. They include eight
root records, 254 recurrence records, every cosine and every mode,
the full nonconstant maximum, the exact widths above and the strict
width bound below 2^(-75). Every rational bounds field is recomputed.
The positive squared norm preserves the upper inequality when multiplying
the negative eigenvalue bound. Pair energy is integral, so flooring the
certified rational upper bound gives 120815550367. Since T-61s is an
integer, flooring commutes with its addition, giving 1597620964591.
Bonferroni bounds the endpoint union below; complementing and replacing
its intersection sum by an upper bound gives precisely this survivor
upper bound. The exact improvement over L123 is 3255485033.

Two initial audit-harness failures are preserved: comparing in-memory
tuples with parsed JSON lists failed despite equality of the complete
saved artifacts (`scripts/finite-support/l124-critical-audit-initial.json`),
and a Fraction in the audit report could not be serialized
(`scripts/finite-support/l124-audit-serialization-failure.txt`). Source
snapshots `critical_audit_l124_initial.py` and
`critical_audit_l124_serialization_failure.py` in the same directory
retain those versions. The final harness compares serialized objects
and records the norm as numerator/denominator integers. No mathematical
or original-program correction was needed; no acceptance relies on
either failed run. All original spectral and upstream input artifacts
retain their pre-audit hashes.

Acceptance establishes only this uniform full-configuration diagnostic.
It supplies neither an attaining Boolean core nor a selected-family
supersaturation bound. ATTEMPTS/010's allowed antipodal configurations
and ATTEMPTS/019's above-threshold relaxation remain intact. The exact
core maximum, transfer, threshold saving and arbitrary-center safety
remain unresolved; the 955–957 bracket is unchanged.

## Mathlib

Full matching fixed-field spectral certificate, implementation and
61-point numerical bound: **not checked** in Mathlib. Supporting
circulant/Fourier, symmetric Rayleigh, trigonometric enclosure and
Bonferroni coverage: **not checked**. The named primary results above
are standard imported inputs; unknown Mathlib coverage is not absence.
