# L035 — The scalar CM extension has no effective weight-one half twist

## Hypotheses

Let S have the very-general cubic-RM data in the
[family audit](../foundations/05-cubic-rm-family.md). Write
T=T(S), E=Q(zeta_7+zeta_7^(-1)), dim_Q T=18 and dim_E T=6.
The E-action preserves the weight-two Hodge structure on T,
whose Hodge numbers are (1,16,1). The same argument applies
to any marked RM deformation with these data.

Set K=E(i), i^2=-1, and

\[
V=T\otimes_E K.
\]

Give K Hodge type (0,0), equip V with the inherited Hodge
structure, and let K act by multiplication on its own factor.
For any CM type Sigma of K, use van Geemen's positive half-twist
convention. Effective weight one means that the whole underlying
rational vector space has only types (1,0) and (0,1).

## Conclusion

For every CM type Sigma,

\[
\dim_{\mathbb C} V_{\overline\Sigma}^{2,0}=1,
\qquad
\dim_{\mathbb C} V_{\Sigma}^{0,2}=1.                 \tag{1}
\]

Thus none of the eight CM types gives an effective weight-one
half twist of V. In particular, none gives the effective
polarized weight-one structure required for the proposed
abelian realization. The obstruction is already effectivity;
no polarization calculation is needed to reach this conclusion.

The threshold is a zero forbidden top piece, whereas its
dimension is exactly one for every type. This stops the fixed
scalar-extension recipe. It asserts neither a failure of
algebraicity of the cubic RM action nor a classification of
other auxiliary Hodge structures or other CM actions.

## Proof

**Imported criterion.** The saved
[assessment](../drafts/literature/2026-09-27-cubic-rm-auxiliary-cm-half-twist.md)
authorizes this applicability calculation. Use van Geemen,
*Half twists of Hodge structures of CM-type*,
[arXiv:math/0008076v1, sections 1.3--1.4, p. 2, and 2.5, p. 4](https://sites.unimi.it/vangeemen/0008076.pdf#page=2).
These are sections 1.3--1.4, pp. 814--815, and 2.5, p. 817,
in [J. Math. Soc. Japan 53 (2001), 813--833](https://www.jstage.jst.go.jp/article/jmath1948/53/4/53_4_813/_pdf).
With plus denoting the embeddings in Sigma and minus their
conjugates, the proposed shift is

\[
(V_{1/2})^{p,q}
   =V_{\Sigma}^{p+1,q}\oplus
      V_{\overline\Sigma}^{p,q+1}.                    \tag{2}
\]

For an effective structure of weight two it is effective on
all of V exactly when V_overlineSigma^{2,0}=0. Conjugation then
also makes V_Sigma^{0,2}=0. Import this criterion without
reproof; only the embedding support for this V remains to check.

**The distinguished real embedding.** Since T^{2,0} is a line,
E acts on it by an embedding sigma_0:E -> C. Its image is real
because E is totally real. Rationality of the E-action therefore
makes E act on T^{0,2} by the same sigma_0. Put

\[
T_{\sigma}=T\otimes_{E,\sigma}\mathbb C,
\qquad T_{\mathbb C}=\bigoplus_{\sigma:E\hookrightarrow\mathbb R}
                         T_{\sigma}.
\]

Each T_sigma has complex dimension six. The sigma_0 summand
has Hodge numbers (1,4,1); the other two summands have only
type (1,1), of dimension six each. Here T_sigma is an
E-eigenspace after complexification, not a rational subspace.

**Both extensions occur.** The field K is a CM quadratic
extension of E. Above each real sigma there are exactly two
embeddings tau_sigma,+ and tau_sigma,-, taking i to i and -i;
they are complex conjugate. Scalar extension gives

\[
V_{\mathbb C}
  =T_{\mathbb C}\otimes_{E\otimes\mathbb C}
                   (K\otimes\mathbb C)
  \simeq\bigoplus_{\tau:K\hookrightarrow\mathbb C}
                         T_{\tau|_E}.                \tag{3}
\]

This is also an equality of the inherited Hodge decompositions:
the scalar factor has type (0,0). Consequently V^{2,0} has
dimension two, with one line in each of tau_sigma_0,+ and
tau_sigma_0,-, and none at the other four embeddings. Its
conjugate V^{0,2} has the same embedding support, again one
line at each. As a separate dimension check, the E-basis 1,i
identifies the underlying rational Hodge structure V with
T direct sum T, of dimension 36 and Hodge numbers (2,32,2).

**Every CM type fails.** A CM type selects exactly one member
of each of the three conjugate pairs, hence there are 2^3=8
choices. Whichever embedding over sigma_0 it selects, the
other still supports a line of V^{2,0}. The selected embedding
also supports a line of V^{0,2}. This proves (1), independently
of the choices over the other two real embeddings. The cited
criterion now proves the conclusion.

Keeping every summand in the formal shift (2) would give a
one-dimensional piece of type (2,-1) and a one-dimensional
piece of type (-1,2). The effective pieces together have
dimension 34, not the required 36. Deleting the two forbidden
complex lines therefore does not produce a half twist on V.
No rationality or existence claim for a different subspace
is being made. A formal weight-one shift is not the effective
weight-one structure specified in the hypotheses.

This is a REPRODUCTION of the known criterion and elementary
scalar extension, with a new negative consequence for this
notebook's proposed recipe. It is not claimed to go beyond
the checked literature. The general criterion is the cited
input; the calculation (3) and its two top-piece multiplicities
are the necessary specialization.

## Mathlib

Coverage of the full statement and the half-twist criterion:
**not checked**. No library declaration or absence claim is
made. The named van Geemen sections are supporting mathematical
references; they are not cited as a worked instance of this
specific scalar extension or as a Mathlib match.
