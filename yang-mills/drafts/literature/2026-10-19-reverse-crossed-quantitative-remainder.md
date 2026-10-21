# Reverse crossed trace — quantitative source comparison

TARGET: Establish an O(N^(5/2) log(eN)^2) remainder for L107's complete reverse crossed trace R_R after subtracting a^(-3) K_(i,R), for both actual probes.
CHECKED: 2026-10-19
DECISION: EXPLORE
SEARCH_EVIDENCE: Read L105--L107's full relevant arguments, L088/L093's exact factors, L094's obstruction and packet mechanism, L103's energy/spectral inputs, L104's raw symbols and heat-limit passages, L028/L080's coefficient passages, reverse drafts/history 131--133 and ATTEMPTS/028--032; reused ready assessments and performed the six bounded external queries below. No inspected matching remainder theorem was found.
SOURCE_EVIDENCE: Reused the ready left-crossed, complete-coefficient, other/other and H-curvature primary comparisons; additionally inspected Benzi--Simoncini 1501.07376v1 section 6.1, Theorem 6.1, Corollaries 6.2--6.3 and proofs, section 6.2 (6.3)--(6.4), Remark 6.6 and section 5's finite-section qualification; rechecked Ginovyan--Sahakyan 1405.3568v1 Theorem 2 and its Holder proof, printed pp. 6 and 8--9.
COMPARISON: L105 supplies the exact triangular trace and O(N^2) exterior-circulation error; L106 controls the two inverses uniformly with unequal masses; L107 supplies only a successive fixed-parameter limit. Known decay and scalar tools support a bounded specialization test, but none of the inspected sources gives this ordered relative-boundary remainder, and L241's different R_L bound is not transferred.
GAP: Quantify projection replacement, summed axial localization, ordered coefficient freezing, relative-boundary transfer and the final comparison with exactly L107(2), compatibly with the uniform inverse errors and complete heat sum. These are unproved mathematical specialization obligations, not essential inaccessible sources.
REASON: Target-specific source comparison is complete for one later bounded attempt at exactly TARGET. EXPLORE approves scope only, not a rate, mass schedule or new lemma; this newly ready assessment receives separate supervisor approval before research.
LITERATURE_REASON: The target changes from L100's left crossed trace with zero cubic coefficient to L107's reverse crossed trace with a retained cubic coefficient; existing qualitative and left-crossed coverage does not establish the necessary quantitative scope.
SCOPE: SU(2), relative all-face cube, lower-rooted direction-1 forest, sufficiently large admitted even N, a=8/N, tau=1/16, stored coordinates, bare-first coefficient, actual probes 3 and 6, full heat sum; precisely the co-closed-base R_R and K_(i,R) of L105--L107, without an outside factor 3.

## Completed source comparison

This is LITERATURE / NOVELTY_UNCHECKED / EXPLORATION: a new bounded
comparison, with no new mathematical result or claim of novelty.
No lemma, mathematical script, DAG or proof assembly is changed.
The main gap is still the interacting reflected error <=c_box/2,
ultraviolet cutoff removal, continuum axioms and infrared control with
finite positive mass. This one component rate could support a later
quantitative L011 assembly; the other component rates and interacting
comparison remain independent gaps. There is no solution candidate.
Reuse the precise Jaffe--Witten version in
`foundations/01-target-and-scope.md`; this review selects no new
construction route.

### Exact statement and existing proof scope

L105(3) fixes the layer trace

    a^-1 sum_(k,l)c_(i;kl,a) sum_(s,t) S_st
      Tr[K_ts A_k(s)^T T G W_t^T H_l(t)],
    S_st=1_(t<s)+delta_st/2,
    A_k(s)=P Omega_k(s) Q, H_l(t)=Q Omega_l(t) Q.

This is an existing identity, recorded here to delimit source scope.
W_t retains the displacement at t and both generator filters.
L093(2)--(3) distinguishes this order from R_L and its curvature
subtraction. L103(13) supplies the transverse energy sandwich used
in L105, not a free O(N) reverse-prefix bound. L088(3)--(5) fixes
the complete alternating paths and summable actual heat coefficients.
Neither the gradient-base G_R nor a transposed left trace is TARGET.
The subtraction is exactly a^(-3) times L107(2), whose half-factor
comes from the triangular covariance sum. Its value/sign is not needed.

| Existing passage | What is already available | Missing for TARGET |
| --- | --- | --- |
| L105(3), (6), proof sections 1--4 | Exact ordered two-level trace; O(N^3) bound; O(N^2) removal of exterior circulation | A rate after subtracting the generally nonzero cubic coefficient. |
| L106(2)--(3), proof sections 2--3 | Error <= C_i N^3[sqrt(epsilon)+eta^(3/4)/epsilon] when N sqrt(epsilon), N sqrt(eta)>=1; eta=epsilon^2 is covered when N epsilon>=1 | Compatible uniform bounds for every subsequent operation, rather than equal masses or a fixed-mass limit evaluated at varying mass. |
| L106 section 4 | O(N^2) exterior-circulation comparison uniform in both inverse masses | No new estimate is needed for this already covered difference. |
| L107(6)--(7), proof section 2 | Layer HS projection error with a fixed-mass constant C_(i,epsilon,eta) | Its quantitative mass dependence and every actual projection placement, without idempotence of P_delta or Q_delta. |
| L107(8)--(9), proof section 3 | Summed axial block-norm geometric covariance error and transverse inverse polynomial errors, uniform in N at fixed masses | Useful joint mass/degree dependence and relative finite-to-bulk control. An ordinary full-matrix operator error alone does not control its two-level sum. |
| L107 proof section 4, (10)--(11) | Fixed-range freezing and collar removal; exact triangular half-weight; full heat domination | Quantitative errors for the required varying ranges and actual raw coefficient samples at both levels. |
| L107(12)--(13), proof section 5 | Integrable limiting symbol; successive projection and inverse removal | A rate comparing the finite trace and exactly the unregularized functional, including the coefficient/heat-series errors. |

This table compares stated estimates; it neither improves them nor
proves an obstruction to strengthening them. L106's inverse comparison
is already uniform, so it should be imported rather than reproved.
L107's later fixed-mass constants and fixed-degree limits are the
specific missing quantitative information. No new parameter schedule
is asserted in this literature turn.

L028(3)--(4) supplies centered-stencil consistency for smooth
deterministic coefficients; L080(8)--(10) supplies the exact lower
prefix including its constant axial mode. L104's proof section 2
checks the raw traversal and W symbols used by L107. These do not
make any rough projection kernel smooth. L222(9)--(10)'s supporting
modal prefix estimates were also inspected as a possible quantitative
tool: their endpoint-averaged V is not automatically every raw path
sample in L107. Any use must match those samples and the actual two
probe forms separately; its diagnostic conclusion is not an R_R rate.
L222's pending audit qualification remains attached to that optional
input. No additional input is silently assumed established here.

### Primary theorem comparison and reuse

Benzi--Simoncini, [*Decay bounds for functions of matrices with banded
or Kronecker structure*](https://arxiv.org/pdf/1501.07376v1), v1,
29 January 2015, printed pp. 12--15: Theorem 6.1 assumes a banded
Hermitian positive semidefinite factor with spectrum in [0,4rho].
Its proof factors the tensor heat exponential and applies the two
distance/time regimes in (6.2). Corollaries 6.2--6.3 treat different
factors and more coordinates. Section 6.2, (6.3)--(6.4), integrates
heat products for Laplace--Stieltjes functions, retaining the smallest
eigenvalue; Remark 6.6 allows different positive definite banded factors.
Section 5's dimension-uniform finite-section statement requires bounded
spectrum and no nearby function singularity. These support scalar
massive tensor localization, with the actual interval end rows checked
componentwise. They do not supply a summed axial block-norm error,
triangular coefficient trace theorem or mass-uniform signed remainder.
Near-diagonal/time regimes and mass dependence cannot be omitted.
No reproof is needed. This extends the ready left-crossed source
comparison to the tensor cases; it does not import that trace's bound.

Ginovyan--Sahakyan, [*On the trace approximations of products of
Toeplitz matrices*](https://arxiv.org/pdf/1405.3568v1), v1,
14 May 2014, Theorem 2, printed p. 6, proof pp. 8--9: for real
symmetric scalar circle symbols f in Lip(p,gamma), g in Lip(q,gamma),
0<gamma<=1 and 1/p+1/q<=1/2, the normalized trace error for
tr[(B_n(f)B_n(g))^2] is O(n^(-gamma+zeta)) for every zeta>0.
The proof controls shifted scalar products by Holder and four
Dirichlet kernels. It is not a multidimensional matrix-valued theorem
with position-dependent factors, a triangular level selector or
relative vector boundary conditions. No reduction of R_R to its
hypotheses is available here. Thus it is a scope comparison only,
not a theorem imported for the requested rate or evidence against it.

Reuse the ready left-crossed and H-curvature assessments' inspected
Lawler--Limic, *Random Walk: A Modern Introduction* (2010),
[author-hosted text](https://www.math.uchicago.edu/~lawler/srwbook.pdf),
Theorem 4.3.1, Corollary 4.3.3, pp. 81--84, and Theorem 6.3.8(a),
p. 131 with its harmonic-measure proof. They concern transient
finite-range symmetric walks and interior differences of signed
harmonic functions. For the nearest-neighbor transverse scalar
operator the normalization is Delta=6(I-P_walk). These support scalar
Green/energy comparisons; relative vector columns and this ordered
two-level product still require justification. No scalar Dirichlet
condition is assigned to every link component.

Reuse the complete-coefficient assessment's Adams--Lee,
[*Structure of logarithmically divergent one-loop lattice Feynman integrals*](https://arxiv.org/pdf/0709.0781v3),
v3, section II (7)--(15), Appendix A (A1), (A11)--(A18).
Its translation-invariant Brillouin-zone integrals and infrared and
lattice-degree hypotheses have not been identified with this pinned,
variable-coefficient trace or its full heat sum. It supplies no R_R
rate by citation. Reuse the other/other assessment's inspected
Del Debbio--Patella--Rago 1306.1173v1 section 6 (6.1)--(6.17), and
Luscher--Weisz 1101.0963v2 sections 7.2--7.4 and 8.2: full
renormalized Ward/flow finiteness does not assign an isolated bare
forest trace a remainder. No unchanged primary framework is reproved
or browsed again. Full matching and supporting Mathlib coverage for
this quantitative target are **not checked**; unknown is not absence.

### Search, duplicates, failures and bounded continuation

External queries on 2026-10-19:

- `"lattice" "reverse crossed" trace remainder`
- `"Green function" "triangular" "trace" lattice asymptotics`
- `"trace approximation" Toeplitz matrices products error bounds singular symbols`
- `"Decay bounds for functions of matrices with banded or Kronecker structure"`
- `"co-closed" "trace" lattice resolvent remainder`
- `"lattice perturbation" "finite volume" "boundary" "power counting" theorem`

The matrix-function and Toeplitz primary passages above were inspected.
Other hits on trace surveys, non-Toeplitz decay, numerical trace
estimation, twisted-periodic perturbation theory and continuum Hodge
operators were not read at theorem level and supply no coverage.
No matching or stronger theorem was inspected; bounded search does
not establish novelty or global absence. There is no essential
inaccessible source needed for the proposed local test.

Narrow duplicate searches used the quantitative assessments dated
October 17--19, the reverse drafts, histories 131--133 and 330--339.
The reverse records close the qualitative limit, not this remainder;
the accepted left-crossed rate is for a different order and coefficient.
This is a scoped duplicate check, not a global absence claim.
ATTEMPTS/028--032 were read completely. Preserve L094's quadratic
reverse-block obstruction, the failure of termwise projection
commutation, the fixed-mass/varying-mass trap, the large symmetric
generator and the failure of separate first absolute kernel moments.
None is a signed R_R lower bound or a global ban. A joint ordered
kernel/energy estimate remains an independently testable mechanism.

After separate approval, attempt exactly TARGET. First test whether
the existing two-inverse comparison can be combined with a uniform
layer-projection/localization estimate in this original trace order;
a proved partial error bound is useful even if later freezing or
boundary errors remain open. Retain the full summed axial covariance
norm, rather than using entry decay or a full-matrix operator error
without counting both levels. Only uniform finite inequalities can
justify any later mass/degree choice. Frozen symmetry must retain
the diagonal half and both original coefficient levels until their
replacement errors are controlled. Subtract exactly L107(2).

Continue for a uniform relevant error compatible with the requested
budget, or a new obstruction that changes the route. Abandon a
specific shortcut if its actual row/level/heat count misses that budget
or invokes a stopped commutation/moment premise; keep its failed
inequality. An excessive upper bound is neither signed growth nor a
disproof of TARGET. A qualitative limit or dominated convergence
alone is not a quantitative remainder.

Essential continuation inputs are L088 L093 L105 L106 L107, with
L028 L080 L103 L104 for the inherited stencil, energy, mode and
limit conventions. All inverse and projection occurrences, actual
filters, coefficient levels, source/end rows, constant component modes
and complete heat labels remain. Unresolved assumptions are the
quantitative projection, localization, coefficient and boundary
comparisons and their compatibility with inverse removal; none is
assumed true. No outside factor 3, R_L transpose transfer or G_R
substitution is allowed. This source review consumes no mathematical
exploration attempt; usage remains zero of three after the prior audit.

## Original registration — superseded scope record

The following records the preceding registration. Its requirement to
complete source comparison is discharged by the review above, subject
to the supervisor's separate approval of this newly ready assessment.

The main gap remains the interacting reflected error <=c_box/2,
cutoff removal, continuum axioms, infrared control and finite positive
mass. This intermediate remainder could supply another input to a
quantitative L011 assembly; independent component rates and the
interacting comparison remain unresolved. No new reverse-trace
calculation or approval has occurred in this registration.

Essential inputs to assess are L088 L093 L105 L106 L107, with
L028 L080 L103 L104 for their inherited mode, spectral and limit
comparisons. Keep precisely the co-closed-base R_R of L105--L107,
distinct from the gradient-base G_R. Preserve SU(2), the relative
all-face cube, lower-rooted direction-1 forest, admitted even N,
a=8/N, tau=1/16, stored coordinates and bare-first order. The
actual probes are 3 and 6, and there is no outside factor 3 here.
Subtract exactly L107(2)'s K_(i,R) before estimating the remainder;
its numerical value or sign is not needed for this target.

Retain S_st=1_(t<s)+delta_st/2, the displacement at its original
level, both original coefficient levels, every generator/path filter,
both inverses and all projections. All source/end rows, constant
component modes, exterior-circulation terms or their justified
uniform errors, and complete finite-mesh heat coefficients remain.
No R_L norm bound is transferred by transposition. L106's parameter
conditions and two-inverse order must be checked before any proposed
schedule; L107's fixed-parameter limit cannot receive varying masses
by substitution.

Reuse the ready primary assessments before new retrieval. Search
the exact local reverse-trace histories/drafts for duplicates and
compare L094 and ATTEMPTS/028's reverse-block obstruction, together
with ATTEMPTS/029--032's projection, fixed-mass and moment failures.
These are failed sufficient mechanisms, not bans on this trace.
Read primary theorem hypotheses and essential proof regimes when
the reused assessment does not cover the proposed specialization.
Full matching and supporting Mathlib coverage is not checked.

Continuation test: approve a later bounded mathematical attempt only
if the source comparison covers an independently testable uniform
error leading to the stated threshold, or a useful partial rate.
If essential source coverage is missing, record it precisely; if a
mechanism fails, retain the failed inequality without interpreting an
excessive upper bound as signed growth. Neither a qualitative limit
nor the L106 inverse-removal estimate alone establishes the target.
