# L181 — Uniform section multiplicity from the rank-two bracket Gram form

## Hypotheses

Retain the complete conditional family and actual maps of L116, L163
and L165. Thus X=S_1 x B is the product of the identical marked
projective K3 factors with their common hyperkähler metric, ordered
triple, holomorphic forms sigma_1,sigma_2 and L071's compatible
unitary hyperholomorphic connection. The hypothetical locally free
rank-two F is slope-polystable at the original real product class,
has integral c_1(F)=0 and full character

    ch(F)=2-14e_1-21e_2-tau_D+62e_1e_2.

Keep the prescribed mixed tensor and marking. Put V=End_0(F),
p:X -> B, M=R^1p_*V and W=R^2p_*V. Use the actual truncation
inclusion j, trace-adjoint retraction r and top projection a, with
rj=id. The reduced finite split set Z may be empty; W has length
one at each of its points. Write s=|Z| and

    H=H^0(B,M),    t=dim_C H=h^0(B,N),    E=H^2(X,V).

L116 identifies the actual j_1:H -> H^1(X,V) and gives
dim E=724+2t, with the whole W retained. Its hypotheses give
0<=t<=48. Retain L163's single harmonic antilinear R, the common
theta_i=[bar(sigma_i)], the actual J,Phi_1 and K=J^{-1}Phi_1.
For t>0 its Hermitian forms Q_1,Q_2 are positive definite and
Q_1(u,v)=Q_2(Ku,v), with K diagonalizable with strictly positive
real eigenvalues. The charge-21 stability hypothesis used there
for strictness is retained. Let Q be L165's actual complex bilinear
Serre form on E, with its fixed trace conventions.

No prescribed t or s, existence of F, section integrability,
multiplicative or metric-compatible Leray splitting, independent
factor harmonic action, or harmonicity of products is assumed.

## Conclusion

For the actual unhalved degree-one Yoneda bracket set

    beta:Sym^2 H -> E,    beta(u odot v)=[j_1u,j_1v],
    G(x,y)=Q(beta(x),beta(y)).

The form G is nondegenerate on the whole Sym^2 H, including the
zero-dimensional convention when t=0. Consequently beta is injective,

    rank G=t(t+1)/2 <=724+2t,

and t is even with

                         0<=t<=38.

These conclusions hold also when Z is empty. They extend L180's
audited endpoint mechanism to every parameter allowed by the stated
inputs. The conditional local ADVANCE / REPRODUCTION (step 611,
2026-10-29) survives the separate conceptual audit below (step 613),
with no substantive correction or stronger bound. It is a specialization
of assessed trace, harmonic and duality tools, not a new general trace
identity or a certified originality claim. No cardinality bound is
derived in this step. The remaining parameter pairs, other stable
types, existence of F, transport and primitive algebraic-cycle
realization remain unresolved. No complete Hodge candidate is asserted.

## Proof

**Scope and imported tools.** The invocation-start SPECIALIZE gate is
`drafts/literature/2026-10-29-rank-two-bracket-uniform-multiplicity.md`.
Reuse L180's audited graded specialization, with its precise imports:
Vasyutkin–Chupakhin, *Constructing a Minimal Basis of Invariants for
Differential Algebra of 2 x 2 Matrices*, J. Appl. Ind. Math. 16 (2022),
356–364, Section 2, equations (1),(4), Assertion 1 and the traceless
display after (6), pp.357–359,
[DOI](https://doi.org/10.1134/S1990478922020156); and Procesi,
*The invariant theory of n x n matrices*, Adv. Math. 19 (1976),
306–381, Corollary 4.4(c) and Theorem 4.6 with proofs, pp.319–323,
[primary text](https://abrochier.org/m2/Procesi.pdf#page=14).
The ordinary traceless complex 2-by-2 coefficient identity is

    2tr(ABCD)=tr(AB)tr(CD)+tr(AD)tr(BC)-tr(AC)tr(BD).

For graded products, differential and trace use Lepri–Manetti,
*Connections and L-infinity liftings of semiregularity maps*,
[arXiv:2102.05016v3](https://arxiv.org/pdf/2102.05016v3#page=3),
22 May 2021, Section 2, pp.3–4, and Lemma 2.6 with proof,
pp.6–7, with F in internal degree zero. These results do not impose
t or s. They are imported, not reproved. L163's harmonic and
strict-positivity theorems and L165's actual Serre trace description
are used with their canonical hypotheses and precise citations.
The changed task is the finite-dimensional specialization below;
L180's endpoint exclusion itself is not assumed at another endpoint.

In particular L180's coefficient-to-form calculation, before its
endpoint dimension substitution, gives for arbitrary V-valued
degree-one Dolbeault forms alpha,beta_0,gamma,delta

    tr([alpha,beta_0][gamma,delta])
      =2(tr(alpha gamma)tr(beta_0 delta)
                       +tr(alpha delta)tr(beta_0 gamma)).       (1)

Products include wedge and composition. The acbd exterior sign
reverses the minus in the ordinary coefficient identity; summing
the four bracket words cancels the tr(alpha beta_0)tr(gamma delta)
terms. The proof and its audit in L180 check repeated inputs as
well as distinct ones. This is a local identity of forms, so the
dimension of H and Z play no role. The derivation rule and trace
compatibility make it descend to all closed-input cohomology classes;
exact changes disappear by Stokes after integration on compact X.
Thus (1) applies on the full Sym^2 H at every t, with no requirement
that first-order deformations integrate.

**Actual scalar cups at variable t.** For t>0 put

    tau(u,v)=tr(j_1u cup j_1v) in H^2(X,O_X).

Scalar Dolbeault Kunneth for the K3 product, as used in L180, gives
unique alternating bilinear forms omega,eta on H with

    tau(u,v)=omega(u,v)theta_1+eta(u,v)theta_2.                  (2)

Here theta_1^2=theta_2^2=0 and theta_1 theta_2 generates H^4(X,O_X).
This decomposes only scalar cohomology. Set

    Omega_hol=sigma_1 wedge sigma_2,
    T_0=integral_X Omega_hol wedge theta_1 wedge theta_2
       =16 Vol(X)>0,
    R_H=j_1^{-1}Rj_1.

The volume equality uses the common sigma_i bar(sigma_i)=4dvol_i
normalization. R_H is an antilinear bijection on H. Applying L163's
definition of its factor forms to (2), exactly as in L180, gives

    Q_2(u,v)=(T_0/8)omega(u,R_H v),
    Q_1(u,v)=(T_0/8)eta(u,R_H v).                              (3)

The index reversal comes from wedging with the complementary theta_i.
Both expressions use the actual harmonic representative R alpha_v
of j_1 R_H v. R is not asserted to preserve products.

If omega(u,w)=0 for every w, (3) and surjectivity of R_H imply
Q_2(u,v)=0 for every v. Strictness gives u=0. Hence omega is
nondegenerate. Combining (3) with Q_1(u,v)=Q_2(Ku,v) gives

                     eta(u,w)=omega(Ku,w)                     (4)

for every pair u,w. These arguments use L163's variable-t strictness,
whose Q_1 proof uses the stable charge-21 second-factor restrictions,
and whose Q_2 proof uses the actual j_3 and J with W retained.
They do not use a numerical endpoint or a nonempty split set.

**The full Gram form.** With u odot v=(u tensor v+v tensor u)/2 define

    A_2(u odot v,w odot z)
       =omega(u,w)omega(v,z)+omega(u,z)omega(v,w),
    D(u odot v)=Ku odot v+u odot Kv.

L165's actual Serre form has the expression

    Q(x,y)=c_X integral_X Omega_hol wedge tr(x cup y)

with a single nonzero constant c_X. Substituting (2) into (1) gives

    G(u odot v,w odot z)=2c_X T_0[
        omega(u,w)eta(v,z)+eta(u,w)omega(v,z)
       +omega(u,z)eta(v,w)+eta(u,z)omega(v,w)].

Using (4), on the entire symmetric square this is

                     G(x,y)=2c_X T_0 A_2(Dx,y).                (5)

For clarity, the nondegeneracy proof also works in variable dimension.
On H tensor H put B(u tensor v,w tensor z)=omega(u,w)omega(v,z).
Its linear map to the dual is the tensor square of the isomorphism
omega:H -> H^*, so B is nondegenerate. B is symmetric because
omega is alternating. The tensor flip is self-adjoint for B; its
symmetric and alternating eigenspaces are B-orthogonal and span
H tensor H over C. A radical vector for B restricted to Sym^2 H
would therefore be orthogonal to all H tensor H and hence zero.
Since A_2 is twice that restriction, it too is nondegenerate.

Choose an eigenbasis e_1,...,e_t of the actual K with lambda_i>0,
as supplied by L163 for t>0. The basis e_i odot e_j (i<=j) of
Sym^2 H has D-eigenvalues lambda_i+lambda_j>0. Thus D is invertible,
and (5) proves nondegeneracy of G. No uniform positive lower bound
on the eigenvalues across F is needed; their strict positivity for
each datum suffices.

**Zero space, empty support and numerical consequence.** If t=0,
H=Sym^2 H=0 and the rank is zero directly. The unique map from the
zero space to its dual is an isomorphism, so the nondegeneracy and
injectivity conclusions hold without selecting an eigenvector or
asserting a nonzero Q_i diagonal. The following inequalities hold
in this case as well.

For any t, beta(x)=0 implies G(x,y)=0 for every y and hence x=0.
Equivalently G^flat=beta^vee Q^flat beta has rank at most dim E.
L116 gives the whole obstruction dimension, so

    t(t+1)/2 <=724+2t,
    f(t):=t^2-3t-1448 <=0.                                   (6)

There is no subtraction of s: the two degree-two contributions
have dimensions 724-s+2t and s. If Z is empty, W=0 and the same
sum is 724+2t. No step evaluates at a point of Z, divides by s,
or requires s>0, so (1)–(6) retain their meanings when Z is empty.

Now f(39)=-44 and f(40)=32. For every integer n>=40,
f(n+1)-f(n)=2n-2>0, so (6) implies t<=39. Since omega is a
nondegenerate alternating complex bilinear form for t>0, t must
be even: a matrix A of omega satisfies A^T=-A, whence for odd t
det A=det A^T=det(-A)=-det A and det A=0 in characteristic zero,
a contradiction. The t=0 case is already even. Therefore t<=38.
The adjacent permitted even values show the precise threshold:

    t=38: dim Sym^2 H=741 <=800=dim E,
    t=40: dim Sym^2 H=820 >804=dim E.

Passing the rank test at t=38 does not construct F or establish
compatibility of its other constraints. It only shows that this
dimension comparison alone has no contradiction at that value.
The full bilinear Gram calculation is essential; the zero diagonal
quartic of a single bracket would not determine this rank.

This extends the same audited mechanism, preserving L179's smaller
formal checklist and the distinct stops in ATTEMPTS/057,/090,/092–096.
It supplies no metric comparison with a Leray complement or arbitrary
replacement for the actual K. Independent existence and cycle-realization
gaps remain after the separate audit below.

**Separate conceptual audit, 2026-10-29 (step 613).** The invocation-start
SPECIALIZE assessment is
`drafts/literature/2026-10-29-uniform-bracket-multiplicity-critical-audit.md`.
This audits the uniform specialization, retaining L116, L163, L165
and L180 as conditional inputs and checking their uses here. L117's
actual cup identities enter through L163. It is not a fresh audit of
every ancestor. The precisely cited primary results above and their
approved source readings are reused; no additional source hypothesis
or independent factor action is introduced.

First check the whole bracket domain. For degree-one closed
End_0(F)-valued forms its unhalved formula is alpha beta+beta alpha.
Graded trace makes its trace zero. Changing alpha by bar-partial f,
with f of degree zero, changes its bracket with closed beta by
bar-partial[f,beta]. It therefore defines a symmetric bilinear map
H x H -> E, hence the stated linear beta on all Sym^2 H. No equation
[alpha,alpha]=0 is imposed on its domain.

For the signs in (1), order a decomposable term Aa,Bb,Cc,Dd as abcd.
The scalar products with pairings (ab)(cd), (ac)(bd), (ad)(bc) have
signs +,-,+ relative to the ordinary coefficients. The imported
four-matrix identity consequently has all three plus signs in scalar
form notation. Calling these products P,U,V_0, the four bracket words
give (P+U+V_0)/2, (-P+U+V_0)/2, (-P+U+V_0)/2, (P+U+V_0)/2.
Their sum is 2(U+V_0), as asserted. Separate multilinearity extends
this to arbitrary forms and repeated inputs; repeated exterior indices
contribute zero. The case alpha=beta, gamma=delta gives
4tr(alpha gamma)^2; all four inputs equal gives zero. The latter is
a null-vector identity, not a radical condition on the Gram form.
The differential is a derivation and commutes with trace; Stokes
against the closed volume on compact X removes every exact change.
Thus this full-domain identity descends independently of t and Z.

Next, scalar Kunneth gives exactly the two lines in (2), since K3
H^1(O)=0. Their squares vanish by factor dimension and their product
is nonzero. This does not split the V-valued product. The actual j_1
is onto all H^1(X,V), so R_H is an antilinear bijection on the entire
H. Harmonic preservation makes the representative of j_1 R_H v
precisely R alpha_v. Inserting (2) in L163's integrals gives (3):
theta_2 selects omega and theta_1 selects eta. Even-degree interchanges
introduce no relative sign, and sigma_i bar(sigma_i)=4dvol_i gives
the same nonzero T_0/8 in both comparisons.

For all nonzero H, Q_2 is strict: a radical vector makes
theta_2 cup j_1u pair to zero with all Rj_1v. Serre duality and the
actual identity theta_2 cup j_1=j_3J force u=0. With W retained,
j_3 is still an isomorphism: L116's retraction kills the incoming
H^0(W) boundary, and finite support kills H^1(W). Q_1 has a different
strictness argument. A zero diagonal kills the second cotangent
component of the harmonic representative; closedness makes its
first-component evaluations holomorphic sections of
End_0(F|_{ {x} x B}). The retained charge-21 stability and stable
simplicity kill them for every x. No point of Z or fibrewise harmonicity
is required. Hence surjectivity of the single R_H legitimately gives
nondegenerate omega and eta(u,w)=omega(Ku,w) for every u,w. L163's
spectral theorem concerns the actual K, with strictly positive spectrum.

For the Gram form, expanding (1) using theta_i^2=0 gives exactly
the four mixed terms before (5), with one common Serre constant c_X.
Substituting eta=omega(K-,-) yields A_2(D-,-) term by term. The
tensor flip F satisfies B(Fx,y)=B(x,Fy). Its two eigenspaces span
the tensor square and are orthogonal, so nondegenerate B restricts
nondegenerately to each. The stated symmetric-tensor convention gives
B|_{Sym^2}=A_2/2, including repeated inputs. Every basis tensor
e_i odot e_j has eigenvalue lambda_i+lambda_j>0 for D, including
i=j. Thus G is nondegenerate on the full space of dimension t(t+1)/2.
No uniform lower bound on those eigenvalues across F is needed.

For t=0 the domain and its dual are zero, their unique map is an
isomorphism and beta is injective directly. No positive diagonal or
eigenvector is invoked. For all retained t, G^flat factors as
beta^vee Q^flat beta, hence has rank at most the full dim E. L116's
two degree-two terms have dimensions 724-s+2t and s; both belong
to E and sum to 724+2t. If Z is empty the second term is zero and
the same formula holds. No step evaluates at a split point, divides
by s or removes the finite-point contribution.

Multiplying the rank inequality by two gives (6). Direct substitution
gives f(39)=1521-117-1448=-44 and f(40)=1600-120-1448=32.
The difference f(n+1)-f(n)=2n-2 is positive for n>=40, excluding
all integer t>=40. Nondegenerate alternating omega rules out odd t
by the characteristic-zero determinant argument, and t=0 is already
even. Therefore the final bound is even t<=38. The adjacent even
tests are 741<=800 at t=38 and 820>804 at t=40. Passing the former
is only compatibility with this dimension comparison.

All required comparisons and both boundary cases survive. This audit
is EXPLORATION / REPRODUCTION: it verifies the existing conditional
claim without a repair, stronger restriction or advance beyond the
assessed sources. No cardinality combination is made. L179's witness
and ATTEMPTS/057,/090,/092–096 remain intact; they are neither inputs
nor substitutes for the actual product. Remaining parameters, F
existence, other stable types, transport and primitive algebraic
realization are unresolved.

## Mathlib

Full matching Mathlib coverage for this actual-cup uniform Gram bound
has not been checked. The tensor-square argument, determinant parity
test, spectral theorem and pullback-rank inequality are supporting
finite-dimensional facts, not a claimed full matching formal theorem.
Their specializations are proved above; the trace, harmonic and duality
results are imported with the cited qualifications. Unknown coverage
is not absence. The separate informal audit above does not provide Lean
verification, certified novelty or a complete Hodge-conjecture solution.
