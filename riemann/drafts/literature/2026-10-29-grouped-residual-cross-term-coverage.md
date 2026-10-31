# Grouped residual cross term: completed source comparison

TARGET: Evaluate L478 (13)'s complete signed cross term 2 Re sum_(m<=M,h<=M^3) g_(h,m) J(1,m/h) up to an error o(T(log T)^8), retaining its exact weights, fixed cutoff and closed interval.
CHECKED: 2026-10-29
DECISION: EXPLORE
SEARCH_EVIDENCE: Bounded searches for twisted fourth moments, Riemann--Siegel polynomial moments, Gonek's rational-frequency saddle method and finite cyclic Fourier analysis; inspected the primary passages below and reused the previous moment/Hardy assessments and recorded failures. No exact weighted-sum theorem was established; failed searches imply no novelty.
SOURCE_EVIDENCE: Gonek (1984), Lemmas 1--5, pp. 129--132, especially Lemma 2 (24)--(25); Conrey--Ghosh--Gonek (1998), Section 4 Lemmas 1--2, pp. 504--506; Bettin--Bui--Li--Radziwill accepted manuscript (2020), Theorem 1.1 and Theorem 1.3; Tao (2009), 245C Notes 2, Section 2 Lemma 17 and finite cyclic case of Theorem 21. Direct links and actual inspected cases are recorded below.
COMPARISON: Known saddle and rational-twist methods offer an applicable transform/error decomposition, not the requested complete estimate. Full-zeta smooth twisted moments and the c>1 summed lemmas cannot be substituted for the critical-line sharp finite sum. L478's coefficientwise T^(3/2) failure and L319's unsigned involution remain intact.
GAP: Establish the summed endpoint/phase errors and evaluate the retained signed rational arithmetic sum with the exact four cutoffs and logarithmic weights to error o(T(log T)^8); neither obligation is supplied by an inspected theorem. Nonstationary terms, composite moduli, noncoprime products and exact endpoint coincidences remain included.
REASON: This separate literature-only review supplies primary coverage for one bounded arithmetic attempt on the unchanged target. EXPLORE approves testing the specified mechanism, not its estimate; standard source results must be cited rather than reproved. No theorem application, new lemma or mathematical script is part of this turn.
LITERATURE_REASON: The newly nominated grouped target required essential saddle/rational-sum coverage beyond the ready individual-integral diagnostic; that comparison is now completed and reusable for the unchanged scope.
SCOPE: Real T tends to infinity; M=floor(sqrt(T/(2pi))); g_(h,m) and J(1,m/h) are exactly L478 (13)/(4) on [T,2T], with all h<=M^3 and m<=M. No RH, simplicity, spacing, external half-plane, independence or Haar-to-height transfer.

The intended quantity is the complete signed cross term in L478 (2),
not a component lower bound for the full moment. An asymptotic includes
its leading contribution, if any; a little-o bound for the whole term
is not being presumed. The error scale uses L478's upper bound for the
constant-phase contribution. That upper bound is not a lower bound.
Even a successful evaluation leaves the other second-moment terms,
a suitable fourth-moment upper bound, the full L1 threshold and all
actual-Xi sign gaps unresolved.

The initial nomination required comparison with twisted/shifted moments
and weighted divisor methods. The completed comparison follows below.
A formal stationary-point location still does not supply a uniform
expansion or its summed error. No rational exponential-sum model has
been derived or asserted to equal (13) in this literature-only turn.

Continue only if the comparison supplies a concrete applicable method,
with remaining arithmetic obligations named. If the proposed method
merely reproduces the coefficientwise T^(3/2) budget, gives an error
above T(log T)^8 without an independently testable refinement, or
requires unavailable essential coverage, park that method and select
an independent target under the shared recovery rules. Do not repeat
the passing finite expansion or the failed individual-integral budget.

L478 is not yet separately audited. Its identity may be checked as
an input-scope obligation; do not silently treat its negative certificate
as a theorem about the actual moment size. Mathlib coverage is unchecked.

## Primary statements and essential proof cases inspected

### Gonek's scalar saddle formula

S. M. Gonek, *Mean values of the Riemann zeta-function and its
derivatives*, Invent. Math. **75** (1984), 123--141,
[author-hosted primary PDF](https://sas.rochester.edu/mth/people/faculty/gonek-steve/assets/pdf/5-mvzdrvs.pdf),
Lemma 2, p. 130, (24)--(25). For fixed real a, large A, A<B<=2A
and r>0, the integral of
exp(it log(t/(re)))(t/(2pi))^(a-1/2) on [A,B] is

    1_(A<r<=B) (2pi)^(1-a) r^a exp(-ir+i pi/4) + E,
    E=O(A^(a-1/2))
       +O(A^(a+1/2)/(|A-r|+sqrt A))
       +O(B^(a+1/2)/(|B-r|+sqrt B)).

Read Lemma 1's local quadratic change and Lemma 2's near-endpoint,
interior and exterior cases: the endpoint layers use an O(A^a)
bound, the interior uses Lemma 1 and tail integration by parts, and
the far exterior uses integration by parts. Lemmas 4--5 instead sum
integer frequencies for a>1 and subpower coefficients; their proof
uses absolute convergence. Those summed conclusions do not cover (13).

### An existing rational-twist decomposition

J. B. Conrey, A. Ghosh and S. M. Gonek, *Simple zeros of the Riemann
zeta-function*, Proc. London Math. Soc. (3) **76** (1998), 497--522,
[author-hosted primary PDF](https://sas.rochester.edu/mth/people/faculty/gonek-steve/assets/pdf/simplezeros.pdf),
Section 4, Lemmas 1--2, pp. 504--506. Lemma 1 treats real r>0 on
c0<c<2 with c0>0, giving the rational exponential phase and a
distance-to-endpoint error. Lemma 2 treats
A(s)=sum a(n)n^(-s), B(s)=sum_(n<=y)b(n)n^(-s), with
|a(n)|<=C d_(k1)(n)(log n)^l1 and the analogous (k2,l2) bound,
fixed nonnegative integer orders and T^epsilon<<y<<T. On
c=1+1/log T it evaluates integral chi(1-s)B(1-s)A(s)ds/(2pi i)
as sum_(n<=y)(b(n)/n)sum_(m<=nT/(2pi))a(m)e(-m/n), with
error O(sqrt(T)y(log T)^(k1+k2+l1+l2)).
Read the proof's far, dyadic intermediate and sqrt(T) endpoint
regions; it invokes Shiu for short divisor sums. These analytic lemmas
are distinct from the paper's conditional zero conclusions. Neither
the critical-line finite specialization nor its required error is
asserted here. The underlying Shiu primary theorem was not retrieved;
it is not an approved new input for this attempt.

### Twisted fourth moments: comparison, not a matching import

S. Bettin, H. M. Bui, X. Li and M. Radziwill, *A quadratic divisor
problem and moments of the Riemann zeta-function*, JEMS **22** (2020),
3953--3980, DOI 10.4171/JEMS/999,
[accepted author manuscript](https://pure.manchester.ac.uk/ws/portalfiles/portal/173978895/BettinBuiLiRadziwill_twisted_fourth_moment.pdf).
Read Theorem 1.1 (manuscript pp. 2--3): four actual zeta factors,
shifts O(1/log T), two polynomial twists of length T^vartheta with
subpower coefficients, and smooth Phi supported on [1,2], with
Phi^(j)<<_j T^epsilon. Its six-term formula has error
O_epsilon(T^(1/2+2vartheta+epsilon)+T^(3/4+vartheta+epsilon));
the stated useful asymptotic range is vartheta<1/4. Read also
Theorem 1.3's smooth quadratic-divisor hypotheses and the proof setup
in Section 2.1--2.2: the approximate functional equation retains its
smooth product weight. None is a formula for four sharply truncated
individual factors with the residual's remaining theta phase.
No removal of smoothing, replacement by full zeta, or isolated
three-versus-one term extraction is justified by these statements.
Hughes--Young's older range is a reference within this comparison,
not a separately inspected essential theorem.

### Exact finite arithmetic operations

T. Tao, *245C Notes 2: The Fourier transform*, 6 April 2009,
[primary notes](https://terrytao.wordpress.com/2009/04/06/the-fourier-transform/),
Section 2, Lemma 17, Corollary 20 and Theorem 21's finite cyclic
case, with its proof paragraph and Corollary 22's inversion formula.
For a compact abelian group with probability Haar measure, a
nontrivial character integrates to zero. Read the translation proof
and finite cyclic basis argument. Finite Z/mZ therefore permits
exact residue-class decompositions with normalized counting measure,
for arbitrary positive integer m, without a primality assumption.
This supplies algebra, not an estimate for the changing weighted sum.
No Haar-to-height inference is proposed.

## Applicability and one bounded subsequent attempt

Essential inputs are L478 (4), (13), L477's exact theta and M, and
the retained L316 analytic phase. Keep L478's unaudited status explicit.
The scalar source permits real saddle parameters; rational h/m is not
excluded. Establish the exact normalization and all phase replacement
costs before identifying any proposed rational-phase main sum. The
source convention A<r<=B retains an error of full saddle size near
either endpoint; it is not a half-weight asymptotic at an endpoint.
Both coincidences and arbitrarily close approaches must be charged.
No exact expansion for L478 is being derived in this review.

Use that endpoint-sensitive transform/error decomposition, followed by
finite residue-class or geometric-progression summation in the original
n,k,l,m variables, to test the *complete* signed sum. Retain the
conditions n,k,l,m<=M and h=nkl; replacing its truncated divisor
weight by an unrestricted d_3 would change the target. Decomposition
of logarithmic weights, partial summation and finite convolution/error
counting are the proposed research obligations. The finite Fourier
input covers composite moduli but supplies no cancellation when
products share factors with m; those contributions must remain.
The retained signed arithmetic sum must be evaluated or bounded at
the stated accuracy, not just displayed after a transform.

Do not apply the c>1 summed lemma on c=1/2, shift a contour without
bounding both horizontal sides, or use its fixed-coefficient constants
for a T-dependent truncation without a uniform justification. The
scalar lemma and finite operations provide an alternative which needs
no such contour move. Its summed endpoint and arithmetic estimates
are open calculations, not missing assumed theorems. If a new
non-elementary input such as Shiu or a spectral exponential-sum theorem
becomes essential, stop that dependent work for separate coverage.
The existing sources suffice for one finite arithmetic attempt;
they do not suffice to claim its success in advance.

The continuation/abandonment test remains the original o(T(log T)^8)
error for a genuine evaluation, allowing a nonzero main term. A
controlled smaller error or informative obstruction would determine
the route. Another T^(3/2) coefficientwise budget or an unchanged
unsigned stationary involution supplies no refinement. Preserve that
negative evidence and park an exhausted implementation. Even success
leaves the other I_2 terms, the needed I_4 estimate, the full L1
threshold, negative-mass saving and all-height signs unresolved.

## Search scope, duplicates and access qualifications

Queries included: Hughes Young twisted fourth moment theorem length;
Gonek mean values derivatives 1984 PDF; Gonek stationary phase Lemma 2;
Riemann Siegel fourth moment Dirichlet polynomial; mean value chi
Dirichlet polynomials; trilinear exponential sums modulo; Shiu
Brun Titchmarsh multiplicative functions; finite cyclic Fourier analysis.
The generic trilinear and Shiu leads supplied no newly inspected primary
theorem used here. Conrey's 1988 fourth-derivative paper was located
through search, but its AIM PDF open returned 404: unread comparison
lead, not coverage. Gonek's shell download failed DNS; web PDF text
and the focused primary formula extraction were readable. Screenshot
requests supplied no inspectable images; no image verification is
claimed. The displayed Gonek formula was recovered in readable primary
mathematical text, including the plus signs in both denominators.

Read the exact local failure records in
`ATTEMPTS/2026-10-29-full-residual-termwise-moment-certificate.md` and
`ATTEMPTS/2026-09-24-actual-phase-poisson-ratio-test.md`; reused the
completed residual-moment and Hardy-L1 assessments. No matching result
in that scoped record already evaluates the complete sum. No broad
archive or sibling notebook search was performed. Literature readiness
is local progress; no mathematical progress beyond these sources,
novelty certification, RH implication or critical audit is claimed.
Mathlib matching and supporting declaration coverage remain unchecked.
