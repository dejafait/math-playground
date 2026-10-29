# L182 — Actual trace-free cubic product is detected by the retained four-word traces

## Hypotheses

Retain L116, L163 and L181's complete conditional family. Thus
X=S_1 x B is the product of the identical marked projective K3
surfaces with their common hyperkähler metric, ordered triple,
holomorphic forms sigma_1,sigma_2 and compatible unitary
hyperholomorphic connection. The hypothetical locally free rank-two
F is slope-polystable at the original real product class, has integral
c_1(F)=0 and full character

    ch(F)=2-14e_1-21e_2-tau_D+62e_1e_2.

Retain the full mixed tensor, marking, and charge-21 restriction
stability used for L163's strictness. Set V=End_0(F), p:X -> B,
M=R^1p_*V, W=R^2p_*V. The finite reduced split set Z may be empty;
W has length one at its points. Keep the actual truncation inclusion
j, trace-adjoint retraction r and projection a of L116, with rj=id.
Put H=H^0(B,M), retain the approved surviving range even 0<t<=38,
where t=dim H, and write a_u=j_1u. L163 supplies actual isomorphisms

    j_1:H -> H^1(X,V),
    j_3:H^2(B,M) -> H^3(X,V),
    J:H -> H^2(B,M),
    j_3 J=theta_2 cup j_1,   j_3 Phi_1=theta_1 cup j_1,
    K=J^{-1}Phi_1,   theta_i=[bar(sigma_i)].

Use L180/L181's actual alternating scalar cups

    tau(u,v)=tr(a_u cup a_v)
            =omega(u,v)theta_1+eta(u,v)theta_2,
    eta(u,v)=omega(Ku,v).

The same harmonic R and strictly positive factor forms remain in
force; no extra metric compatibility is imposed. All products first
take place in End(F), with wedge and composition. Define the
holomorphic projection pr_0(A)=A-tr(A)Id_F/2 in every Dolbeault
degree. No existence of F, integrability of sections, multiplicative
Leray splitting, independent factor rotations, or harmonicity of
products is assumed.

## Conclusion

The actual transported trilinear map

    C(u,v,w)=J^{-1}j_3^{-1}pr_0(a_u cup a_v cup a_w)

satisfies

    2C(u,v,w)=omega(v,w)Ku+eta(v,w)u
             +omega(u,w)Kv+eta(u,w)v
             +omega(u,v)Kw+eta(u,v)w.                       (1)

No symmetry of C is assumed. More precisely, the untransported
identity

    2pr_0(a_u a_v a_w)
      =tau(v,w)a_u+tau(u,w)a_v+tau(u,v)a_w                 (2)

is equivalent, for these actual groups and all u,v,w, to L180(2)'s
full four-word trace identity paired with every a_x, x in H.
L180 proves that identity before its endpoint substitution, so it
applies at the present t. Consequently this universal cubic test
adds no condition to the retained full four-word traces and supplies
no improvement of even t<=38 or any bound on s=|Z|. Equivalence is
with the full trace identity, not with its weaker numerical rank
consequence alone.

This is a local NEGATIVE / REPRODUCTION (step 615, 2026-10-29): it
closes the approved independence test, not a new universal identity
or an originality claim. It constructs no compatible cohomology
algebra or F and does not settle t=0, other stable types, transport,
or primitive algebraic-cycle realization. Separate critical audit of
this specialization has not been performed.

## Proof

**Imported coefficient identity and the specialization.** The prior
SPECIALIZE assessment is
`drafts/literature/2026-10-29-actual-cubic-product-compatibility.md`.
Import S. A. Vasyutkin and A. P. Chupakhin, *Constructing a Minimal
Basis of Invariants for Differential Algebra of 2 x 2 Matrices*,
J. Appl. Ind. Math. **16** (2022), 356–364, Section 2, Assertion 1
and its proof, p.358, with (4) and the trace-free projection (6),
pp.358–359,
[DOI](https://doi.org/10.1134/S1990478922020156),
[inspected author text](https://www.researchgate.net/publication/365419265_Constructing_a_Minimal_Basis_of_Invariants_for_Differential_Algebra_of_2times_2_Matrices).
For ordinary traceless complex 2-by-2 matrices A,B,C, its trace-free
specialization is

    2pr_0(ABC)=A tr(BC)-B tr(AC)+C tr(AB).                 (3)

Indeed in Assertion 1 all terms containing tr(A), tr(B) or tr(C)
vanish; the remaining scalar term tr(ABC)Id disappears under pr_0,
and the three displayed right-hand matrix terms are already
trace-free. This is an import with its necessary specialization,
not a reproof of Cayley–Hamilton or the source identity.

For composition, differential and graded trace, reuse E. Lepri and
M. Manetti, *Connections and L-infinity liftings of semiregularity
maps*, [arXiv:2102.05016v3](https://arxiv.org/pdf/2102.05016v3),
22 May 2021, Section 2 product/(2.1), p.4, Lemma 2.6 with proof,
pp.6–7, Definition 3.1/(3.2) and Example 3.3, pp.7–8. F has
internal degree zero; its Dolbeault one-forms have odd degree.
These sources do not state (1) for the notebook's actual maps.

**All exterior signs and words.** For V-valued one-forms
alpha,beta,gamma put T(alpha,beta)=tr(alpha beta). On one
decomposable term alpha=A a, beta=B b, gamma=C c, use abc as
exterior order. The terms alpha T(beta,gamma), beta T(alpha,gamma),
gamma T(alpha,beta) have respective orders abc,bac,cab, with
signs +,-,+. Thus (3), with its minus on the middle matrix term,
becomes

    2pr_0(alpha beta gamma)
      =T(beta,gamma)alpha+T(alpha,gamma)beta
                              +T(alpha,beta)gamma.         (4)

Moving a scalar two-form past a one-form has positive sign. The
identity is separately multilinear, so expansion proves it for
arbitrary one-forms, including repeated exterior indices, whose
corresponding exterior monomials vanish on both sides. Traces of
two odd inputs satisfy T(beta,alpha)=-T(alpha,beta).

To check all six orders explicitly set

    U=T(beta,gamma)alpha,
    V_0=T(alpha,gamma)beta,
    W_0=T(alpha,beta)gamma.

The right sides giving twice the trace-free ordered products are

    alpha beta gamma:  U+V_0+W_0,
    alpha gamma beta: -U+V_0+W_0,
    beta alpha gamma:  U+V_0-W_0,
    beta gamma alpha:  U-V_0-W_0,
    gamma alpha beta: -U-V_0+W_0,
    gamma beta alpha: -U-V_0-W_0.

These are (4) with its arguments reordered, using only the stated
alternation. They do not impose an unproved symmetry on the product.
Repeated entire inputs give

    pr_0(alpha alpha gamma)=T(alpha,gamma)alpha,
    pr_0(alpha gamma alpha)=0,
    pr_0(gamma alpha alpha)=-T(alpha,gamma)alpha.

In particular pr_0(alpha^3)=0. This is trace-free vanishing; no
vanishing of the unprojected form alpha^3 is asserted.

**Descent and actual transport.** In a holomorphic frame the
Dolbeault differential is a derivation of the endomorphism product,
and trace and pr_0 commute with it. For closed inputs all products
above are closed. Replacing any one input by an exact term changes
each product by an exact term, with the derivation sign for that
position. Formula (4) therefore descends to (2) in H^3(X,V).
This argument takes products before trace-free projection; V has
not been treated as an associative subalgebra.

The scalar cohomology decomposition into theta_1,theta_2 is exactly
the one in L180/L181. Since the scalar classes have degree two,
L163's actual endpoint identities give, for each u,v,w,

    j_3^{-1}(tau(v,w) cup a_u)
       =omega(v,w)Phi_1u+eta(v,w)Ju.

Apply J^{-1} to this equality and to the other two terms of (2).
This proves (1) with the actual K=J^{-1}Phi_1. No splitting of the
endomorphism cohomology ring, representative harmonic product, or
independent choice of the scalar forms is used.

**Exact Serre detection of the defect.** For arbitrary u,v,w define
the defect of (2) as

    D(u,v,w)=2pr_0(a_u a_v a_w)
              -tau(v,w)a_u-tau(u,w)a_v-tau(u,v)a_w
             in H^3(X,V).

Because tr(a_x)=0, the scalar subtraction in pr_0 contributes
nothing after multiplying by a_x and taking trace. Scalar classes
of degree two commute with all the displayed classes. Hence

    tr(D(u,v,w) a_x)=2tr(a_u a_v a_w a_x)
       -tau(v,w)tau(u,x)-tau(u,w)tau(v,x)
       -tau(u,v)tau(w,x) in H^4(X,O_X).                    (5)

The right side is exactly the defect of L180(2): its three positive
terms are tau(u,v)tau(w,x), tau(u,x)tau(v,w), and
tau(u,w)tau(v,x). L180 obtains this full four-word formula locally,
before its endpoint dimension substitution, and its proof checks
coincident inputs. Thus it holds for all the present u,v,w,x, not
only for the four words in the bracket expansion or for diagonal
brackets. This proves that L180's retained trace identity makes
every class in (5) zero.

For the reverse detection, retain the perfect Serre pairing from
L163,

    H^3(X,V) x H^1(X,V) -> C,
    (d,a_x) |-> c integral_X sigma_1 sigma_2 tr(d a_x),

where c is any one fixed nonzero normalization constant. Its precise
primary input is J.-P. Demailly, *L2 vanishing theorems for positive
line bundles and adjunction theory*,
[alg-geom/9410022v3](https://arxiv.org/pdf/alg-geom/9410022v3),
28 February 1995, Section 4.A, (4.3)–(4.4'), PDF pp.27–28, with
the trace self-duality of V and the nowhere-zero holomorphic volume
form as justified in L163. X is compact Kähler, and V is a locally
free holomorphic bundle. The trace form is nondegenerate on its
trace-free rank-two endomorphisms in characteristic zero.

The actual j_1 is onto H^1(X,V). Therefore vanishing of (5) for
every x makes D(u,v,w) orthogonal to the entire Serre-dual space,
so D(u,v,w)=0. Conversely (2) makes (5) vanish; this gives the
four-word trace identity for all x. Since
H^4(X,O_X)=C theta_1 theta_2 and its integral against sigma_1 sigma_2
is T_0=16 Vol(X) != 0, the integrated and scalar-class versions
are equivalent as well. All word orders and repeated inputs are
included by arbitrary choice of u,v,w,x.

This equivalence also holds after applying the actual isomorphism
J^{-1}j_3^{-1}; transport cannot leave an undetected extra component.
It does not say that L181's numerical inequality alone implies the
four-word identity, or that any abstract forms satisfying that
inequality are realized by F. Rather the actual retained identities
already imply the full proposed cubic constraint. There is no new
rank or parameter test. For scale, L181's retained endpoint of the
inequality remains 741<=800 at t=38, versus 820>804 at t=40;
the cubic supplies no strengthening of either comparison.

Park exclusion by this universal degree-three identity alone.
Reopening requires materially additional geometric control, not
repolarization of the same trace pairing. The actual lower products,
section quadrics, realization of the remaining data and the main
Hodge gap remain unresolved. ATTEMPTS/094's distinct degree-(1,1,2)
cyclicity stop and ATTEMPTS/096's smaller formal witness are not
premises of this proof and remain preserved.

## Mathlib

Full matching coverage for this graded cubic specialization,
actual j_3/J transport and Serre-detection equivalence has not been
checked. No absence claim is made. The imported ordinary matrix
identity and duality theorems are the mathematical inputs; generic
matrix or linear-algebra support is not claimed to formalize this
family-specific result.
