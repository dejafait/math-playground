# Corollary 919d: fixed-rectangle reality and positive-time simplicity (audited)

## Hypotheses

Use L019's positive theta kernel and L058's actual family

    F(lambda,z)=integral_0^infinity exp(lambda*u^2) K(u) cos(zu) du,
    0<=lambda<=1/20,
    Omega={z: |Re z|<100, |Im z|<1/2}.

Use C919c's audited full closed-band boundary nonvanishing, retaining
its inherited C919b Python 3.15.2 Decimal arithmetic contracts and
L919 normalization. Those contracts are not independently verified
or strengthened here. Use L018's initial zero correspondence and the
two precisely cited external theorems below. No initial simplicity,
numerical zero census, RH or global reality assumption is made.

## Conclusion

Every zero of F(lambda,.) in Omega is real for 0<=lambda<=1/20.
Every such zero is simple for 0<lambda<=1/20, including lambda=1/20.
Initial zeros retain arbitrary multiplicities in the hypotheses; no
initial simplicity conclusion is asserted. The result inherits the
stated arithmetic qualifications of the boundary input.

This is a local application of known theorems, not a new propagation
theorem or a resolution of RH. It provides no explicit zero count,
brackets, separation, weights or uniform numerical head margin. In
particular it does not pay C919c's required margin above 1/2000000000,
all-degree mixed positivity or any global extension.

## Proof

### Imported theorems

Import Michel Planat and Dale James Raymond, *Certified Collision
Exclusion and an Unconditional Upper Bound Lambda<0.156821 for the
de Bruijn-Newman Constant*, arXiv:2611.06245v1, 4 November 2026,
Section 7, Theorem 7.2 (Compact interior propagation), with its
Lemma 7.1: https://arxiv.org/html/2611.06245v1#S7.
For T,X,Y>0 and Omega={|Re z|<X,|Im z|<Y}, the theorem requires
joint holomorphy near [0,T] times the closed rectangle, F_t=-F_zz,
real type at real times, nonvanishing on the entire boundary at all
times, and reality of all initial interior zeros. It concludes interior
reality and simplicity for 0<t<=T, allowing initial multiplicities.
Only this analytic theorem is imported from the recent preprint.
Its global bound and computational artifacts are not inputs.

For the initial zero locations import Dave Platt and Tim Trudgian,
*The Riemann hypothesis is true up to 3 times 10^12*,
arXiv:2004.09765v1, Theorem 1, printed p. 2:
https://arxiv.org/pdf/2004.09765v1.
It verifies critical-line location through height 3,000,175,332,800.
Section 2 explains the sign-change count and Turing comparison
accounting for all zeros. Only location in the much smaller required
range is used here; no brackets or simplicity are imported.

### Initial rectangle, both ordinate signs and zero ordinate

L058 identifies F(0,z)=Xi(z). By L018, an initial zero corresponds
with its full multiplicity to a nontrivial zeta zero rho=beta+i*gamma,
where

    z=gamma+i*(1/2-beta).

If 0<Re z<100, then 0<gamma<100<3,000,175,332,800, so
Platt-Trudgian gives beta=1/2. Thus z is real. If -100<Re z<0,
L018's conjugation symmetry makes beta-i*gamma a zero of xi with
positive ordinate -gamma<100, with the same multiplicity. Apply the
same theorem to that zero, giving beta=1/2 again.

For Re z=0 write z=i*y, y real. Specialize the positive-kernel
argument in Planat-Raymond Section 7.1 to the local integral:

    F(0,i*y)=integral_0^infinity K(u) cosh(y*u) du>0.

L019 supplies K(u)>0 on u>=0. L058's compact domination supplies
convergence for each y, and cosh(y*u)>=1. Thus this case contains no
zero, including y=0. This checks the ordinate omitted from the
positive-height theorem without assuming initial simplicity. Every
initial interior zero is therefore real, with all copies retained.

### Exact application and qualifications

Apply Theorem 7.2 directly to F with T=1/20, X=100, Y=1/2.
All three constants are positive. L058 gives joint entirety on C^2,
the required conjugation symmetry for real lambda, and exactly
F_lambda=-F_zz. Hence the required complex neighbourhood and heat
sign hold without a rescaling. L919's relation F(lambda,z)=
8H_(4lambda)(2z) is inherited only through the boundary certificate;
using H_(lambda)(2z) instead would have the wrong time normalization.

C919c covers the entire boundary for every time in [0,1/20], with
corners and both time endpoints included. Its horizontal boundary
proof uses L018 at zero time and the strictly narrower de Bruijn
strip at positive times. Its right vertical side uses C919b's
audited certificate; evenness supplies the left side, with the same
arithmetic contracts. There is no unpaid missing side or endpoint.
No uniform numerical full-boundary modulus estimate is asserted.

The initial-zero hypothesis was checked above. The cited theorem now
gives the stated positive-time conclusion; the initial conclusion is
already paid by the finite-height input. In particular the theorem's
closed positive-time endpoint gives simplicity at lambda=1/20.
Its treatment of an initially multiple zero is part of the imported
theorem, not an implicit simple-branch assumption in this application.
No propagation toward smaller time or infinite-zero continuation is
used. This completes the citation-based application.

The exact source hypotheses, Lemma 7.1's backward multiple-root case,
and Theorem 7.2's endpoint case were checked in the prior step2159
assessment and reopened in step2160. No new propagation reproof or
mathematical computation was necessary. The existing outer-only,
inner-evaluator and L917/L920/L922 stops are unchanged: qualitative
reality and simplicity supply no numerical head eigenvalue bound.

### Independent conceptual audit, 21 November 2026 (step2165)

**Verdict.** Accepted with the original rectangle, closed time band,
initial multiplicity allowance and arithmetic qualifications. No
mathematical correction, stronger conclusion or dependency change is
needed. This is the first independent conceptual audit of this saved
application, classified KNOWN_IMPORTED under the unchanged step2159
IMPORT assessment. It verifies a local use of known results, not
progress beyond the inspected theorems or a candidate proof of RH.

**Analytic hypotheses and coordinates.** Read L058's full domination
proof, not merely its local simple-branch statement. Its majorant (1)
works for complex lambda on each compact set and for every mixed
derivative, so the theorem has an open complex neighbourhood of both
time endpoints. Differentiating twice in z gives the minus sign in
F_lambda=-F_zz; the real integral gives conjugation at every real time.
The source PDE applies to F itself. Rechecked L919's kernel identity
K(u)=4Phi(u/2) and substitution u=2w: the inherited boundary coordinates
are t=4lambda and source position 2z, not t=lambda. The factor 8 is
nonzero and changes neither zeros nor their multiplicities.

Read L018's affine map and L019's strictly positive complete kernel.
For both signs of Re z, the required positive zeta ordinate is less
than 100. Platt-Trudgian v1, Theorem 1 and Section 2, printed p.2,
were reopened at the cited PDF: its verified range exceeds 100, and
its Turing comparison accounts for all zeros, not a sample. Only
location is used. At Re z=0, L058's domination and L019's positivity
justify the displayed cosh integral; it is strictly positive. There
is no discarded zero copy or implicit initial simplicity assumption.

**Boundary contract.** Read C919c's entire boundary argument and its
independent audit, C919a's strip specialization, and C919b's hypotheses,
arithmetic contracts and endpoint audit. Polymath v2 Theorem 3.2 was
reopened. Its strict t>t0 hypothesis is respected: L018 separately
pays lambda=0. For positive lambda the local squared height bound is
1/4-2lambda<1/4, including lambda=1/20. The horizontal sides and
corners are therefore excluded. C919b covers the closed right side;
evenness gives the left side with the sign of y reversed. Its
zero-time limit retains a strict normalized margin and a nonvanishing
normalizer. This audit consumes that accepted certificate under its
Python 3.15.2 Decimal contracts; it neither reruns nor independently
verifies the arithmetic implementation. The theorem needs qualitative
full-boundary nonvanishing, not a supplied numerical global minimum.

**Imported proof cases.** Reopened Planat-Raymond v1 Section 7,
Lemma 7.1, (22)-(23), and Theorem 7.2 with their complete proofs.
The scaled Taylor quotients are holomorphic at scale zero. Gaussian
orthogonality gives distinct real forward Hermite roots; symmetric
Rouche disks make each perturbed root real and simple. A fixed disk
exhausts the cluster. Backward splitting retains a nonreal pair even
for odd multiplicity; the possible central root does not remove it.
The compact zero-free complement excludes untracked zeros. At the
supremum of persistence, off-axis disk persistence rules out nonreal
zeros, and backward splitting rules out multiple zeros. These nearby
earlier zeros stay inside the rectangle. The same argument includes
the final time; the empty census is vacuous. No uniform separation or
infinite trajectory enumeration is assumed. Polymath v2 Proposition
3.1(i)-(ii), including its final exhaustive Rouche count, agrees with
the local heat sign and repeated-root cases; it is a comparison,
not a substitute for the compact theorem. No reproof is needed.

**Limits.** Initial multiple zeros remain permitted; simplicity is
asserted only for positive time. The accepted conclusion gives no
actual three-interval placement, separation constant or numerical
head eigenvalue bound. C919e remains conditional on its hypothetical
box. The original confinement, outer-only, inner-evaluator and
L917/L920/L922 stops remain in force in their stated scopes. There
is no backward-time propagation, global preprint claim or unstated
RH input. No mathematical script was required for this analytic
hypothesis audit. Full matching Mathlib coverage remains unchecked.

## Mathlib

Full matching coverage of this compact heat-flow propagation theorem,
finite-height input and computer-assisted boundary application has
not been checked. No matching formal theorem is asserted. Supporting
holomorphy or implicit-function results alone would not constitute
the full multiple-root propagation statement; unknown coverage is
not evidence of absence.
