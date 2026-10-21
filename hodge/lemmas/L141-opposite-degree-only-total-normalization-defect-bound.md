# L141 — Degree-only upper bound for the total opposite normalization defect

## Hypotheses

Retain the common conditional opposite-family setting of L129, L138,
L139 and audited L140. Thus B=S_1 and Y=S_2 are the identical marked
smooth projective complex K3 surfaces of L071/L118, with their unchanged
common hyperkähler metric and real product polarization Omega. Suppose
F on B x Y is holomorphic locally free, Omega-slope-polystable, of rank
two, with integral c_1(F)=0 and

\[
              \operatorname{ch}_2(F)=-14e_1-21e_2-\tau_D,
\]

where e_1=eta tensor 1, e_2=1 tensor eta, integral_S eta=1, and tau_D
is the unchanged full integral self-adjoint mixed tensor. Use the actual
opposite charge-21 classifying map and its original integral reduced
image Z. Its finite birational unramified normalization is nu:B -> Z.
Let C be its finite set of multiple-fibre values, and set

\[
 Q=\nu_*O_B/O_Z,\qquad
 \Lambda=\operatorname{length}(Q),\qquad
 r_z=\#\nu^{-1}(z),\qquad
 P=\operatorname{length}_{\mathbb C}(R_{\rm off}).
\]

Here R_off is the actual reduced ordered off-diagonal coincidence scheme.
Use precisely L137's embedding of the original Z, as retained by
L138--L140, with fixed integers N>=3 and

\[
 \delta=4k^2\ell^2q(D(H),D(H))\geq8,\qquad
 T=\frac{\delta(\delta+1)}2,\qquad
 U=2+\frac\delta2+\frac32\delta^{N-2}T^4,\qquad K=\lfloor U\rfloor.
\]

These choices are independent of F and its unknown image defect. No
existence of F or collisions, minimal gluing, image normality or
Cohen--Macaulayness, coherent vanishing, effective numerical embedding
parameters, or contradictory lower estimate is assumed.

## Conclusion

Put

\[
              J=\left\lfloor\frac{(\delta-4)^2(\delta-6)}6
                 \right\rfloor.
\]

For every multiple-fibre value z, r_z<=delta-5. The entire actual
normalization defect satisfies

\[
 \boxed{\quad
 0\leq\Lambda
 \leq\left\lfloor\frac{(\delta-4)P}{6}\right\rfloor
 \leq J<K\leq U.
 \quad}                                                     \tag{1}
\]

Thus J is a degree-only upper bound strictly sharper than L138's
fixed-parameter bound for every admissible delta,N. In particular
chi(Z,O_Z)>=2-J, using L138's exact Euler identity. If C is empty,
P=Lambda=0. Arbitrary finite fibre partitions are retained. No optimal
integer-partition bound or actual geometric attainment is asserted.

This is a conditional ADVANCE / REPRODUCTION of assessed known tools
and finite-sum arithmetic. The separate step-443 critical audit below
preserves it. It
supplies upper control only, not a contradictory lower bound, F, a
collision, a cycle or transverse transport. Universal primitive rational
Hodge realization remains unresolved.

## Proof

**Coverage and precise inputs.** The pre-invocation SPECIALIZE assessment
is `drafts/literature/2026-10-20-opposite-degree-only-total-defect-bound.md`.
Reuse its completed literature comparison without additional browsing.
L129 gives the entire actual algebraic stalk bound

\[
                \lambda_z=\operatorname{length}(Q_z)
                       \leq\binom{r_z+1}{3}.                \tag{2}
\]

L138 supplies finite support contained in C, Lambda=2-chi(O_Z), and
the parameters U, N>=3 and delta>=8. L139 supplies the exact ordered
count, while audited L140 bounds that same count:

\[
        P=\sum_{z\in C}r_z(r_z-1)
                     \leq (\delta-4)(\delta-6).              \tag{3}
\]

Reducedness is already part of L139's justification of this equality;
there is no replacement of a nonreduced scheme by its set of points.
For the finite-support bridge use the assessed
[Stacks, Lemma 33.33.3, tag 0AYT](https://stacks.math.columbia.edu/tag/0AYT):
a coherent sheaf with zero-dimensional support on a proper scheme over
a field has global sections equal to the direct sum of its stalks and
has no higher cohomology. Z is projective, Q is coherent with finite
support by L138, and all residue fields are C. Hence

\[
                    \Lambda=\sum_{z\in C}\lambda_z.          \tag{4}
\]

This is the same application already justified in L138; no general
normalization, projection or local-arrangement theorem is reproved.
The needed specialization is the uniform finite-sum estimate below.
The scoped duplicate search found no completed aggregation. The failed
minimal-gluing, automatic-vanishing and middle-Hom-Euler mechanisms in
ATTEMPTS/070,073,078 are not used or reopened.

**Eliminate every unknown fibre size.** Fix z in C. Its nonnegative
summand in (3) is at most P, hence

\[
                  r_z(r_z-1)\leq(\delta-4)(\delta-6).        \tag{5}
\]

If r_z>=delta-4, then, since delta>=8 and x(x-1) is increasing on
the positive integers,

\[
 r_z(r_z-1)\geq(\delta-4)(\delta-5)
             >(\delta-4)(\delta-6),
\]

contradicting (5). Both r_z and delta are integers, so r_z<=delta-5.
Consequently (2) gives

\[
 \lambda_z\leq\frac{(r_z+1)r_z(r_z-1)}6
              \leq\frac{\delta-4}{6}r_z(r_z-1).              \tag{6}
\]

Sum (6) over the entire finite set C, using (3)--(4). Every fibre
is retained, with its own unrestricted size, giving

\[
 \Lambda\leq\frac{\delta-4}{6}P
          \leq\frac{(\delta-4)^2(\delta-6)}6=:V.             \tag{7}
\]

Lambda is a nonnegative integer, so taking floors gives the first
three inequalities of (1). If C is empty, (3) is the empty sum and
L138's support containment makes Q=0. Equations (4), (6)--(7) then
hold with both P and Lambda zero; no maximum of an empty fibre set
has been taken.

**Strict comparison for every admissible fixed parameter set.** For
delta>=8, both delta-4 and delta-6 are positive and less than delta,
so

\[
                   0<V<\frac{\delta^3}{6}.                 \tag{8}
\]

Since N>=3 and T=delta(delta+1)/2>=delta, the old bound satisfies

\[
        U\geq2+\frac\delta2+\frac32\delta^5
                    >\frac{\delta^3}{6}+1>V+1.             \tag{9}
\]

The middle inequality follows from
(3/2)delta^5-delta^3/6=delta^3(9delta^2-1)/6>0 and
2+delta/2>1. Thus K=floor(U)>=floor(V)+1=J+1, proving J<K.
By definition K<=U. This comparison uses no selected numerical value
of k, ell or N and no sampling. Finally L138's exact Euler identity
and Lambda<=J give chi(O_Z)=2-Lambda>=2-J.

This proves the uniform improvement sought in the continuation test.
It bounds an actual quotient length, using L129 rather than an invalid
identification with the pair count. It neither assumes minimal gluing
nor infers actual equality from flat tangent-arrangement sharpness.
The new degree-only threshold may constrain a later Euler comparison,
but no lower estimate approaching or exceeding it is supplied. F
existence and universal primitive Hodge realization remain independent
unresolved gaps. The bound remains potentially ineffective through
the fixed degree's unspecified projective choices.

**Separate critical audit, 2026-10-20 (step 443).** The pre-invocation
SPECIALIZE assessment is
`drafts/literature/2026-10-20-degree-only-defect-critical-audit.md`.
This audit is RESEARCH / EXPLORATION / REPRODUCTION, actual task
proof_audit. The entire argument above survives: no substantive error,
stronger estimate or existence conclusion was found. This is not a
second mathematical advance or a fresh proof of the imported theorems.

First, the objects in the four direct inputs agree. L129 estimates the
entire algebraic quotient at the entire fibre of the opposite
normalization, for every finite number of branches and every tangent
span. Its use of L128's actual completed-map identification is retained;
flat-arrangement sharpness is not a claim about an actual collision.
L138 uses that same original reduced image and normalization, and L139
counts the original ordered pairs over it. Audited L140 bounds this
original count by its auxiliary residual count; L141 does not silently
replace P by the auxiliary count or require its new pairs to be reduced.
All four inputs retain the same full negative mixed tensor and common
metric. No charge, factor order or embedding has changed.

For the global length passage, Q is coherent on projective Z and has
support in the finite set C by L138. Thus the precisely cited Stacks
0AYT applies to Q. Each stalk is a finite-length module over a local
complex algebra whose residue field is C, so its module length is its
complex dimension. The finite-support direct sum consequently gives
exactly (4), not merely a bound by the number of support points.
No vanishing of H^1(O_Z) enters. If C is empty, support containment
forces Q=0. If C is nonempty, all r_z are integers at least two;
L139 and reducedness give (3) with both orders of every pair.

For the fibre-size step, every summand r_z(r_z-1) in (3) is
nonnegative and therefore bounded by its whole sum. At the proposed
first excluded integer r_z=delta-4, the excess over L140's threshold
is exactly delta-4>0:

\[
 (\delta-4)(\delta-5)-(\delta-4)(\delta-6)=\delta-4.
\]

The function r(r-1) is increasing for integers r>=1. Hence every
r_z>=delta-4 is excluded, giving precisely r_z<=delta-5, without
rounding a quadratic root or assuming all fibres have the same size.
The local coefficient is
binom(r_z+1,3)/[r_z(r_z-1)]=(r_z+1)/6 for each z in C,
so its replacement by (delta-4)/6 has the correct inequality direction.
Summing over C uses no assumption of double-only fibres or optimal
integer partitions. For C empty it is a zero sum and involves no
division by P or selection of a maximal fibre.

Let A=(delta-4)P/6 and V=(delta-4)^2(delta-6)/6.
The proved real inequalities are 0<=Lambda<=A<=V.
Integrality of Lambda gives Lambda<=floor(A); monotonicity of the
floor function gives floor(A)<=floor(V)=J. The proof does not need
A or V to be integral. The parameter range is also justified by the
input: L138 obtains N>=3 from the image embedding and normalization,
and delta>=8 from L137's integral ample K3 class and positive k,ell.
There is no extrapolation to smaller unsupported degrees.

Finally, delta^(N-2)>=delta and T>=delta yield the lower bound for U
in (9). The difference between that lower bound and delta^3/6+1 is

\[
 1+\frac{\delta}{2}
       +\frac{\delta^3(9\delta^2-1)}6>0
       \qquad(\delta\geq8).
\]

Since V<delta^3/6, this proves U>V+1 uniformly, including the
smallest allowed degree and ambient dimension. In particular
U>J+1, so floor(U)>=J+1; mere U>V would not have sufficed.
Thus the strict integer comparison J<K, and then K<=U, are valid.
The exact Euler identity from L138 gives chi(O_Z)>=2-J with its
asserted sign. These are symbolic checks of all admissible parameters,
not finite numerical samples.

The direct inputs remain L129, L138, L139 and L140. The known failures
in ATTEMPTS/070,073,078 are not premises: no minimal-gluing equality,
automatic coherent vanishing or bound on a middle-Hom Euler term is
used. The bound remains conditional, potentially ineffective through
the fixed projective degree, and supplies only upper control. Neither
F existence nor a contradictory lower comparison nor universal
primitive Hodge realization follows. The mathematical argument and
dependency graph are unchanged. Full matching Mathlib coverage remains
not checked.

## Mathlib

Full matching Mathlib coverage for this conditional aggregation and its
comparison with L138 is **not checked**. The general finite-support
input is precisely cited above; the finite-sum and integer inequalities
are proved here. Unknown coverage is not evidence of absence, and no
Lean verification is claimed.
