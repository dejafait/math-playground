# Rank-zero Beilinson--Kato input

Checked 2026-09-26, reusing the prior SPECIALIZE assessment. For an
elliptic curve B/Q, use the period-normalized Beilinson--Kato element
z_B in H^1(Q,V_p B) specified in Burungale--Skinner--Tian--Wan,
*Zeta elements for elliptic curves and applications*,
[arXiv:2409.01350v2, Section 1.1.3, printed page 5](https://arxiv.org/pdf/2409.01350v2#page=5).
Their stated consequence of Kato's explicit reciprocity law is

\[
\operatorname{loc}_p z_B\in H^1_f(\mathbf Q_p,V_p B)
\quad\Longleftrightarrow\quad L(B,1)=0.
\]

The construction and cyclotomic family are recalled in
[Section 3.2.1, printed page 26](https://arxiv.org/pdf/2409.01350v2#page=26);
[Theorems 3.13--3.14, printed page 29](https://arxiv.org/pdf/2409.01350v2#page=29)
give interpolation and the Coleman reciprocity law. These are imported
inputs. The underlying reference is Kato, *Asterisque* 295 (2004),
Theorem 12.5; its full proof has not been independently read here.

For the application set B = E^K. The retained hypotheses give
L(B,1) != 0, good ordinary reduction at p, and split p in K.
Fix a twist identification V_p B = V_p E tensor chi_K and its
restriction over K. No numerical normalization of a dual exponential
is needed: L012 normalizes by the actual local Tate pairing.
The cited reciprocity theorem supplies no anticyclotomic lift.

## Mathlib

Full coverage of the reciprocity statement: **not checked**.
Supporting coverage for restriction, quadratic twisting, and local
Tate duality: **not checked**. The linked statements are arithmetic
sources, not Mathlib matches.
