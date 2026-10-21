# L091 — The global cubic norm makes the seven-adic filter redundant on T

## Hypotheses

Use L069's entire fields K and D, and L088's rational cubic F, with

    g(X)=X³−4X²−160X−1264,
    F=Q(theta)=Q[X]/g, D=K tensor_Q F,
    [K:Q]=12, [F:Q]=3, [D:Q]=36.

Use exactly L074's supported space W_S: all normalized maximal-prime
valuations of a representative are even outside the primes above two
and eleven, and its D/K element norm is square. Negative valuations
and nonunit representatives of localized ideal-class lifts are allowed.
Let T be precisely L084's subspace of W_S. Import L088's audited
conclusion that N_D/F(z) is square in F for every [z] in T.

Use L090's audited entire seven-adic field U=K tensor_Q Q7, unramified
of degree twelve with residue field k=F_(7^12). The entire cubic over
U splits, with ordered roots alpha,beta,gamma reducing to 4,i,−i,
where i²=−1 in F49. Thus D tensor_Q Q7=U³. Write nu for the
nonsquare unit class in U and retain L090's exact primitive image

    J7={ (1,1,1), (1,nu,nu) }.

No S-unit basis, localized class-kernel value, global realization of
an arbitrary local tuple, point-class hypothesis or integer solution
is assumed.

## Conclusion

Every [z] in T has loc_7([z]) in J7. Hence

    T intersect loc_7^(-1)(J7)=T.

More generally, this holds for any class in D*/D*² with even valuations
at every prime above seven and square D/F norm. On the entire local
even-valuation square-class subgroup, the necessary envelope imposed
by both norm-square conditions D/F and D/K is exactly J7.

Thus seven gives no additional pruning of this unchanged T. Neither
dim T<=13+dim ker(n_S) nor the supported-unit upper bound fourteen
improves; no rank bound, global class realization or integer exclusion
follows. This is a field-specific reproduction of the assessed norm
methods. Independent critical application audit completed on 2026-10-18
confirms the conclusion without a mathematical correction.

## Proof

### Imported results and the specialization being performed

The unchanged prior SPECIALIZE assessment is
`drafts/literature/2026-10-18-seven-filter-on-t.md`. The general
results below are cited, not reproved. The additional work is the
ordered completion-norm comparison on these particular fields,
including both embeddings over the quadratic completion.

Import J.S. Milne, *Algebraic Number Theory*,
[v3.08, 19 July 2020](https://www.jmilne.org/math/CourseNotes/ANTc.pdf),
Proposition 8.2 and Corollary 8.4, printed p.136: completion of a
finite separable field extension is the product over all extending
places, and its norm is the product of the factor norms. Import
Stacks Project [Lemma 31.18.6, tag 0BD2](https://stacks.math.columbia.edu/tag/0BD2):
the determinant norm for a finite locally free algebra of positive
degree commutes with arbitrary base change. Characteristic zero
supplies separability; D/F and D/K are finite free of degrees twelve
and three, respectively. No normality is required.

For unramified local extensions, use Milne, *Class Field Theory*,
[v4.03, 6 August 2020](https://www.jmilne.org/math/CourseNotes/CFTc.pdf),
III Proposition 1.2 and Lemmas 1.3–1.5 with proof, printed p.98:
the norm on units reduces to the residue-field norm. For the residue
norm formula over an arbitrary finite base use Keith Conrad,
[*Finite fields*](https://kconrad.math.uconn.edu/blurbs/galoistheory/finitefields.pdf),
Theorem 5.7, pp.10–11, accessed 2026-10-18 (no version date identified),
with Theorem 4.6 and proof, pp.9–10. In particular the finite base may
be F49; a prime-base-only formula would not cover the quadratic
completion below. Odd-characteristic unit-square lifting is the
simple-root case of Pete L. Clark, *Algebraic Number Theory II*,
[161-page notes](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf),
Corollary 1.77, p.57, and Theorem 1.79, p.58. Every square-root lift
used below starts with a nonzero residue root, whose derivative is
a unit since the residue characteristic is seven.

### All local factors and their ordered norm maps

By L090, the reduction gbar=(X+3)(X²+1) has distinct roots over F49,
and its second factor is irreducible over F7. Its lifted entire
Q7-algebra is therefore

    F tensor_Q Q7 = Q7 × V,

where V is the unramified quadratic extension. In the first factor
theta maps to alpha. In V write theta_V for the image of theta.
There are two embeddings j_beta,j_gamma:V -> U sending theta_V to
beta,gamma. Their images are the same quadratic subfield U_2 of U,
and the embeddings differ by the nontrivial Q7-automorphism of V.
The rational component has degree one; the other component has
degree two. These exhaust all three degrees of F.

The corresponding entire D algebra is

    (K tensor_Q Q7) tensor_Q7 (F tensor_Q Q7)
        = U × (U tensor_Q7 V) = U_alpha × U_beta × U_gamma.

Explicitly the last two factors arise from the map
u tensor v -> (u*j_beta(v),u*j_gamma(v)). In particular the two
V-actions are different, while the U-action from K is diagonal in
all three factors. Over the rational factor of F the extension has
degree twelve. Over V there are two degree-six factors, since
[U:U_2]=6. The total degree over Q7 is 12+12+12=36, and the total
degree over each factor of F is twelve. No factor is discarded.

For a localized representative z=(z_alpha,z_beta,z_gamma) in (U*)³,
the two components of its D/F norm are precisely

    N_U/Q7(z_alpha),
    j_beta^(-1)(N_U/U_2(z_beta))
        * j_gamma^(-1)(N_U/U_2(z_gamma)).                 (1)

Here each inverse is defined on U_2; the second line lies in V*.
The inverse embeddings are necessary to view both norms in the same
base V. In particular this is a product of two degree-six norms,
not one component being square separately. The D/K norm is

    z_alpha*z_beta*z_gamma in U*.                       (2)

These are determinant base-change formulas for the full algebras,
so they apply to arbitrary nonzero representatives, not only units
or values of a Kummer map.

### Even valuations and both residue bases

Since seven is outside the support of W_S, each component of any
[z] in T has even valuation. U is unramified and seven is a
uniformizer, so write

    z_j=7^(2m_j)*u_j,  m_j in Z, u_j in O_U*,
    j=alpha,beta,gamma.

Every factor 7^(2m_j) is square in U, including when m_j<0. Its
norm is square under every factor norm, and its inverse-embedding
image is square in the corresponding base. Thus replacing each
z_j by u_j leaves the input square classes and every norm-square
condition unchanged. This is local square removal, not an assertion
that z is an S-unit globally. It covers the supported nonunit lifts.

For a finite field of odd cardinality Q let chi_Q denote its
quadratic character on nonzero elements. For q=7 or 49 and n=12
or 6 respectively, the cited norm formula gives, for a in k*,

    chi_q(N_(k/F_q)(a))
      = (a^((q^n−1)/(q−1)))^((q−1)/2)
      = a^((q^n−1)/2) = chi_(7^12)(a).                 (3)

The local unit norm reduces to this finite-field norm. Unit square
classes in U and in either base are exactly their nonzero residue
square characters, by the cited lifting theorem. Each inverse
embedding in (1) preserves the quadratic character: a field
isomorphism preserves being a square. This explicitly includes
the nontrivial automorphism of the quadratic base, rather than
identifying its two embeddings without accounting for them.

Consequently, if e_j in F2 denotes the square-character bit of u_j
(zero for square and one for nonsquare), the ordered D/F norm
bits in Q7 and V are

    (e_alpha, e_beta+e_gamma).                         (4)

The D/K norm bit is

    e_alpha+e_beta+e_gamma.                            (5)

All norm valuations have already been removed by actual square
factors. Hence these character bits decide square classes of the
norms, not just a necessary unit-residue approximation.

### The complete envelope and containment

L088 makes the global D/F norm square for every [z] in T, so both
entries in (4) vanish. Thus

    e_alpha=0, e_beta=e_gamma.

Of all eight unit square-class tuples, exactly two satisfy these
equations: (0,0,0) and (0,1,1). Equation (5) vanishes on both and
therefore introduces no additional restriction. Conversely each of
these two local tuples has square norms in both directions by
(4)–(5), so the entire even-valuation necessary envelope is exactly
{(1,1,1),(1,nu,nu)}. This equality is only a local norm calculation;
it asserts no global realization of its second tuple in T.

This is exactly L090's J7, proving loc_7(T) subset J7 and the stated
redundancy. Changing the identification of the unramified field
preserves unit square characters, fixes the rational root alpha
and can only exchange beta,gamma. Both tuples are invariant under
that exchange. Thus no entire-fiber identification escapes the
comparison. The rational factor together with the D/K norm would
already suffice, but the quadratic factor calculation verifies
all completion norms as required.

This argument is symbolic and exhaustive; it uses no precision
sample or new arithmetic certificate. It imports L088's global
norm conclusion and L090's field/image result without rerunning
their certificates. The bounds 13+dim ker(n_S) and fourteen, the
localized class arithmetic and primitive integer lifting are all
unchanged. Seven-adic local properness versus the unrestricted
four-class Kummer image is consistent with redundancy on T.

### Independent critical application audit — 2026-10-18

This audit uses the prior SPECIALIZE assessment
`drafts/literature/2026-10-18-seven-norm-redundancy-audit.md` and is
REPRODUCTION. The audited L088 global norm and L090 entire field/image
are imported as stated; their certificates are not rerun. The check here
is their application to every class of the unchanged T, not merely to
units or point classes. The result passes without correction.

**Reconstruction of the ordered algebra.** Independently reducing the
fixed cubic gives X³+3X²+X+3=(X+3)(X²+1) over F7. The rational
root is 4 and the quadratic roots are distinct and nonrational, since
the nonzero squares in F7 are 1,2,4. The cited simple-root theorem
therefore gives the rational completion and the unramified quadratic
completion V. L090 supplies the entire unramified degree-twelve U.
In U[X]/g, evaluation at alpha,beta,gamma identifies all three factors
with U, while an element of K acts by the same scalar on each factor.
Over V the two evaluations are j_beta and j_gamma, not a common
scalar action. Their images are the same U_2 and differ by conjugation.

Apply the cited determinant base-change and completion norm theorems
with these scalar actions. For the first factor one obtains the
degree-twelve norm to Q7. On the beta factor the degree-six norm
lands in U_2 and must be transported by j_beta inverse to V; on the
gamma factor it must instead be transported by j_gamma inverse.
Taking their product gives the V component. Thus (1) is the norm of
the whole twelve-dimensional V-algebra. Over K's completion U all
three summands have rank one, giving (2). The ranks are 12 over Q7
and 6+6 over V, accounting for all 36 rational local dimensions.

**Valuations and characters.** For an arbitrary supported representative
write its three valuations as 2m_alpha,2m_beta,2m_gamma, with each
m_j an arbitrary integer. The norm valuations before removing squares
are respectively

    24m_alpha in Q7,
    12(m_beta+m_gamma) in V,
    2(m_alpha+m_beta+m_gamma) in U.

These use normalized valuations and residue degrees 12,6,6; all three
extensions are unramified. The factors 7^(2m_j) themselves are squares,
so deleting them changes none of the three norm square classes.
This also works for negative m_j and does not require a global unit
representative. Seven is outside L074's entire support, so this reduction
applies to every T-class, including localized ideal-class lifts.

For a residual unit a in k=F_(7^12), the Q7 norm has quadratic
character a^(((7^12−1)/6)*3)=a^((7^12−1)/2). The V norm has
character a^(((7^12−1)/48)*24)=a^((7^12−1)/2). These are the
cited finite-field norm formulas over the actual two residue bases.
The conjugation between j_beta and j_gamma preserves square status;
it does not introduce another exponent or a vanishing character.
In particular, relative degree six does not make the norm of every
unit square. Unit-norm reduction and odd-characteristic square lifting
now give the exact character rows

    D/F at the rational place: (1,0,0),
    D/F at the quadratic place: (0,1,1),
    D/K at its unique place: (1,1,1).

Their common kernel consists of 000 and 011; the last row is the sum
of the first two. Conversely any unit tuple with either of these bit
patterns has square norms in all the displayed bases, because its norm
valuations are even and its residual unit characters are trivial.
Thus the equality claimed for the local envelope is also sufficient,
without asserting that either nonidentity tuple globalizes in T.

**Universal implication and identification check.** L084 defines T
inside precisely L074's W_S, and L088 proves its D/F norm square
without a point-class or S-unit restriction. The preceding two D/F
rows therefore vanish for every class of T. L090 identifies their
kernel with the exact J7 in the same theta ordering. Every Q7-field
identification of U preserves square classes and fixes alpha; on the
quadratic subfield it either fixes or exchanges beta and gamma. Both
kernel tuples are invariant. The condition is consequently independent
of the allowed whole-fiber identification.

This accepts ATTEMPTS/041's seven-specific stop. It verifies a necessary
condition already satisfied by all of T, not a global realization,
another independent restriction or a full Beal candidate. Both dimension
bounds, actual localization at eleven, localized class arithmetic and
integer lifting remain unresolved. No arithmetic script is needed for
this exhaustive symbolic audit; no dependency or argument changes.

## Mathlib

Full matching coverage for this field-specific redundancy result,
and supporting coverage for the ordered tensor norms, unramified
unit square classes and residue norm characters: **not checked**.
Unknown availability is not evidence of absence. No Lean verification
or independent reproof of the imported general theorems is claimed.
