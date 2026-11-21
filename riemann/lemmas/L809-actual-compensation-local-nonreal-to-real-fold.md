# Lemma 809: one actual compensation event in degree five

## Hypotheses

Use L019/L021's actual theta law and moments, L795's normalization of
P_d, and the exact two-node Gaussian rule of audited L805. Define

\[
 Q=Q_{2,5},\quad E=P_5-Q,\quad H(x,\tau)=Q(x)+\tau E(x).
\]

Use audited L807's exact error identity and transition X_2. Retain
L778's audited analytic evaluator and Decimal/transcendental software
contracts, and L791's Cauchy normalization. No fitted model, selected
coefficient midpoints, L806 conclusion or branch correspondence from
tau=0 is assumed. The rational arithmetic program is trusted, not
formally verified. The finite certificate passed the independent critical
audit in step557 below; the inherited backend contracts remain premises.

## Conclusion

There exists exactly one zero of (H,H_x) in the closed max-norm box
of radius 10^(-7) about the exact rational center

\[
 (c,t)=(43.721094942044,\ .988536981668).
\]

Call it (x_*,tau_*). Outward bounds are

\[
\begin{split}
 43.721094842044&\le x_*\le43.721095042044,\\
 .988536881668&\le\tau_*\le .988537081668,\\
 .386625355&\le x_*/X_2\le .386625358,\\
 113.083878862&\le X_2\le113.083878863.
\end{split}                                                    \tag{1}
\]

At the event, .414088663<=H_tau<=.414088673 and
-.000229455<=H_xx<=-.000229452. Thus 0<tau_*<1, x_*>0,
the parameter derivative is positive, the quadratic derivative negative,
and the actual correction lies in its strictly positive sector x_*<X_2.

For every tau in [t-10^(-6),t+10^(-6)], exactly two roots, counting
multiplicity, lie in |z-c|<1/10. For tau<tau_* they are simple nonreal
conjugates; at tau_* they form the double positive root x_*; for
tau>tau_* they are two distinct simple positive real roots. Three
other disjoint disks of radius 1/10 contain one simple root each
throughout this slab. Their exact rational centers are

\[
 21.963634,\qquad 82.294347-3.823747i,\qquad
 82.294347+3.823747i.                                      \tag{2}
\]

A different nonreal pair therefore remains on both sides. The total
real-root count here changes from one to three, not three to five.
This is a finite specialization of known validation methods and a
local calibration of actual signed compensation. It asserts no
first/last/global collision, correspondence with a pair of Q, all-degree
sign theorem, originality of the general methods, or RH candidate.
Known actual P_5 endpoint hyperbolicity does not specify (1).

## Proof

**Imported results and applicability.** The invocation-start ready gate is
`drafts/literature/2026-11-05-theta-compensation-crossing-test.md`.
Jean-Philippe Lessard, *Rigorous verification of saddle-node bifurcations
in ODEs*, Indagationes Mathematicae 27(4) (2016),1013–1026,
[DOI](https://doi.org/10.1016/j.indag.2016.06.012),
[author PDF](https://www.math.mcgill.ca/jplessard/ODEs_files/saddle_node.pdf),
Theorem2/Corollary3, pp3–4, give the preconditioned contraction criterion
used below. Definitions1–2/Theorem1, p2, give the scalar fold test:
H=H_x=0, H_tau!=0, H_xx!=0. H is a real polynomial, hence smooth;
the scalar linearization has one simple zero eigenvalue, no other
eigenvalues and range {0}. Both nonzero derivatives are checked.
The fold theorem is imported, not reproved. The explicit polynomial
inequalities below additionally certify the quantitative root disposition.

Import the Pellet test from Becker, Sagraloff, Sharma and Yap,
*A Near-Optimal Subdivision Algorithm for Complex Root Isolation based
on the Pellet Test and Newton Iteration*,
[arXiv:1509.06231v4](https://arxiv.org/pdf/1509.06231v4),
Definition1,(3)–(4),Theorem1, pp12–13. With T_j=H^(j)(m)/j!,

\[
 r^k|T_k|>\sum_{j\ne k}r^j|T_j|                         \tag{3}
\]

counts exactly k roots in the open disk, with multiplicity, excluding
boundary roots. We use K=1, k=2 for the event disk and k=1 for (2).
The polynomials have degree exactly five throughout; no simple-root
assumption, isolation algorithm or termination claim is imported.
Cauchy's coefficient estimate and the Banach fixed-point theorem are
standard named inputs, with their hypotheses checked below. Gaussian
existence/exactness and the error identity are reused local results,
not general theorems to reprove.

**Fifth-order actual extraction and provenance.** As in L791, let
G(w)=xi(1/2+sqrt(w)/2)/8=sum a_j w^j. Audited L778 gives an exact-integral
polynomial P_0, coefficient intervals retaining cell errors, and

\[
 |G-P_0|\le E_G<3.141\,10^{-48}\quad(|w|\le1600).
\]

The analytic difference on this complex disk has jth coefficient
bounded by E_G/1600^j. For j=0,...,5 add that symmetric error to
the full P_0 coefficient interval, then multiply by 8*4^j*j! to get
gamma(j)=j!m_j/(2j)!. This preserves both cell widths and analytic
tails; no derivative comes from a real pointwise estimate. All six
gamma lower endpoints are positive. The complete fifth interval,
about 1.7539230912133153*10^(-9), is saved under `gamma/5` in the
certificate below; the approximation is not an input. Exact rational
enclosures for orders0..4 lie inside L791's outward Decimal boxes;
endpoint equality is unnecessary.

The ancestor is `scripts/actual-fredholm/fixed-pair-certificate-431.json`,
SHA256 `2c0aae858cc1e15b17e46dff0e1b81fa41582b4c84f5d74e3477fb72399335de`.
It matches L791's source and step433's original digest. Its entire
evaluator object equals the audited replay. The replay's whole-file
digest is different and is not substituted for this ancestor. Complete
step478/542/551/553 hash maps, relevant program hashes, PASS/no-failure
records and their recorded checks are inspected programmatically.
The actual-moment source remains SHA256
`2b429e4029fd7f50b30ea61b43d1be5aa22155b4c680c69440a716ff26643b2e`.
Complete step542 node/weight endpoints equal step553's selected inputs.
These are provenance checks reusing audited mathematical input; they
neither repeat the evaluator audit nor attest its backend.

Write S_j=w_1v_1^j+w_2v_2^j and t_j=m_j/m_0. Ascending coefficients are

\[
 p_j=(-1)^j\binom5j\frac{\gamma(j)}{\gamma(0)},\qquad
 q_j=(-1)^j\binom5j\frac{j!S_j}{(2j)!},\qquad q_0=1.
\]

Gaussian exactness gives p_j=q_j for j<=3 as an exact identity, not
from overlapping intervals. Hence E has only e_4=p_4-q_4>0 and
e_5=p_5-q_5<0. L807 gives, for these same moments and rule,

\[
 h_2=t_4-S_4>0,\quad B_2=(t_5-S_5)/h_2>0,\quad
 X_2=90h_2/(t_5-S_5)=e_4/(-e_5).                         \tag{4}
\]

The certificate encloses all these quantities. No actual fourth/fifth
moment is replaced by its Gaussian counterpart. Formula (4) follows
from L807; overlapping computed intervals are only a consistency check.

All subsequent arithmetic uses exact Fractions. Addition sums endpoints,
negation reverses endpoints/signs, multiplication takes extrema of four
products, and reciprocal division requires exclusion of zero. Node/weight
boxes are outward coarsened to 10^(-40) and coefficients to 10^(-50),
with containment checks. Correlation loss widens the boxes; coefficient
midpoints never replace the actual family. E_0,...,E_3 are exact zeros
from Gaussian exactness. Both the actual polynomial and its derivatives
are enclosed on the full boxes below. The slab is in (0,1) and its leading
coefficient box is strictly negative, so the degree cannot drop.

**Validated double root.** Set F(x,tau)=(H,H_x), so

\[
 DF=\begin{pmatrix}H_x&E\\ H_{xx}&E'\end{pmatrix}.
\]

At (c,t), enclose this matrix, take rational entrywise midpoints, and
invert the resulting point matrix to get A. Its determinant and det(A)
are nonzero. A need not equal the actual inverse. Put r=10^(-7),
Z_0=(c,t)+[-r,r]^2 and T(z)=z-AF(z). Interval Horner evaluation yields
F(c,t), DF(Z_0), A F(c,t) and I-A DF(Z_0), all saved in full. With

\[
 Y_i=\sup|(AF(c,t))_i|,\quad
 R_i=\sum_j\sup|(I-A DF(Z_0))_{ij}|,\quad Z_i=rR_i,
\]

exact rational comparisons give

| coordinate | R_i strictly below | Y_i+Z_i strictly below | required radius |
| --- | --- | --- | --- |
| x | 10^(-5) | 1.4*10^(-12) | 10^(-7) |
| tau | 4*10^(-8) | 3*10^(-13) | 10^(-7) |

Thus T is a strict contraction and strict self-map of a closed max-norm
box in its polynomial domain R^2. The imported criterion gives a unique
fixed point and, since A is invertible, exactly one F-zero in that box
for the fixed actual coefficients. All its x values are positive and
all tau values are in (0,1). Whole-box bounds give H_tau and H_xx as
in the conclusion. In particular the x root has multiplicity exactly
two. Dividing its x box by the positive X_2 box proves (1). Approximate
Newton values are not used as evidence.

**Uniform isolation and orientation.** Put I=[t-10^(-6),t+10^(-6)],
J=[c-1/10,c+1/10]. The event box is strictly inside I times J. At
real center m, the full Taylor intervals are

\[
 T_k(m,I)=\sum_{j=k}^5\binom jk(q_j+I e_j)m^{j-k}.
\]

At m=c, r=1/10, k=2, the lower dominant term in (3) exceeds 1.2
times the other upper sum (actual ratio >1.2128). This certifies two
roots in the fixed event disk for every tau in I. At the three centers
(2), exact complex Taylor rectangles give strict k=1 inequalities at
the same radius. For U+iV use max{dist(0,U),dist(0,V)} as a lower
modulus bound and max|U|+max|V| as an upper bound; no floating square
root enters. Every raw strict margin is positive. The coarse display
comparisons for the nonreal centers are not themselves decisive and
are not used in place of these raw comparisons. Exact squared distances
exceed squared sums of radii. The four disjoint counts 2+1+1+1 exhaust
degree five. Conjugation and the disks' distance from zero/the real axis
give the one positive root and separate nonreal pair of (2).

The following hold uniformly on the full rectangle J times I:

\[
 -.000304<H_{xx}<-.000155,\qquad E>.409.
\]

At both J endpoints H<-2*10^(-7); at the left endpoint
H_x>2.28*10^(-5), and at the right H_x<-2.28*10^(-5).
At tau_* strict concavity and H=H_x=0 give H(x,tau_*)<=0 for every
x in J, with equality only at x_*. For tau<tau_*,

\[
 H(x,tau)=H(x,tau_*)-(tau_*-tau)E(x)<0\quad(x\in J).
\]

So the isolated two-root disk has no real root; its two roots are
distinct simple nonreal conjugates by reality and the count. For
tau>tau_*, H(x_*,tau)=(tau-tau_*)E(x_*)>0, whereas both J endpoints
remain negative. The intermediate value theorem supplies a positive
root on each side of x_*; the disk count makes both simple and excludes
further roots there. At tau_* H_xx!=0 makes the positive root exactly
double. This proves orientation throughout this explicit slab, without
tracking a branch to either remote endpoint.

Additional strict side checks are saved. At tau=t-10^(-6), let
a=H(c,tau), b=H_x(c,tau), m=-sup_J H_xx>0. Taylor's inequality gives
H(c+y,tau)<=a+by-my^2/2<=a+b^2/(2m). Its interval upper bound is
<-4*10^(-7). At tau=t+10^(-6), H(c,tau)>4.1*10^(-7) and both
J endpoints are negative. These certify explicit side evidence as well.

**Evidence and bounds of the attempt.** Reproduce with
`python3 scripts/theta-gauss/compensation_crossing_555.py --validate`.
The complete `scripts/theta-gauss/compensation-crossing-certificate-555.json`
has 114 passing checks and no failures. It retains all coefficients,
analytic corrections, moments/defects, Jacobians/residuals, preconditioner,
radii/strictness, complete Taylor/Pellet data, side signs and provenance.
The single elimination proposal and one unvalidated Newton iteration are
preserved in `scripts/theta-gauss/compensation-proposal-555.json`.
They only select (c,t); a midpoint root list only selects (2).

The initial radius-one neighborhood failed the coarse uniform concavity
test. Its other-root proposal filter also wrongly kept only real
candidates; that short list was not a certified root count. Preserve
the complete initial failure in
`scripts/theta-gauss/compensation-crossing-initial-555.json`. The sole
permitted refinement shrank the pair disk to radius 1/10 with the same
event box and parameter slab; the corrected proposal retains all three
other roots. No degree, node count, precision, family or branch sweep
occurred. Implementation type/endpoint-format errors were repaired before
final validation and have no evidentiary role.

L808's endpoint geometry is a contrast, not a premise identifying this
pair. The event coexists with another nonreal pair and is not a transition
to five real roots. This is local progress by specialization of known
methods, without a claim of progress beyond their general conclusions.
All-degree compensation and actual-Xi mixed positivity remain open.

### Independent conceptual and arithmetic audit — 5 November 2026, step557

The invocation-start SPECIALIZE assessment was
`drafts/literature/2026-11-05-theta-compensation-crossing-audit.md`.
Run `python3 scripts/theta-gauss/compensation_audit_557.py`.
The complete independently reconstructed evidence is
`scripts/theta-gauss/compensation-audit-certificate-557.json`:
259 checks pass, with no failures. The checker imports no producer code,
uses only Python standard-library exact rational arithmetic, and does not
run a fresh theta evaluation or a root proposal. No mathematical defect
or change to the conclusion was found. This is conventional reproduction
of a finite specialization, not a new general sign result.

**Actual inputs and correlation.** All entries of the saved step478,
542, 551, 553, final555, proposal555 and initial555 hash maps agree with
the current files. The relevant producer/imported-program hashes and
step433 evaluator/checker hashes agree too. The fixed ancestor and moment
digests above are unchanged, and the entire evaluator object equals the
step433 replay. Prior PASS flags and check lists are retained as audit
history; they do not establish the reconstructed arithmetic.

The checker rebuilds all six Cauchy additions from the complete source
endpoints. In particular order five adds E_G/1600^5 before multiplying
by 8*4^5*5!=983040. L778's complex-disk estimate applies to that analytic
coefficient, not to a differentiated real error. The gamma(0) lower
endpoint is strictly positive, so normalization is permitted. Orders0..4
are enclosed by L791's prior Decimal boxes; the new order5 retains the
full source cell width and analytic error. This reuses L778's analytic
audit and software contracts without attesting the backend anew.

Every node/weight endpoint is taken from audited L805's independent
boxes; their full equality with step553's selected inputs and all outward
roundings are checked. All moments through five, P,Q,E coefficients,
h_2,B_2,X_2 and the event ratio exactly reconstruct the final certificate.
The six coefficient factors are
1,-5/2,5/6,-1/12,1/336,-1/30240. L805's Gaussian identities, for the
same actual law, give S_j=t_j for j<=3. Thus E_0=...=E_3=0 exactly;
an interval overlap is not used as an identity. L807 gives both remaining
defects, and (1/336)/(1/30240)=90 verifies the normalization in (4).
Independent boxes lose coefficient correlations conservatively: the
single fixed actual family is contained in every box used simultaneously.
Neither midpoints nor unrelated polynomials replace that family.

**Whole-box fold.** Every entry of F(c,t), the center and whole-box
Jacobians, the point matrix, its inverse A, AF(c,t), I-A DF, both row
norms and both self-map margins exactly matches an independent
reconstruction. The point matrix times A is the identity in exact
rational arithmetic and det(A)!=0. The row norms are approximately
9.741207651e-6 and 3.688913440e-8, both strictly below1; the corresponding
Y_i+Z_i are approximately 1.353904834e-12 and 2.880949664e-13, each
strictly below r=1e-7. These approximations are displays only; all strict
comparisons use full rational values in the certificate. The polynomial
map is C1 on all R^2, so its closed box lies in an open smooth domain.
The derivative bounds hold on every point of that box and every segment
joining two of its points. Banach therefore supplies a unique fixed point;
invertibility of A makes it an F-zero. Strict H_tau>0 and H_xx<0 on the
event box verify both fold nondegeneracies and exact multiplicity two.
All displayed coordinate, derivative, X_2 and ratio bounds are checked.

**Every uniform root count.** Independently reconstructed Taylor
rectangles, modulus bounds, radius powers, dominant lower terms and full
omitted-term upper sums agree at all four centers. Dominant/other ratios,
in the event, real, lower nonreal and upper nonreal disks respectively,
are approximately 1.212837241,79.14492617,10.38301150,10.38301150.
The complete rational margins are strictly positive. The nonreal disks'
coarse display bounds are valid but not decisive; the raw inequalities
are decisive. All six separation margins are positive. The leading
coefficient is uniformly negative, so the counts2+1+1+1 exhaust the exact
degree five for every parameter in the slab, including tau_*.
The event and real disks are invariant under conjugation; the other
two disks are conjugate and avoid the real axis. A count-one root in
the real disk is consequently real and simple, and that disk is positive.
Each nonreal disk contains one simple root. All boundary roots are
excluded by strict Pellet dominance.

**Full slab, not endpoint inference.** The event box lies strictly inside
J times I. The independent full-rectangle enclosure for H_xx has endpoints
approximately -.00030323861245 and -.00015583781056. Its upper endpoint
is negative; the E lower endpoint exceeds .40972164285. Both full-slab
endpoint upper values are below -2e-7, and the slope signs and both
separate side checks also reconstruct exactly. For the fixed actual
tau_*, Taylor's theorem and H_x(x_*,tau_*)=0 give
H(x,tau_*)<0 whenever x in J differs from x_*. For every tau<tau_* in I,
subtracting (tau_*-tau)E(x)>0 gives strict negativity on all of J.
Any real root in the open event disk would lie in J, so none exists.
Conjugation and the multiplicity count two then give two distinct simple
nonreal roots: a repeated nonreal root would require its conjugate with
the same multiplicity and hence at least four roots in this disk.
For tau>tau_*, positivity of H(x_*,tau) and the two negative endpoints
give roots in both open intervals on either side of x_*. They lie inside
the disk; its multiplicity count two makes them simple and exhausts it.
At tau_* the already validated double root exhausts this disk. Thus
the full-slab one-to-three real-root count is justified, while the
separate nonreal pair persists. This argument does not identify remote
branches or infer an interior result from actual P_5 endpoint hyperbolicity.

The initial radius-one curvature box is independently reconstructed and
contains zero; the original single-other-disk proposal and both failure
labels remain unchanged. That neighborhood is still unvalidated. The
successful radius1/10 certificate is assessed on its own full evidence.
The saved qualification that mentions L808 does not import a conclusion
from L808: only prior input provenance is used here. L808 remains a
contrast and adds no mathematical premise or DAG edge. All-degree signs,
uniform compensation, formal arithmetic verification and independent
backend attestation remain outside this audit.

## Mathlib

Full matching coverage has not been checked. Availability of the actual
theta specialization, augmented fold certificate and uniform Pellet
counts is unknown. No formal verification or absence claim is made.
The cited general theorems and inherited audited analytic/backend
contracts remain the precise informal inputs.
