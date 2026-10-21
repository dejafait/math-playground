# L042 — Conductor-eleven finite quadratic enclosure at seven

## Hypotheses

Let E/Q have minimal equation y^2+y=x^3-x^2-10x-20, with
coefficients [0,-1,1,-10,-20]. Use the primitive untwisted ordinary
series on the trivial Teichmuller branch, total minimal real Neron
period, and kappa(gamma)=8 as in
[foundations/05](../foundations/05-kato-divisibility.md).
Write L_7(E,T)=sum a_i T^i; here a_2 denotes the quadratic p-adic
coefficient, not the Weierstrass coefficient or Fourier coefficient.

Import audited L039's independently proved minimality, Delta=-11^5,
conductor eleven and non-CM status, and its complete torsion-free relative
integral presentation. Import audited L041's exact functional
F=phi/5, phi=(5/2,5,1) on quotient coordinates, and all-rational-argument
denominator ten. Its normalization retains L040's published computational
optimality and external-source qualifications. The generic adapter's
SUPPLIED_CONDITIONAL provenance is retained; L039's local arithmetic
supplies this exact instance's arithmetic separately. These mathematical
inputs are not inferred from hashes or software success flags.

Full new evidence is `scripts/conductor-eleven/quadratic-seven/certificate.json`,
SHA256 `ed25ec33467d21ba4bf7c3ca1d868824a76225222e46017bb52e9cb9d3196124`.
Complete distinct replay is the adjacent `verification.json`.
Reproduce from the notebook root:

```bash
python3 scripts/conductor-eleven/quadratic-seven/build_certificate.py
PYTHONDONTWRITEBYTECODE=1 python3 scripts/conductor-eleven/quadratic-seven/verify_certificate.py
```

All prior inputs remain read-only; fresh complete upstream reports and
their log are under the adjacent `upstream-replay/`. Production replay
passes. The separate critical audit of this assembly and programs also
passes, as detailed below. This is a known-method reproduction, not a BSD candidate.

## Conclusion

Seven is good ordinary, with #E(F_7)=10 and t=a_7(E)=-2. At n=2,
M=3, C=0 and u=222, the exact L027 sum is

\[
b=-\frac{496}{1367631},\qquad v_7(b)=0,\qquad
N=\min(n-1,M)=1>0.
\]

Consequently

\[
v_7\left(a_2+\frac{496}{1367631}\right)\ge1,
\qquad a_2\ne0,\qquad v_7(a_2)=0.
\]

The bounded schedule stops at its first successful depth. Depths three
and four were not attempted. This supplies the fixed quadratic premise
only. Neither lower coefficient vanishing, two rational points, central
complex vanishing, L026's other hypotheses, Sha finiteness nor comparison
with complex order is supplied. A quadratic certificate alone implies
no rank-two equality; the main arbitrary-curve BSD gap remains unresolved.

## Proof

**Named method and applicability.** Apply L027's existing enclosure,
rather than reprove convergence. Its primary inputs are Stein--Wuthrich,
*Algorithms for the arithmetic of elliptic curves using Iwasawa theory*,
Math. Comp. 82 (2013), 1757--1792,
[Section 3, pp.1762--1766, Propositions 3.1/3.5 and Corollary 3.3](https://wstein.org/papers/mcom2649-iwasawa-alg.pdf#page=6),
and Conrad, *Hensel's Lemma*,
[Theorem 4.1, printed p.6](https://kconrad.math.uconn.edu/blurbs/gradnumthy/hensel.pdf#page=6).
The prior SPECIALIZE assessment covers this exact changed model and
adapter. The old conductor-389 certificate is methodology only: none
of its trace, ordering, scale, dimension or coefficient values is used.
The ordinary interpolation multiplier remains present; no factors are
removed and no lower coefficient is presumed zero.

**Good ordinarity and all-level denominator.** Since Delta=-11^5 is
5 modulo seven, reduction is good. Completing the square gives the
following complete affine count; the verifier independently tests all
49 ordered pairs in F_7^2 in the original equation.

| x | y satisfying the equation modulo seven |
|---|---|
| 0 | none |
| 1 | 3 |
| 2 | 2,4 |
| 3 | none |
| 4 | 1,5 |
| 5 | 1,5 |
| 6 | 1,5 |

There are nine affine points. Homogenization at Z=0 gives X^3=0,
so the only projective point at infinity is [0:1:0]. Thus the complete
count is ten and t=7+1-10=-2, a seven-adic unit. L039 supplies non-CM
and minimality. Seven meets L041's p>=5, p!=5 and good-ordinary conditions.
Its complete integral generator values are
(-1/5,1/5,0,1,1/2,-1/2,-1,-1,-1/2,1/2,1,0), with denominator ten.
L041's integral-lattice argument therefore supplies C=0 at every rational
argument, including every level in L027's limiting construction. The
finite path sample does not replace that all-level proof.

**Teichmuller and unit-root precision.** The six least-positive residues
modulo 49, with complete residual and derivative checks, are:

| d | w | v_7(w^6-1) | 6w^5 modulo seven |
|---|---|---|---|
| 1 | 1 | infinity | 6 |
| 2 | 30 | 2 | 3 |
| 3 | 31 | 2 | 2 |
| 4 | 18 | 3 | 5 |
| 5 | 19 | 3 | 4 |
| 6 | 48 | 2 | 1 |

Each lies in [1,48], is d modulo seven and has sixth power one modulo
49. The verifier enumerates every candidate in each residue class,
finding exactly the displayed integer. The zero residual at w=1 is an
exact root, assigned infinite valuation. Every derivative is a unit.
Conrad's simple-root criterion, as already specialized in L027, identifies
these residues with the Teichmuller roots modulo 49.

For f(X)=X^2+2X+7, u=222 is a unit congruent to t=5 modulo seven.
Its exact residual and derivative are

\[
f(222)=49735=145\cdot7^3,\qquad f'(222)=446=5\pmod7.
\]

Since 145 is a unit, the residual valuation is exactly three. The verifier
also enumerates all residues in [0,342] congruent to five modulo seven
and finds 222 as the unique root modulo 343. L027's Hensel application
therefore gives v_7(alpha-222)=3 for the ordinary unit root. The other
root has valuation one. The root approximation affects only scalar
powers, never the exact rational cusp arguments.

**Every oriented path and full quotient.** For all d=1,...,6 and
j=0,...,6, set r=w_d 8^j modulo 49 in [1,48]. The complete 42-term
array is saved, including j=0,1 and every j>2. Distinct replay computes
r by repeated multiplication and checks that the multiset is exactly
the units modulo 49. Its two exact arguments are r/49 and r/7, giving
84 distinct paths from infinity. Integer parts in the latter family are
retained: no approximate root or unsupplied periodicity adjustment is used.

Every one of the 326 segment occurrences has an integer lift
h=(A,B;C,D) with AD-BC=1, start=B/D and end=A/C in canonical
projective coordinates. The ordered chains start at infinity, have
matching consecutive endpoints and end at the exact reduced argument.
Backward continued-fraction evaluation confirms the endpoint separately
from the builder's forward recurrence.

For each segment the verifier exhausts all twelve actual L039 lifts g_i
and finds exactly one for which gamma=h g_i^(-1) has lower-left entry
divisible by eleven. It checks det(gamma)=1, gamma g_i=h entrywise,
and equality with the saved reduction and index. Thus h{0,infinity}
is precisely the positively oriented generator g_i in the relative
quotient. This avoids the builder's modular-inverse coset lookup and
does not assume the conductor-389 order.

Telescoping identifies each entire cusp path with its raw Z^12 sum.
The verifier reconstructs all twelve raw entries and every one of the
three quotient coordinates, using L039's complete integral presentation.
It checks each evaluation both by F=(1/2,1,1/5) on quotient coordinates
and by all twelve normalized generator values on the raw vector. All
24 source relations and nine saturated relations pair to zero. The
complete lattice and normalization are prior audited inputs, not inferred
from those zero pairings or these finitely many paths.

**Complete finite sum.** In the following table, column j is the value
at r=w_d8^j modulo 49. It records every A=S(r/49) and B=S(r/7);
the B value shown is constant across all seven columns in its row.

| d | A at j=0 | j=1 | j=2 | j=3 | j=4 | j=5 | j=6 | B for all j |
|---|---|---|---|---|---|---|---|---|
| 1 | 6/5 | 6/5 | -13/10 | -13/10 | -13/10 | 6/5 | -13/10 | 7/10 |
| 2 | -13/10 | 6/5 | 6/5 | -13/10 | 6/5 | -13/10 | -13/10 | 7/10 |
| 3 | -13/10 | 6/5 | -13/10 | 6/5 | 6/5 | 6/5 | 6/5 | -9/5 |
| 4 | -13/10 | 6/5 | -13/10 | 6/5 | 6/5 | 6/5 | 6/5 | -9/5 |
| 5 | -13/10 | 6/5 | 6/5 | -13/10 | 6/5 | -13/10 | -13/10 | 7/10 |
| 6 | 6/5 | 6/5 | -13/10 | -13/10 | -13/10 | 6/5 | -13/10 | 7/10 |

The weights binomial(j,2) are (0,0,1,3,6,10,15). The weighted A sums
by row are (-41/2,-28,79/2,79/2,-28,-41/2), totaling -18.
Each row's B weight sum is 35 times its displayed B value, and
35(4*7/10-2*9/5)=-28. Hence the complete exact L027 sum is

\[
b=\frac{-18}{222^2}-\frac{-28}{222^3}
=\frac{-3968}{10941048}=-\frac{496}{1367631}.
\]

The distinct replay accumulates integer generator values 10F(g_i),
giving totals sum_A10=-180 and sum_B10=-280. It obtains the same
b=(222 sum_A10-sum_B10)/(10*222^3), and independently checks every
individual rational term and their sum. Thus neither saved aggregates
nor a truncated polynomial establish the equality. In particular the
B sum is nonzero and the scale is 1/5; neither may be copied from L033.

**Limit enclosure and retained qualifications.** Seven divides neither
496 nor 1367631=111^3, so v_7(b)=0. All hypotheses of L027 now hold
with n=2, C=0 and M=3. Its all-level convergence/error argument gives
v_7(a_2-b)>=min(1,3)=1. This exceeds v_7(b), so the ultrametric
inequality gives v_7(a_2)=0 and nonvanishing. A finite P_2 coefficient
alone would not give this limiting conclusion; the imported L027 tail
and L041 all-level denominators are essential.

The ten grouped complete replay checks have no failures, including
84/84 paths, 326/326 recorded segment occurrences and 42/42 terms.
Fresh upstream replay checks the entire L039 lattice/operators and dual
rank witness, L040's complete finite arithmetic/enclosure and L041's
calibration. Full reports, including every structural check, are retained
under `upstream-replay/`. Every bound prior byte is unchanged. Hashes bind
prior audited proofs and evidence; they do not prove external theorems.

An initial verifier interface error required identical upstream count
dictionaries even though the actual dictionary additionally records 218
segments. Its failure is preserved in `development-failure-01.json`.
The corrected comparison checks every required domain count and all 218
segment occurrences; the complete replay then passes. No mathematical
input, path, term, or bound was changed. The separate critical audit below
reviews both programs and the assembly, including complementary path
choices and preservation of normalization. There is no theorem
beyond the assessed known method, no rank-two implication and no BSD
candidate.

**Separate critical audit (2026-10-10).** The complete L027 enclosure,
L028 convention, audited L039/L040 qualifications, L041 all-level proof,
this assembly and both coefficient programs were reviewed under the
prior SPECIALIZE assessment. No mathematical correction was needed.
Reproduce the bounded audit from the notebook root:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/conductor-eleven/quadratic-seven/audit.py
```

The full report is `scripts/conductor-eleven/quadratic-seven/critical-audit/audit.json`;
the complete complementary witnesses are the adjacent `alternative-paths.json`.
Every original coefficient program, certificate, report, retained development
failure and upstream report is copied under `originals/` before replay.
The pre-replay manifest binds these and all prior bound inputs. The preserved
builder runs at an isolated root and reproduces the certificate byte for
byte. The preserved verifier runs on a separate copy with every output
redirected through its ROOT; BASE and CAL remain the original read-only
input locations. Its result equals the original report except for output
paths. All original and prior bound bytes remain unchanged. Hashes establish
provenance, not the truth of any mathematical input.

The fresh upstream execution checks the entire structural and dual evidence,
the independent twist ratio and the calibration. In particular all required
structural domains are checked: 120 orbit assignments, twelve cosets,
24 relations, 36 relation lookups, sixty paths, 43 row and thirteen column
operations and their inverses, 48 source-relation images, eighteen saturated
images and 24 generator reconstruction identities. All 218 upstream segment
occurrences are separately required. The complete structural report agrees
with its original. This confirms the repaired domain comparison without
requiring equality between dictionaries with different declared key sets.
The retained development failure is not erased or relabeled as success.
Original coefficient replay checks all 84 paths, 326 segments and 42 terms,
not a sampled subset or only the reported total.

For an independent path choice, the audit uses the **ceiling** Euclidean
expansion with minus signs, instead of either production program's floor
continued fraction. For each positive noninteger r=a/b in lowest terms,
set k=ceil(a/b) and replace (a,b) by (b,kb-a) until the denominator is zero.
At each step 0<=kb-a<b, so termination is finite. Reconstructing backwards
by v=k-1/v checks the exact original r. Starting from
(p_0,q_0)=(0,-1), (p_1,q_1)=(1,0), append
(p_2,q_2)=k(p_1,q_1)-(p_0,q_0) and shift the pair.
Every actual step checks q_2>0 and p_2 q_1-p_1 q_2=-1.
Consequently

\[
h=\begin{pmatrix}-p_2&p_1\\-q_2&q_1\end{pmatrix}\in SL_2(\mathbf Z)
\]

sends 0 to the previous cusp and infinity to the next. Exhausting all
twelve original lifts gives exactly one i with gamma=h g_i^(-1) in
Gamma_0(11); determinants, the lower-left divisibility and gamma g_i=h
are checked entrywise. Thus the positively oriented segment is the
integral generator g_i. Adjacency and the final endpoint identify its
sum with {infinity,r} by the imported path-addition theorem. This argument
uses complete geometric witnesses, independently of the scalar evaluation.

All 84 chains begin with ceil(r), whereas the corresponding original chain
begins with floor(r). Hence every oriented decomposition is different.
There are 534 alternative segment occurrences. Eighty-three raw Z^12 sums
are different; one agrees despite its different geometric chain, which
does not weaken the comparison. For every path, all twelve raw coordinates
and all three quotient coordinates are checked. More strongly, let delta
be the alternative raw vector minus the original one, K the audited
12-by-9 saturated-kernel matrix, and H its retained 9-by-12 head map.
The saved integer vector c=H delta satisfies Kc=delta entrywise in all
84 cases, and Pi delta=0 in all three coordinates. Thus the equality
holds in the full integral relative quotient. The alternative file records
every chain, lift, Gamma_0 matrix, raw vector, quotient and integer witness.

The audit reevaluates all twelve normalized generators with (1/2,1,1/5),
all 24 source relations and nine saturated columns, and denominator ten.
The mathematical all-level implication is unchanged: integral path
generation and F(g_i) in (1/10)Z put F(M) in (1/10)Z, hence in Z_7.
No finite sample alone establishes C=0. L040's independent q=5 and L028's
positive-twist/total-period conventions still supply the normalization;
the audit does not infer it from the coefficient or a lower vanishing claim.

Full replay enumerates the six exact Teichmuller residues, including the
infinite residual valuation at one, and their unit derivatives. Independent
enumeration again selects 222 modulo 343; its residual is exactly 145*343
and its derivative is five modulo seven. These meet the imported Hensel
hypotheses. All 42 term labels and binomial weights are independently
generated, using the complementary paths for both symbol families and
integer arguments unchanged. Exact rational summation gives the displayed
six A row sums, sum A=-18, sum B=-28 and b=-496/1367631, agreeing with
every individual saved term, including the zero weights and j>2 terms.

Finally, L027's infinite-tail estimate is n-1-C=1, and its scalar-root
substitution estimate is M-C=3. Both require the certified all-level bound.
Their minimum is one, while the reduced numerator and denominator of b
are both units at seven. The strict inequality therefore gives the claimed
valuation of the limiting coefficient, with no assumption on a_0 or a_1.
The primitive multiplier and kappa(gamma)=8 remain unchanged.

Five altered copies test a changed full-relative coordinate, root residual,
nonzero j=6 term, gamma and limiting bound. Each complete verifier run
rejects, replaces a seeded success with a fresh report binding the altered
certificate, and leaves empty result fields. These sensitivity tests are
supplementary; they are not universal software correctness proofs. All
nineteen audit comparisons pass with no unexpected failures.

This validates only the fixed quadratic input by known methods. L039's
generic SUPPLIED_CONDITIONAL status remains separate from its independently
proved local arithmetic; L040's published optimality and external-source
qualifications remain imports. Central vanishing, independent points,
Kummer membership, elimination of Sha defects, complex-order equality and
uniform production are not supplied. The production schedule stays stopped.

## Mathlib

Full matching arithmetic enclosure, ordinary convergence, calibrated
relative-symbol evaluation and this finite certificate: not checked.
Supporting valuation, Hensel, binomial and exact linear-algebra coverage:
not checked. Unknown coverage is not absence. Named inputs are cited
above and the prior mathematical results retain their qualifications.
