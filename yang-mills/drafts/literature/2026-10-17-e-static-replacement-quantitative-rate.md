# E static replacement — quantitative source comparison

TARGET: Determine whether L101's full-prefix static-replacement error is O(N^(5/2) log(eN)^2) for both actual probes, retaining all axial levels, the moving-cut endpoint and the full heat spectrum.
CHECKED: 2026-10-17
DECISION: EXPLORE
SEARCH_EVIDENCE: Inspected L101(1)–(14), L097 proof sections 2–3, L065 hypotheses and scalar form proof, L008's exact probes, L028's coefficient/lift hypotheses, the original E-prefix draft and ATTEMPTS/024–025/030; searched these local routes and literature records for duplicates and conducted the bounded external queries below.
SOURCE_EVIDENCE: Inspected Chung–Yau, Discrete Green's functions, author-hosted revised text, sections 2–4, (2)–(11) and Theorem 3; Dowker, arXiv:1207.2096v2, sections 7–8, (29)–(37), and section 10, (42), (47); reused the broad assessment's Adams–Lee Appendix A comparison without another reading. Precise versions, hypotheses and applicability follow.
COMPARISON: Exact scalar interval kernels and the local square-root multiplier are available, but no inspected source gives the actual variable-coefficient full-prefix trace error at O(N^(5/2) log(eN)^2). L101's O(N^(27/10)) is a weaker upper allowance, not a lower bound; L222's smooth exterior diagnostic rate covers a different error.
GAP: Replace L101(12)'s coarse transverse split by a quantitatively controlled axial/transverse comparison on the actual H_k=Zeta_k U B, or bound its original signed pairing directly, before the complete heat sum; the static trace's subsequent continuum rate is excluded.
REASON: The previously uncovered target now has inspected standard spectral/kernel inputs and a precise remaining comparison, with no essential inaccessible source. Approve one later bounded attempt on this unchanged target, without asserting its estimate or novelty.
LITERATURE_REASON: The target changes from a smooth exterior diagnostic to L101's rough full-prefix static replacement; essential quantitative theorem coverage for that error is missing.
SCOPE: Fixed-box SU(2), straight lower-rooted direction-1 forest, admitted even N, a=8/N, tau=1/16, both actual L010 probes with L008's triplet average of squares and clover shear, all axial levels, transverse end rows, upper jumps and constant modes; only the full error in L101(3), not its remaining continuum comparison, L097's own rate or the complete response.

This completes the separate literature approval requested by the prior
checkpoint. No new estimate, lemma or mathematical script is supplied.
The broad assessment's complete-response rate remains unapproved.

## Exact local comparison and previously failed routes

Write E_(i,N) for R_E minus the finite static sum displayed in L101(3).
This is the entire error from L101(6) to (3), including the exterior-
circulation terms F_k in (7), not only the square-root replacement.
The scalar F_11 is uniformly bounded by L065; it stays between the
two factors in the exact signed trace. No level-diagonal residual or
positivity of F_11 is assumed.

L101(9) bounds the squared multiplier error by mu/(mu+lambda).
Its (10) retains both pinned endpoint differences, with an upper jump
of size (N-1)||Zeta_k(N-1)U||_HS^2. Equations (11)–(12) use only a
transverse rank bound and total axial energy before choosing
eta=N^(-2/5). They give Hilbert–Schmidt error O(p(k)N^(6/5))
against O(p(k)N^(3/2)) factors and the recorded O(N^(27/10))
heat-summed error. These are existing estimates, not new calculations.
L097(11)–(17) is the same coarse mechanism in a different pairing;
repeating its cutoff choice is not a new test.

The available neighboring-level bounds are on the deterministic
Zeta_k(s), not on arbitrary columns of Zeta_k U B or on their upper
zero extensions. L008 fixes both actual forms and the smooth compact
displacement; L028 supplies uniform coefficient extensions before
retraction. L101(8) imports a mode polynomial p and a complete
heat-weighted summability bound. Any sharper modal estimate must
retain polynomial mode dependence that this full sum can absorb.
L101(13) defines the static cumulative insertion with its moving-cut
endpoint; that finite expression remains unchanged in this target.

The original E-prefix draft records the present bound and limit, not
this stronger rate. The scoped duplicate search found no ready rate
proof. ATTEMPTS/024 excludes deletion of an upper Dirichlet correction;
025 excludes a frozen axial-profile/absolute-norm power gain for the
different first-pair trace. Neither refutes the error after subtracting
L101's own static trace. ATTEMPTS/030 excludes substituting a varying
mass into a merely fixed-mass transverse-H limit. The proposed test
must use a uniform finite-N spectral or kernel estimate instead.

## Inspected primary inputs and applicability

Fan Chung and S.-T. Yau, [*Discrete Green's functions*](https://fanchung.ucsd.edu/wp/green.pdf),
J. Combin. Theory Ser. A 91 (2000), 191–214; inspected the author-hosted
22-page revision (additional revisions are undated), sections 2–4,
PDF pp. 4–6 and 9–10. Connected induced subgraphs with nonempty
Dirichlet boundary have positive restricted normalized Laplacian;
(4), (10), (11) give its heat expansion and inverse. Theorem 3 gives
the two-ended path inverse, with the proof retaining both endpoint
zeros and the diagonal source. For n=N-1 its path normalized
Laplacian is L_D/2: its inverse carries that factor of two. This is
a scalar building block, not the raw min(s,t) prefix covariance.
It cannot replace the latter by a pinned bridge without keeping the
boundary difference. The theorem supplies no variable-Zeta trace rate.

J. S. Dowker, [*Heat-kernels on the discrete circle and interval*](https://arxiv.org/pdf/1207.2096v2),
v2, 31 August 2012, section 7, printed pp. 10–11, (29)–(31),
section 8, pp. 12–13, (34)–(37), and section 10, pp. 14–16, (42), (47).
The Dirichlet modes have eigenvalues 4 sin^2(pi n/(2p)),
1<=n<p, and normalized sine eigenvectors; p=N matches L_D exactly.
The image construction cancels both boundary values. The Neumann formula retains the
normalized constant mode and its 1/p kernel term. The massive interval
formula is supplementary; no unverified index convention is needed
because the approved attempt can use (30)–(31). The parsed auxiliary
display (32) has different doubled-period arguments; its rendering
is unresolved and it is not an imported input. The needed spectrum
is stated directly in (30). These scalar formulas give no estimate
for varying Zeta_k, signed F_11 or the full heat-weighted response.

These citations obviate a new proof of scalar path diagonalization
or the interval heat kernel. Their cochain/component applicability
is only through L101's already established joint-mode comparison;
they do not impose scalar Dirichlet conditions on every gauge link.
Estimating the actual prefix/multiplier composition is the uncovered
specialization to test. No singular inverse is assumed bounded on an
infinite lattice, and no transverse multiplier is commuted through
a spectral projection on the strength of these citations.

The broad quantitative assessment's Adams–Lee Appendix A reading is
reused: its translation-invariant Brillouin-zone theorem does not
cover this pinned variable-coefficient trace or its uniform heat sum.
Repeating that proof would not fill the identified difference.
Full matching Mathlib coverage and supporting kernel coverage are
not checked; no absence claim is made.

The official [Clay page](https://www.claymath.org/millennium/yang-mills-the-maths-gap/)
still links the same 14-page Jaffe–Witten
[*Quantum Yang–Mills Theory*](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf).
Checked on 2026-10-17: section 4, printed p. 6, still requires the
continuum theory for every compact simple group with the stated
axiomatic and mass-gap properties. This does not change the precise
target/version recorded in foundations/01-target-and-scope.md.

## Bounded search record and decision

Queries on 2026-10-17 included:

- `discrete Dirichlet Laplacian cumulative sum Brownian covariance fractional Sobolev square root resolvent estimate lattice`
- `finite difference Laplacian square root resolvent Hilbert Schmidt commutator smooth multiplication heat kernel estimates`
- `discrete Dirichlet heat kernel box eigenvalues sine estimates`
- `Chung Yau discrete Green functions Dirichlet eigenvalues path heat kernel 2000 pdf`
- `discrete static approximation resolvent prefix`
- `Dirichlet prefix Hilbert static Laplacian`
- `Brownian covariance discrete resolvent estimates`
- `Laplacian static replacement error`

These located the inspected interval/graph sources above. Fractional
Laplacian, Kato square-root, manifold-kernel and stochastic-numerics
hits were only leads, not inspected theorem inputs. No matching
actual-probe theorem was established by this bounded search; no
novelty or global absence claim follows. The necessary scalar
formulas are accessible, so none of those unread leads is an
essential source blocker for the proposed finite-dimensional test.

Decision: EXPLORE, for exactly the saved TARGET. In the next research
turn test a joint axial/transverse spectral or resolvent estimate on
the full H_k, retaining its Brownian prefix covariance and actual
Zeta_k(s), instead of merely repeating the rank/total-energy split.
Use the cited scalar formulas and imported local bounds; do not
reprove them as new lemmas. A direct signed pairing estimate remains
within this same error target if a factorwise bound is inadequate.

Continue only on obtaining a complete heat-summed bound
|E_(i,N)|<=C_i N^(5/2)log(eN)^2 with C_i independent of N, a strictly
stronger bound, or new evidence identifying a precise obstruction
and a different test. Abandon any particular shortcut that drops
the upper jump, suppresses low modes without their full cost,
commutes variable coefficients without a bound, or requires more
than the available heat-summable mode dependence. A failure of a
factorwise estimate is not signed growth of E_(i,N).

The main gap remains interacting cutoff removal with reflected
error <=c_box/2, continuum axioms and finite positive mass. This
component rate could remove one obstruction to a later complete
O(a^(-5/2)log(1/a)^2) remainder. Even success leaves the static
trace's continuum rate, other component rates, L220's separate audit
status and a coupling-uniform interacting expansion unresolved.
Essential continuation inputs: L008 L028 L065 L097 L101, with
L101's imported L085/L088/L091/L092 identities retained. No new
residual commutation, endpoint smoothness, rate or cancellation is
assumed. No cross-notebook input is used. Mathematical exploration
usage remains zero; this source review does not spend that budget.
