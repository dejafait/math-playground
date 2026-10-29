# L131 — Finite adjoint transport changes the degeneracy transition

## Hypotheses

Retain L123's original F=Q, A, K, p>=5, conductor, residual-image,
incoherence, integral-CM and level hypotheses. Use only levels n=1,2
of its original smooth proper Shimura curves X_n and Jacobians J_n.
Use L129's geometric integral lattices L_n=H_1(X_n(C),Z_p), with
direct sums over components, and its original covariant operators
U_n=[K_n g K_n], g_p=diag(1,p), and diamonds
d_n(u)=[K_n diag(1,u) K_n], u in Z_p^times. All displayed matrices
are p-components; all other finite components are the identity.
These are elements of the projective quaternionic group, so local
scalar matrices are trivial. Composition is rightmost first.

At p a representative k=[[a,b],[c,d]] of K_n has unit determinant,
c in p^n Z_p and a/d in 1+p^n Z_p; a,d are units. Tame levels
remain unchanged. Put

\[
 w_n=\begin{pmatrix}0&-1\\p^n&0\end{pmatrix},\qquad
 \pi:X_2\longrightarrow X_1,\quad [z,b]\longmapsto[z,b],
 \qquad r:X_2\longrightarrow X_1,\quad[z,b]\longmapsto[z,bg].
\]

The existence of r and the covariant identity pi_* U_2=p r_*
are L129. Set e_n=lim U_n^{j!}, let e_mu,n be the average of
the order-(p-1) diamond subgroup, and put C_n=e_mu,n e_n L_n.
All these operators retain their original physical labels.

For the coefficient side let V_n=T_p(J_n) over the chosen geometric
point, D_n=Hom_Zp(V_n,Z_p(1)), and let a^vee on D_n mean
precomposition by a on V_n. Write E_n=e_mu,n e_n for the same
physical projector on V_n and D_n^0=E_n^vee D_n. Thus D_n^0 is
the integral dual of E_n V_n, extended by zero on its complement.
Let b=T_p(pi^*:J_1->J_2) and beta=b^vee:D_2->D_1.
Here pi^* is exactly the coefficient pullback, not a normalized map.

The standard comparison inputs are imported in their already assessed
scope, rather than reproved:

- Fornea, *Plectic Heegner classes*,
  [arXiv:2603.28327v2](https://arxiv.org/html/2603.28327v2),
  Section 2.1.2/(15), (16)--(18), Proposition 2.9 (including both
  intermediate p-level cases), and Remark 2.12: original labels,
  pullback compatibility and Kummer/universal-coefficient comparison.
- Milne, *Jacobian Varieties*, corrected 12 June 2021,
  [Theorem 2.5 and Proposition 6.1/Corollary 6.3](https://www.jmilne.org/math/xnotes/JVs.pdf),
  pp.7--8,19--20, and *Abelian Varieties*, v2.0 (2008),
  [I Remark 10.7](https://www.jmilne.org/math/CourseNotes/AV.pdf),
  p.45: integral Jacobian and Tate lattices and functoriality.
- Sertoz--Ouaknine--Worrell, *Computing transcendence and linear
  relations of 1-periods*,
  [arXiv:2505.20397v1](https://arxiv.org/html/2505.20397v1),
  (4.5.54)--(4.5.55), (7.3.29)--(7.3.35), (7.4.37)--(7.4.42):
  integral curve/Jacobian pushforward, pullback and transfer. Take
  all marking and puncture sets empty and apply componentwise.

We use underlying geometric Z_p-modules. No comparison of Betti
Galois actions, auxiliary neat-level descent, Krekov/Maksoud global
control theorem, finite Sha, or new arithmetic assumption is made.

## Conclusion

For n=1,2 right translation by w_n defines a degree-one involution
W_n of X_n, hence an integral lattice automorphism W_n,*.
Let U_n^t be the covariant action of the transposed Hecke cycle,
equivalently [K_n g^{-1} K_n]. There is an integral comparison
iota_n:D_n -> L_n for which

\[
 \iota_n U_n^\vee=U_n^t\iota_n,\qquad
 \iota_n d_n(u)^\vee=d_n(u^{-1})\iota_n,
 \qquad \iota_1\beta=\pi_*\iota_2.                 \tag{1}
\]

Define F_n=W_n,* iota_n. Then

\[
 F_n U_n^\vee=U_n F_n,\qquad
 F_n d_n(u)^\vee=d_n(u)F_n,\qquad
 F_n:D_n^0\overset\sim\longrightarrow C_n.         \tag{2}
\]

The exact finite transition square is

\[
             F_1\beta=r_*F_2:D_2^0\longrightarrow C_1.
                                                               \tag{3}
\]

In particular r_*(C_2) is contained in C_1. No p-factor is inserted
in (3): it is the dual of the actual coefficient pullback transported
by degree-one automorphisms. On C_2 the consistency identity is

\[
              \pi_*=p\,r_* U_2^{-1}.              \tag{4}
\]

This passes the necessary finite map/label/lattice test. It supplies
no surjectivity for r_* and no identification with the controlled
tower under forgetting pushdowns. It does not repair L128 Step 1,
transfer any full-Hecke relation to N_0, or prove the held scalar or
any rationality, nonvanishing, strictness or BSD claim. It is a
known-method specialization (REPRODUCTION). **Separate conceptual audit
(step 549): PASS for (1)--(4) at levels 1 and 2.** The integral checks
are recorded below; the controlled tower is not identified. No result
beyond the checked sources is claimed.

## Proof

**Level and labels.** Direct multiplication gives, for n=1,2,

\[
 w_n^{-1}kw_n=
 \begin{pmatrix}d&-c/p^n\\-p^n b&a\end{pmatrix}.                 \tag{5}
\]

Its entries are integral, determinant a unit, lower-left entry
divisible by p^n and diagonal ratio d/a in 1+p^n Z_p. Thus
w_n^{-1}K_n w_n is contained in K_n. Since w_n^2=-p^n I is
projectively trivial, conjugation is an involution and containment
is equality. Away from p nothing changes. Right translation is
therefore an automorphism of the same level curve and extends to
its smooth proper model (including cusps if any). Its square is
the identity, so its integral homology map and inverse are integral.
This uses no rational division by p^n on a lattice.

Further multiplication gives

\[
 w_n^{-1}\operatorname{diag}(1,u)w_n
   =\operatorname{diag}(u,1)
   \sim\operatorname{diag}(1,u^{-1}),
 \quad
 w_n^{-1}g w_n=\operatorname{diag}(p,1)\sim g^{-1}. \tag{6}
\]

The symbol ~ means equality in PGL_2(Q_p), not a rescaling of a
Hecke operator on a lattice. Conjugation by a degree-one normalizer
preserves the correspondence cycle and all its multiplicities.
Consequently W_n,* conjugates d_n(u) to d_n(u^{-1}) and U_n to
U_n^t, and also conjugates these operators back. There is no
diamond or p scalar suppressed in (6). In particular both p-U
cycles have degree p, as follows also by conjugating the p branches
of (15). We have fixed the original uniformizer p throughout.

**Integral duality with the correct transpose.** Kummer identifies
V_n with H^1_et(X_n,Z_p(1)); comparison with singular cohomology
and universal coefficients identifies its Z_p(1)-valued dual with
L_n. The H_1 lattices are finite free, so this is integral, not
merely a Q_p isomorphism. This defines iota_n; Tate twists cancel
in this geometric comparison. A geometric correspondence acts
trivially on the scalar twist.

For a finite curve map f, Jacobian pullback corresponds to
cohomological pullback. Evaluation has the integral naturality
formula <f^*alpha,x>=<alpha,f_*x>. Jacobian norm corresponds to
cohomological trace, whose adjoint under evaluation is integral
homological transfer f^!. These are the imported push-pull
comparisons above, with ramification multiplicities retained.
Thus for a cycle with legs f_1:Y->X and f_2:Y->X, the physical
Jacobian action f_2,* f_1^* has precomposition dual corresponding
to f_1,* f_2^! on homology: the transposed cycle, not the original
labeled cycle. Swapping the Hecke legs replaces g by g^{-1}; for
a degree-one diamond it replaces u by u^{-1}. Applying the same
evaluation naturality to pi^* gives precisely pi_* with no degree
normalization. This proves all of (1), rather than identifying
covariant and dual operators by commutativity.

Combining (1) and (6) proves the operator equalities in (2).
The physical endomorphism algebras have finite Z_p-rank; their
ordinary idempotents are integral limits. Continuous conjugation
and duality preserve these limits. Inversion permutes the finite
diamond subgroup, whose average is integral since p-1 is a unit.
Therefore iota_n carries D_n^0 onto the adjoint-ordinary,
trivial-finite-diamond direct summand, and W_n,* carries that
summand onto exactly C_n. This proves the last assertion of (2).
No integral inverse of a rational matrix has been used on V_n or
L_n: both comparisons and geometric automorphisms are isomorphisms
of their actual integral lattices.

**The transported transition and multiplicities.** On the whole
lattices the transported map is

\[
 F_1\beta F_2^{-1}=W_{1,*}\pi_*W_{2,*}^{-1}.
\]

The underlying composite morphism sends [z,b] at level two to
[z,b w_2^{-1}w_1] at level one. Here

\[
 w_2^{-1}w_1=\begin{pmatrix}p^{-1}&0\\0&1\end{pmatrix}
       \sim\begin{pmatrix}1&0\\0&p\end{pmatrix}=g.              \tag{7}
\]

It is exactly r. Both outside maps are degree-one isomorphisms;
the middle map retains the full forgetting multiplicity. The two
index-p intermediate stages in Proposition 2.9 give total generic
fiber degree p^2, counted over all source components. Conjugation
by isomorphisms changes neither this count nor any ramified-fiber
ramification multiplicity. In particular (7) does not replace a
multi-valued Hecke correspondence by a single branch or divide a
trace by p. Equality of these morphisms gives equality of integral
pushforward maps on the full lattices.

Proposition 2.9 gives b E_1=E_2 b, using both intermediate p-level
cases for U and the stated diamond compatibility. Taking
precomposition duals gives beta E_2^vee=E_1^vee beta. Thus beta
maps D_2^0 into D_1^0. Restricting the full-lattice equality using
(2) proves (3) and r_*(C_2) subset C_1.

As a direct check of the U-label after transport, let
s_{n,a}=[[1,0],[a p^n,p]], a=0,...,p-1, be the original branches.
Then s_{2,a}g=g s_{1,a}, with equality of matrices, so r_* U_2
and U_1 r_* have identical p branch cycles. Their equality extends
over the proper curves with multiplicities, and agrees with the
dual pullback calculation. Diamonds likewise commute with g with
their labels reduced from level two to level one.

Finally L129 gives pi_* U_2=p r_* on the entire integral lattice.
U_2 is an integral automorphism of C_2, so composing on the right
with its integral inverse proves (4). This keeps L129's obstruction:
forgetting pushdown has image in p C_1 here and cannot be surjective
at a nonzero target. The actual transported transition (3) is r_*;
its surjectivity has not been established by this computation.
There is no contradiction and no license to substitute either map
in an imported control theorem. Even though L129 proves the
divisibility implicit in p^{-1} pi_* U_2, that fact alone gives no
control or all-level comparison.

The finite test is complete at this point. The argument neither
identifies the action conventions of the source's controlled
homology nor tests tame bad-U labels, residual projectors, completed
limits, flatness, local signs or relation transfer. Those are separate
questions, as are the independent arithmetic gaps.

### Separate conceptual audit, step 549 (2026-10-29)

**Verdict and imported scope.** PASS for the finite integral assertions
(1)--(4), including the specified source and target summands. This
verifies the step-547 specialization; it is not a new general theorem.
Use the smooth proper geometric components of the original levels.
The comparison and transfer references in the hypotheses apply with
empty markings and punctures. Basepoints for the Jacobian comparison
are chosen over C, not assumed rational over Q. Genus-zero components
have zero first homology and Tate module and cause no exception.
No auxiliary neat-level descent or control theorem is used here.

**Evaluation fixes the direction and product order.** Let

\[
 q_n:V_n\overset\sim\longrightarrow
 H^1(X_n(\mathbf C),\mathbf Z_p)\otimes\mathbf Z_p(1)
\]

be the imported Kummer and comparison isomorphism, using the same
geometric choices at both levels. Integral universal coefficients
give a perfect evaluation pairing with L_n. Define iota_n by

\[
       \ell(v)=\langle q_n(v),\iota_n(\ell)\rangle
       \quad(v\in V_n,\ \ell\in D_n).
\]

Thus no polarization degree, inverse isogeny or rational division
enters iota_n. For ell in D_2 and v in V_1, write x=iota_2(ell).
Naturality of coefficient pullback gives q_2(bv)=pi^*q_1(v), so

\[
 \langle q_1(v),\iota_1\beta\ell\rangle
 =\ell(bv)
 =\langle\pi^*q_1(v),x\rangle
 =\langle q_1(v),\pi_*x\rangle.
\]

Perfection proves iota_1 beta=pi_* iota_2 on the entire lattices.
In particular dualizing pullback gives pushforward, not transfer.

For the physical Jacobian correspondence a=f_{2,*}f_1^*, its action
under q_n is Tr_{f_2} f_1^*. The integral norm/trace and transfer
comparison in the cited sources gives

\[
 \langle\operatorname{Tr}_{f_2}f_1^*\alpha,x\rangle
 =\langle f_1^*\alpha,f_2^!x\rangle
 =\langle\alpha,f_{1,*}f_2^!x\rangle.
\]

Therefore iota_n a^vee=f_{1,*}f_2^! iota_n. Both legs, not merely
the multiplication order in a commutative algebra, are transposed.
For an automorphism d this is (d^{-1})_*. The scalar Tate module
is the target of evaluation on both sides and cancels; a geometric
correspondence does not act on it by its degree. This directly checks
the distinction responsible for L128's step-534 HOLD.

**Normalizer and the full Hecke cycle.** Recompute (5) with a unit
determinant representative of the actual K_n. Its diagonal ratio
becomes d/a, its lower-left entry is -p^n b, and all entries remain
integral. Since conjugation twice is the identity in the projective
group, the containment is equality. Thus the geometric W_n has an
integral inverse even though its displayed matrix has determinant
p^n. Right translation affects no other finite component or the
Archimedean coordinate. Its holomorphic isomorphism extends to the
proper curve, so there is no orientation sign or degree factor.

For an explicit transpose check put H_n=K_n intersect g K_n g^{-1}.
The Hecke curve X_{H_n} has legs forgetting and right translation
by g. Right translation by g identifies it with the curve of level
K_n intersect g^{-1} K_n g and interchanges the two legs. Hence its
transposed cycle is precisely [K_n g^{-1} K_n]. Conjugating by w_n
sends the original two legs to these legs because
w_n^{-1} g w_n is g^{-1} projectively. The same calculation sends
diag(1,u) to diag(1,u^{-1}). These are equalities in the original
projective group, not rescalings of lattice endomorphisms.

Multiplicity is checked before applying an ordinary projector.
Inside K_n, membership in H_n adds exactly c in p^{n+1} Z_p;
the p representatives [[1,0],[a p^n,1]] exhaust its cosets, as in
L129's audited calculation. For the transposed subgroup the extra
condition is b in p Z_p. Conjugation by w_n maps the displayed
representatives to [[1,-a],[0,1]], giving its full p cosets as well.
Thus neither conjugation nor transposition omits a branch or inserts
a factor. The proper cycles retain ramification multiplicities.
This proves the first two identities of (1) and the labeled
intertwining identities of (2).

**Whole-lattice transition and degree.** Composition is rightmost
first, so W_1 pi W_2^{-1} sends [z,b] to
[z,b w_2^{-1}w_1]. Direct multiplication gives
w_2^{-1}w_1=diag(p^{-1},1), whose projective class is g, with
identity away from p. Hence this composite is r on the open curves
and on their proper extensions. Functoriality of integral pushforward
gives F_1 beta F_2^{-1}=r_* on all of L_2, without a projector or
a surjectivity assumption.

To check the degree independently, put H=K_1 intersect K_2^circ.
The p cosets of H in K_1 are represented by [[1,0],[p a,1]].
The p cosets of K_2 in H are represented by diag(1,1+p j), with
a,j modulo p. Thus [K_1:K_2]=p^2. In the projective arithmetic
quotient the generic stabilizer is trivial, so the total degree
over any target component, summing all source components above it,
is p^2. The degree-one W_i preserve this degree and every special
fiber's ramification multiplicity. This also distinguishes r from
a single p-U branch: its whole map has degree p^2, whereas each
projection leg of the p-U cycle has total degree p.

**Restriction really is integral.** The two p-level stages of
Fornea Proposition 2.9, at m=1, give b U_1=U_2 b. They use the
same intermediate H just considered: the diagonal cosets for H/K_2
and the lower-unipotent cosets for K_1/H. Both are needed for the
full pullback. The diamond compatibility is also for the original
labels. Taking factorial-power limits and the finite-diamond average
therefore gives b E_1=E_2 b. These limits and the average lie in the
integral finite-rank endomorphism modules; p-1 is a unit. Dualizing
gives beta E_2^vee=E_1^vee beta, so beta(D_2^0) is contained in
D_1^0, without requiring b or beta to be surjective.

The already checked labeled equalities imply F_n E_n^vee=E_n F_n.
Since F_n and its inverse are integral on the full lattices, they
identify these idempotent images integrally, not just after tensoring
with Q_p. Restricting the whole-lattice transition proves (3).
As a separate branch check, s_{2,a}g=g s_{1,a} for every a modulo p.
The two sums over all p branches therefore give r_* U_2=U_1 r_*
as proper cycles with their multiplicities. Diagonal matrices commute
with g, so the diamond labels agree too. This independently agrees
with r_*(C_2) being contained in C_1.

Finally U_2 on C_2 has integral inverse: its factorial powers tend
to the identity, so its reduction modulo p is invertible, and hence
its determinant on the finite free Z_p-module C_2 is a unit.
L129's audited full-lattice identity pi_* U_2=p r_* now proves (4).
In particular pi_*(C_2) is contained in p C_1. If C_1 is nonzero,
C_1/p C_1 is nonzero and this forgetting map is not surjective.
This is compatible with (3), whose transition is r_*, and preserves
the obstruction recorded in ATTEMPTS/063.

The source checks used Fornea v2 after (6), (15)--(18), both p-level
proof cases of Proposition 2.9, (21) and Remark 2.12; Milne's cited
integral lattice/functoriality passages; and Sertoz--Ouaknine--Worrell
(4.5.51)--(4.5.55), (7.3.29)--(7.3.35), (7.4.37)--(7.4.42), at the
versioned URLs in the hypotheses. Their existing coverage is reused.
No numerical or finite-modulus experiment stands in for the proof.

The audit accepts no identification with Fornea's controlled homology,
no all-level relation transfer, and no tame bad-U or residual-projector
comparison. It leaves L128 on HOLD and supplies no Kummer membership,
nonzero localization, strictness or rank/order equality. The original
finite test is retained with its hypotheses; no new DAG input is used.

## Mathlib

Full matching theorem and supporting formalization not checked.
No absence claim is made. This argument uses the cited informal
integral comparison theorems and exact matrix/correspondence
identities, not a Lean certificate.
The separate step-549 conceptual audit passes only the finite
specialization (1)--(4) described above; formalization remains unchecked.
