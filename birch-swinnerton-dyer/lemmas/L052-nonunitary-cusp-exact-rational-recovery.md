# L052 — fixed nonunitary-cusp exact rational recovery

## Hypotheses

Let E/Q be y^2=x^3+1, with minimal differential omega_E=dx/(2y),
normalized associated conductor-36 newform f, and total real period
Omega(E)=integral_(E(R)) |omega_E|. Use L050's certified minimal model,
Delta=-432, conductor 36 and one real component. Use the separately
audited L051 interval for the oriented path {1/6,infinity}, with
A_f({a,b})=2*pi*i integral_a^b f(z) dz. Import the published
origin-preserving Q-isomorphism (X_0(36),[infinity])=E and the precise
differential/cusp-torsion results cited below. Use L048's audited
total-period lattice convention and torsion-reduction argument.

This is a fixed known-method specialization under the prior
[SPECIALIZE assessment](../drafts/literature/2026-10-12-nonunitary-exact-value-recovery.md).
It assumes neither a database optimality label, a general Manin conjecture,
a unitary cusp, a non-CM curve nor any BSD prediction.

## Conclusion

For this exact minimal model and orientation,

    Re(A_f({1/6,infinity}))/Omega(E) = -1/12.

An independently justified integer K=24 clears the real normalized
integration value of every rational-cusp path on this curve. In particular
its reduced denominator is at most 24. Complete exact enumeration of
L051's interval finds only -1/12 among all reduced rationals of denominator
at most 24, with rational existence supplied by the denominator theorem.
The finite certificate and independent full finite replay pass. The separate
critical audit below validates this fixed source specialization and recovery
assembly, retaining its imported analytic and geometric inputs.

This supplies one exact symbol, not a full integral-generator table,
a p-adic coefficient, rational point, Sha result, complex-order comparison
or BSD candidate. It is local reproduction of known results and algorithms,
not progress beyond the sources checked.

## Proof

**Primary imports and independent normalization.** Cai, Chen and Liu,
*Heegner points on modular curves*, Trans. AMS 370 (2018), 3721--3743,
DOI 10.1090/tran/7053,
[Section 3 opening, p.3732](https://archive.ymsc.tsinghua.edu.cn/pacm_download/632/12220-Heegner_points_on_modular_curves.pdf#page=12),
identify (X_0(36),[infinity]) with the elliptic curve of minimal equation
y^2=x^3+1. This is an origin-preserving Q-isomorphism phi of degree one.
For a genus-one curve with rational origin the Abel--Jacobi map to its
Jacobian is an isomorphism. Hence phi induces an isomorphism J_0(36)->E;
its kernel is trivial and connected, so E is the optimal quotient for
its associated newform. The classical identification of weight-two cusp
forms with holomorphic differentials gives dimension one here. L050's
associated normalized form is therefore the form attached to this map.
No L-value, rank or torsion column from the source is used.

Cesnavicius, Neururer and Saha, *The Manin constant and the modular degree*,
author PDF dated 28 January 2022,
[Theorems 1.2 and 7.2, pp.3,45--46](https://maths.qmul.ac.uk/~asaha/research/manin-paper.pdf#page=3),
give phi^*omega_E=c_phi*(2*pi*i*f(z) dz), with nonzero integer c_phi,
for a surjection X_Gamma->E at the exact conductor. When 8 and 27 do not
divide N, c_phi divides deg(phi). Here Gamma=Gamma_0(36),
Gamma_1(36) is contained in Gamma, N=36 is the exact conductor by L050,
8 does not divide 36, 27 does not divide 36 and deg(phi)=1.
Thus c_phi is +1 or -1. Compose phi with [-1] if needed to choose
c_phi=1. This preserves the origin, degree, optimality and torsion orders.
The source/target real-period ratio is one since E is its own optimal
curve. CM and additive reduction at 2 and 3 are allowed by this theorem.
This imports the differential theorem rather than reproving it or assuming
the general Manin conjecture.

**Arbitrary-cusp torsion and the fixed denominator.** Wuthrich,
*Numerical modular symbols for elliptic curves*,
[arXiv:1608.06423v2, 23 March 2017, Proposition 1 and complete proof,
pp.3--4](https://arxiv.org/pdf/1608.06423v2#page=3),
treats arbitrary rational cusps using c_0=1, cusp fields,
Manin--Drinfeld and torsion reduction. The largest square dividing 36
is 6^2, so delta=6 and all cusp images lie in E(Q(zeta_6))_tors.
Its reduction proof uses Silverman, *The Arithmetic of Elliptic Curves*,
second edition, VII.3.4: at good primes ell>2 splitting completely in
the cusp field, reduction is injective on torsion, including ell-primary
torsion since the local ramification index is one < ell-1.
The proof permits a conservative annihilator from any selected such
point counts, as already audited in L048. The stronger unitary-cusp
shortcut is not used: at r=1/6, gcd(gcd(6,36),36/gcd(6,36))=6.

Choose ell=7 and 13. Trial division up to their square roots tests
respectively divisors [2] and [2,3], none dividing ell. Both primes exceed
two, are 1 modulo 6 and do not divide Delta: Delta modulo them is 2 and
10. Thus E has good reduction at both. The polynomial for zeta_6 is
X^2-X+1; its distinct roots are [3,5] modulo 7 and [4,10] modulo 13,
with nonzero derivative 2X-1 at each root. Both primes split completely
in Q(zeta_6), and are unramified. The residue field at either selected
prime above ell is F_ell.

The complete point counts can be checked as follows. At 7 the square
residue root lists are 0:[0], 1:[1,6], 2:[3,4], 4:[2,5]; the other
residues have no roots. For x=0,...,6 the values x^3+1 are
[1,2,2,0,2,0,0], giving y-counts [2,2,2,1,2,1,1]. At 13 the square
residue root lists are 0:[0], 1:[1,12], 4:[2,11], 9:[3,10],
3:[4,9], 12:[5,8], 10:[6,7]; the other residues have no roots.
For x=0,...,12 the right-hand sides are
[1,2,9,2,0,9,9,6,6,2,0,6,0], giving y-counts
[2,0,2,0,1,2,2,0,0,0,1,0,1]. Both lists sum to eleven.
Each smooth projective Weierstrass curve has exactly one point at infinity,
so #E(F_7)=#E(F_13)=12 and their gcd T is 12.
All actual y-lists are retained in the certificate, not only these totals.

For any cusp a, put P_a=phi(a), with P_infinity=O. Manin--Drinfeld
and the origin-preserving map put P_a in the stated torsion group.
The cited injections and Lagrange's theorem show 12 P_a=O.
Consequently for every cusp pair {a,b}, the Abelian integral of
phi^*omega_E gives

    T A_f({a,b}) in Lambda_E,  T=12,

where Lambda_E is the full minimal differential period lattice; its
class modulo the lattice is T(P_b-P_a)=O. L048's audited convention,
from Cremona, *Algorithms for Modular Elliptic Curves*, corrected second
edition (1997),
[Section 2.8 following (2.8.9), p.30](https://johncremona.github.io/book/fulltext/chapter2.pdf),
is Re(Lambda_E)=(Omega(E)/2)Z. In this connected-real-locus case,
a lattice basis can be omega_1 and omega_1/2+i b, b>0;
Omega(E)=omega_1, so its real projection has generator omega_1/2.
Taking real parts therefore yields

    24 Re(A_f({a,b}))/Omega(E) in Z.

This also specializes Wuthrich's arbitrary-cusp formula with period
ratio q^+=1 and c_infinity=1. Wuthrich integrates {infinity,r}; the
present path is its negative. Negation preserves this lattice, so no
orientation sign is inferred from the denominator argument. The interval
alone determines the sign. A reduced rational in (1/24)Z has denominator
dividing 24 and hence at most B=24. This establishes rational existence
independently of the analytic approximation.

**Exact isolation, including all reduced denominators.** Import the
separately audited L051 interval J=[l,u], where D=2^96 and

    l=-6602346876266374004306815782/D,
    u=-6602346876111015594619213162/D.

Its containment, including all Fourier tails and total-period arithmetic,
is a named input; no new numerical approximation is used. Direct rational
arithmetic gives

    -3 < 24l < -2 < 24u < -1.

Thus the sole integer in 24J is -2, and the existent value must be -2/24.
For completeness, reduced rational enumeration uses q=1,...,24 and
ceil(q l)<=a<=floor(q u), retaining gcd(|a|,q)=1. The full results are:

| q | ceil(q l) | floor(q u) | reduced numerators |
|---|---|---|---|
| 1 through 11 | 0 | -1 | none |
| 12 | -1 | -1 | -1 |
| 13 through 23 | -1 | -2 | none |
| 24 | -2 | -2 | none (gcd(2,24)=2) |

There are no skipped denominators or numerator ranges. The candidate
-1/12 is strictly inside J, with exact distances

    (-1/12)-l = 116518807267229881/118842243771396506390315925504 > 0,
    u-(-1/12) = 116518807264174049/118842243771396506390315925504 > 0.

The actual interval width is
38839602421900655/19807040628566084398385987584, while the lattice
spacing is 1/24. Uniqueness is proved by exact endpoint inequalities and
complete enumeration, not width alone or rounding to an expected value.
Existence follows from the preceding cusp/scale theorem and L051
containment. It follows that the desired exact value is -1/12.

**Complete finite evidence and qualifications.** Reproduce from this
notebook using

    python3 scripts/nonunitary-cusp/recover_exact_value.py
    python3 scripts/nonunitary-cusp/verify_exact_value.py

The full certificate is `scripts/nonunitary-cusp/exact_value_certificate.json`;
the report is `scripts/nonunitary-cusp/exact_value_verification.json`.
The producer has no expected rational-value input. It enumerates all y for
every x at both selected primes and every denominator row. The verifier
imports no producer code. It independently reconstructs square-residue
histograms, checks all 20 x-entries and their complete y-lists, checks
primality/good reduction/splitting, and tests all 624 (a,q) cases in
-q<=a<=q, 1<=q<=24. Since J is inside (-1,0), that rectangular range
contains every possible numerator. It verifies each ceiling/floor by
defining inequalities, every reduced candidate, all isolation inequalities
and positive margins, and binds the unchanged audited interval certificate
by SHA-256. Complete selected counts, denominator rows and result fields
were inspected without truncation. No failure occurs in this finite test.

The scripts verify the finite specialization evidence, not the primary
model identification or Manin theorem; those are precise source imports
applied above. L051's analytic certificate is imported as an audited lemma,
not replayed afresh by this verifier. Existing failed/audited schedules and
reports are unchanged. The production replay is not a separate critical
audit or formal proof of universal software correctness. An all-cusp
denominator bound does not produce a full table of exact cusp values.

**Separate critical audit, 2026-10-12, BSD-174.** Under the unchanged
[approved audit scope](../drafts/literature/2026-10-12-nonunitary-exact-recovery-critical-audit.md),
the full proof, both finite implementations and all load-bearing finite
evidence pass review. No mathematical hypothesis, conclusion or direct
input is changed. The following are the applicability and finite checks.

1. The published pointed model identification supplies an actual Q-map
   of degree one, not merely an isogeny-class label. Abel--Jacobi for this
   pointed genus-one curve identifies its Jacobian with it, so the induced
   quotient has trivial connected kernel. Its one-dimensional space of
   holomorphic differentials contains the associated normalized newform.
   L050's minimality and conductor calculation, also checked in L051's
   separate audit, give the exact target and N=36. Theorem 1.2 above
   applies since both bad-prime conductor exponents are two; its exceptional
   cases require exponent at least three. Integrality and divisibility by
   degree one give absolute multiplier one. Changing the sign of the map
   leaves the normalized form and path fixed and permits multiplier +1.
   Thus there is no circular determination of scale from the answer.
   Theorem 7.2's complete proof and Wuthrich's Proposition 1 and proof
   were reopened; the already inspected Cai--Chen--Liu model statement
   in the approved assessment is reused (fresh PDF retrieval timed out).
   No unpublished model computation or new source hypothesis is substituted.

2. All 20 x-entries and complete y-lists are replayed, including the one
   projective point at infinity in each count. A separate Euler-criterion
   count gives character lists
   [1,1,1,0,1,0,0] at 7 and
   [1,-1,1,-1,0,1,1,-1,-1,-1,0,-1,0] at 13.
   The identity #E(F_p)=p+1+sum_x chi(x^3+1) gives twelve in both cases.
   The two distinct cyclotomic roots, primality and good-reduction checks
   verify both degree-one residue fields. The imported full torsion
   injection applies because e=1<p-1 at each place. Each point count kills
   every cusp image in E(Q(zeta_6)); this is an annihilator bound, not a
   claim that the cusp subgroup has order twelve. Subtraction retains the
   same bound for two arbitrary endpoints. The nonunitary cusp 1/6 is
   covered by the first assertion of Wuthrich's proposition.

3. The negative discriminant gives the connected real locus. As checked
   in L048, the full lattice has real projection (Omega/2)Z even though
   its positive real period equals the total period Omega. Consequently
   T=12 and c=1 give 24F in Z. No extra component factor or division by
   a target/source isogeny ratio occurs. Reversing {infinity,1/6} negates
   the integration functional and preserves this lattice condition;
   the independently audited L051 interval fixes the negative sign.

4. The complete finite replay checks every one of the 24 denominator
   rows, all 624 numerator cases, both scaled endpoints, every candidate
   and all margins. Rational existence is supplied before enumeration
   by the geometric argument. As a distinct check, set

       J'=[-83333334/10^9,-83333333/10^9].

   With l=L/D and u=U/D as above, the two strict inclusion cross products
   L*10^9+83333334D and -83333333D-U*10^9 are respectively
   52741095804664738475029300224 and
   26331708299911996498514650112, both positive. Hence J is contained
   in J'. The four positive numerators in
   -3<24 inf(J')<-2<24 sup(J')<-1, with denominator 10^9,
   are 999999984,16,8,999999992. Thus the only integer in 24J' is -2.
   Independent integer cross-multiplication enumeration of all
   -q<=a<=0, 1<=q<=24 gives just (a,q)=(-1,12) in reduced form.
   This larger containing interval has width 10^-9<1/24; existence and
   the strict integer inequalities, not that width alone, prove recovery.
   The new interval is an outer rational bracket of L051's certificate,
   not an independent analytic evaluation.

5. Ten single-field changes separately corrupt the input hash,
   differential scalar, orientation, splitting roots, a complete y-list,
   clearing factor, interval endpoint, denominator-row completeness,
   reduction of a candidate and final recovered value. Calling the full
   verifier on each saved altered certificate rejects it at the relevant
   assertion; all rejection tracebacks are retained. These bounded tests
   verify the fixed replay's response to these changes, not the geometric
   truth of its hard-coded hypotheses or universal software correctness.
   Eleven original certificates, reports and producer/verifier files
   retain their before/after SHA-256 hashes. The production report is
   matched in full, without overwriting it.

Reproduce the audit with separate output files by running

    python3 scripts/nonunitary-cusp/audit_exact_value.py

The fresh complete replay is
`scripts/nonunitary-cusp/exact_audit_full_replay.json`; full independent
checks and preservation hashes are in
`scripts/nonunitary-cusp/exact_audit_checks.json`; all altered inputs and
rejections are in `scripts/nonunitary-cusp/exact_audit_cases/`.
No finite check failed and no mathematical repair was required. This
validates the fixed known-method recovery under the stated source imports;
it does not replay L051's Fourier computation again, produce other exact
symbols, or remove any of the BSD gaps stated in the conclusion.

## Mathlib

Full matching coverage for the fixed exact recovery, the published
X_0(36) model identification, cube-free differential theorem and
arbitrary-cusp torsion-reduction/period combination was not checked.
Supporting rational arithmetic and finite enumeration are separate from
a full matching theorem. No absence claim or formal verification is made.
