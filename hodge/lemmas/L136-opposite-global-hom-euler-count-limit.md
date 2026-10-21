# L136 — Whole opposite Hom Euler identity retains an uncontrolled middle term

## Hypotheses

Retain L071, L118, L120, L121 and audited L135 in their equality-kernel
setting. In particular B=S_1 and Y=S_2 are the identical marked smooth
projective complex K3 surfaces with the specified common hyperkähler
metric, real ample h and product class Omega. The full integral mixed
tensor tau_D is self-adjoint, satisfies tau_D^2=156 e_1e_2, and has
D sigma=2lambda sigma with 1<lambda<5/4. Suppose F on B times Y is
locally free of rank two, Omega-slope-polystable, with integral c_1=0 and

    ch_2(F)=-14e_1-21e_2-tau_D.

Let G on Y times B be the exchanged actual F. L118 gives one common
polarization for which all its fibres E_x are stable of charge 21,
and a natural classifying morphism f with injective KS differential.
L120 identifies B with the normalization of the reduced image. L121
gives a finite reduced off-diagonal coincidence scheme R_off, disjoint
from the diagonal, possibly empty. Put N=length(R_off); this counts
ordered pairs. No existence of F or of a coincidence is established.

On T=B times B let i:B -> T be the diagonal, p:Y times T -> T the
projection, G_1,G_2 the two pulled-back actual families, and

    K=Rp_*(G_1^vee tensor G_2),   M=H^1(K),   W=H^2(K).

These are the full Hom coefficient and ordinary cohomology sheaves;
no trace-free coefficient is imposed between independent parameters.

## Conclusion

The actual ordinary cohomology sheaves satisfy

    H^0(K)=0,
    W ≅ i_*(H^2(Y,O_Y) tensor O_B) ⊕ direct_sum_{r in R_off} k(r).

The diagonal has precisely its reduced scheme structure. Its coefficient
line is the trivial trace line, not an unspecified line bundle. The
residue-field identifications off the diagonal need choices of generators.
There are no other cohomology sheaves outside degrees 0,1,2.

Absolute coefficient HRR and the whole-complex Euler identity give

    chi(T,K)=-200,
    -200=-chi(T,M)+2+N,
    N=chi(T,M)-202.                                      (1)

Thus N<=C would require chi(T,M)<=C+202. The covered spectral sequence,
reverse derived duality and local stalk data supply no such upper
estimate in this attempt. The Euler-count mechanism is parked at that
specific missing estimate. This is a NEGATIVE / REPRODUCTION sufficiency
test, with a new conditional notebook calculation, not a result beyond
the inspected general tools. The separate critical audit below preserves it.
It proves neither that arbitrary N is geometrically possible nor that
no different argument could bound N. F existence, collision existence,
a useful global normalization-defect comparison, transport and universal
primitive rational Hodge realization remain unresolved.

## Proof

**Scope and named imports.** The prior SPECIALIZE assessment is
`drafts/literature/2026-10-20-opposite-hom-global-euler-count.md`.
Reuse its primary-source coverage; no further literature search or new
positivity assertion is used. The actual-family specialization is needed
because Markman's full-moduli diagonal theorem has incompatible
rank/codimension hypotheses for this four-dimensional pair base.
In particular we do not apply his Chern-class formula with the parameter
dimension substituted for the moduli dimension.

Import perfect pushforward and arbitrary derived base change from
[Stacks Lemma 36.30.4(1), 0B91](https://stacks.math.columbia.edu/tag/0B91),
and minimal free representatives and spreading from
[Lemmas 15.77.6–7, 0BCC](https://stacks.math.columbia.edu/tag/0BCC) and
[0BCD](https://stacks.math.columbia.edu/tag/0BCD). The projection is
proper, flat and finitely presented and the coefficient is locally free.
Stable Hom/simplicity are Huybrechts–Lehn, *The Geometry of Moduli Spaces
of Sheaves*, first edition (1997), Proposition 1.2.7 and Corollary 1.2.8,
pp. 11–12, together with named surface Serre duality. L118 checks common
stability and the same numerical invariants. Use L135's actual coefficient
sequence/minimal-complex comparison and graded reverse-Serre computation,
whose cited deformation and connecting-map sources cover two independent
bundle deformations also when their central parameters agree.

Use the bounded coherent hypercohomology spectral sequence from
[Stacks Lemma 20.29.1 and Example 20.29.3, 0FLJ](https://stacks.math.columbia.edu/tag/0FLJ).
Use absolute smooth proper HRR from
[Stacks 42.66, 02UO](https://stacks.math.columbia.edu/tag/02UO), equivalently
Fulton, *Intersection Theory*, second edition (1998), Theorem 15.2,
pp. 286–287, and Example 15.2.8, pp. 291–292. These are imported
theorems, not reproved below. All characters and integrations are in
rational cohomology. No algebraic Chow equality is claimed.

**Amplitude and the ordinary bottom sheaf.** At every pair the derived
fibre is RHom_Y(E_x,E_z). As in L135 its dimensions are (0,76,0) when
the bundles are nonisomorphic and (1,78,1) when they are isomorphic.
This follows from stable Hom, Serre duality and surface HRR; the Euler
pairing is -76. Minimal representatives and spreading therefore give
amplitude [0,2] locally on T. In particular the last-row cokernel
commutes with every base change, unlike a general middle cohomology
sheaf. The support of W is exactly i(B) union R_off.

The sheaf H^0(K)=p_*(G_1^vee tensor G_2) is torsion-free on integral T.
Indeed multiplication by any nonzero regular base function is injective
on the coefficient: the product projection is flat and the coefficient
is locally free. Applying left-exact p_* preserves that injection.
Away from the coincidence support, the perfect complex is concentrated
in degree one, so H^0(K) vanishes on a dense open. A torsion-free
coherent sheaf on an integral scheme with zero generic fibre is zero.
This proves the first assertion without confusing ordinary Hom with
the nonzero derived Hom at a coincident pair.

**Actual diagonal restriction of the top sheaf.** On the diagonal the
two pulled-back actual families are the same G, so derived base change
identifies Li^*K with the relative pushforward of End(G) on Y times B.
The trace and scalar inclusion split that coefficient as

    End(G)=O_{Y times B} ⊕ End_0(G).

All trace-free endpoint fibre cohomology vanishes, by stability and
surface Serre duality. Minimal representatives hence put its relative
pushforward locally in degree one. Thus its top sheaf is zero, and
the actual trace identifies

    H^2(Li^*K)=H^2(Y,O_Y) tensor O_B.                    (2)

Since K has a local finite free representative ending in degree two,
taking its last cokernel commutes with tensoring by O_B. Consequently
i^*W equals (2). This uses top-degree base change only and asserts no
ordinary middle-sheaf pullback theorem.

It remains to eliminate transverse thickness; (2) alone does not do so.
At r=(b,b), write R=O_{T,r}, m its maximal ideal and J the diagonal
ideal. A minimal representative is R -> R^78 -> R in degrees 0,1,2.
Let I be the ideal of its last row. Then W_r=R/I. Applying (2) gives
R/(I+J) ≅ R/J as R/J-modules. The right side is faithful, so I is
contained in J.

For a tangent vector t=(u,v), the actual reverse degree-zero connecting
map on the central identity of E_b is

    delta_rev(t)(id)=kappa_b(u)-kappa_b(v).

This is the coefficient sequence for the two actual dual-number
families. L135's finite-flat-Cech comparison identifies it with the
linearized minimal complex, also at this diagonal point: no step of
that coefficient comparison uses distinct central parameters.
The graded reverse-Serre transpose is, with its notation,

    P(id,ell(t)beta)=-Q(delta_rev(t)(id),beta).            (3)

Here ell is the linearized last row, P in degrees (0,2) is nonzero
on the generator id and Q in degrees (1,1) is perfect. Both Hom factors
vary independently. L118's injective natural KS differential implies
that the kernel of delta_rev is exactly u=v. By (3) the kernel of ell
is the same diagonal tangent space. Thus the last-row coefficients
have two independent conormal linear parts, spanning the diagonal
conormal space in m/m^2.

The diagonal is smooth of codimension two in smooth T. Choose regular
parameters x_1,x_2,z_1,z_2 with J=(x_1,x_2). Since I is contained in J,
each last-row entry is a linear combination of x_1,x_2. Two entries
have independent conormal linear parts, so the determinant of their
two coefficient rows is a unit in R. They therefore generate J itself.
This proves I=J, including all higher-order row terms. Equivalently it
is the Nakayama test on J/I; its relevant dimension is two normal
directions, rather than L135's four off-diagonal directions.

This holds at every closed diagonal point. Coherence and finite type
then give J W=0 on a neighborhood of the whole diagonal; any nonzero
remaining coherent quotient would have a closed support point. Now
(2) identifies the entire diagonal summand with the trivial trace line.
There is no hidden twist, since identity and trace were constructed
using the actual G, not local universal bundles with untracked base lines.

L121 separates the finite off-diagonal support from the diagonal, and
audited L135 gives W_r=k(r) at each such point. Coherent sheaves on the
disjoint closed support pieces decompose by their comaximal ideals.
This proves the stated complete description of W, including N=0.

**Absolute sixfold coefficient index.** Use point classes y on Y and
b,c on the two B copies, all of integral one. Write t_1,t_2 for the
two full pulled-back mixed tensors. L071's rank-two character identity
gives beta^2=(2 times 14 times 21+156)P=744P and
ch(F)=2+beta+62P. In the Y-first order this says

    ch(G_1)=2-21y-14b-t_1+62yb,
    ch(G_2)=2-21y-14c-t_2+62yc.                           (4)

The odd characters vanish, so dualizing G_1 changes no term in (4).
The Todd classes of the three factors are 1+2y, 1+2b, 1+2c.
Integrating either parameter factor first, with its Todd factor, gives

    integral_B ch(G)(1+2eta_B)=-10+20y.                  (5)

In (5) a single mixed class has parameter degree two and cannot pair
with the parameter Todd class to top degree. Even the product t_1t_2
in the full sixfold integrand has parameter degrees two on each copy,
so contributes zero to the absolute integral. These vanishings concern
this index, not the whole relative Chern character. The full mixed
square 156 has already entered the coefficient 62 in (4) and is retained.

Absolute HRR, Fubini for factor integrations, and y^2=0 give

    chi(T,K)
      =integral_{Y times B times B} ch(G_1^vee) ch(G_2)
                                      (1+2y)(1+2b)(1+2c)
      =integral_Y (-10+20y)^2(1+2y)
      =200-400=-200.                                   (6)

An independent direct expansion makes the coefficient free of mixed
generators equal to

    4-84y-28(b+c)+418y(b+c)+196bc-1736ybc.

Multiplying all three Todd factors yields top coefficient -200 again.
Equivalently, integrating Y first, the pure part of the relative
character is -76+362(b+c)-1344bc. Its remaining mixed part has degrees
(2,2) on the parameter copies and pairs to zero with their Todd factors.
The parameter integral is -304+1448-1344=-200. This is a check of the
absolute calculation, not an ordinary higher-image GRR assumption.

**Whole-complex Euler identity and the stopping threshold.** The bounded
spectral sequence E_2^{a,j}=H^a(T,H^j(K)) converges to the coefficient
hypercohomology. All terms are finite-dimensional, and its alternating
sum is unchanged by differentials. Therefore no degeneration is needed:

    chi(T,K)=-chi(T,M)+chi(T,W).

The diagonal trace line has Euler characteristic chi(B,O_B)=2; each
off-diagonal residue field contributes one. Hence chi(T,W)=2+N,
and (6) proves (1). M has generic rank 76, but its Euler characteristic
is not its rank or a nonnegative cohomology dimension. The justified
nonnegativity N>=0 gives the lower bound chi(T,M)>=202, which is the
wrong direction for bounding N above.

For clarity, reverse derived duality from
[Stacks Remark 48.12.6, 0G81](https://stacks.math.columbia.edu/tag/0G81)
gives K^vee ≅ K_rev[2], with K_rev=Rp_*(G_2^vee tensor G_1).
The coefficient pairing is the perfect composition/trace pairing and
the relative canonical line is trivialized by a fixed Y two-form.
The surface shift is two even though T has dimension four. Exchange
of the parameter factors identifies K_rev with the pullback of K.
On the Calabi–Yau fourfold T, derived Serre duality consequently gives
the same Euler value; it supplies no upper estimate on chi(T,M).
It does not identify M with an ordinary locally free self-dual sheaf:
derived truncations can carry additional sheaf-Ext terms supported on
the diagonal and isolated points. The local stalk computations evaluate
W, not these global middle cohomology groups.

Thus neither taking the Euler sum nor this duality comparison removes
the unknown chi(T,M). No IT, ordinary middle pullback, middle-sheaf
stability, singular metric extension, or H^1(O_image) vanishing is among
the justified inputs. The bounded test stops here. This is a precise
unresolved estimate, not a theorem that all conceivable consequences of
the full geometric hypotheses fail. ATTEMPTS/046's Hom-jump warning
and ATTEMPTS/073's coherent-vanishing stop remain intact.

**Verification and qualifications.** Reproduce the exact rational
bookkeeping with `python3 scripts/opposite-hom/check_global_euler.py`.
The full certificate is
`scripts/opposite-hom/global_euler_certificate.json`; seven arithmetic
checks pass, both indices are -200, and no upper count bound is output.
The full coefficient and absolute-integrand expansions were inspected,
not merely their previews. The script checks cohomological arithmetic;
the sheaf identification and the actual KS comparison are the proof
above. It constructs neither a coherent M with arbitrary N nor F.

**Separate critical audit, 2026-10-20 (step 423).** The pre-invocation
SPECIALIZE assessment is
`drafts/literature/2026-10-20-opposite-global-hom-euler-critical-audit.md`.
This is RESEARCH / EXPLORATION / REPRODUCTION, actual task proof_audit.
No substantive error, stronger bound or existence conclusion was found.
The audit checks this specialization with its stated inputs, rather
than reauditing the entire upstream conditional construction.

The fixed coefficient is locally free on the product with the proper
smooth surface Y. Thus 0B91 applies, and each derived fibre has no
cohomology outside [0,2]. Minimal representatives and spreading give a
finite free representative ending in degree two near each point of T.
For such a representative P, the equality

    H^2(P tensor_R R/J)=coker(d^1 tensor_R R/J)
                       =H^2(P) tensor_R R/J

is right exactness of tensor, without any Tor vanishing assumption.
The same applies to residue fields. The endpoint fibre dimensions
come from stable Hom and Serre duality for the actual charge-21
fibres, with index 8-4(21)=-76. The generic complement of the
coincidence support is nonempty, since that support consists of the
dimension-two diagonal and finitely many points in dimension four.
Flatness of the product and local freeness make multiplication by
every nonzero base function injective on the coefficient. Left
exactness of pushforward therefore proves the torsion-freeness used
to conclude H^0(K)=0. Nonzero derived Hom on the diagonal is consistent
with this ordinary-sheaf vanishing.

On the diagonal, trace has the global right inverse a |-> (a/2)id_G.
Stability makes both trace-free endpoint groups vanish at every
fibre. Perfect base change and the same minimal-complex argument
therefore put the trace-free summand in degree one. The scalar
summand has top image H^2(Y,O_Y) tensor O_B, with the natural trace
identification. This proves (2) for the actual family, globally.
At a diagonal closed point, R/(I+J) is consequently a free rank-one
R/J-module. Its annihilator over R/J is (I+J)/J, whereas that of
R/J is zero. Hence I subset J; this is stronger than merely saying
that the radical support is the diagonal.

The smooth diagonal is a regular immersion by
[Stacks Lemma 37.62.18, 0FDP](https://stacks.math.columbia.edu/tag/0FDP),
and its conormal sheaf is Omega_B by
[Lemma 29.33.7, 08S2](https://stacks.math.columbia.edu/tag/08S2).
Here B is a smooth complex surface. Locally, generators x_1,x_2
of J extend to a regular system of parameters of R. Thus
J/mJ -> m/m^2 is injective, with image the annihilator of the
diagonal tangent space. In particular linear independence in that
image really detects generation of J/mJ, not just of its radical.

L135's actual two-family comparison still applies at equal central
parameters: its affine Cech terms remain R-flat, the bounded free
comparison has a tensor-acyclic flat cone, and its epsilon diagram
commutes for every tangent map R -> C[epsilon]/(epsilon^2).
Neither this construction nor exact GAGA uses b unequal to c.
With the central isomorphism chosen to be id, the reverse
degree-zero connecting map is kappa(u)-kappa(v). Directly on a
degree-one forward form beta the differential is a_v beta+beta a_u.
Graded cyclicity gives

    Tr(beta a_u)=-Tr(a_u beta),
    P(id,ell(u,v)beta)=-Q(kappa(u)-kappa(v),beta).

The degree-two form sigma_Y causes no odd sign. Serre duality makes
Q perfect and P(id,-) nonzero. L118 supplies the natural injective
KS map at this very point, so the kernel is exactly {(u,u)} and
the last-row linear span has dimension two. Two row entries in
I subset J therefore have expressions a_i1 x_1+a_i2 x_2 whose
coefficient matrix has invertible residue determinant. Its determinant
is a unit in R; its inverse expresses x_1,x_2 in I. This proves
I=J for the entire stalk, not just a first-order approximation.

Remove the finitely many off-diagonal support points when treating
the diagonal. The coherent image of J tensor W -> W vanishes at
every closed point there, hence everywhere there by finite type.
The diagonal sheaf is consequently its own pushforward of i^*W.
The global trace identification already constructed determines its
line as the trivial one, with no transition ambiguity. The remaining
closed support consists of L135's residue-field stalks; disjoint
closed support gives the direct decomposition. These arguments
retain the case of no off-diagonal points.

For an independent index check, rank truncation with c_1=0 gives
ch_4=ch_2^2/12. L071's full mixed square gives
2(14)(21)+156=744, hence coefficient 62. Dualization has signs
(-1)^j on ch_j; only j=0,2,4 occur, so (4) is unchanged on the
dual. Parameter integration explicitly gives
2(2)-14=-10 and -21(2)+62=20 as the coefficients in (5).
The cross product t_1t_2 has parameter degrees (2,2); all available
parameter Todd terms have degrees zero or four, so none completes
it to (4,4). The same degree check removes each single mixed term
and its products with pure classes on the other parameter. This
does not discard the square contribution already in 62.

The two parameter integrations followed by the fibre Todd class
give 2(100)+2(-10)(20)=-200. Direct expansion gives the independent
top coefficient

    32-336-224+1672+392-1736=-200.

These are respectively the constant, fibre-point, two parameter-point,
two fibre/parameter, parameter-product and sixfold terms after all
Todd factors. Rerunning the existing checker passes all seven
assertions. The complete /coefficient_character and /absolute_integrand
values of its certificate were inspected with the JSON inspector;
the last displayed sum agrees with them. This checks arithmetic
only, not the sheaf or KS arguments.

Finally, bounded coherent hypercohomology gives an alternating Euler
identity regardless of differentials. The diagonal term contributes
2, the N ordered off-diagonal residue fields contribute N, and the
ordinary middle term has sign minus. Thus (1) has its stated sign
and constant. Relative duality has shift +2:
K^vee=K_rev[2], since the relative dualizing complex is O[2] after
fixing sigma_Y. Absolute duality on T then contributes the separate
even dimension-four shift and no new Euler inequality. It is not
ordinary duality of M, nor a vanishing of its higher cohomology.
The sole upper-count threshold is still chi(M)<=C+202 for N<=C.
None of the tested inputs establishes it. ATTEMPTS/078 therefore
remains the correct stopping decision, with ATTEMPTS/046 and 073
preserved. This audit creates no new dependency, main argument,
count estimate, F, cycle or transverse transport.

## Mathlib

Full matching Mathlib coverage for this actual-family diagonal
specialization and Euler-count limit is **not checked**. The Stacks,
Huybrechts–Lehn, Serre-duality and HRR references above are the named
mathematical inputs. Unknown library coverage is not evidence of absence.
