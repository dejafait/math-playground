# Vanishing-amplitude coefficient saddle: completed source comparison

TARGET: Assess saddle-point asymptotics with a vanishing polynomial amplitude for the actual-Xi coefficient near a hypothetical off-line zero quartet, retaining fixed multiplicity and identifying the exact deflated-amplitude and complementary-arc bounds needed for a signed leading term.
CHECKED: 2026-10-31
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched saddle-point vanishing amplitudes/polynomial zeros, stronger parameter-uniform expansions, exact zeta/Xi deflation, and the Flajolet--Sedgewick note/errata; read the primary statements and proof cases below. Reused L463's source audit and compared the scoped endpoint, small-displacement and Hermite failures. No matching actual-Xi signed transition was located; this is not a novelty claim.
SOURCE_EVIDENCE: O'Sullivan arXiv:1702.03777v2 (30 March 2018), Assumptions 1.1, Theorem 1.2/(1.6)--(1.7), Proposition 1.3/(1.12), Section 4/(4.1)--(4.6), Corollary 5.1 and proof, Theorem 6.1/(6.4)--(6.5); DLMF 2.4(iii)--(iv)/(2.4.11)--(2.4.16); Temme 1308.1547v1 Section 4/4.1/(4.1)--(4.5); Flajolet--Sedgewick online book dated 3 October 2008, pp.586--589, Proposition VIII.7/Theorem VIII.8/proof/Note VIII.37, and p.603 Note VIII.48; bramble_trace paper 41 displayed v4 Section 4.5/(18i)--(18n).
COMPARISON: Known complete saddle expansions allow amplitude zeros and fixed multiplicity, with an absolute supremum-dependent error; this component needs citation, not invention. Their hypotheses do not supply a uniform Xi amplitude norm, a nonzero signed first term, or a smaller full-contour error at d<=3/8. A separately testable coefficient formula in Note VIII.37 needs an applicability/arithmetic audit before use.
GAP: Actual-Xi quotient/jet bounds and complementary-contour saving remain unproved; fixed-data expansions do not automatically cover height-dependent phases. No signed Xi transition is imported or approved. The newly nominated exact-model source audit is independent of those Xi estimates.
REASON: Complete the source gate by identifying the known amplitude-zero tools and the precise unfilled Xi obligations; park the unsupported signed application and nominate one bounded source-formula check, not another abstract expansion or existential witness.
LITERATURE_REASON: The amplitude-zero and moving-height scope was absent from L463's nonvanishing-saddle assessment; exact primary theorem/error coverage was essential. Previously ready L463 and local-factorization coverage was reused.
SCOPE: Literature-only comparison for a fixed hypothetical quartet +/-gamma +/- i d, gamma tending to infinity, fixed 0<d<=3/8 and arbitrary fixed multiplicity m>=1. SPECIALIZE describes known tools covering part of the target, not approval of a Xi sign theorem or new mathematics. No simplicity, isolation, separation, quotient nonvanishing or low-order sign is assumed.

## Completed comparison and decision

The main gap is actual-Xi initial signs at unbounded heights, ultimately
all-degree mixed positivity. The intermediate target was a sign-resolving
coefficient expansion at a quartet/saddle encounter. Its downstream use
would be exceptional-height information below L463's positive tail;
other heights, indices and effective overlap remain independent gaps.
The admission test was a specified nonzero signed term with smaller
local and complementary-contour errors. It has **not** passed for Xi.
This literature step is EXPLORATION / NOVELTY_UNCHECKED, with no lemma,
transition formula, mathematical script or mathematical negative result.

### Primary theorem hypotheses and relevant proof cases

Cormac O'Sullivan, *Revisiting the saddle-point method of Perron*,
[arXiv:1702.03777v2, 30 March 2018](https://arxiv.org/html/1702.03777v2),
Assumptions 1.1, considers a bounded piecewise continuously differentiable
contour C through z0, a neighborhood B, and p,q holomorphic on a domain
containing B union C. The phase is nonconstant, with
p(z)=p(z0)-p0(z-z0)^mu(1-phi(z)), mu a positive integer, p0 nonzero,
phi holomorphic and phi(z0)=0. The geometric data, phase and amplitude
are independent of the large positive parameter N; K_q bounds |q| on
B union C. Theorem 1.2 requires strict decrease of Re p away from z0
along the outgoing contour. Its expansion (1.6), coefficients (1.7)
and Proposition 1.3 have errors explicitly independent of q apart from
K_q. No q(z0)!=0 hypothesis is imposed.

For an interior saddle with opposite incoming/outgoing sectors and even
mu, Corollary 5.1 and its proof retain only the even coefficients
alpha_(2j). Its remainder after M terms is
exp(N p(z0)) O(K_q N^(-(2M+1)/mu)); this is an absolute estimate.
Theorem 6.1 also explicitly treats a factor (z-z0)^(a-1), Re a>0,
with the prescribed continuous branch and outgoing sector. Thus fixed
integer vanishing orders are covered. The q-independent error constant
does not mean independence from a changing phase, neighborhood or
contour. Nor does K_q alone ensure relative accuracy when the displayed
terms vanish or cancel. These are source statements, not Xi estimates.

Inspected the relevant localization proof (2.8): its exponential error
uses a positive real-phase gap on the complementary compact path.
Inspected the alternative proof (4.1)--(4.6): it selects a local inverse
of the phase coordinate, avoids other zeros of p', shrinks a domain,
and uses a Cauchy remainder bounded by K_q. Read the opposite-sector
cancellation proof of Corollary 5.1 and the polynomial-factor proof
case following Theorem 6.1. These cases explain exactly which fixed
domain/gap/phase controls would need uniform replacements for Xi.
No uniform replacement is derived here.

[DLMF 2.4(iii)--(iv)](https://dlmf.nist.gov/2.4#iii), accessed
31 October 2026, hypotheses (a)--(c) and (2.4.11)--(2.4.16), permits
an amplitude expansion with exponent lambda-1, Re lambda>0. It requires
analytic data, appropriate continuous branches, endpoint convergence
and a strict real-phase gap, uniformly over its stated angular sector.
The interior-saddle case splits two half-paths and chooses their
fractional-power branches separately. This does not prohibit amplitude
zeros, and is not a height-uniform theorem for a deflated Xi quotient.

N. M. Temme, *Uniform Asymptotic Methods for Integrals*,
[arXiv:1308.1547v1, 7 August 2013](https://arxiv.org/html/1308.1547v1),
Section 4/(4.1) warns about parameter-dependent phases/amplitudes and
domains. Section 4.1/(4.2)--(4.5) separates a pole near a Gaussian
saddle. That pole case is not a polynomial amplitude zero. Coalescing
stationary points likewise differ from a zero at a simple stationary
point. Neither is imported as the missing signed Xi theorem.

Philippe Flajolet and Robert Sedgewick, *Analytic Combinatorics*,
[author-hosted online book](https://ac.cs.princeton.edu/home/AC.pdf#page=600),
PDF running date 3 October 2008, printed pp.586--589: read conditions
L1--L3, Proposition VIII.7, Theorem VIII.8 and its circle/tail proof,
then the relaxation to signed multipliers and Note VIII.37. The
large-powers theorem fixes A,B, initially with nonnegative coefficients,
B(0)!=0, aperiodic B and the stated analytic radii, and fixes the
degree/power ratio in a compact subinterval of its spread. Note VIII.37
explicitly discusses A(zeta)=0, A'(zeta)!=0. It is a concrete source
lead for cancellation, not an arbitrary-multiplicity moving-Xi theorem.
Its short displayed coefficient formula is **unverified here**. It
needs checking against exact coefficients and the phase-dependent
general expansion before any signed import. No error is asserted or
counterexample calculated in this literature turn. Note VIII.48,
p.603, also discusses exact vanishing multipliers at a saddle; it
does not supply Xi bounds.

### Actual-Xi obligations and duplicate comparison

L018 supplies the entire Xi function and its symmetries. L463 fixes
H_a(y)=Xi(a+iy)Xi(a-iy) and the positive b(a)^2 normalization. The
primary [bramble_trace paper 41](https://rstation.ai/problems/riemann_hypothesis/papers/41)
still displays v4, 24 October 2026 07:18 UTC. Its (18k) explicitly
uses nonzero factors on a fixed neighborhood in Re y>3/8; (18j)
and (18n) supply the complementary bound and saving there. Reuse
L463's completed analytic audit, without repeating it or auditing the
retained external zero-free manuscript. The strict boundary and its
trust qualifications remain unchanged. No new zero-free result is
proposed, so the parked-envelope baseline is not being reopened.

For the nominated fixed quartet, exact finite deflation is meaningful
with the full specified multiplicity. It does not remove other nearby
zeros. A logarithm of the remaining factor on a common neighborhood
would therefore require an additional nonvanishing statement, and
uniform logarithmic derivatives would require quantitative bounds.
Keeping that factor inside the amplitude avoids the logarithm
requirement of the abstract theorem, but still requires its supremum,
enough jets to identify a first nonzero signed term, and an error
strictly smaller than that term, together with the entire contour
comparison. Uniform phase curvature/domains cannot be inferred from
the fixed-data theorem. No such Xi estimates were found in the sources
checked. These are missing application inputs, not a nonexistence
theorem for the desired estimates.

L461's negative-witness existence and L462's fixed-anchor tail do not
resolve this local profile. The September 24 endpoint moving-saddle
failure uses another integral and older derivative envelopes; it is
not a global ban. The October 28 small-displacement review and L474's
finite-Blaschke proof control an aggregated positive quotient norm on
microscopic disks, not a signed fixed-d coefficient at every height.
The October 31 zero-preserving Hermite review requires different node
data. Their recorded failures remain; none is counted as new evidence.
No cross-notebook input was read. Full matching Mathlib coverage is
unchecked, not absent.

### Search, access and continuation

Queries included `saddle point method vanishing amplitude uniform
asymptotic expansion polynomial zero saddle`, `Wong asymptotic
approximations integrals saddle point vanishing amplitude zeros Hermite
polynomial`, `Cormac O Sullivan asymptotics saddle point method
holomorphic q zero uniform error theorem 2017`, `saddle point vanishing
amplitude uniform parameter zero amplitude asymptotic expansion Wojdylo`,
`"zeta" "saddle point" "vanishing" amplitude`, `"Riemann xi"
"deflated" saddle`, and the exact VIII.37/errata queries. Exact Xi
searches did not locate a matching theorem. Search snippets were used
as leads only. The O'Sullivan v2 primary HTML and the cited book text
were accessible. The guessed O'Sullivan author-PDF address failed;
it is not an essential blocker because the primary full text was read.
The book's web-extracted math can confuse xi/zeta glyphs: no formula
depending on that ambiguity is imported. PDF screenshots returned 403,
and shell download failed DNS; no visual verification is claimed.

Inspected the author's linked [June 6, 2010 errata PDF](https://algo.inria.fr/flajolet/Publications/AnaCombi/errata.pdf)
by searches for pp.588--589/VIII.37 and the relevant book section;
no matching entry was found. The separate Princeton errata search
rendering was only an access lead after the direct page returned 403.
No assertion of exhaustive errata coverage follows. The older 2005
book drafts and Wong/Olver/Wojdylo originals remain unread leads;
O'Sullivan's explicit statement/proof suffices for the nominated check.

Park the actual-Xi signed transition until the listed application
inputs are available. Do not spend the next turn rederiving an abstract
amplitude-zero expansion or L461's witness. A newly prepared, separately
approvable [exact-model source audit](2026-10-31-vanishing-multiplier-formula-audit.md)
tests Note VIII.37 at a fixed elementary multiplier. This is independent
of unknown Xi quotient bounds and directly checks a proposed source
input. A creative Xi mechanism is not yet justified: the missing
uniform bounds and signed term remain central obstructions. No generic
model is being substituted for actual Xi, and no candidate is claimed.

## Original nomination (pre-review state)

The paragraphs below preserve the initial scope and admission test;
their references to uninspected sources describe the nomination, not
the completed source comparison above.

The main gap is actual-Xi low-order signs at unbounded heights. The
intermediate question is whether a polynomial zero can be retained in
the coefficient integral with a sign-resolving error, instead of taking
a logarithm of that zero. Its possible downstream use is local signed
coefficient information at exceptional zero ordinates. It leaves the
independent sign problem open; an existential witness alone duplicates
L461.

For source comparison use L018's actual Xi and L463's normalization.
For an assumed quartet, remove exactly its finite polynomial with full
multiplicity, leaving an entire quotient. The proposed window has the
positive coefficient saddle within O((log gamma)^(-1/2)) of the positive
zero factor, with center height within that scale of gamma. The saddle
belongs to the remaining analytic exponential factor; do not assume
it stays at the unshifted degree/log-height ratio. These specify a
comparison scope, not a derived formula or a bound for the quotient.
Fixed d excludes an unassessed joint limit d -> 0.

Search exact terminology and stronger results for saddle-point
coefficient extraction with vanishing amplitudes and prescribed
polynomial factors, including multiplicities. Inspect primary theorem
hypotheses and essential proof cases. Compare the signed leading scale,
moving parameters, remainder and complementary contours. Distinguish
zeros of an amplitude from merging stationary points. Import matching
known expansions rather than reprove them as new mathematics.

Continuation test: a source-ready application must specify a nonzero
signed leading term, an error smaller than its magnitude away from
transition zeros, and all necessary bounds on the actual remaining Xi
factor. If only a known witness or abstract expansion with unsupported
Xi hypotheses is available, record that limitation. Do not promote it
to an actual-Xi sign theorem. No proof attempt is approved yet.

The recorded endpoint moving-saddle attempt of 24 September concerns
an older Mellin saddle and derivative envelope, not a polynomial zero
retained in this coefficient integral. Preserve its stop without using
that older envelope as a current zero-free limitation. The October 28
small-displacement review concerns an aggregated positive quotient
norm; the October 31 Hermite correction review concerns unknown-node
interpolation. Neither supplies this signed transition. This bounded
comparison does not prove novelty.

Essential inputs are L018 and L463; L461/L462 are comparisons only.
The strict Re(s)>7/8 premise does not ensure the quotient is nonzero
near d<=3/8 after removing one quartet. Other zeros and multiplicities
may obstruct that step. No such absence, RH, or positive low-order
sign is assumed. No cross-notebook input. Mathlib coverage is unchecked.

Next routing is literature_comparison / standard / high. A later
creative attempt is possible only if coverage yields a justified Xi
application: its bounded test would be the signed coefficient at a
zero/saddle encounter, addressing exceptional-height information.
That test is not source-ready now. No new calculation or lemma was
performed in nominating it.
