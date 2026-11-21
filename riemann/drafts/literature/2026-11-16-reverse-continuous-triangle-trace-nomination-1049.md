# One triangle with the audited pair trace — nomination1049 / review1050

TARGET: Test whether C467p's h=0 trace extends to a bounded continuous adjoint on C467k's actual j=0 triangle, with initial value f(x)^3, all four complex weighted derivatives in L1 and the complete cutoff identity.
CHECKED: 2026-11-16
DECISION: EXPLORE
SEARCH_EVIDENCE: Separate review1050 searched characteristic initial-boundary compatibility, prescribed outflow data, boundary-degenerate continuous transport, triangle characteristic boundaries and Calogero adjoints; compared scoped reverse records, reviews1042/1046 and stops1000/1009/1023/1043. No inspected theorem supplies this exact continuous triangle test or incompatibility; queries and limits below, without a novelty claim.
SOURCE_EVIDENCE: Reuse reviews1042/1046 and C467k/m/o/p's audited geometry and supporting Stokes/DCT/ODE scope. Fresh primary reads: Iyer, Method of Characteristics (2026), Prop7/Remark8/Lemma9/Thm10 proof and Remark11; Imagawa–Kawagoe, arXiv HTML labelled2409.15603v1, introductory hypotheses/(1.2)/(1.4), Thms1.1/1.2, section2 boundary definitions, section3 Lemma3.1 proof and section4 directional-regularity step; Calvo–Hingant–Yvinec, arXiv:2004.01947v1, (H1)–(H6), section2 setup, Lemmas2.5/2.6 proofs, Props2.8/2.9/2.11 and section2.3 initial/boundary proof cases. Precise links and qualifications below.
COMPARISON: Known local noncharacteristic existence, inflow graph-space solutions and half-line degenerate characteristic/flux results require hypotheses not verified for the original triangle. Their conclusions do not provide the prescribed whole-edge value, collapsed-vertex continuity and four separate complex weighted derivatives together. C467p's free-side pair construction and the joint-smooth stop do not decide this class.
GAP: Construct exactly the nominated continuous j=0 triangle test with C467p's full edge trace, all four complex weighted derivatives in L1 and the complete independent-cutoff identity, or prove incompatibility in precisely this class. This is a mathematical gap, not an essential inaccessible-source blocker.
REASON: Literature-only review1050 completes nomination1049's changed-boundary comparison, preserving its exact TARGET and proposed test. EXPLORE permits one bounded mathematical attempt; no triangle lemma, characteristic estimate, obstruction or cutoff-limit result is derived here.
LITERATURE_REASON: The imposed whole outer-edge trace and collapsed radial boundary were essential uncovered hypotheses outside review1046's pair-only scope and review1042's joint-smooth class. This is their first separate source comparison; adequate prior coverage is reused.
SCOPE: Only the original n=3 j=0 triangle of C467k, raw time, actual B/beta/H/H0/F, original algebraic-square form and common minus sign; one existential common time, |x|<=1/256 and the same fixed bump with b=1/4096. No changed flow, connector, weight or time and no other triangle or chamber matching are included.

## Proposed next test, not a mathematical result

Fix the test phi_p selected by C467p(33)–(35), with its audited
continuous one-sided h=0 trace. Use the actual C467k map

    Z_0=(1-r) vbar 1+r[(1-lambda)V_0+lambda V_1],
    V_0=(v_1,v_2,v_3), V_1=(v_2,v_1,v_3),
    0<=r,lambda<=1.

Seek one real psi, 0<=psi<=1, continuous on
[0,tau] x [-X,X] x [0,1] x [0,1], with

    psi(0,x,r,lambda)=f(x)^3,
    psi(t,x,1,lambda)=phi_p(t,x,1-2lambda,0).

At r=0 require a value independent of lambda, as befits the collapsed
vertex. Require smoothness locally for t>0 and 0<r<1, with neighborhood
extensions in x and lambda at their fixed endpoints. Smoothness at r=1,
r=0 or t=0 is not imposed. No joint smooth corner jet is assumed.

For the original complex coefficients of C467k(17), require the
undivided equation dpsi wedge Re(-Z_0^*Omega)=0 in that interior,
and absolute integrability on the full parameter box of

    |A psi_t|+|U psi_x|+|B psi_r|+|V psi_lambda|.

Keep the original zeros at lambda=1/2. Require the full C467k(20)
identity to pass from epsilon<=t<=T and eta<=r<=1-zeta to its
entire domain as epsilon,eta,zeta tend independently to zero, with
the actual continuous traces and every x, lambda, time and radial
face retained. No corner term may be discarded by a sign assertion.
This is a prospective condition, not an assertion that integrability
or the pair construction already implies it.

The bounded test is one construction satisfying all these conditions
or an incompatibility in exactly this class. Failure of an auxiliary
velocity estimate is inconclusive. Continue only with such evidence;
do not repeat the joint-smooth argument or infer nonexistence from a
failed sufficient class. No all-six-triangle construction is requested
by this first test, and no x-side zero-neighborhood is prescribed.

Main gap: L030–L032/C032a actual-Xi all-degree algebraic-square
positivity. A positive result would supply one pair-to-triangle match;
a precise incompatibility could reject this selected boundary trace.
The other radial matches, chamber traces, exterior payment, global
assembly, realization, other degrees and Xi transfer remain open.

Essential inputs for source comparison: C467p/C467o audit1049,
C467k/audit1033, C467m/audit1041, C467l/audit1037,
C467j/audit1029 and C467e/audit1017, carrying C466z/audit988,
C466/audit993 and C466a qualifications. Reuse review1046's primary
comparisons and review1042's network comparisons within their stated
hypotheses. Preserve stops1000/1009/1023/1043 in their scopes.
Full matching Mathlib coverage is unchecked. At nomination1049 the next
task was literature_comparison, standard/high; that nomination supplied
no ready decision. Separate review1050 below supplies the source gate
for this unchanged target.

## Separate source comparison1050 — 16 November 2026

This is the required literature-only turn, not a triangle proof attempt.
The proposed test above, including all endpoint extensions, coefficient
zeros and arbitrary independent cutoffs, is unchanged. EXPLORE means
that the inspected sources do not settle it; no originality is certified.

### Search and local overlap

Queries actually issued included `transport equation characteristic
boundary prescribed outflow continuous solution compatibility initial
boundary theorem`; `linear transport equation characteristic boundary
continuous solution tangency inflow boundary data compatibility theorem`;
`"A revisit on well-posedness" advection separation Imagawa Kawagoe arxiv`;
`"Lifshitz-Slyozov" "non-smooth rates" boundary theorem 2004.01947`;
`"transport equation" "triangle" "characteristic boundary" continuous`;
`"degenerate transport" "boundary" "continuous" solution weighted
derivatives`; and `"Calogero" "transport" "boundary" adjoint`.
Search snippets supplied leads only.

Reused [review1046](2026-11-16-reverse-continuous-pair-adjoint-nomination-1045.md)
and [review1042](2026-11-16-reverse-matched-adjoint-transport-nomination-1041.md)
in full, without repeating their Boyer, Chen–Comi–Torres,
Arlotti–Banasiak–Lods, Ambrosio–Crippa or network-source extractions.
Those comparisons already delimit the regularity, invariant-flow,
transmission and trace assumptions of their inspected theorems. Their
decisions do not automatically extend to this changed boundary problem.

Read C467k's hypotheses and conclusion, (17)–(20) and audit1033's
edge convention; C467p's hypotheses, conclusion and selection (33)–(37);
and C467m's complete pair-to-triangle map/orientation paragraph.
The full j=0 edge uses the original positive-h pair, s=1-2lambda,
with no slot permutation. Equality of the underlying maps and opposite
face orientations is recorded geometry; it is not an assertion that
unknown transported tests match. C467k(19) bounds the known original
coefficients, while C467p's estimates concern the already constructed
pair test. Neither is recorded as a triangle-test existence theorem.

Scoped searches of November16 reverse assessments, histories and
attempts for continuous triangles, full edge traces and collapsed
vertices located nomination1049 and its history, rather than an earlier
solution of this target. Read stops1000/1009/1023/1043 and their audit
updates. They respectively concern a specified compact forward payment,
a specified forward cap/initial family, the unaugmented reverse
zero-defect current, and the joint-smooth pair class. Their hypotheses
are preserved; none is extended to exclude this continuous triangle
problem. This is a bounded duplicate/failure check, not an exhaustive
novelty survey. No other notebook was read.

### Primary comparisons actually inspected

**Local classical characteristics.** Gautam Iyer, *Method of
Characteristics*, 2026 course notes,
[Proposition7, Remark8, Lemma9, Theorem10 and proof, Remark11](https://www.math.cmu.edu/~gautam/c/2026-632/notes/moc.html).
The setup has smooth F(Du,u,x), a locally flattened hypersurface and
differentiable prescribed data. An admissible initial jet has value g,
tangential derivatives Dg and F=0; noncharacteristic means F_p dot n
is nonzero. The local construction inverts the projected characteristic
map. The proof propagates the zero tangential jet error by a scalar
linear ODE and identifies the constructed gradient. Remark11 separately
warns that data at multiple boundary hits require compatibility.
This is local classical coverage, not an existence theorem for
characteristic or collapsed boundaries.

Applicability here remains unverified: no noncharacteristic chart
covering the entire prescribed edge and both degenerations has been
supplied. The nomination also permits only continuous edge traces and
does not assume boundary jets. Thus the classical theorem cannot be
used either to construct the requested global test or to transfer a
smooth compatibility obstruction to this weaker class. Its hypotheses
must be checked on any domain where it is later used.

**Inflow/outflow without separation.** Masaki Imagawa and Daisuke
Kawagoe, *A revisit on well-posedness of a boundary value problem of a
stationary advection equation without the separation condition*,
[arXiv HTML labelled2409.15603v1, Theorems1.1/1.2, sections2–4](https://arxiv.org/html/2409.15603v1).
For fixed 1<p<infinity, Theorem1.2 assumes a bounded Lipschitz domain,
beta in W1,infinity, mu in Linfinity, positive-measure inflow,
density of Lipschitz functions in the transport graph norm including
both weighted traces for all finite exponents (1.2), and
essinf(mu-div(beta)/p)>0. Source data are Lp; prescribed inflow data
are Lp weighted by |beta dot n|. The conclusion is unique graph-space
strong solvability, controlling beta dot Du and both weighted traces.
Read the flow-based inflow/outflow/characteristic definitions, Lemma3.1's
Green/coercivity and Banach–Nečas–Babuška proof, and section4's
directional-derivative and local-to-global trace steps. No separate
coordinate-derivative regularity is asserted by that conclusion.
The retrieved HTML displays manuscript date24August2026 while its
version label is v1; this review identifies that rendered text, not
an independently checked publisher version.

No such transport realization, coercivity or density verification is
available for the original triangle in the local record. In particular,
the target's whole r=1 value is not already verified as admissible
inflow data for this theorem; no classification of that face is proved
in this review. Graph solvability does not meet the nominated joint
continuity, collapsed-vertex value, interior smoothness and four
separate complex-product conditions. Removing a separation assumption
in this source does not remove its remaining assumptions. No theorem
application or compensating change of weight/reaction is made here.

**A genuinely boundary-degenerate comparison.** Juan Calvo, Erwan
Hingant and Romain Yvinec, *Initial-boundary value problem to the
Lifshitz-Slyozov equation with non-smooth rates at the boundary*,
[arXiv:2004.01947v1, (H1)–(H6), section2, Proposition2.11](https://arxiv.org/html/2004.01947v1).
For its fixed-u linear construction, a,b are nonnegative C0[0,infinity)
and C1(0,infinity), with derivatives bounded on (1,infinity), a>0
inside and 1/a integrable at zero. Phi=b/a has integrable derivative
at zero and threshold Phi0=lim_(x->0+)Phi(x). Nucleation n is
nonnegative locally Lipschitz on
[Phi0,infinity). Given continuous u in [0,rho] with inf u>Phi0
and nonnegative initial density in L1((1+x)dx), the characteristic
formula gives weighted weak-L1 continuity, a moment identity and the
prescribed boundary flux. Inspected Lemmas2.5/2.6, the transformation
A(x)=integral_0^x1/a, the two characteristic representations, and
section2.3's initial/boundary contributions, integrable Jacobian bounds
and boundary-flux limit. The derivative estimate uses the strict
inflow margin and integrability of Phi'.

This is a one-dimensional continuity equation for a density with a
flux condition. No identification of its special velocity, inflow
margin or reciprocal-rate hypotheses with the triangle is established.
It does not supply a continuous adjoint with the selected entire edge
value or the four original complex products. Its coordinate change
is source methodology, not a licensed replacement of the actual
triangle, physical time or weight. No specialization is claimed.

Access: an attempted2004.01947v3 HTML URL returned404; the version1
primary text above was accessible and read. No essential inaccessible
source remains. Search hits concerning transport control, numerical
degenerate schemes, Lasota dynamics, scattering and quantum Calogero
boundary conditions were not read as theorem evidence. The retrieved
primary comparisons, together with ready reviews1042/1046, suffice for
this bounded gate; absence of a direct theorem is not a reason to
repeat browsing indefinitely.

### Decision and next mathematical discriminator

The reviewed results support classical characteristic construction
on verified regular charts, and weak/graph or flux conclusions under
their stated hypotheses. None inspected imports the exact original
triangle test or establishes its incompatibility. No standard theorem
is reproved; no unverified applicability assumption is promoted to a
lemma. Full matching Mathlib coverage is unchecked, and supporting
Stokes/DCT/ODE coverage is not full target coverage.

Decision: EXPLORE for one bounded attempt at exactly the TARGET above.
First save partial reasoning. A possible approach is to examine the
actual interior real characteristic equation and the imposed edge
values, then either construct the test with a common time or prove
an actual-data incompatibility that uses only the nominated regularity.
This is a proposed method, not a calculated velocity, boundary
classification or new compatibility result.

A positive answer must include all four complex products, continuity
at r=0 with a lambda-independent value, the original undivided zeros
at lambda=1/2, and every time/x/lambda/radial face in the full
independent-cutoff limit. A negative answer must exclude precisely
this continuous class. Failed estimates, a failed ansatz, a
positive-time-only construction, or the old joint-smooth jet argument
are inconclusive. Preserve unfinished reasoning and require a refined
mechanism or materially new input before repeating an unsuccessful
attempt. Other triangle matches, chamber matches, exterior payment,
realization, all degrees and Xi transfer remain independent gaps.

Recommended next purpose: proof_attempt/development, deep_research/xhigh.
This develops the existing matched-adjoint mechanism on a new piece
with prescribed data; it is not classified as a newly invented central
mechanism or routine specialization. This review changes no lemma,
mathematical script, PROOF.md argument or DAG input.
