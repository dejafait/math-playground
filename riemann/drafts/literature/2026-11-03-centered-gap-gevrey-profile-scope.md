# Source assessment: weighted decay of the exact centered-gap profile

TARGET: Assess whether the L694/L696 prescribed-center Picard construction admits one fixed profile with sum_m exp(c*sqrt(1+|m|))*|e_m|<infinity for some c>0, retaining L702's smallness condition and the fixed positive centered gap.
CHECKED: 2026-11-03
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 141 checked L694 (1)--(11), L696 Section 2, L702 Section 2/audit, L695's statement/stop and the step-110/112/139 assessments; searched exact and stronger weighted/Gevrey/Kargaev prescriptions and inspected the primary sources below. No inspected theorem states this exact reflected anchored weighted conclusion; no originality inference.
SOURCE_EVIDENCE: Lev arXiv:2007.09930v3, Lemmas 4.2--4.3 and complete proofs (4.5)--(4.13), Sections 4.5--4.10; Mourrat--Weber, Ann. Probab. 45 (2017), Section 2.1 p.2405 and Appendix Propositions 23--24 with complete proofs pp.2472--2473; Dasgupta--Ruzhansky, Bull. Sci. math. 138 (2014), Definition 2.1/Theorem 2.3(R) pp.761--762 and forward proof pp.771--773; Groechenig arXiv:math/0611174v1, Lemmas 2.1(a) and 4.1 with its complete discrete proof, PDF pp.3--5. Exact hypotheses, versions and limits below.
COMPARISON: Known results supply Gevrey cutoffs, derivative-controlled Fourier decay and weighted convolution; Lev supplies the exact supported Picard map and parameter-integral coefficient proof. They cover the general tools, not the uniform weighted nonlinear estimate or same-limit conclusion. Reuse step 110's stronger unanchored Kargaev comparison; no matching import is claimed.
GAP: Prove a parameter-uniform weighted coefficient estimate for the unchanged E_m, weighted convergence of the same Y Picard iterates, and a compatible choice of fixed Gevrey cutoffs/C/r/w/c meeting L702's unweighted smallness. No weighted estimate or compatible selection is established in this literature turn.
REASON: Essential tool coverage now suffices for one bounded specialization attempt on the unchanged target. The required application is the weighted version of L694's two-norm argument, not a reproof of Gevrey Fourier decay or Lev's prescription theorem. L695's absolute-cost stop and L702's endpoint-only stop remain in force at their stated scope.
LITERATURE_REASON: The new hypothesis is a positive stretched-exponential weighted l1 norm of the exact Picard profile, outside the previously assessed unweighted norms and endpoint audit. A separate literature-only turn is required before any derivation or mathematical script for it.
SCOPE: Exactly TARGET. Preserve L694's actual reflected Q and same supported real-coefficient fixed point, L696's prescribed center, a positive gap fixed before n, real cap 1/8, unit masses and the fixed anchor, and L702's smallness condition. If later used in the finite response, retain n=12q+3, both actual endpoints, all n factors including j=0, inverse angle and all M spatial moments. No cross-notebook input.

## Original nomination (preserved)

The nomination below records the state before step 141. Its pending
source language is superseded by the completed comparison below;
all proposed weighted mathematics remains unproved.

This is a continuation nomination, not a source approval or mathematical
attempt. No weighted estimate, compatible parameter selection or new
lemma is asserted. The main gap remains actual-Xi all-degree mixed
positivity and unbounded-height signs.

The proposed bounded mechanism is a weighted estimate for the same
nonlinear Picard map, potentially using a Gevrey-2 choice of its compact
cutoffs. The literature review must identify primary theorem statements
and their constant dependence, inspect the relevant proof cases, and
check duplicates and obstructions. It must distinguish decay of the
prescribed data from decay of the solution. In particular, a weight
parameter chosen after the narrow prescription width cannot silently
change the earlier contraction radius or replace the fixed point.

The essential local construction is L694 (2)--(9) and L696 Section 2.
L702 Sections 2 and 7 supply the additional unweighted smallness
interface. Their established conclusions are reused; the proposed
weighted coefficient bound, weighted convergence and compatible order
of choices remain unproved. The uniform Wiener bound in L702 is not
asserted to hold in a fixed weighted norm as the width shrinks.

A possible downstream use is quantitative control of truncation errors
within a signed analysis of the interior and angular transition terms.
The L695 failure still prevents treating ordinary summable tails as a
paid absolute perturbation on the full circle. Even a successful
weighted construction would not by itself pay exponential rational
amplification, angular logarithmic singularities, numerator-zero charge,
full-spatial comparison, H/support or Xi realization. Those are separate
gaps; no scalar compensation conclusion is presumed.

The review should continue only if it finds an import or sufficiently
precise source coverage for a bounded weighted fixed-point test with
one positive width and one positive weight parameter fixed before n.
If the exact weighted assertion is already known, import it with the
necessary applicability argument. If a source proves incompatibility,
or the proposed estimate cannot be scoped without an essential missing
theorem, record that obstruction or missing input. Do not repeat the
endpoint expansion, sign test, microscopic pairing or absolute-tail
closure under a different name. This nomination does not reset any
exploration or recovery counters.

Matching Mathlib coverage has not been checked. Next-turn work is
literature_comparison (standard/high), because the issue is theorem and
constant applicability before proof development; there is no approved
creative proof target yet.

## Completed comparison, 3 November 2026, step 141

This is a source review only. No lemma, nonlinear estimate, new
parameter selection or mathematical script was produced. SPECIALIZE
authorizes testing the identified applicability difference after the
supervisor's separate approval; it does not assert TARGET is true.

### Primary hypotheses and relevant proof cases

**Exact nonlinear input.** N. Lev, *An example concerning Fourier
analytic criteria for translational tiling*, Rev. Mat. Iberoam. **38**
(2022), 1975--1991, DOI
[10.4171/RMI/1318](https://doi.org/10.4171/RMI/1318).
Reuse step 139's publisher collation: Lemma 4.3 p.1984 (4.6).
Newly read [arXiv:2007.09930v3](https://arxiv.org/html/2007.09930v3#S4.SS3),
27 September 2021, Lemmas 4.2--4.3 and complete proofs, (4.5)--(4.13).
For a fixed smooth supported Phi and smooth varphi with varphi'(0)=0,
the latter gives the coefficient bound
max(|u|,|v|)*C*|v-u|/(1+|k|^m), for |u|,|v|<=1,
with C depending on Phi,varphi,m. Its proof integrates
varphi'(s*t)*Phi(t) between u and v; the zero and nonzero frequency
cases of Lemma 4.2 were inspected. The m-dependent constants are not
Gevrey bounds as stated. The supported-distribution definition of R,
Lemmas 4.5--4.7 and prescription/reflection cases in Sections 4.9--4.10
were also inspected, reusing the ready step-139 assessment. These
establish bounded-output existence, not the requested weighted output.

**Cutoffs and decay.** J.-C. Mourrat and H. Weber, *Global
well-posedness of the dynamic Phi4 model in the plane*, Ann. Probab.
**45** (2017), 2398--2476, DOI
[10.1214/16-AOP1116](https://doi.org/10.1214/16-AOP1116),
[published primary PDF](https://sites.math.northwestern.edu/~auffing/papers/MourratWeber.pdf).
Read Section 2.1, Definition 1 and the plateau construction, p.2405:
for theta>1 compact Gevrey cutoffs can equal one on a compact set and
vanish outside its chosen neighborhood. The construction uses
exp(-x^(-1/(theta-1))) on x>0, products and convolution; its cited
Rodino Example 1.4.9 was not separately read. Read Appendix
Propositions 23--24 and complete proofs, pp.2472--2473.
For theta>=1 the class is closed under products; for compactly
supported f in that class, |f-hat(zeta)|<=C exp(-a|zeta|^(1/theta))
on real frequencies. The proof uses common factorial derivative
bounds and the support; its constants are not uniform over arbitrary
smooth inputs. Theta=2 is the relevant case. The statements concern
real functions; complex use must treat both components. No nonlinear
Picard regularity theorem is supplied by this source.

**Periodic version and constant dependence.** A. Dasgupta and
M. Ruzhansky, *Gevrey functions and ultradistributions on compact Lie
groups and homogeneous spaces*, Bull. Sci. math. **138** (2014),
756--782, [published primary PDF](https://backoffice.biblio.ugent.be/download/8585191/8585192).
Read Definition 2.1 and Theorem 2.3(R), pp.761--762: on a compact
Lie group G, for s>0, derivative bounds C*A^|alpha|*(alpha!)^s
characterize coefficient decay K exp(-B*<xi>^(1/s)) for some K,B>0.
Read Lemma 3.5 and the complete forward case of Theorem 2.3 through
(3.21), pp.771--773, including trivial representations. The proof
tracks the derivative constants into a positive decay exponent.
For G=R/Z the irreducible characters are exp(2*pi*i*k*t), have
dimension one, and the standard Laplacian eigenvalues are
-(2*pi*k)^2. Thus s=2 covers the needed periodic Fourier convention,
with metric constants absorbed in the decay rate. Applying this to
each member of a parameter family separately would not supply uniform
K,B: common derivative constants must first be verified. Neither the
converse proof nor the ultradistribution theorem is needed or imported.

**Weighted summation tool.** K. Groechenig, *Weight Functions in
Time-Frequency Analysis*, Fields Institute Communications **52**
(2007), 343--366; inspected
[arXiv:math/0611174v1](https://arxiv.org/pdf/math/0611174v1),
7 November 2006, Lemma 2.1(a) and Lemma 4.1, PDF pp.3--5,
against the [Fields PDF](https://www.fields.utoronto.ca/programs/scientific/06-07/ISAAC/grochenig.pdf).
The former includes v(k)=exp(c*|k|^(1/2)), c>=0, among
submultiplicative weights. The latter states that l1_v(Z^d) is a
Banach convolution algebra for a submultiplicative v; the full
discrete proof gives norm bound ||a*b||_(1,v)<=||a||_(1,v)||b||_(1,v).
Use d=1. The exact target's exp(c*sqrt(1+|k|)) differs from this
weight by a factor between 1 and exp(c), so finiteness is equivalent;
any norm comparison constants must be retained. This theorem applies
to an established coefficient majorant, not automatically to R.
No weighted inversion or GRS theorem is needed.

### Duplicates, stronger comparisons and access limits

L694 already proves the unweighted same-limit statement; L696 locates
its center, and L702 supplies the width-uniform unweighted bound and
smallness selection. None states the new weighted claim. The scoped
search of their assessments found no matching weighted result.

Reuse the inspected Kargaev comparison in
`drafts/literature/2026-11-03-anchored-fourier-gap-summable-shifts.md`,
Section "Stronger comparisons and reading limits": Kargaev,
Math. USSR-Sb. **45** (1983), Theorem 1 pp.405--406 and Section 4.2
p.409 give stronger unanchored decay/zero-prescription context.
Its omitted OCR conditions are not premises here. KL16 Theorem 2.1
has an unanchored l2 conclusion. Neither comparison identifies the
same exact reflected anchor-cancelling solution. Their full proofs
were not reread or newly certified.

Followed Lev's reference to Kargaev--Volberg, Indiana Univ. Math. J.
**41** (1992), 1143--1164, DOI 10.1512/iumj.1992.41.41057.
Its [publisher record](https://iumj.org/article/3589/) was located,
but full-text retrieval timed out; a PDF access attempt also failed.
It remains an unread theorem-level lead, not evidence for or against
TARGET. This is not an essential blocker: Lev's accessible full
coefficient proof and the inspected Gevrey/weighted tools suffice for
the bounded application test. Shell download of Mourrat--Weber failed
DNS, but the complete relevant text was read through web access.
No access failure is treated as a mathematical obstruction.

Representative executed queries (including unproductive ones):

- `Gevrey compact support Fourier coefficients exp sqrt n weighted Wiener algebra fixed point`
- `Nir Lev example Fourier analytic criteria tiling spectral weighted decay perturbations integers Gevrey`
- `Dasgupta Ruzhansky Gevrey Fourier coefficients compact Lie groups Theorem 2.3 pdf`
- `Mourrat Weber Gevrey appendix compact support Fourier decay smooth cutoff`
- `weighted Wiener algebra submultiplicative weight exp sqrt Banach algebra Grochenig weights time frequency analysis pdf`
- `"Lev" "tiling" "Gevrey" perturbations`
- `"Fourier analytic criteria" "decay" perturbations`
- `"Kargaev" "perturbations" "decay"`
- `"spectral gap" "perturbation" "Gevrey"`
- `"Lev" "integers" "subexponential" Fourier`
- `"Kargaev" "exponential" gap`
- `Kargaev Volberg 1992 perturbation integers Fourier transform rapid decrease`
- `"Kargaev" "rapidly"`
- `"Kargaev" "decay" "Fourier" gap`
- `"Three results concerning the support" pdf`
- `"Kargaev" "Volberg" "decay" "1992"`

Irrelevant search hits were not theorem inputs. A bounded search cannot
establish novelty. Matching Mathlib coverage was not checked; this is
unknown availability, not an absence claim.

### Approved application difference and bounded test

The target is unchanged. Choosing Gevrey-2 cutoffs at the outset is
allowed by L694's selectable smooth-cutoff hypotheses; this is not a
regularity assertion about every previously selected arbitrary smooth
profile. For any selected Phi and exact reflected Q, the solution
must remain the unique Y-ball limit of that same Picard map.

One future proof attempt may test a single parameter-uniform weighted
majorant for L694's E_m(v)-E_m(u), for all real |u|,|v|<=r, all m,k,
retaining the factor r*|v-u| and an off-diagonal stretched-exponential
decay. It must specify constants depending only on the initial kernel,
not the later data width or unknown solution. Import the Fourier-decay
and convolution results above; derive only their applicability to the
exact nonlinear family and same iterates. No bound is asserted here.

The subsequent same-limit argument and order of choices are essential
parts of this one test: establish weighted convergence without
requiring a small weighted norm of Q, and exhibit positive r,w,c fixed
before n with coefficient cap r<=1/8 and r*||e||1<=1/(16*pi^2).
If shrinking w requires a smaller c, the proof must verify that this
does not invalidate an earlier contraction choice; the literature
does not pay that compatibility automatically. The width-uniform
unweighted estimate of L702 may be reused for smallness. No
width-uniform positive weighted exponent or weighted-data norm is
required. Psi only enters through its specified values on Q's support;
unprescribed behavior elsewhere must not become a hidden hypothesis.

Continue only upon a complete same-limit and compatible-choice proof,
or an informative counterexample to a claimed needed estimate. Stop
the proposed weighted-contraction mechanism if it requires changing
the prescription, masses, anchor, or gap as n varies, or if an
uncontrolled dependence makes its simultaneous conditions unsupported.
A failed sufficient estimate does not refute existence of all weighted
profiles. Repeating the accepted endpoint expansion or ordinary l1
argument is not a new test.

The plausible downstream use remains signed interior/transition
truncation control. This assessment supplies no scalar logarithmic
charge, exponential amplification payment, full-spatial mean, H/support
or Xi realization. It neither reopens L695's stopped absolute closure
nor treats a stronger decay adjective as an RH argument. If a later
attempt changes the weight class, prescription, or finite-response
claim, that changed target requires a new source comparison.
