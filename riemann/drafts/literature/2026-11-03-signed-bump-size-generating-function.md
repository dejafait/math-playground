# Source assessment: a size-generating-function test for the signed bump

TARGET: For the original fixed L703 bump, test whether the ordinary generating function of the exact L714 sequence K_(12q+3) has a provably nonremovable singularity forcing a subsequential exponential rate above the actual P_n rate.
CHECKED: 2026-11-03
DECISION: EXPLORE
SEARCH_EVIDENCE: Step 187 searched singularity transfer/Pringsheim, exact triangular-product generating functions, rational diagonals, Cauchy parameter integrals and Lindelof/Rice representations; inspected the primary statements and proof cases below and compared the saved step-174 assessment and local signed-bump failures. No matching theorem or previously established exact size representation was found; no novelty inference follows.
SOURCE_EVIDENCE: Flajolet--Sedgewick (1995), Lemma 1, Section 2, pp.104--105 and Theorems 1--2, pp.105,110--111; Flajolet--Gerhold--Salvy arXiv:0906.1957v2 Theorem 2 and proof pp.5--6, Lemma 1 p.7; Flajolet--Odlyzko (1990) Theorem 1 pp.220--222 and Corollaries 1--3 pp.223--225; Flajolet--Sedgewick May 2004 draft Theorem IV.3 pp.15--16; Bostan--Lairez--Salvy arXiv:1510.07487v2 Definition 1.1 p.7 and Theorems 2.2/3.5 pp.11,17. Direct links and reading limits below.
COMPARISON: Transfer and boundary-singularity theorems do not locate this sequence's singularity; Pringsheim needs coefficient positivity, and rational-diagonal machinery needs a missing binomial-sum representation. Rice's finite-sum contour and Lindelof's size-interpolation integral identify a concrete representation test, with unproved moving-product, contour and growth hypotheses; neither supplies a signed rate or finite singularity.
GAP: Construct an exact size representation for K_(12q+3) retaining the growing product, resolvent and fixed real bump, and identify a genuine nonremovable singularity inside exp(-12*r_P); all exchanges, branch choices and same-singularity cancellation must be proved. No such representation or singularity is established by this review.
REASON: Essential tool comparison is sufficient for one bounded Rice/Lindelof representation-and-singularity attempt under EXPLORE, subject to the supervisor's separate approval of this changed assessment; this approves investigation of the named applicability gaps, not their truth. Generic root-test and positivity shortcuts are parked. No new lemma, mathematical script or specialization is derived here.
LITERATURE_REASON: The saved REVIEW_REQUIRED nomination introduces a family-size singularity mechanism outside the ready physical-variable saddle/Gevrey scope; the new primary Rice/Lindelof comparison supplies a concrete test rather than repeating that assessment.
SCOPE: Only TARGET for the original fixed L703 profile and L714 sequence at u=(3+4i)/10, n=12q+3, q>=1; one exact coefficient-index contour/size-interpolation test is covered. No replacement bump, n-dependent width, positive K_n coefficients, endpoint law, analytic extension of chi, asserted singularity or promotion of L717 to an audited input is allowed.

## Preserved nomination and threshold

The nomination below describes the intended observable, not an established
representation. Its original literature-only instruction is discharged by
this source review. The completed comparison and bounded test follow it.

## Exact proposed object and decision threshold

Use the ordinary generating function

    mathcal K(z)=sum_(q>=1) K_(12q+3)*z^q,
    K_n=(D_n/h)*sum_(j=0)^(n-1)
                    b_(n,j)*B_n(d+u*j/n)/(d+c_0+u*j/n),
    B_n(a)=integral_I chi(v)*exp(-n*a*v/A)dv.

All symbols are exactly those of L714. Its equivalent integral
through H_n and Q_n is available, but their known logarithmic
limits do not constitute a relative asymptotic after integration.
The generating-function mechanism must handle the actual coefficients,
not a model sequence obtained by replacing H_n with exp(nF).

The intended comparison is with the actual P_n, whose proposed rate
is L714 (6),

    r_P=integral_0^1 log|Q_t(u,i/8)|dt+v_+/(8A).

That elementary rate argument has not received its separate audit;
its positivity/support and Riemann-sum hypotheses must be checked
before relying on it. L713's numerical envelope is also unaudited
and is not an assumed threshold. A primary radius/limsup theorem
and a certified singularity inside exp(-12*r_P) would be relevant;
merely invoking the root test without locating a singularity would
restate the original question. Possible zero subsequences are allowed.
No radius, convergence domain or singularity is established here.

## Source-only continuation and abandonment test

Retrieve exact primary hypotheses and the relevant proof cases for
analytic continuation of parameter-integrated generating functions,
nonremovable singularities and signed coefficient growth. Compare
the n-dependent product, the restriction n=12q+3, and the fixed
nonnegative but nonanalytic bump explicitly. Pringsheim-type inputs
requiring nonnegative generating coefficients cannot be presumed
applicable merely because chi>=0. Preserve possible contributions
and cancellations at the same singularity and all array errors.

Continue toward a later bounded creative attempt only if the review
identifies a concrete representation or singularity test not equivalent
to the unresolved signed-rate claim. Stop this proposal if the only
available statement assumes the desired noncancellation or requires
an unproved endpoint law. Do not derive the missing representation
and approve it during the literature turn. Existing local sources
are inputs for comparison; no exact duplicate was found in the
bounded local search, which is not a novelty conclusion.

Essential local inputs are L714--L716 and L703's unchanged bump;
L717 is new unaudited obstruction evidence, not a theorem that may
be silently promoted to an audited premise. L713 defines the original
P_n/R_n comparison; its full-family estimates remain separate. The
main gap is actual-Xi mixed positivity. A subsequential signed
comparison would change the boundary-peak test, while complementary
Jensen defect, other response terms, angular persistence, amplitude/
full charge, H/support and Xi realization remain unresolved. Full
matching Mathlib coverage is not checked.

## Completed source comparison — step 187, 3 November 2026

This is LITERATURE / NOVELTY_UNCHECKED / EXPLORATION. The review has
identified tools and a bounded representation test, not a singularity,
rate, theorem specialization or mathematical obstruction to this profile.
The target remains the exact saved TARGET, rather than a model sequence.

### Local evidence and bounded search

Read L703's profile hypotheses, L713's definitions and complete-response
interface, L714's exact finite reduction and Section 4, and the hypotheses
and conclusions of L715--L716. Reused the step-174 source comparison;
read the common-phase attempt record and step-186 history. A targeted
search of the signed-bump, polynomial-log and resolvent assessments and
signed-bump attempt records found no Rice/Lindelof assessment. This is a
bounded duplicate check, not an assertion about the entire literature.

The absolute horizontal envelope, positive blend and common-phase
failures retain their original scope. L717 remains unaudited. The new
proposal sums in the family-size variable and cannot use those failures
to infer either cancellation or noncancellation of K_n. L714 (6) remains
unaudited; this review read its proof to identify its hypotheses, and did
not critically verify or promote it. The actual support supremum v_+,
not a stipulated endpoint law, appears in the intended threshold.

Search queries included:

- `Flajolet Sedgewick analytic combinatorics nonnegative coefficients Pringsheim singularity transfer theorem parameter integrals pdf`
- `generating function products binomial n j n Lagrange inversion diagonal hypergeometric integral singularity cancellation`
- `parameter integral singularities Cauchy transform smooth density analytic continuation Plemelj theorem primary pdf`
- `generating functions triangular arrays products n dependent nonremovable singularity signed Laplace integrals`
- `"generating function" "triangular array" "singularities" products`
- `"Lindelof" "generating functions" "Gamma" Flajolet Gerhold Salvy`
- `Flajolet Sedgewick Mellin transforms asymptotics finite differences Rice integrals 1995 pdf`

Primary statements and the relevant proof cases were retrieved before
expanding source ranges. The full 2009 book was inaccessible through the
available web reader (403/size restriction), and direct shell retrieval
had a DNS failure. The accessible author-hosted 2004 draft supplies the
boundary theorem below; its theorem numbering is explicitly versioned.
No essential source remains blocked for this bounded test. Search leads
about Ising diagonals and explicit endpoint saddle laws were not inspected
or imported. No API or authentication key was used.

### Boundary and transfer theorems: conditional tools, not a locator

P. Flajolet and R. Sedgewick, *Analytic Combinatorics — Complex
Asymptotics*, zeroth edition, 8 May 2004,
[Theorem IV.3 and proof, printed pp.15--16](https://algo.inria.fr/flajolet/Publications/ch4567.pdf#page=23)
(PDF pp.23--24), were read. A finite Taylor radius has a boundary
singularity; nonnegative Taylor coefficients additionally force one at
the positive radius. The proof's rearrangement uses positivity.
Neither clause provides the radius of the present unknown signed
sequence. Here chi>=0 is an assumption about an integration weight,
not established positivity of K_(12q+3). No such inference is approved.
This is the 2004 numbering, not a claimed inspection of the 2009 book.

P. Flajolet and A. Odlyzko, *Singularity analysis of generating
functions*, SIAM J. Discrete Math. **3** (1990), 216--240,
[Theorem 1, pp.220--222, and Corollaries 1--3, pp.223--225](https://algo.inria.fr/flajolet/Publications/FlOd90b.pdf#page=5),
were inspected, including the small circle, slanted segments, outer
circle and little-o splitting in the proofs. Theorem 1 assumes
analyticity in an indented disk about the sole exceptional point 1,
with opening parameter strictly between 0 and pi/2, and a local
O(|1-z|^a) bound for real a; its coefficient bound is O(n^(-a-1)).
Corollary 2 transfers an asymptotic K*(1-z)^a when a is not a
nonnegative integer; the integer case only gives a little-o conclusion.
These tools require a known germ, continuation domain and local
expansion. None has been supplied for the exact size series. For the
weaker limsup target a located nonremovable singularity would suffice;
a full transfer expansion is unnecessary and is not a new requirement.

### A concrete representation test: finite differences, then size interpolation

P. Flajolet and R. Sedgewick, *Mellin transforms and asymptotics: Finite
differences and Rice's integrals*, Theoret. Comput. Sci. **144** (1995),
101--124, [Section 2, Lemma 1 and its residue proof, pp.104--105](https://algo.inria.fr/flajolet/Publications/FlSe95.pdf#page=4),
were inspected. The finite-difference contour must lie in the analytic
domain, encircle the retained integer interval and exclude omitted
integers. The same section gives gamma/beta forms of the kernel.
Its unbounded-contour alternative needs polynomial growth of degree r
and difference order exceeding r+1. Theorems 1--2 and their contour
proofs, pp.105,110--111, require the stated rational/meromorphic and
growth hypotheses. They do not give uniform asymptotics for a growing
coefficient function. L714 has an alternating factorial sum, but also
a degree-n-1 product, moving resolvent and complex exponential. A finite
Rice contour is therefore a concrete representation template to test;
closing it at infinity or applying fixed-function asymptotics is not
justified. No specialization formula is derived in this review.

P. Flajolet, S. Gerhold and B. Salvy, *Lindelof representations and
(non-)holonomic sequences*, [arXiv:0906.1957v2](https://arxiv.org/pdf/0906.1957v2#page=5),
17 December 2009, Theorem 2 and all three proof stages, pp.5--6,
and Lemma 1 with proof, p.7, were inspected. For phi analytic in Re(s)>0
and |phi(s)|<=C*exp(a_*|s|) in Re(s)>=1/2, with 0<a_*<pi, the
series sum_(m>=1)phi(m)*(-z)^m has the stated vertical-line integral
and continuation to |arg z|<pi-a_*. Horizontal decay, the right edge
and sector convergence are separate checks. Lemma 1, under extra
left-half-plane meromorphy and growth, concerns asymptotics at infinity,
not the location of a finite size singularity. Here an exact interpolation
of K_(12q+3), its growth and a finite singularity are all missing.
The factor 12 cannot be ignored in an interpolation's vertical growth.
These are applicability tests, not assumptions or a claim that the
Lindelof theorem forces the desired singularity.

### Alternative exact-representation and parameter-integral comparisons

A. Bostan, P. Lairez and B. Salvy, *Multiple binomial sums*,
[arXiv:1510.07487v2](https://arxiv.org/pdf/1510.07487v2), 15 June 2016,
Definition 1.1, p.7, Theorem 2.2 and its closure proof, p.11, and
Theorem 3.5, p.17, were inspected. The binomial-sum algebra over a
characteristic-zero field is generated by delta, geometric and binomial
sequences, with algebra operations, affine index changes and partial
summation. Its rational constant-term/diagonal representations require
membership in that algebra. L714's variable-length product, division
and arbitrary bump integral have no supplied membership proof. The
presence of factorials or binomial weights alone does not supply one.
The affine restriction n=12q+3 would be permissible only after the
underlying membership had been verified. No exclusion from that algebra
is proved here; this is an unmet hypothesis, so rational-diagonal
singularity algorithms are not imported for K_n. The converse proof
of Theorem 3.5 was not needed or used.

As a supplementary parameter-integral caution, O. Costin's author-hosted
[complex-analysis notes, Sections 39.4.1--39.4.5, pp.82--83](https://people.math.osu.edu/costin.9/805/c10.pdf#page=82),
were read. These examples distinguish sectionally analytic Cauchy
integrals and exhibit a nonzero jump on a segment whose interior points
are nevertheless regular for continued branches of the logarithm.
A jump between two prescribed boundary branches is not, by itself,
a nonremovable singularity of the Taylor germ. These notes are
supplementary exposition, not a matching theorem imported for K_n.
A PMC lead on unrestricted Plemelj formulas was access-blocked and is
not used. No representation of the present array as a Cauchy transform
has been established, and chi's nonanalyticity alone supplies none.

### Bounded research test and decision

EXPLORE covers one attempt at the following representation test within
TARGET; it does not approve a new representation as proved. Start with
the exact finite L714 coefficient sum, retaining D_n/h, the resolvent
and the bump integral. Test the source Rice contour in the coefficient
index, then whether its gamma/beta kernel and the remaining product
permit an analytic interpolation in the size index q with a controlled
contour. Keep the bump variable real throughout. Recover the exact
integer coefficients before invoking any size summation or continuation.
The purpose is an integral or functional representation whose finite
analytic obstructions can be examined, rather than defining a radius
by the unknown coefficient limsup.

Evidence justifying continuation would be an exact representation with
proved convergence/interchanges on a nonempty size domain and an
explicit candidate obstruction whose removability can be tested
independently. A representation alone would be an intermediate result,
not the requested rate. Any claimed singularity must belong to the
Taylor germ on its disk of convergence, survive integration and
same-point cancellation, and lie at modulus strictly less than
exp(-12*r_P). L714 (6) needs its outstanding audit before that comparison
can be claimed. Zero subsequences and log(0)=-infinity remain allowed.

Stop this particular Rice/Lindelof test if the moving contour/product
cannot be controlled in one bounded attempt, if only a formal integer
identity or an arbitrary interpolation is obtained, or if the singularity
claim merely renames the unknown rate or assumes endpoint/noncancellation
information. A proven obstruction to the needed representation would
also be informative. Failure of this template would not refute every
possible size-generating-function method; reopening would require a
materially different, independently testable representation. Do not
continue with pointwise F/Q_n refinements or more generic transfer
browsing without a new mathematical input.

The actual-Xi mixed-positivity gap, complementary Jensen defect, other
complete-response terms, angular persistence, amplitude/full charge,
H/support and realization remain independent. Full matching Mathlib
coverage was not checked; no absence claim is made. The next assessment
uses the exact unchanged TARGET text above. Its new EXPLORE decision
is saved for separate supervisor approval; no research attempt has
been performed during this literature-only invocation.
