# Longer arithmetic dictionary: completed source comparison

TARGET: Assess source coverage for testing whether L637's normalized bump has squared projection o(1), uniformly for T<=X<=2T, onto span_C{Z(t)n^(-it):1<=n<=floor(T^(1/5))}, using L737's full moment form and L926's subpower conditioning.
CHECKED: 2026-11-09
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the November4 BCR/weight assessment and step261 audit, the completed endpoint comparison and L926 audit, and both recorded arithmetic stops; new exact projection/localization and BCR searches are listed below. No inspected theorem states the exact fixed-Z projection result at the changed length.
SOURCE_EVIDENCE: Reopened https://arxiv.org/pdf/1411.7764v1 Theorem1 pp1-2, Section3.2 Cases2-3 pp14-15 and Section3.3 p16; https://rstation.ai/problems/riemann_hypothesis/papers/41/v3 Theorems2/2a, Section5(19)-(27) and Section9(64)-(65); https://dlmf.nist.gov/25.10#E3 equations25.10.1-3 and remainder. Earlier diagonal/zero-frequency proof reads are reused explicitly below.
COMPARISON: BCR's arbitrary-coefficient theorem covers the changed length after normalization and comparable smooth windows; L737 supplies the full finite logarithmic form and local numerator, and audited L926 supplies subpower conditioning for every natural prefix. Paper41 has a related concentration/projection theorem at growing proportional orders, whose hypotheses exclude the fixed Z dictionary; its endpoint inverse claim is already reproduced in L926.
GAP: The uniform longer-length projection conclusion remains unproved. A later specialization must charge coefficient normalization in the moment error and compare that error and the local numerator against the full logarithmic margin using L926; no new moment theorem or new finite inequality is needed as an assessed source input.
REASON: Essential analytic source coverage is now available for one bounded changed-length test. This literature-only step supplies source comparison, not a derived projection estimate; the separately saved ready continuation requires next-turn approval.
SCOPE: Exact fixed L637 w,u0,psi,g and actual Hardy Z; T<=X<=2T; n<=floor(T^(1/5)); arbitrary complex coefficient vectors varying with T,X; complete gcd/log moment form. No RH, nonvanishing, diagonal dominance, microscopic moment theorem, signed transfer or Xi positivity is presumed.

## Invocation-start nomination, preserved

The following nomination described the earlier missing coverage. Its
requests for assessment are discharged only to the extent specified in
the completed comparison below; its proposed estimate is still unproved.

The main gap remains L030-L032/C032a actual-Xi all-degree mixed
positivity. The proposed diagnostic asks how far an actual arithmetic
dictionary can realize the fixed microscopic bump. A uniform vanishing
projection would extend a concrete realization obstruction; it would
not prove RH or rule out other observers or dictionaries. A rigorous
nonvanishing sequence could instead justify a different realization
test. Neither possibility has been calculated in this audit turn.

Compare three continuations. Repeating finite conditioning review has
no unpaid finite step after L926's audit. Increasing the signed dyadic
pilot repeats step226's absence of a scalable negative pattern and
cannot certify full spectra. The changed-length moment/projection test
has the materially new L926 input and a specific finite exponent and
uniform observable, so select it for source assessment. Preserve both
old stops. A genuinely new central creative mechanism has not been
identified: the missing actual-theta or signed-realization relation is
still the blocker, rather than a reason to relabel this specialization.

Read the exact BCR theorem and applicable coefficient/weight proof
cases for this changed length before larger passages. Reuse the
previous primary-source assessments where their hypotheses match.
Compare manuscript Section5's actual analytic conclusions, not only
the inverse estimate, and search for stronger known localization or
projection statements. The November4 assessment explicitly excluded
longer lengths, so it is not a ready gate here. The October21 baseline
and external-input register were read for this nomination; no zero-free
input is proposed or needed, and no cross-notebook input is involved.

Essential prospective input is L737's full moment specialization and
local numerator under L637's hypotheses, with audited L926 replacing
the crude finite coefficient loss. The moment theorem at this new
length and enough positive full-form margin are unresolved application
assumptions, not conclusions. L925 is not required for the nomination.
Full matching Mathlib coverage remains unchecked.

Continue only after exact sources justify a coefficient-uniform
application with a discriminating projection bound at this fixed length.
If the necessary hypotheses or margin/error comparison are uncovered,
keep REVIEW_REQUIRED or park the failed application with its precise
obstruction. Do not silently shorten the length or expand a numerical
grid. Save a separate ready mathematical target only after the source
comparison, for later approval; this nomination approves no mathematics.

## Completed comparison — 9 November 2026

This is one LITERATURE / EXPLORATION / NOVELTY_UNCHECKED step. It makes
no new mathematical assertion about the longer projection. The source
gate changes from REVIEW_REQUIRED to SPECIALIZE; the unresolved analytic
comparison is the purpose of the later test, not an assumed input.

### Local reuse and failure checks

Read L637's precise hypotheses and fixed bump; L737's full proof including
its separate step261 conceptual audit; L926's hypotheses, conclusion and
import qualifications. Reused the completed November4 multiplier source
assessment and the November9 endpoint comparison, including its exact
paper41 overlap discussion. The scalar divisor/totient/Schur sources and
the finite inverse proof have unchanged hypotheses and need no further
audit in this turn. Full matching Mathlib coverage remains unchecked.

The November4 short-dictionary stop concerns only T^(1/10); it is not
a theorem at all lengths. The conditioning approval-loop note closes
further unchanged finite reviews, not the use of L926. Step226's positive
dyadic Rayleigh trials give neither a full spectral bound nor a scalable
negative family; that numerical route remains parked. None is evidence
against the present longer-length diagnostic. No cross-notebook input
was consulted. L925 is not an input.

### Exact primary moment hypotheses and proof cases

S. Bettin, V. Chandee and M. Radziwill, *The mean square of the product of
the Riemann zeta-function with Dirichlet polynomials*, J. reine angew.
Math. 729 (2017), 51–79, DOI 10.1515/crelle-2014-0133;
[arXiv:1411.7764v1](https://arxiv.org/pdf/1411.7764v1), manuscript dated
1 December 2014, Theorem1, printed pp1–2. Reopened the theorem and
Section3.2 Cases2–3, pp14–15, and Section3.3, p16. Reuse the earlier
inspected Section3.1 diagonal and Section3.2 Case1 residue computation
recorded in the November4 assessment; do not reprove their arithmetic.

For a fixed smooth phi supported in [1,2], Y tending to infinity,
M=Y^theta, theta<17/33, and
A(s)=sum_(n<=M) a_n n^(-s) with a_n <<_eta n^eta, the theorem states

    integral |zeta(1/2+it) A(1/2+it)|^2 phi(t/Y) dt
      = sum_(d,e<=M) a_d conjugate(a_e)/lcm(d,e)
          * integral [log(t*gcd(d,e)^2/(2*pi*d*e))+2*gamma]
                       phi(t/Y) dt
        + O_(eta,phi)(Y^(3/20+eta) M^(33/20)+Y^(1/3+eta)).

Here eta>0 is fixed and the implied coefficient-bound constant matters.
The needed length T^(1/5) is inside the stated range. A fixed source
exponent theta=1/4 permits zero padding at each of L737's comparable
scales Y_j=alpha_j T once T is large. This is a hypothesis comparison,
not a claimed new remainder or projection bound. A later calculation
must use the padded cutoff in the displayed source remainder and must
not substitute the physical length there without justification.

Reuse L737's nonnegative three-window partition and weight family
phi_(j,x)(v)=rho_j(alpha_j v)w(alpha_j v-x), x=X/T in [1,2]. Its
supports remain in a fixed compact subset of (1,2), and its derivative
and Mellin seminorms are uniformly bounded. The changed dictionary
length does not change this family. The reopened Case2 integrates by
parts in the weight, Case3 separates it by its Mellin transform before
Proposition1/(3.7), and Section3.3 uses the same high-frequency argument.
These are the weight operations checked by step261; no compact-family
uniformity is inferred merely from a pointwise big-O statement.

For arbitrary nonzero complex c, reuse the normalized source coefficients
a_n=sqrt(n)c_n/B, B=max_(n<=N)sqrt(n)|c_n|, with zeros thereafter.
Their bound is 1 independently of phases, sparsity and T,X. Restore B^2
in both main and error terms. L737 already proves B^2<=N||c||_2^2 and
identifies the resulting full form (5), retaining 2*gamma and both
coefficient logarithms. Its finite identity and bound (6)–(10) are
available at any finite natural prefix; its analytic conclusion remains
only the original short-length theorem. No entrywise error is promoted
to a quadratic-form estimate, and the zero coefficient vector is separate.

The later task must test the available margin A_t-4log N against this
charged error, with Q(c) controlled by L926 for a fixed positive epsilon.
It must then compare the existing local numerator L737(14), whose proof
uses no length restriction, to the resulting actual norm lower bound.
This review does not evaluate those competing exponents, choose new
constants, prove the margin, or assert a vanishing ratio.

### Known overlap: finite conditioning and analytic concentration

bramble_trace, *Generalized Laguerre positivity at growing orders*,
[v3, 23 October2026](https://rstation.ai/problems/riemann_hypothesis/papers/41/v3).
Read Theorems2 and2a with their parameter restrictions, Section5
(19)–(27) including the full Lemma5 proof, and Section9 (64)–(65) with
its projection paragraph and coefficient-cost qualification.

Lemma5 includes real shift zero and its finite inverse claim is exactly
the overlap reproduced in L926; there is no new finite estimate here.
Lemma4 and (26) instead require a fixed strictly positive lower shift.
Their constants do not authorize endpoint passage. No shifted extension
or new audit of that manuscript is needed for this target.

Section9 explicitly bounds concentration and then projection for its
Laguerre-weighted arithmetic observer space. That is relevant prior
localization work and must not be described as absent. Its Theorem2
assumes fixed 0<alpha<1/2 and odd m=2p+1 with m/log T tending to alpha;
Theorem2a likewise assumes a positive proportional-order ratio. These
hypotheses exclude fixed p=0. Its measure is |Q_n(t)|omega(t)dt for the
specified growing Laguerre order, whereas the present norm is w_XT dt
with generators Z(t)n^(-it). No uniformity as alpha tends to zero or
fixed-order projection theorem is stated. Thus (65) is not a direct
import for this exact target. This comparison justifies specialization
of classical BCR and the audited local bounds rather than reproof of
the manuscript's growing-order argument.

### Real-axis input and bounded discovery

Reopened [DLMF25.10](https://dlmf.nist.gov/25.10#E3), version1.2.8,
release15 September2026, (25.10.1)–(25.10.3) and the following
O(t^(-1/4)) remainder paragraph. The cited source is Titchmarsh,
revised Heath-Brown, 2nd ed. (1986), Section4.17, p89, (4.17.4).
This is the undifferentiated real-axis formula with its floor cutoff,
not a derivative estimate or a complex-strip estimate. It matches the
input used for L737's numerator. No stronger zeta bound is required as
an essential source for the bounded test.

New queries actually issued in this step:

- `"zeta" "Dirichlet polynomials" "bump" projection localized`
- `"Hardy" "projection" "Dirichlet" localization`
- `"mean square of the product" "arbitrary" "coefficients" Bettin Chandee Radziwill`
- `"zeta" "Christoffel" "Dirichlet polynomials"`
- `"zeta" "localization" "arithmetic" "projection"`
- `"mean square of the product of the Riemann" Bettin Chandee Radziwill theorem`

Search results predominantly concerned abstract Hardy spaces, different
Dirichlet norms and unrelated projections. They supplied no inspected
matching fixed-bump theorem. The BCR author PDF and arXiv record were
returned; the exact v1 theorem above was the primary input actually read.
The critical-strip mean-square paper arXiv:2312.10614 was an unread lead
about a different real-part range, not an imported theorem. Search
snippets, unrelated RH claims and secondary summaries are not evidence
for the needed statement. Failure to find a match is no novelty claim.

### Continuation and bounded decision

No essential source is blocked. Save the exact mathematical target in
drafts/literature/2026-11-09-longer-arithmetic-dictionary-test.md for
separate next-turn approval. The later attempt must keep N=floor(T^(1/5)),
all fixed bump/weight hypotheses and arbitrary moving complex vectors.
Continue only with a coefficient-uniform o(1) projection bound or a
rigorous nonvanishing sequence; an inconclusive envelope requires naming
the precise unpaid inequality and stopping this application mechanism.
Do not shorten N or enlarge the stopped numerical pilot.

The potential downstream use is an extended realization obstruction,
not a mixed-sign or RH proof. Actual-Xi all-degree mixed positivity,
signed transfer and other dictionaries remain independent open gaps.
This is established-route specialization, not a new central creative
mechanism. No concrete actual-theta/signed-realization mechanism has
been identified that justifies a creative nomination now. No lemma,
mathematical script, PROOF argument or DAG edge was changed.
