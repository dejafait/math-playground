# L130 — Conditional finite local membership of the retained-plus coefficient

## Hypotheses

Retain the complete construction of L123. Explicitly, A/Q is modular,
K/Q is imaginary quadratic, p>=5 is inert in K and split multiplicative
for A, and L=K_p. The conductor is unramified in K, its inert part is
square-free, the residual image contains SL_2(F_p), and each split
conductor exponent is at most two. The set cal S={p} is incoherent in
Fornea's Definition 1.2. Use w=infinity, conductor one, trivial character,
and the source's integral CM embedding and level choices (in particular
the standard reduction vertex and g_v=1). These hypotheses retain the
source construction; the duality argument does not produce them for
arbitrary A.

Put T=T_p(A), V=T tensor Q_p, and let c denote the outer action on
H^1(K,V). Use the actual complete integral J^dagger of L123, integration
before Hecke localization, the stated domain of pr_A, and cohomological
descent from the conductor-one class field L_1 to K. Define

\[
 b_K=\operatorname{desc}_{L_1/K}
       \bigl(\operatorname{pr}_A(J^\dagger\otimes1)\bigr)
       \in H^1(K,V),\qquad R=\operatorname{loc}_{K,p}(b_K).       \tag{1}
\]

This is exactly the global class before localization in L123 (5), not
a raw measure value or a projection of a truncated moment. In L123's
notation b_K=(1+c)b_0, where b_0 is the descended projected integral J.
L123, including its separate step-515 audit, supplies this identification.

**Conditional arithmetic input.** Suppose there is a specified
P in A(Q) tensor_Z Q_p whose rational Kummer class

\[
 w=\kappa_{\mathbf Q}(P)\in H^1(\mathbf Q,V),\qquad
 w_p=\operatorname{loc}_p(w)\ne0.                            \tag{2}
\]

Here rational Kummer means the Q_p-linear extension of the Kummer map
of rational points. No injectivity of localization on all of
A(Q) tensor Q_p is assumed. No such P is constructed, and analytic
order two is not used to infer (2). No finiteness of Sha is assumed.
For a local field F write A(F)^wedge for lim_n A(F)/p^n A(F); local
point spaces use this completion before tensoring with Q_p.

## Conclusion

There is a unique z in H^1(Q,V) restricting to b_K, and

\[
 \operatorname{loc}_p(z)\in H_f^1(\mathbf Q_p,V),\qquad
 R=\operatorname{res}_{L/\mathbf Q_p}\operatorname{loc}_p(z)
       \in H_f^1(L,V)^{\sigma_p=+1}.                         \tag{3}
\]

The finite local condition is the rational local Kummer image. All
other local conditions for z hold as well, so z belongs to the rational
Selmer group defined by these finite conditions. This is conditional
on (2). It does not identify z with a rational Kummer class, prove z
or R nonzero or zero, produce a strict class, or compare rational rank
with analytic order. L123's D^{++}=u_1 tensor R/4 retains its original
normalization and gains only conditional finite membership of its
second factor.

This is a REPRODUCTION/specialization of standard duality, with an
applicability argument for the existing coefficient, not progress
beyond the sources checked or a new BSD case. The written
specialization passes the separate step-544 conceptual audit below,
under precisely its stated conditional input and imported construction.

## Proof

**Cited duality and local inputs.** Use Karl Rubin, *Euler systems*,
[1999 AWS manuscript](https://swc-math.github.io/aws/1999/99RubinES.pdf),
I.7.3(ii) (statement on printed p. 17, proof pp. 18--19). Its setup
requires a number field, a finite free p-adic representation with finite
ramification, and mutually orthogonal chosen rational finite subspaces
at the places above p. For a nonzero coefficient M and finite sets
Sigma_0 contained in Sigma, singular localization of the relaxed
group S^Sigma(K,W_M) is orthogonal to finite localization of the dual
strict group S_{Sigma_0}(K,W_M^*), over Sigma minus Sigma_0.
Only orthogonality is needed here, not exactness of the complements.
The theorem applies to arbitrary Sigma, including {p}; its proof
explicitly removes the initial requirement to include all ramified and
infinite places. It is imported, not reproved.

Use the same manuscript's I.2.2 proof (printed p. 3, citing B.2.4) for
H^1(F,T) tensor Q_p = H^1(F,V); I.3.4 and I.3.6--3.10 (pp. 5--8) for
finite local conditions and quotient/limit conventions; I.4.1--4.3
(pp. 8--10) for local duality and orthogonality; I.5.1 and I.5.6
(pp. 11--13) for global groups and limits; and I.6.4, Remark 6.6 and
Proposition 6.7 (pp. 16--17) for elliptic Kummer local conditions.
The appendix proof of B.2.4 is not independently replayed; the
rationalization is an explicitly cited standard input.

Also use Rubin, *Euler systems and modular elliptic curves*,
[Section 5](https://swc-math.github.io/aws/1999/99RubinDur.pdf),
printed pp. 5--6: the Weil identification with the dual, the rational
Kummer subspace and its self-orthogonality, and the Lie exponential
isomorphism from the tangent space to the completed rational local
point space. These statements include split multiplicative reduction;
the later integral evaluation in Proposition 5.2 is not used. These
are the assessed inputs, not replacements for the actual coefficient
construction.

**1. Descent and localization.** L123 gives b_K=b_0+c b_0 in H^1(K,V).
The outer action here squares to one, although the raw coefficient
operator C need not. Thus c b_K=b_K. Inflation--restriction gives

\[
 \operatorname{res}_{K/\mathbf Q}:
 H^1(\mathbf Q,V)\xrightarrow{\sim}H^1(K,V)^{c=+1}.          \tag{4}
\]

Indeed its possible kernel and cokernel are H^1 and H^2 of Gal(K/Q)
with coefficients V^{G_K}; both vanish by averaging, since division
by 2 is available. This proves existence and uniqueness of z.
Equivalently z=cor_{K/Q}(b_K)/2. Restricting this expression gives
(b_K+c b_K)/2=b_K, so the inverse introduces no extra half into b_K
or R. The earlier descent from L_1, including any p-divisible degree,
has already taken place over Q_p as justified in L123.

Choose compatible decomposition groups for the fixed embedding in
L123. Restriction from G_Q to G_K and from G_{Q_p} to G_L commutes on
cocycles. Consequently

\[
 R=\operatorname{res}_{L/\mathbf Q_p}(z_p),
 \qquad z_p=\operatorname{loc}_p(z).                         \tag{5}
\]

This uses the actual global b_K; it does not manufacture a global
preimage of a given local R. Its local outer invariance agrees with L123.

**2. The finite line at p.** The principal polarization and Weil pairing
identify T with T^*=Hom(T,Z_p(1)) and V with V^*. The rational space

\[
 F=H_f^1(\mathbf Q_p,V)
   =\kappa_{\mathbf Q_p}\bigl(A(\mathbf Q_p)^\wedge
                                  \otimes_{\mathbf Z_p}\mathbf Q_p\bigr)
\]

is its own orthogonal complement for the local Tate pairing, by the
cited I.6.4/Remark 6.6 and elliptic Section 5. The latter's Lie
exponential identifies the local point space with the one-dimensional
Q_p tangent space of A. Kummer is injective on that space, so dim F=1.
Naturality gives w_p in F; (2) therefore gives F=Q_p w_p. This is a
rational spanning assertion, not an assertion that a chosen integral
vector generates the local lattice. No alternation assertion for the
cohomology pairing is used.

**3. One global scaling and conditions away from p.** The cited
rationalization isomorphism provides s>=0 and a,b in H^1(Q,T) with

\[
 a\longmapsto p^s z,\qquad b\longmapsto p^s w.               \tag{6}
\]

Each of the two elements of H^1(Q,T) tensor Q_p has a finite p-power
denominator; take the larger exponent and multiply the other lift
accordingly. This is one common global s, fixed before varying places
or finite coefficients. It is an existence statement for these two
classes, not a precision bound for the raw measure or pr_A composite.
Under the Weil identification also regard b as a class for T^*.

For every finite prime ell different from p, including every bad prime,
the proof of Rubin I.6.7 gives H_f^1(Q_ell,V)=0: the local p-adic point
completion is finite and the rational finite subspace is zero. Apply
I.4.2 to V and V^*=V. The orthogonal complement of this zero subspace
is the zero finite subspace on the dual side. Since the annihilator
of zero is the whole space, H^1(Q_ell,V)=0. The inverse-image definition
I.3.4 now gives

\[
 H_f^1(\mathbf Q_\ell,T)=H^1(\mathbf Q_\ell,T)
 \quad(\ell\ne p).                                        \tag{7}
\]

This agrees with the integral Kummer isomorphism stated after
Definition 3.7 in Darmon--Fornea, *Mock plectic points*,
[published Section 3.7](https://www.cambridge.org/core/journals/journal-of-the-institute-of-mathematics-of-jussieu/article/mock-plectic-points/1FB89BA4F920603AEE9D624B3897E876).
For (7) the general local assertions of Rubin suffice; no hypotheses
about the particular mock class are transferred to A.

At the real place G_R has order 2 and p is odd. Averaging annihilates
H^1(R,T), H^1(R,T/p^nT) and H^1(R,V), so this place contributes zero
at every level. There are no complex places of Q. At p, a has no
condition yet, while b_p lies in H_f^1(Q_p,T): its rational image is
p^s w_p in F and the integral condition is the inverse image of F.
Thus a belongs to S^{\{p\}}(Q,T) and b to S(Q,T^*) in Rubin's notation.
No finite-Sha premise enters these assertions.

**4. Apply the cited theorem at every finite level.** Set O=Z_p,
M=p^n with n>=1, Sigma={p}, and Sigma_0 empty. T is free of rank two
and unramified outside the finite set of bad reduction primes and p
(Neron--Ogg--Shafarevich). Its finite subspace at the only prime above
p is F, identified with its dual orthogonal complement in Step 2.
All setup hypotheses of I.7.3 hold.

Write W_n=p^{-n}T/T, identified with T/p^nT by
t mod p^n -> p^{-n}t mod T, and likewise for the dual. Let a_n,b_n be
the reductions of a,b. Lemma I.3.8(i) identifies the image of each
integral finite subgroup with the finite subgroup in H^1(Q_v,W_n).
Therefore

\[
 a_n\in S^{\{p\}}(\mathbf Q,W_n),\qquad
 b_n\in S(\mathbf Q,W_n^*).                                 \tag{8}
\]

At a bad prime this is the induced finite condition. It is not an
assertion that every finite-coefficient class is unramified, or that
the induced finite subgroup is the whole finite-coefficient H^1.
Only reductions of the checked integral classes are being used.

Theorem I.7.3(ii) pairs singular localization of a_n with finite
localization of b_n over the one-element set {p}, giving

\[
 \langle (a_n)_p,(b_n)_p\rangle_{p,n}=0
                         \quad\hbox{in }\mathbf Z_p/p^n.    \tag{9}
\]

This pairing descends to the singular quotient in the first variable
by I.4.3(ii). The arbitrary-Sigma clause of I.7.3 is essential; ramified
primes have not been silently dropped from an enlarged-set formula.

**5. Rational pairing and return to R.** Cup products and local
invariants commute with reduction Z_p(1) -> Z_p(1)/p^n. The integral
cup product of a_p,b_p has invariant in Z_p, using
H^2(Q_p,Z_p(1))=Z_p; its reduction modulo p^n is (9). These are the
compatible local pairings in I.4.1, with the Tate-module and finite
Weil identifications above. Thus the integral invariant belongs to
every p^n Z_p and is zero. The local finite cohomology limits are those
in I.3.10; there is no interchange with the original CM integral or
with Hecke localization.

Extending coefficients to Q_p, bilinearity and (6) yield

\[
 0=\langle p^s z_p,p^s w_p\rangle_p
   =p^{2s}\langle z_p,w_p\rangle_p.
\]

Thus z_p annihilates Q_p w_p=F, and F^perp=F implies z_p in F. The
other rational local conditions follow from Step 3. Restriction
preserves local Kummer images by naturality, so (5) gives R in
H_f^1(L,V). Its established outer invariance gives precisely (3).

The test passes as a conditional specialization. It supplies neither
(2) nor rational Kummer membership of z. In particular the rational
Selmer group cannot be identified with rational points by silently
assuming finite p-primary Sha. Finite membership gives neither
strictness nor nonvanishing, and L005's good-reduction certificate is
not applied at this multiplicative prime. L128 and the stopped tower
comparisons are not inputs.

**Separate conceptual audit (step 544, 2026-10-29).** The conditional
conclusion (3) passes. The following checks concern the applicability
argument; they neither replay the source construction imported in L123
nor supply (2).

For descent, the audited full-integral passage of L123 gives
B=pr_A(J tensor 1) over L_1, its unique descent b_0 to K, and
pr_A(J^dagger tensor 1)=B+d*B. Equivariance of that descent gives
b_K=b_0+c b_0. Averaging on the *cohomological* Gal(K/Q)-action is
therefore legitimate. The restriction of cor(b_K)/2 is b_K itself;
the local restriction in (5) has no further division. In particular
the scalar 1/4 in D^{++} is unchanged. Neither C^2=1 on the raw
module nor a map on truncated moments is used.

The rationalization in Rubin I.2.2's proof applies to these actual
global H^1 classes. Taking the maximum of the two denominator
exponents gives (6) with one s independent of n and of the place.
No bound uniform over all classes or primes is required. The integral
finite condition is an inverse image, so torsion ambiguities in the
chosen lifts do not spoil it. At every ell different from p, the
zero rational finite subspace in I.6.7 and exact orthogonality in
I.4.2, applied to the principally polarized A and its dual, imply
H^1(Q_ell,V)=0. This includes bad reduction. I.3.8(i), whose proof
does not assume an unramified representation, then gives exactly
the finite conditions needed for a_n and b_n. The stronger
unramified identification in I.3.8(ii) is not used at bad primes.
At the real place multiplication by 2 is invertible on all three
coefficient types, so no real term survives. I.7.3(ii)'s arbitrary-set
case thus applies to Sigma={p}, Sigma_0 empty, not merely to a set
enlarged by ramified places. Its orthogonality assertion is enough;
no assertion about lifting all finite Selmer classes is needed.

For clarity about the last transfer, write the integral Weil
evaluation as e:T x T^* -> Z_p(1). Under the identifications
W_n=T/p^nT and W_n^*=T^*/p^nT^*, the finite evaluation is

\[
 e_n(p^{-n}t\bmod T,\ p^{-n}f\bmod T^*)
          = e(t,f)\bmod p^n\mathbf Z_p(1).
\]

This is the normalized Cartier-dual evaluation of I.4.1, not the
evaluation of two fractional lifts into Q_p(1) without normalization.
It shows that (9) is the reduction of the integral cup product of
a_p,b_p; it introduces no p^{-2n} multiplier. Under local invariants
the maps from level n+1 to n are reduction Z_p/p^{n+1} -> Z_p/p^n.
The local cohomology limits used in I.4.1 therefore identify the
integral invariant with an element of Z_p whose every reduction is
zero. It is zero, and scalar extension gives exactly the factor
p^{2s} written in Step 5. Torsion choices of lifts disappear on this
scalar extension and cannot change the rational conclusion.

Finally, elliptic Section 5 begins with an arbitrary elliptic curve
over Q. Its rational exponential and Kummer self-orthogonality give
the one-dimensional finite line also at split multiplicative p;
the later integral formal-group evaluation is unnecessary. Assumption
(2) spans that rational line, even if an integral lift is divisible
by p. Its annihilator is the same line, so the verified pairing
vanishing gives z_p in F. Naturality of local Kummer gives (3).
This accepts a standard conditional Selmer input, not an unconditional
coefficient theorem, a rational-point identification, or a BSD result.

## Mathlib

The full conditional specialization, the Fornea coefficient construction,
Poitou--Tate duality in these conventions, and the local Kummer and
Tate-module rationalization statements: **not checked**. The cited
primary results are mathematical inputs, not claims of matching Mathlib
theorems. No formal verification is claimed.
