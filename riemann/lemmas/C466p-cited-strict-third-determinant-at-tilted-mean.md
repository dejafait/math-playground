# Corollary 466p: cited strict third determinant at the tilted mean

## Hypotheses

Use C466a's completion, \(c_0=\xi(1/2)>0\),
\(h(z)=\xi(1/2+\sqrt z)/c_0\), \(B(s)=\log h(s)\), and
\(p=\theta_1=c_0\Theta\). Retain its imported smooth probability
density on \((0,\infty)\), transform \(1/h\), and external
strip, symmetry, paired-product, counting and height-100 qualifications.
Use C466k's positive tilted mean \(x=B'(1)>0\) and C466l's
signed determinant convention.

Import the stated theorem of Suvrit Sra, *On some positivity properties
of the Riemann Xi function*, [arXiv:2611.02944v1, 2 November 2026](https://arxiv.org/pdf/2611.02944v1),
Appendix C.16 (definition), C.18 Lemma C.26 and proof, printed pp45-49.
Its additional trust base includes verified zeros through
\(U=3\cdot10^{12}\), positive anchored-residual extraction (C.14-C.15),
first-64-zero/count/derivative enclosures, and C.18's outward
quadrature, residue, pivot and covering certificates. These are
external theorem inputs; no independent certificate replay or audit
of the source proof is asserted. This is a separate import from
C466a's older Hub-v1 density assertion, without identifying their
theorem numbers or extending the latter's audit to arXiv-v1.

## Conclusion

With exactly the signed, algebraic determinant of C466l,
\[
 \mathcal D_3(p;B'(1))
 =-\det[p^{(i+j)}(B'(1))]_{i,j=0}^2>0.
\]
Also \(\mathcal D_3(\Theta;B'(1))=c_0^{-3}
\mathcal D_3(p;B'(1))>0\). These conclusions are relative to the
cited theorem and retained inputs, not independent numerical enclosures.

## Proof

Lemma C.26 states \(\mathcal D_k(\Theta;y)>0\) for
\(y>0\), \(1\le k\le4\). C.16 uses
\((-1)^{k(k-1)/2}\det[\Theta^{(i+j)}(y)]\), so at \(k=3\)
its sign is minus, precisely as in C466l. We use only \(k=3\).

The source's (1.1)-(1.2) use the same \(\xi,c_0,h,B\).
Its C.18 proof sets \(p=c_0\Theta=\theta_1\).
For completeness, the identification across versions requires no
agreement of their constructions: both normalized smooth densities
are probability measures with Laplace transform \(1/h(s)\) for
every real \(s>0\). The standard uniqueness theorem for Laplace
transforms of finite measures on \([0,\infty)\) makes the measures
equal. Continuity then makes the densities equal at every positive
point, and their smoothness identifies all derivatives there.

C466k's tilted probability density \(q(u)=h(1)e^{-u}p(u)\)
has mean \(B'(1)\). Its finite, strictly positive mean places
the evaluation point inside the theorem's open domain. Neither
a numerical value of this mean nor an effective boundary onset
is necessary for this application.

Since \(c_0\) is constant,
\(p^{(r)}=c_0\Theta^{(r)}\) for every \(r\). Factoring \(c_0\)
from each of the three rows gives
\[
 -\det[p^{(i+j)}(x)]_{i,j=0}^2
 =c_0^3\left(-\det[\Theta^{(i+j)}(x)]_{i,j=0}^2\right)>0.
\]
This proves the claim by the cited theorem, with no reproof of its
sign calculation. In particular, no weak-PF confluence argument or
conjugate Gram matrix has been used.

C466l identifies this determinant with its full weighted signed
integral. Its positivity imposes no pointwise sign on that integrand;
C466o's negative patches and the recorded pointwise stop are retained.
The citation supplies no independently replayed margin here, and this
application proves no unbounded-order statement, density-to-Xi
transfer, L030-L032/C032a positivity, or RH. The source certificates
remain in the trust base even though the application needs only
the positive argument rather than a particular certificate box. ∎

## Mathlib

Full matching coverage has not been checked. No declaration for this
actual-density sign or independent formal certificate is asserted.
Laplace uniqueness and determinant homogeneity are supporting standard
mathematics; unknown formal coverage is not evidence of absence.
