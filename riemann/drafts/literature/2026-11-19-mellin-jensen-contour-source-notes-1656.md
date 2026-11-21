# Mellin/Jensen contour source review1656

Literature-only working record, 19 November2026. No specialized contour
identity, asymptotic, lemma or mathematical script is derived here.

The primary finite Rice input is Flajolet--Sedgewick, *Mellin transforms
and asymptotics: Finite differences and Rice's integrals*, Theoretical
Computer Science144(1995),101--124, DOI10.1016/0304-3975(94)00281-M,
Section2, Lemma1/(6), pp104--105, and Section4, Theorem2 and its proof,
pp110--111: https://algo.inria.fr/flajolet/Publications/FlSe95.pdf .
Its finite analytic-contour theorem and its unbounded-contour theorem
have different hypotheses. The latter requires polynomial growth;
C048j is a relative bound on a different observable. No application
of either theorem to the actual coefficients is yet proved here.

Read C028b's whole proof, C028g's hypotheses and full limit proof,
C048j/C048a's complete hypotheses and relevant contour normalization,
L019/L021's moment normalization, and source-notes1652. Reused the
existing component audits rather than reopening their proofs.

The candidate interpolation to examine in a separate mathematical step
is G(s)=Gamma(s+1)I(s+1/2)/Gamma(2s+1), initially Re(s)>-1/2.
This is a proposed definition and applicability test, not a proved
specialization or an imported formula for J_d. Its samples, analyticity,
finite-contour orientation and vertical growth must all be checked.
At c=-1/4 the precise proposed extra absolute-convergence obligation is

    integral_R |G(c+it) d!/product_(k=0)^d(c+it-k)| dt < infinity.

This tests only x=-1, fixed integer d>=3, before a degree-uniform
signed route. It would not suffice for contour closure or H_d=o(d).
No convergence, divergence, exponential rate or sign has been claimed.

Duplicate comparison: L718 concerns a different moving-size gamma
interpolation and accumulating coefficient poles. Its failure is not
a theorem about G. The existing actual-family Cauchy circle, recorded
in assessment1344/comparison1345 and C019c/d, is a distinct route.
Ono2610.38870v1 supplies it without a Mellin interpolation, and the
previously assessed edge/full-contour limitations remain unchanged.
Do not recreate that circle representation as a new discovery.

Read primary Rice Section2 and Theorem2 with both proof cases through
the author's PDF and its author-hosted mirror. OCR obscures some
displayed formulas; the precise finite formula also appears in the
indexed author PDF text. Screenshot requests produced no inspectable
image through this tool interface. A shell download failed DNS; browser
text access succeeded. No access failure is currently an essential
source blocker. The saved provisional work above is completed below.

## Completed source comparison

**Rice theorem, imported template only.** For an analytic f on a domain
containing [n0,infinity), a positive closed contour C in that domain
enclosing [n0,d] and excluding earlier nonnegative integers gives

    sum_(k=n0)^d (-1)^k binom(d,k) f(k)
      =(-1)^d/(2*pi*i) integral_C f(s) d!/product_(k=0)^d(s-k) ds.

The residue proof uses the factors (-1)^(d-k)binom(d,k). Section2/(7)
instead integrates upwards on Re(s)=c<n0, with prefactor
(-1)^(d+1)/(2*pi*i), assuming polynomial growth O(|s|^r) throughout
Re(s)>=c and d>r+1. Theorem2(i) requires meromorphic continuation and
polynomial control on escaping concentric circles; (ii) requires that
control outside a compact set in a half-plane and retains its vertical
integral plus noninteger residues. Both proof cases use closing arcs.
These hypotheses justify importing the template, not applying it here.

Formula access was corroborated against the authors' March27,1994
prepublication, Section2, p4, Lemma1/(6)--(7):
https://static.aminer.org/pdf/PDF/001/091/229/mellin_transforms_and_asymptotics_finite_differences_and_rice_s_integrals.pdf .
That copy has21 pages, whereas the final1995 paper has24. The finite
residue signs and the opening condition agree; it is not silently
treated as the published pagination. No obscured coefficient beyond
these readable formulas is needed. Norlund's older book is a historical
reference in the paper and was not separately inspected or imported.

**Actual interpolation already exists locally.** A subsequent exact
factorial search found L828 Section2/(5)--(6), L829's hypotheses, and
assessment647's integer-interface paragraph. Reuse that unconditional
entire E construction and its previously checked sampling convention;
do not present the preliminary G above as a new interpolant. The
continuation uses precisely L829's normalized E, not an arbitrary
interpolation with the same integer samples. L828's conditional
complete-Bernstein assertions are not inputs. L829's scalar pass is
finished and supplies no vertical growth statement. No new relation
between G and E is derived in this review.

**Gamma input for the proposed test.** NIST DLMF5.11.9 gives

    |Gamma(x+iy)| ~ sqrt(2*pi)|y|^(x-1/2)exp(-pi|y|/2),

as y tends to either infinity, uniformly for bounded real x:
https://dlmf.nist.gov/5.11.E9 . Read the formula and its uniformity
sentence, not merely a search snippet. DLMF5.5.5's duplication formula
was also inspected, with 2z excluding nonpositive integers:
https://dlmf.nist.gov/5.5.E5 . The existing factorial interface in
assessment647 can be reused. No new gamma asymptotic proof is needed;
the actual E specialization and the Lambert factor remain calculations.

**Domain comparison and missing estimate.** C048j concerns I/S on
|p|>=exp(12), Re(p)>=-|p|/(4log|p|); E includes a reciprocal gamma
factor and a shift. Neither its vertical growth nor growth on closing
arcs is a conclusion of C048j. Even a contour with Re(p)>0 has a
bounded portion outside that estimate. Thus C048j is not, by itself,
the full coefficient-contour or relative signed-error theorem needed
by this transfer. This is a hypothesis mismatch, not a proof that all
such contours fail. On the specific proposed line s=-1/4+it, the
shifted p=1/4+it lies in C048j's sector when its modulus is large;
the finite remainder must retain exact E. This elementary domain
comparison approves no new contour deformation or inequality.

For the normalized E version, the independently testable missing
absolute-convergence estimate is exactly

    integral_R |E(-1/4+it) d!/
                    product_(k=0)^d(-1/4+it-k)| dt < infinity,
                    each fixed integer d>=3.

This is only the absolute vertical-contour route's first gate. Its
value, convergence and exponential scale remain unproved here. A
failure would stop this specific opening; a pass still leaves closing
arcs, degree-uniform signed remainder and zero-height conversion unpaid.
The bounded next calculation is to establish the finite specialization
and test this integral, without moving degree and height simultaneously.

**Known exact alternative and stronger overlap.** Ken Ono,
*An Asymptotic Jensen--Polya Criterion for GRH*, arXiv2610.38870v1,
28October2026, introduction's coefficient formula and Section2.2
(2.8)--(2.10), https://arxiv.org/html/2610.38870v1 , supplies an exact
Cauchy circle for the actual reciprocal family. Its applicability to
K=Q and its positive rescaling are already recorded in assessment1344
and C019c/d. Read those records and the primary formulas and the
coefficient-extraction argument. Source F there is unnormalized Theta;
C028b's F divides by gamma_0. This is not a Mellin-Barnes formula for I.
Reuse comparison1345 for the stronger root-count theorem's essential
proof scope and omitted edge hypotheses. No new root-count theorem,
Lean verification or full-paper audit is imported. Its growing
exceptional set does not pay the weighted statistic C028b requires.

**Search and stopping record.** Queries were `Jensen polynomials xi
Mellin Barnes integral representation unshifted`, `Flajolet Sedgewick
Norlund Rice integrals finite differences integral1995`, `"Jensen"
"Mellin-Barnes" xi polynomial`, `"Jensen" "Rice" "xi"`,
`"Jensen polynomials" "Mellin" "Riemann"`, `"Jensen polynomials"
"Norlund"`, and `"Jensen polynomials" "Rice integral"` (including
the accented Norlund variant). Broad queries returned irrelevant hits;
no mathematical inference or novelty claim uses them. The direct
primary Rice paper and existing exact-circle assessment suffice for
the proposed limited test. O'Sullivan2007.13582v2 (1.2)--(1.3) and
Section3.1 were read for the actual family, reciprocal convention and
compact limit; they give no automatic full weighted-height conclusion.

Local searches were restricted to C028/C048, Mellin/Jensen-named
assessments and attempts, and the exact L718/L828/L829 passages located
there. Read the November5 global-import and endpoint-loop stops and
the L718 failure record. Preserve all of them. L718's noninteger-size
pole accumulation is not asserted for E. The old bulk source screen559
and edge comparison1345 already reject automatic signed asymptotics;
no repeated Airy import is proposed. The new actual-E vertical test is
independent of their unpaid local edge reference, and of L829's
finished fixed derivative diagnostic. No cross-notebook input was read.

**Decision and limits.** SPECIALIZE for the finite Rice template and
its prospective actual-E viability test. Source coverage is sufficient
for a separate REPRODUCTION calculation, with newly written coverage
subject to separate approval. No specialized contour result or vertical
growth result was proved in this literature turn. The informative
negative is source scope: automatic full-contour import fails at an
explicit unverified growth premise, and both interpolation and circle
representations have local predecessors. It changes the next action
to a fixed-line test before any signed contour proposal. It neither
rules out the test nor establishes progress beyond the checked sources.

The central gap remains L030--L032/C032a, equivalently C028b's
H_d=o(d); C028g identifies S_F but does not force zero. A viable
contour could eventually support a degree-uniform comparison, but
reference geometry, signed margins and root-height transfer remain
independent. No creative proof target is ready: those ingredients are
still absent. The limited growth test is established-route calculation,
not creative work. Mathlib full matching coverage is unchecked.
