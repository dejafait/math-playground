# Lemma 377: unbounded actual full-multiplicity count deficit

## Hypotheses

Let F_0 and G be exactly the zero-regulator transform and its right
regulator response in L366 (1). Thus, with the entire completion xi_c
of L018,

\[
 F_0(t)=2\xi_c(1/2+it),\qquad
 G(t)=-(t^2+1/4)\operatorname{Re}
          \frac{\xi_c(5/2+it)}{5/2+it}.
\]

Use ordinary real derivatives. Choose one finite H_*>=2pi above the
eventual onsets in L372 and L368. For a fixed H>=H_* and X>=H,
N_U^mult([H,X]) denotes the number of real zeros of U in the closed
interval, with full analytic multiplicities. By L372 the zeros of G
on this ray are simple, so its multiplicity count equals its distinct
count, denoted N_G([H,X]). No RH, simplicity of F_0 zeros, common-zero
exclusion or discriminant sign is assumed.

## Conclusion

For every fixed H>=H_* there is a finite real constant K_H such that,
for every sufficiently large T, some X in [T,2T], away from every
positive ordinate of every nontrivial zeta zero, satisfies

\[
 N_{F_0}^{\rm mult}([H,X])-N_G([H,X])
       \le K_H-\sqrt{\log\log T}.                    \tag{1}
\]

In particular this difference is unbounded below on every such fixed
ray, with witnesses tending to infinity. No effective onset or value
of K_H is asserted.

For the actual pair define, as in L374,

\[
 \mathscr L(U)=U'^2-UU'',\quad
 B=2F_0'G'-F_0G''-F_0''G,\quad
 D=B^2-4\mathscr L(F_0)\mathscr L(G).
\]

There is no eventual ray on which **both** F_0 and G have no common
real zero and D<=0 holds everywhere. This excludes only that conjunction.
It does not separately decide eventual disjointness or D<=0, sign the
total L367 margin, extend a Laguerre-sign/zero-exclusion range, or
resolve RH. The specialization is a **REPRODUCTION** of known count
oscillation, not a new oscillation theorem. The separate critical audit
below retains the statement without correction or strengthening.

## Proof

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-07-signed-count-deficit-specialization.md`;
its parent records the inspected primary statements and essential proof
cases. We import those theorems rather than reprove them.

**Precisely cited unconditional inputs.** Alexander Dobner, *Large
deviations of the argument of the Riemann zeta function*,
[arXiv:2101.01747v2](https://arxiv.org/html/2101.01747v2),
25 March 2024, Theorem 1 (PDF p. 2), with definitions/(1) on pp. 1–2
and the negative-sign proof case in the final paragraph of Section 6,
pp. 18–20, supplies constants kappa,d>0 such that, for every sufficiently
large T and every

\[
 \sqrt{\log\log T}\le V\le
 \kappa\left(\frac{\log T}{\log\log T}\right)^{1/3},
\]

\[
 \operatorname{meas}\{t\in[T,2T]:-S(t)\ge V\}
 \ge T\exp\left(-\frac{dV^2}
       {\log(\log T/(V^3\log V))}\right)>0.          \tag{2}
\]

This is its unconditional Theorem 1, not its RH-dependent Theorem 2.
S is the standard argument divided by pi: its branch starts real at 2,
with horizontal cuts to the left of zeros and the pole, and takes
averaged limits at jumps. At heights that are not zero ordinates this
agrees with the usual path from 2 to 2+it to 1/2+it.

Richard P. Brent, David J. Platt and Timothy S. Trudgian, *Accurate
estimation of sums over zeros of the Riemann zeta-function*, Math. Comp.
**90**, no. 332 (2021), 2923–2935,
[published author offprint](https://maths-people.anu.edu.au/~brent/pd/rpb276-MC-preprint.pdf),
[DOI 10.1090/mcom/3652](https://doi.org/10.1090/mcom/3652),
p. 2923 and Section 2, (5)–(8), Lemma 2 and proof, pp. 2926–2927,
give the full-multiplicity total-strip convention and normalization.
Writing

\[
 M(t)=\frac{t}{2\pi}\log\frac{t}{2\pi}-\frac{t}{2\pi},
\]

their total count N(t), with half weight at an upper endpoint ordinate,
satisfies, for t>=2pi,

\[
 N(t)=M(t)+7/8+S(t)+R(t),\qquad
 |R(t)|\le\frac1{150t}.                            \tag{3}
\]

The branch conventions agree with Dobner's. We use (3) only off all
zero ordinates, where no half-weight term remains. Both inputs are
unconditional and count all strip zeros with their full multiplicities;
neither equates this total count with a critical-line count.

**Multiplicity transfer and the fixed lower endpoint.** By L018,
xi_c is nonzero outside the open critical strip and is not identically
zero. Its zeros there have exactly the analytic multiplicities of
zeta. L366 (1), multiplication by 2 and composition with the affine map
t -> 1/2+it therefore identify the real zeros of F_0 with critical-line
zeros, preserving their multiplicities. In particular no assertion that
all strip zeros occur on this line is used.

Let C(X) count critical-line zeros with 0<t<=X, with full multiplicity,
and let c_H count those with 0<t<H, also with full multiplicity.
The latter is finite: zeros of the nonzero entire completion in the
bounded closed strip rectangle have no accumulation and hence form a
finite set. For X>=H,

\[
 N_{F_0}^{\rm mult}([H,X])=C(X)-c_H.                 \tag{4}
\]

The strict upper inequality in the definition of c_H is deliberate:
if H is a zero, its whole multiplicity stays in (4). We never subtract
that multiplicity or treat it as uniformly bounded in a moving endpoint.
For X off all positive strip-zero ordinates, the inclusion of
critical-line zeros among all strip zeros gives C(X)<=N(X). Thus (4)
and (3) imply

\[
 N_{F_0}^{\rm mult}([H,X])
 \le M(X)+7/8+S(X)+R(X)-c_H.                        \tag{5}
\]

L372 (12) supplies a finite E_H>=0, independent of X, such that
|N_G([H,X])-M(X)|<=E_H for every X>=H, including either closed
endpoint being a G zero. Subtracting its lower count bound from (5),
and using X>=H>=2pi, gives

\[
 N_{F_0}^{\rm mult}([H,X])-N_G([H,X])
 \le S(X)+K_H,\qquad
 K_H=7/8+E_H+\frac1{150H}-c_H.                      \tag{6}
\]

Every term in K_H is finite and fixed once H is fixed. K_H need not
be positive. Only bounded fixed-ray errors have been absorbed.

**Allowed negative thresholds and moving endpoint selection.** Put
V(T)=sqrt(log log T) for T>e^e. It meets the lower endpoint of Dobner's
allowed range exactly, tends to infinity, and satisfies

\[
 \frac{V(T)}{\kappa(\log T/\log\log T)^{1/3}}
 =\frac{(\log\log T)^{5/6}}{\kappa(\log T)^{1/3}}
 \longrightarrow0.
\]

To check this limit directly, set u=log log T; its numerator/denominator
ratio is kappa^(-1) u^(5/6) exp(-u/3), which tends to zero.
Also log T/(V(T)^3 log V(T))=exp(u)/(u^(3/2)(log u)/2)
tends to infinity, so the logarithmic denominator in (2) is positive
for all sufficiently large T. Consequently (2) supplies a positive-
measure set A_T in [T,2T] where S(t)<=-V(T).

Let Z be the set of all positive ordinates of all nontrivial zeta
zeros, including off-line zeros. For each integer n>0 there are only
finitely many such zeros of height at most n: by L018 they are zeros
of a nonzero entire function in the compact rectangle
0<=Re s<=1, 0<=Im s<=n. An infinite set in that rectangle would have
an accumulation point and contradict the identity theorem. Thus Z is
countable and has Lebesgue measure zero. A_T minus Z still has positive
measure; choose X there. Take T>=H as well as above the fixed theorem
thresholds. Then X>=H, (6) applies with no moving upper-endpoint
correction, and S(X)<=-sqrt(log log T). This proves (1).

For any prescribed B>0 and lower height Y, choose T>=max(H,Y)
sufficiently large that sqrt(log log T)>K_H+B and (2) applies.
The selected X>=Y then has count difference less than -B. This proves
unboundedness below with witnesses arbitrarily far out, rather than
merely equality of main terms or a finite-height deficit. We did not
need to avoid G-zero endpoints because L372 already treats them.

**The limited comparison with L374.** Suppose an eventual ray has no
common real zeros of F_0 and G and has D<=0 everywhere. Increase its
lower endpoint to a fixed H>=H_*; both assumptions persist. F_0 is real
entire by L018 and is not identically zero, since its complex extension
has F_0(-i/2)=2xi_c(1)=1. The expression for G is real analytic on an
open neighborhood of the real ray: its complex scalar factors have no
real singularity, and restriction followed by real projection is real
analytic. L368 gives \(\mathscr L(G)>0\) throughout this ray, so G is not
identically zero either. These verify all analytic and nonzero
hypotheses of L374, in addition to the two supposed physical premises.

L374 therefore gives the closed-endpoint bound
N_F_0^mult([H,X])-N_G([H,X])>=-1 for every X>=H. Equation (1), with
T so large that K_H-sqrt(log log T)<-1, contradicts it. There is no
such joint eventual ray. No attempt to deduce one of the two physical
premises from the other, or from the exact shifted response formula,
has entered the proof. The common-zero counterexamples and geometric
obstructions remain valid context, not inputs to the count transfer.
This completes the assessed specialization. ∎

### Critical audit, 2026-10-08

The separately approved SPECIALIZE assessment is
`drafts/literature/2026-10-07-actual-signed-count-deficit-audit.md`.
This REPRODUCTION audit checks the assembly against the precise source
statements and the completed L372/L374 audits. It finds no mathematical
error and adds no stronger claim. The canonical direct inputs remain
L018, L366, L368, L372 and L374.

**Source domains and the argument branch.** Dobner v2's definition and
Theorem 1 were reopened and agree with (2), including its negative-sign
clause. The completed source review's Section 6 proof-case inspection is
reused; the conditional Section 7 is not used. The saved inspection of
Brent–Platt–Trudgian, Section 2 (5)–(8) and Lemma 2 with proof, supplies
exactly (3). A repeat PDF fetch timed out after returning document
metadata; this audit relies on the previously completed inspection, not
on that metadata as new evidence. No source hypothesis has changed.
The offprint link above now uses the author's tilde URL recorded in
that review.

For branch agreement at a selected X>0, the vertical segment at real
part 2 meets no cut: every zero and the pole have real part less than 2.
The horizontal segment at height X meets no cut when X is not an
ordinate of a strip zero; trivial zeros and the pole have height zero.
Both branches thus continue the same real logarithm at 2 along precisely
this path. No integer multiple of 2pi can be inserted. Values at jumps
need not be compared because these X are excluded.

With u=log log T, V=sqrt(u) tends to infinity, and its ratio to the upper
allowed threshold is kappa^(-1)u^(5/6)e^(-u/3), tending to zero. The
denominator in (2) is exactly

\[
 u-\tfrac32\log u-\log\log u+\log2,
\]

which tends to infinity. Thus the lower endpoint V is admissible and
(2) has a strictly positive finite right side for every sufficiently
large T. This uses the unconditional theorem with S, not a normalization
for pi S or an RH-dependent range. No sharp oscillation exponent is
needed or claimed.

**Multiplicity and both endpoints.** At a critical-line zero rho of
order m, write xi_c(s)=(s-rho)^m a(s), a(rho) nonzero. Substitution in
L366 gives F_0(t)=2i^m(t-Im rho)^m a(1/2+it), so the analytic order is
exactly m. Off-line zeros contribute to N(X) but not C(X); consequently
only C(X)<=N(X) is justified and only that direction is used. The
factor 2 and affine substitution create no zeros. Finiteness of c_H
follows from compact finiteness of zeros of the nonzero entire xi_c,
including the bottom and side boundaries of the rectangle.

For X>=H, subtraction of the set 0<t<H leaves exactly H<=t<=X.
If H is a zero its entire multiplicity remains; if X=H the result is
the corresponding singleton count. This is why replacing c_H with a
half-weighted count at H would be incorrect. At selected X outside Z,
N(X) has no half-weighted endpoint. The proof never bounds a moving
endpoint multiplicity, nor assumes that F_0 zeros are simple.

In L372 (12) one can take

\[
 E_H=|f(H)|/\pi+C_0/(\pi H)+2E/\pi+1,
 \qquad f(t)=\tfrac t2\log(t/(2\pi))-\tfrac t2.
\]

The constants C_0 and E there are fixed before H and X are chosen.
This gives N_G([H,X])>=M(X)-E_H even when either endpoint is a G zero,
and M=f/pi matches (3) exactly. Subtracting this lower bound from the
upper bound (5) gives (6), with the sign +E_H and the fixed subtraction
-c_H. Since X>=H, |R(X)|<=1/(150H). Every contribution to K_H is
therefore independent of X. A bounded derivative of an argument has
not been substituted for the bounded full phase error already proved
in L372.

**Null-set deletion and quantifier order.** Z contains ordinates of
all strip zeros, not just real zeros of F_0. Each bounded-height part
is finite by compactness and the identity theorem, so Z is a countable
null set even with unrestricted multiplicities. Deleting it from the
positive-measure negative-deviation set leaves eligible X. First choose
H>=H_* and fix E_H,c_H,K_H. Then choose T above the source threshold,
the admissibility threshold and H. This produces (1) in every such
dyadic interval. For each further B>0 and Y, increase T so that T>=Y
and sqrt(log log T)>K_H+B. The resulting X>=Y has deficit less than
-B. Nothing requires H to grow with T, uniformity in H, or an effective
onset. The selected point may be a G zero without affecting the bound.

**All hypotheses in the conditional application.** F_0 is real entire
and cannot vanish identically on an interval: its entire extension has
F_0(-i/2)=1. For an explicit common real-analytic domain, G is the real
restriction of the holomorphic function

\[
 -\frac{z^2+1/4}{2}
 \left(\frac{\xi_c(5/2+iz)}{5/2+iz}
       +\frac{\xi_c(5/2-iz)}{5/2-iz}\right)
 \quad (|\operatorname{Im}z|<5/2).
\]

Conjugation for xi_c identifies this restriction with L366. The
denominators cannot vanish in this open strip. Thus both functions
are real analytic on the connected real line and on an open
neighborhood of any ray. L368 (2), with its strictly positive envelope
and constant, supplies L(G)>0 above one fixed onset, also at G zeros;
it rules out G being identically zero on the connected component.
Choose H above that onset, L372's onset, 2pi, and the hypothesized
onset for both disjointness and D<=0. The latter two hypotheses
persist on the shortened ray. They are not inferred from a source or
from a geometric model. L374 now supplies deficit >=-1 for every X>=H,
including its dependent-pair case and closed endpoints. The preceding
fixed-H selection gives a deficit <-1 and hence the contradiction.

**Verdict and limits.** Every load-bearing case passes. The contradiction
negates only the conjunction of the two eventual premises. It gives
no choice between them, no actual common zero, no sign of the total
L367 margin and no RH conclusion. L371/L373's common-zero failures and
L375/L376's geometric failures are not invalidated. This completed
review verifies an existing specialization of known results; it is
not a new oscillation theorem or a mathematical strengthening.

## Mathlib

Full matching coverage for Dobner's oscillation theorem and this
actual-pair count specialization is **not checked**. No Mathlib theorem
is imported here. L018 supplies the completion/zero correspondence;
the remaining specialization uses compact finiteness of analytic zeros,
affine multiplicity preservation, count inclusion, elementary limits
and deletion of a countable null set. Supporting formal coverage for
those steps has not been checked; unknown availability is not evidence
of absence. No numerical certificate or mathematical script is needed.
