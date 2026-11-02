# Centered first arithmetic jet: numerical-radius source comparison

TARGET: Test whether |partial_alpha B_N(0;a)| <= (2 log N+C) a^*G_N a for every N>=2 and complex a, with one absolute C, using the numerical radius of L627's centered multiplier compressed to its rational basis indices n<=N.
CHECKED: 2026-11-01
DECISION: EXPLORE
SEARCH_EVIDENCE: Bounded exact, numerical-radius, restricted-shift, rational Bernstein and multiplicative-weight searches completed; queries and local duplicate/failure checks below. No matching constant-2 theorem or counterexample was identified; no exhaustive absence or novelty claim.
SOURCE_EVIDENCE: Inspected Haagerup–de la Harpe, Proc. AMS 115 (1992), Theorem 1(1), Proposition 1 and Lemma 1/Proposition 2(1)/proof of Theorem 1(1), printed pp. 372–376; Baranov–Zarouf arXiv:1310.1182v1, definitions pp. 1–2, Theorem 2.3/(2.5), pp. 4–5 and complete equal-exponent proof Section 4.3 Step 3/(4.11), p. 11; Gorkin–Partington accepted manuscript dated 3 May 2019, model-space definitions pp. 2–4, Theorem 3.4 and complete proof including repeated-zero limiting case pp. 8–9. Reuse prior HLS/Lubinsky and arithmetic-source assessments unchanged.
COMPARISON: General numerical-radius formulas provide a test framework; nilpotent and one-variable restricted-shift theorems require additional structural hypotheses, while rational Bernstein bounds concern a different derivative. None of the inspected theorems supplies the proposed compressed tensor-space constant 2 with one absolute additive C. The earlier 16/3 full-output bound remains the available local estimate.
GAP: Establish or refute the uniform numerical-radius bound for precisely L627's centered compression, including arbitrary complex coefficients, the multiplicative index cutoff n<=N and all rational-basis boundary entries. Source comparison is adequate for one bounded mathematical attempt, not an approval of the inequality.
REASON: A sharper first scalar jet could reduce L629's degree-one cost while retaining the exact signed functional. Higher degrees, the total observer budget and pointwise Xi signs remain unresolved; this is distinct from the parked absolute norm budgets.
LITERATURE_REASON: The nominated target changed from the full signed half-budget to a centered compressed numerical-radius estimate with the specific constant 2. This turn completes its missing theorem-level comparison; the unchanged ready target should next receive mathematics.
SCOPE: Every integer N>=2, arbitrary complex a, exactly G_N and B_N of L623/L624, full divisor tail and analytic C_N(q), and one absolute additive C. Downstream retain N=floor(T^(1/100)), L622's window and common real unit observer. No zero-free, pointwise-sign, raw-tail truncation or cross-notebook premise.

## Exact local scope and reused coverage

The main gap remains actual-Xi pointwise initial signs at unbounded heights
and all-degree mixed positivity. The intermediate target is TARGET. Its
plausible downstream use is a smaller arithmetic-degree-one cost in
L629's finite signed functional. Even success would leave degrees two
through eight, the total signed budget, the reference/transfer audits
and pointwise signs open.

Read L627's hypotheses and Sections 1–6, in particular (4)–(6) and
(9)–(10); L623's hypotheses and (1); L624's hypotheses, (1) and (5);
and L629's hypotheses and (1)–(4). These define the precise object
being compared, without deriving a new estimate. In L627's notation,

    f=sqrt(C_N) F P=sum_(n<=N) y_n f_n,
    ||f||_2^2=a^*G_N a,
    partial_alpha B_N(0;a)=mu_N||f||_2^2-<Hf,f>.

Here the f_n are orthonormal rational tensor vectors with their full
infinite coefficient tails. Pi_N projects onto their span for n<=N;
it does not truncate the raw divisor coordinate r. Thus the saved
numerical-radius formulation is already L627's scalar identity.
Retain the centered diagonal, raising entries and exceptional lowering
entry from (6)/(9)–(10). Their independent audit status remains open.
No compression identity for products of this operator is presumed.

Reuse [the full-Gram logarithmic-degree assessment](2026-11-01-full-gram-log-degree-energy.md):
its inspected Hedenmalm–Lindqvist–Seip Section 2.2/Lemma 2.3 and
Theorem 3.1, Lubinsky arctangent Theorem 1.5, and weighted Bernstein
Theorem 1.1/Corollary 1.2 remain adequate for those inputs. Their
measure, multiplier-supremum and weight-parameter qualifications do
not disappear when the desired constant changes. Hughes–Young and
complete-sum holomorphy coverage are reused; no new zeta estimate is
proposed, so the zero-free literature baseline is not reopened.

## Primary numerical-radius comparison

U. Haagerup and P. de la Harpe, *The numerical radius of a nilpotent
operator on a Hilbert space*, Proc. Amer. Math. Soc. 115(2) (1992),
371–379, DOI [10.1090/S0002-9939-1992-1072339-6](https://doi.org/10.1090/S0002-9939-1992-1072339-6).
Read the [UNIGE published copy](https://access.archive-ouverte.unige.ch/access/metadata/2e3d55fc-f7d2-42af-95ae-6c06df864dbb/download),
printed pp. 372–376, Theorem 1(1), Proposition 1, Lemma 1,
Proposition 2(1), and the proof of Theorem 1(1).
For a bounded operator T on a complex Hilbert space with T^k=0,
k>=2, the theorem gives

    w(T)<=||T|| cos(pi/(k+1)).

Proposition 1's proof also records the general formula

    w(T)=(1/2) sup_theta ||exp(i theta)T+exp(-i theta)T^*||.

The nilpotent proof uses a positive difference of power-Gram matrices
and the finite shift extremum. It cannot be invoked merely because
an operator is compressed to finite dimension: nilpotency is an
essential unverified hypothesis here. L627 includes centered diagonal
and lowering entries as well as raising entries. The displayed general
formula supports an all-angle test, but supplies no logarithmic constant.
No part of this theorem is reproved or used to assert a new inequality.

## Primary rational Bernstein comparison

A. Baranov and R. Zarouf, *A model space approach to some classical
inequalities for rational functions*, J. Math. Anal. Appl. 418(1)
(2014), 121–141, DOI [10.1016/j.jmaa.2014.03.059](https://doi.org/10.1016/j.jmaa.2014.03.059).
Inspected [arXiv:1310.1182v1, 4 October 2013](https://arxiv.org/pdf/1310.1182v1),
definitions pp. 1–2, Theorem 2.3/(2.5), pp. 4–5 and Section 4.3,
Step 3/(4.11), p. 11. With normalized circle measure, n>=1,
0<r<1, and f=P/Q of degree at most n with no poles in
r<=|z|<=1/r, the equal-exponent statement is

    ||f'||_Lp <= n(1+r)/(1-r) ||f||_Lp,  1<=p<=infinity.

The relevant proof uses the reproducing-kernel integral representation,
Hölder and the kernel norm identities; the entire equal-exponent case
was read. This bounds an ordinary one-variable derivative, not the
centered multiplier quadratic form on a prime tensor space with an
index-product cutoff. A bridge controlling that exact space and the
constant 2 plus an absolute additive error remains unproved. Pole
separation alone does not supply the bridge. No tensorized or weighted
specialization is claimed in this literature turn.

## Primary restricted-shift comparison

P. Gorkin and J. R. Partington, *Norms of truncated Toeplitz operators
and numerical radii of restricted shifts*, Comput. Methods Funct.
Theory 19 (2019), 487–508, DOI
[10.1007/s40315-019-00282-z](https://doi.org/10.1007/s40315-019-00282-z).
Read [accepted manuscript, 3 May 2019](https://eprints.whiterose.ac.uk/id/eprint/146209/1/norms_of_ttos_final.pdf),
model-space definitions pp. 2–4, Theorem 3.4 and complete proof
pp. 8–9, including its final repeated-zero limiting case.
For a finite Blaschke product B with distinct real zeros in the disk,
the numerical radius of S_B=P_(K_B) M_z restricted to
K_B=H2 minus B H2 is attained on the real axis. The proof uses
interpolation and disk automorphisms; it extends by approximation
to repeated real zeros. This is a theorem about that restricted
shift, not every real matrix or rational multiplier compression.
No identification of the full multiplicative-cutoff space with such
a one-variable model and operator has been established. Consequently
one may not restrict our complex-coefficient test to real vectors or
real-axis numerical range using this citation.

## Search, duplicates and recorded failures

Queries actually run for the changed target included:

- `"numerical radius" "Dirichlet" polynomial`
- `"Dirichlet polynomials" "numerical radius" multiplier`
- `"divisor" "Gram" "numerical radius"`
- `"logarithmic derivative" "gcd matrices"`
- `"2 log N" "Gram" derivative Dirichlet`
- `"centered" "numerical radius" multiplier Dirichlet`
- `"numerical radius" "Toeplitz" "rational" compression`
- `"Haagerup" "de la Harpe" numerical radius nilpotent pdf`
- `"Bernstein" "rational functions" "L2" prescribed poles inequality`
- `"Bernstein" "rational functions" "Hardy" Baranov Zarouf`
- `"multiplicative" "weighted Bernstein" polynomials logarithmic`
- Exact-title searches for the Baranov–Zarouf and Gorkin–Partington papers.

No exact match or known counterexample for TARGET was identified.
This is bounded coverage, not a novelty certification. Zarouf's
arXiv:1003.0297v3 was opened and its model-space theorem and some proof
excerpts inspected; it is not counted as a fully reviewed additional
input. The explicit equal-exponent theorem/proof above suffices for
this comparison. The AMS PDF returned 403; UNIGE resolved access.
The ar5iv rendering and direct shell downloads failed; the primary
PDF text was accessible through the web tool. No essential source
blocker remains and no unread lead is required for the approved test.

Narrow local searches in the ready full-Gram/collective arithmetic
assessments and full-Gram history found the nomination rather than
an existing constant-2 proof. Read the recorded failures:

- [Freezing](../../ATTEMPTS/2026-11-01-collective-zero-shift-freezing-stop.md): L623's long-prime-power deformation prohibits uniform entry freezing.
- [Prefix inverse](../../ATTEMPTS/2026-11-01-divisor-inverse-o1-prefix-stop.md): L624 prohibits the shifted-prefix I+o(1) shortcut.
- [Absolute Cauchy budget](../../ATTEMPTS/2026-11-01-full-gram-absolute-cauchy-budget-inconclusive.md): L628's absolute majorant misses 1/2, without refuting it.
- [Signed jet budget](../../ATTEMPTS/2026-11-01-full-gram-signed-jet-budget-inconclusive.md): L629's available first-degree cost 64/75 is an upper cost, not an attained obstruction.

The proposed scalar numerical-radius test retains these deformations
and boundary contributions. It is not a rerun of the stopped absolute
budget. It does not repair higher degrees by itself.

## Bounded continuation and decision

Approve the unchanged TARGET as EXPLORE for one mathematical attempt.
Use L627 (4)–(6)/(9)–(10) and L623 (1)/L624 (1)/(5) for the exact
operator and centering; use L629 (1)–(4) only for its downstream role.
The transfer context retains L622/L619(H=T), L465/L471/L018 and their
named Hughes–Young/holomorphy/HLS imports. No cross-notebook input.
Source coverage permits an attempt, not treating the unaudited local
identities as an independent critical review of those results.

The test must prove the bound for every N and complex vector with a
single absolute additive C, or exhibit a rigorous unbounded family
whose normalized first-jet magnitude minus 2 log N is unbounded.
A bound with a larger leading constant, even 2 log N+o(log N) with
uncontrolled additive error, does not pass. Neither does a floating
finite matrix or a fixed-N excess when C is unspecified. Retain all
complex directions; real entries alone do not justify a real-axis
shortcut. Failure of this estimate would refute only this intermediate
target, not the full signed budget or RH. Save partial reasoning and
reassess if the bounded attempt is inconclusive; preserve earlier stops.

No new mathematical estimate, lemma, mathematical script, proof assembly
or DAG change was made. This is LITERATURE / NOVELTY_UNCHECKED with
outcome EXPLORATION. Full matching Mathlib coverage for the target and
these operator comparisons has not been checked and remains unknown.
