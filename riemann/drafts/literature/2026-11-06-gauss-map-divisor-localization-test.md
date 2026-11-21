# A determinant perturbation of the fixed torus's Gauss map — proposed test

TARGET: Test whether J_epsilon=J+epsilon*conjugate(F(Phi_u)) near the complex-point set lifts to a homotopy of the fixed torus's oriented Gauss map that localizes both Lai index classes with nonpositive contributions, allowing nonisolated J zeros and leaving u and its prescribed collar unchanged.
CHECKED: 2026-11-06
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse the completed global-index source search and duplicate comparison in 2026-11-06-global-complex-point-index-scope.md; no inspected theorem supplies this determinant prescription, its lift, or the required local signs for the vanishing full form. No novelty inferred; separate next-turn approval is required before mathematical work.
SOURCE_EVIDENCE: Lai Trans. AMS172(1972) Theorems4.8/4.10 pp16-17 and Theorem5.10/pullback proof pp24-25; Forstneric AIF37(1987) Section2 determinant map, Definition2/Lemma8/proof pp11-15 and Theorem9 p16; Forstneric JGA13(2003) formulas(1.1)-(1.2) p79 and unconstrained cancellation proof pp82-83. All inspected in the completed global-index review; precise links below.
COMPARISON: Known Grassmannian classes and determinant winding supply the invariant and isolated-contact tools, not a sign-compatible localization of an arbitrary original complex-point set. An explicit Gauss-map homotopy could preserve the invariant while avoiding any assertion that a perturbed surface satisfies q>=0; the proposed lift and sign checks remain entirely unproved.
GAP: Establish or refute this one scalar perturbation's geometric lift, regularity, orientation-separated contributions and complete treatment of its zeros. No finite zero census, isolated original contacts, positivity-preserving surface perturbation, or nonzero required contribution is assumed.
REASON: A bounded new test at the global contour-assembly gap uses the now-inspected class identity and full form; it does not repeat monomial local existence, fixed-chart annular observables, or fixed-cutoff inversion. This fresh assessment is a nomination for separate approval, not a result.
SCOPE: Actual r=2,k=1 G,R,C,F,Phi_u,J=det(I-iDu) of L847; hypothetical real C2 periodic exchange-equivariant u equal to L849 on a smaller open diagonal collar, q_u=F(Phi_u)J real nonnegative. Every divisor, diagonal and Jacobian zero retained. Only the Gauss map may be homotoped; u and the form remain fixed. No cross-notebook input.

## Exact proposed attempt and source boundary

The main target is still L030-L032/C032a all-degree mixed positivity.
This test seeks a conditional constraint on the actual prescribed
contour class. It can be useful without proving an Xi sign: a sign
localization might exclude compensation in a later global obstruction,
whereas failure would retire this particular index mechanism.

The positive scalar epsilon is one parameter. Test the displayed
prescription in a neighborhood of the original complex-point set,
using explicit coordinates on the oriented Grassmannian and its two
complex-plane loci. Determine whether it can be lifted, with a cutoff
away from the fixed diagonal collar, to an actual continuous homotopy
of Gauss maps with controlled zero loci. Do not presume the scalar
determinant is a free coordinate globally or that its winding has the
same sign in both orientation classes. Check normalization factors
between J and a positively oriented orthonormal tangent frame.
No algebraic consequence or geometric lift of the prescription has
been proved in the source-review turn.

The primary inputs, with their limits, are:

- [Lai, pp16-17 and 24-25](https://scispace.com/pdf/characteristic-classes-of-real-manifolds-immersed-in-complex-2lh0zj0xb1.pdf): universal classes, orientation reversal, and the bundle pullback proof. The smooth embedding conclusion gives two zero totals for a torus. The attempt must justify use for the original C2 Gauss map by an explicit homotopy/class argument, without smoothing its positive surface.
- [Forstneric 1987, Section2 pp11-16](https://www.numdam.org/item/10.5802/aif.1076.pdf): determinant map on oriented planes, winding under frame and coordinate changes, local index oriented by the tangent complex line, and the isolated graph derivative formula. These do not by themselves localize a nonisolated set. Homotopy invariance of singular homology is the standard named input already imported in L847; any proposed homotopy must actually be constructed.
- [Forstneric 2003, pp79,82-83](https://users.fmf.uni-lj.si/forstneric/papers/2003J.Geom.Anal.pdf): comparison formulas and cancellation. No source isotopy is used to preserve our constraints. If further substantial topology is needed instead of the explicit-coordinate test, record that changed scope and return to literature before importing it.

L855 provides an exact finite-n positive germ and J formula, not
arbitrary-germ index signs. It is an important consistency test;
also test orientation reversal and exchange. L849's actual collar
retains L848's analytic/trusted-software qualifications. L853/L854
are not premises. The local collar's zeros must not be discarded
because they are zeros of the density rather than automatically
complex points. No use of simple G zeros or RH is allowed.

## Discriminator and unresolved downstream steps

Continue only with a complete lift and a justified localization,
including the nonisolated case, whose orientation-separated local
terms are nonpositive, or with an informative counterexample or
failure of this exact prescription. Do not report isolated-germ signs
alone as completion. A necessary positive compensating contribution,
an unavoidable failure to lift, or dependence on an unproved
sign-preserving surface perturbation stops this prescription.

Even a successful nonpositive localization would leave open whether
the prescribed collar forces any strictly nonzero contribution;
that must not be inferred from L855's conditional local model or
from a fixed-cutoff crossing. Actual global matching, the complete
contour-existence question and all-degree transfer remain independent
gaps. Save partial reasoning and require a materially changed idea
before repeating a failed test. Full matching Mathlib coverage is
unchecked; no formalization claim is made.
