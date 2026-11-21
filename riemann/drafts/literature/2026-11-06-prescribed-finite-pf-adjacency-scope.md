# Arbitrary prescribed finite PF order — completed source comparison

TARGET: Assess whether arbitrary prescribed finite PF order can coexist with an eventual positive fixed-shift ray and infinitely many negative minors on the adjacent shift.
CHECKED: 2026-11-06
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Bounded exact/stronger-result searches for finite-order PF polynomials, eventual Toeplitz positivity, adjacent fixed shifts, Schoenberg sectors and dominant-root recurrence oscillation; targeted local comparison with L837, L772 and the saved adjacency assessment/stop. No inspected source states the full rational adjacency family; no novelty inference follows.
SOURCE_EVIDENCE: Reused Alexandersson arXiv:1208.5607v1 Theorem6 pp.5,11–12 and Katkova math/0505174v1 Definition2/TheoremsA/B pp.4–5; inspected Adm–Garloff–Tyaglov JMAA467(2018) Section5 Theorems5.7/5.8 and (5.11)–(5.12), pp.161–162; Bell–Gerhold Israel J.Math.157, Theorems1/2 pp.334–335 and complete Section3 pp.339–341. Links and qualifications below.
COMPARISON: Sector sufficiency already handles arbitrary prescribed finite m as a hypothesis test; Widom handles distinct complex variables. Bell–Gerhold supplies positive-density negative signs once the actual recurrence is nonzero and has no positive dominant root, without a periodic-phase requirement. These methods do not themselves supply the requested rational family or positive neighboring ray.
GAP: Choose and verify a rational degree-five deformation, sector membership for each prescribed m, distinctness, a strict positive shift3 dominance bound and the actual shift4 recurrence hypotheses. No such family or sign specialization was derived in this literature turn; Xi transfer is independent.
REASON: Essential method coverage is adequate for a separate bounded known-method specialization. The newly inspected oscillation theorem removes an unnecessary periodic-phase restriction, so further general browsing is not needed. The ready continuation is nominated separately and requires supervisor approval next turn.
LITERATURE_REASON: PF2 to every prescribed finite PF_m changes the essential hypothesis; source comparison was missing. Bell–Gerhold is a specific new relevant lead for the required infinite negative subsequence.
SCOPE: Real finite polynomials with a_0=1, strictly positive rational coefficients and zero extension; all ordered minors through prescribed size m. Known-method distinct-root specializations only, not an actual-Xi mechanism or a family already proved to exist.

## Completed comparison, 6 November 2026

The main gap is actual-Xi all-degree mixed positivity L030–L032/C032a.
The intermediate question is the exact TARGET. Its downstream use is to
test the abstract adjacency inference even when an arbitrarily large
fixed finite-PF band is supplied. A countermodel would identify a need
for additional Xi structure; it would settle neither Xi signs nor RH.
Success requires both infinite-rank statements, not finite samples.

### Sources and applicability

Reuse the inspected proof and conventions recorded in
`2026-11-06-adjacent-shift-propagation-model-scope.md` for Per Alexandersson,
*Schur polynomials, banded Toeplitz matrices and Widom's formula*, EJC
19(4) (2012), P22, [arXiv:1208.5607v1](https://arxiv.org/html/1208.5607v1),
Theorem6 p.5, Lemma15/Proposition16 and Section3.2 pp.11–12. Theorem6
and the normalization were checked again: s_0=1, distinct complex
variables x_i, elementary coefficients s_i, shift c, positive rank r.
It gives the exact sum over c-element subsets, with bases equal to
products of the selected variables and explicit cross-difference
coefficients. No PF assumption is needed. The remaining task is to
check the chosen parameters, every dominant tie and the smaller terms;
the theorem asserts no sign automatically. No reproof is justified.

Reuse Olga M. Katkova, *Multiple positivity and the Riemann zeta-function*,
[math/0505174v1](https://arxiv.org/pdf/math/0505174v1), Definition2/(8)
p.4 and TheoremsA/B p.5. For a real polynomial with positive constant,
TheoremB's absence of roots in the open sector
|arg z|<pi*m/(m+1) suffices for PF_m, including boundary roots. It
addresses every ordered minor, for each finite m, not only PF2.
TheoremA instead gives a necessary zero-free angle pi*m/(d+m-1)
for degree d. Neither theorem states adjacent-ray signs. Theorem3
p.6 concerns exponential/cosh multipliers of the actual entire xi_1,
not the finite rational model required here. Theorem ASWE p.5 is an
all-order classification, not a finite-order adjacency theorem.

Supporting primary-paper comparison: Mohammad Adm, Jürgen Garloff and
Mikhail Tyaglov, *Total nonnegativity of finite Hurwitz matrices and root
location of polynomials*, JMAA467 (2018), 148–170,
[author-hosted published PDF](https://www-home.htwg-konstanz.de/~garloff/JMAA-3_Adm_Garloff_Tyaglov.pdf),
Section5, Theorems5.7/5.8 and (5.11)–(5.12), pp.161–162. These restate
Schoenberg's necessary/sufficient sectors and the exact quadratic
criterion: for (u+c exp(i theta))(u+c exp(-i theta)), c>0 and
0<=theta<=pi, membership in PF_m is equivalent to
theta<=pi/(m+1). This is the known quadratic input, not a new result.
Their subsequent assertion about arbitrary products outside the angle
is not imported: no product-necessity inference is needed. The
Hurwitz-matrix conclusions later in the paper do not match this target.
Schoenberg's original papers are references, not newly inspected inputs;
the already assessed sufficient theorem is enough for the proposed test.

New method input: Jason P. Bell and Stefan Gerhold, *On the positivity
set of a linear recurrence sequence*, Israel J.Math.157, 333–345,
DOI10.1007/s11856-006-0015-1,
[author-hosted published PDF](https://fam.tuwien.ac.at/~sgerhold/pub_files/papers/2007_osc_rec.pdf).
Its header dates the volume 2006; bibliographies also give 2007.
Theorem2 p.335: a nonzero real sequence satisfying a constant-coefficient
linear recurrence, with no positive dominating characteristic root,
has positivity and negativity sets of positive natural density.
Dominating means maximal modulus in the nonzero power-sum representation
(p.334). No irrational-phase, rational-coefficient or nondegeneracy
assumption is imposed. Section3 pp.339–341, Lemmas7/8 and the complete
Theorem2 proof, treats irrational frequencies, rational periodic
frequencies and mixed cases. Theorem1 pp.334–338 supplies existence of
the densities; the proof reduces to torus functions and controls the
vanishing remainder. Import the theorem. A specialization must establish
reality, nonvanishing, combined bases/nonzero coefficients and absence
of a positive maximal-modulus base. This is stronger than infinitude,
but supplies no effective onset or prescribed arithmetic progression.

### Search, overlap, failures and access

Queries included “Polya frequency finite order Toeplitz zeros polynomial”,
“Toeplitz eventual positivity Polya”, “Polya frequency adjacent minors”,
“Schoenberg multiply positive polynomial sector sharp”, “Polya frequency
arbitrary order polynomial nonreal”, and “Bell Gerhold positivity set
dominant theorem”. Exact adjacent/eventual formulations did not yield a
matching primary theorem. Snippets, blogs, discussion issues, aggregation
pages and lecture-note leads were not used as theorem evidence.

The primary lead Katkova–Ostrovskii, *Zero sets of entire generating
functions of Polya frequency sequences of finite order*, Math.USSR-Izv.
35(1) (1990), 101–112,
[publisher record](https://www.mathnet.ru/eng/im1273), was inspected only
at its bibliographic record/abstract. The full-PDF endpoint timed out
and its download link redirected to the record. Its exact theorems are
unread; neither coverage nor obstruction is inferred from its title.
It is not essential to the sufficient-sector/Widom/recurrence test,
so dependent work is not parked on this access failure. No repeated
access attempt is proposed.

L837 and its preserved PF2 stop are the exact local starting point.
L772's conclusion was checked: its infinitely log-concave entire
sequence and one negative order-five minor establish neither prescribed
PF_m nor the two required rays. The saved source assessment already
checks condensation's difference-of-products limitation and the
nonmatching PF-infinity preservation results; those reviews are reused.
Targeted local searches found no recorded prescribed-finite-order
adjacency construction. This is bounded overlap evidence, not novelty.
No cross-notebook input was used. Matching Mathlib coverage remains
unchecked, not absent.

### Separate bounded continuation

Nominate a rational-quadratic deformation of L837 at degree five,
retaining its three real linear factors and shifts3/4, as the single
ansatz to test for each prescribed m>=2. Choose parameters only during
the mathematical turn. This nomination specifies no family and proves
no parameter interval. In particular do not infer its signs by
continuity from finitely many ranks of L837, and do not retain period6
as an unproved requirement.

The separate assessment
`2026-11-06-prescribed-finite-pf-degree-five-test.md` records the exact
next target and ready method scope. Success must include rationality,
positive coefficients, all ordered PF_m minors via an applicable
criterion, distinctness, a complete positive-ray remainder bound and
either a fully checked Bell–Gerhold application or a complete negative
subsequence proof. R and the parameters may depend on m; no uniform
onset as the quadratic roots coalesce is claimed or required.
Abandon this ansatz if the sector, dominant coefficient or recurrence
hypotheses fail without a specified repair; preserve that evidence.

Decision: SPECIALIZE, with a REPRODUCTION continuation. No full matching
theorem or constructed family was established. The new imported
oscillation input is source progress only. Actual-Xi realization,
strict overlap and all-degree signs remain independent. There is no
new signed Xi mechanism here to justify creative routing; finite-PF
specialization is not relabeled creative for scheduling.

## Original nomination retained (superseded review instructions)

The following records the initial uncovered question. Its instruction
that the next turn be literature-only described the pre-review state;
the completed comparison above and the separate nominated assessment
govern resumption.

The exact question is: for every prescribed integer m>=2, do there exist
a real polynomial P(z)=sum_(n=0)^d a_n z^n with a_0=1 and all a_n
positive rational numbers for 0<=n<=d, an integer 1<=k<d, and an integer
R>=1 such that its zero-extended coefficient sequence is PF_m,
D_(r,k)(P)>0 for every integer r>=R, and D_(r,k+1)(P)<0 for infinitely
many positive integer r? Here D_(r,k)=det[a_(k+j-i)] for 0<=i,j<r,
and PF_m means every ordered Toeplitz minor of size at most m is
nonnegative. P,d,k,R may depend on m. This is a proposed question,
not a theorem or an assumed existence statement. It does not require
one P to satisfy all finite orders simultaneously.

The main gap remains actual-Xi all-degree mixed positivity
L030–L032/C032a. A source answer could determine whether even a very
large fixed finite-PF band can support an abstract adjacency inference,
or whether that inference needs additional signed Xi structure. Neither
answer would by itself settle Xi, overlapping onsets, or RH. C832a and
L834 motivate the comparison but are not premises about this family.

Essential local input: audited L837, including its exact PF2 scope, and
the preserved PF2 adjacency failure in
`ATTEMPTS/2026-11-06-pf2-adjacent-ray-propagation-stop.md`.
Reuse `2026-11-06-adjacent-shift-propagation-model-scope.md` for the
inspected sector/Widom hypotheses, condensation limitation, nonmatching
PF-infinity preservation results and already checked local failures.
These do not establish source coverage outside their stated scope.
No cross-notebook input is proposed. Matching Mathlib coverage is
unchecked, not absent.

Next turn is literature-only. Perform one bounded exact-statement and
stronger-result comparison, using the saved sources first and reading
only essential theorem hypotheses/cases. Do not run mathematical scripts
or construct a family during that review. Import a matching theorem or
counterexample with a precise citation; otherwise nominate one concrete
bounded mathematical test under an adequately justified assessment.
Record an obstruction if a stronger theorem precludes the family. Stop
this nomination if it merely reproduces the PF2 conclusion or supplies
no test of the strengthened hypothesis; preserve the existing stop.

A central creative attempt still requires a specific new signed Xi
mechanism. This generic finite-order comparison is not relabeled
creative; no such mechanism was found or tested during the L837 audit.
