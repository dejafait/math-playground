# L017 — Degree-27 full orbit exceeds the auxiliary coarse enclosure

## Hypotheses

Let K = Q_3(pi), pi^27 = 3, v(3) = 1, O = O_K, J = log(O^times), I = J/6, and G the Q_3-linear extensions of all Aut_Z_3(I). Write GY for the union of g(Y) over g in G, and hull(Y) for the smallest closed field disc centered at zero containing Y. Retain the one-factor packet, beta = 1 and strict nonunit scalar a = pi. No O-module invariance of J is assumed.

Use L015's bound J subset pi^(-54)O and L016's complete lattice J = H + sum_(j=1)^13 Z_3 q_j, H = pi^14 O. In particular q = q_1 is an actual unit logarithm, not merely an approximation. Its power-basis coefficient at 0 is 16/9 and at 26 is zero, and v(q) = -2. L016 supplies the functional

\[
\phi(y)=3c_0-\frac{31}{3}c_1+9c_{15}-9c_{18},
\qquad y=\sum_{r=0}^{26}c_r\pi^r,
\]

with phi(J) subset Z_3, phi(q) = 0, phi(18pi q) = -992/3, and log(1+pi)-q in H. All analytic and complete-unit-filtration qualifications of those inputs remain in force.

For primitive-line basis extension import **Bürgisser–Kulkarni–Lerario, Nonarchimedean integral geometry, Selecta Mathematica 32, article 10 (2026), Lemma 3.1.5**, with lattice scalar ring R = Z_3 and V the underlying 27-dimensional Q_3-space of K ([published source](https://doi.org/10.1007/s00029-025-01120-y)). Its supporting Smith-normal-form discussion is §2.2; Proposition 2.1.1 concerns the coordinate norm, not the field norm. We give the needed orbit specialization below. No new general transitivity theorem or logarithm theorem is being reproved.

The auxiliary group and radius prescription are **Dupuy–Hilado, arXiv:2004.13108v2 (April 29, 2020), §6.2, printed pp. 19–20**, especially Aut(L:I) and the unnumbered coarse enclosure following (6.8) ([primary PDF](https://arxiv.org/pdf/2004.13108v2#page=19)). L015 specializes that prescription to radius 3e = 81 here. This lemma tests that toy prescription with its full stated lattice group. It does not assume an original IUT initial-data realization or identification with the original indeterminacies.

## Conclusion

The exact branch orbits and their union are

\[
G(\pi O)=I,\qquad G(\pi J)=I/9,\qquad
G(\pi(O\cup J))=I/9.
\]

Their minimum lattice contents relative to I are respectively 0 and -2. The union has

\[
\operatorname{hull}(G(\pi(O\cup J)))=\pi^{-135}O,
\qquad \min v=-5,\qquad R=3^5=243>81.
\]

An explicit I-preserving involution sends the literal input pi q to q/54 and sends pi log(1+pi) to an element of the same sharp valuation -5. Thus the auxiliary coarse enclosure fails in this fixed packet, by a factor of three. This is not a demonstrated essential IUT flaw.

## Proof

### Exact contents of both literal branches

For any nonzero y, define its I-content as the minimum 3-adic valuation of its coordinates in a Z_3-basis of I. Equivalently it is the unique integer k for which y belongs to 3^k I but not 3^(k+1)I. This characterization makes it independent of the basis.

Since v(6pi O) >= 28/27 > 14/27, we have 6pi O subset H subset J, hence pi O subset I. But pi is not in 3I = J/2: phi(2pi) = -62/3 is nonintegral. Thus pi has content 0 and the ideal branch has minimum content 0.

For y in J, L015 gives v(y) >= -2. Consequently v(54pi y) >= 3 + 1/27 - 2 = 28/27 > 14/27. This proves 54pi J subset H subset J, or pi J subset I/9. On the other hand pi q does not belong to I/3 = J/18, because phi(18pi q) = -992/3 has valuation -1. The integral-valued content of pi q is therefore exactly -2. This proves the logarithm branch's exact minimum content, rather than inferring it from failure of a sufficient membership premise.

### Whole-group saturation

If w is primitive in I, the rank-one intersection Q_3 w intersect I is Z_3 w: a scalar times w is integral exactly when that scalar is in Z_3, as seen in a unit coordinate. The cited Lemma 3.1.5 extends w to an I-basis. Extending two primitive vectors and mapping one resulting basis to the other shows that G is transitive on primitive vectors of I. This is the precise finite-lattice specialization needed here.

Let M be either literal branch, a Z_3-module. Suppose M subset 3^k I and it contains x of exact content k. Then w = 3^(-k)x is primitive in I. For any nonzero y in 3^k I, write 3^(-k)y = 3^m t with m >= 0 and t primitive. Choose g with g(w) = t. The element 3^m x is in M and g(3^m x) = y. Zero is also in M. Conversely every g preserves 3^k I. Thus GM = 3^k I. Apply this with k = 0 to pi O and k = -2 to pi J. Taking the union proves the asserted complete orbit equality. This uses every automorphism and the Z_3-stability of the actual input; a sampled transformation alone would not prove it.

### Field radius and an explicit attaining involution

L015 gives v(I) >= -3. L016's q has v(q) = -2 (the constant term 16/9 attains it; every other term has larger valuation). Hence z = q/6 in I attains v(z) = -3. Therefore I/9 has minimum valuation -5 and hull pi^(-135)O, giving radius 243. The field valuation is distinct from the coordinate content used above.

Here is a compact direct witness independent of basis transitivity. Put

\[
w=9\pi q,\qquad z=q/6,\qquad
A(y)=\frac{27}{8}c_0,\qquad B(y)=-\frac{3}{496}\phi(y).
\]

We already proved w in I. The functional A is integral on I: for y=j/6 with j in J, A(y) = (9/16)c_0(j), integral because J subset pi^(-54)O implies v_3(c_0(j)) >= -2. The functional B is also integral on I: B(j/6) = -phi(j)/992, and 992 is a 3-adic unit. The zero constant coordinate of pi q and L016's functional values give

\[
A(z)=1,\quad A(w)=0,\quad B(z)=0,\quad B(w)=1.
\]

Define

\[
g(y)=y+(A(y)-B(y))(w-z).
\]

It maps I into I by integrality. Since (A-B)(w-z) = -2, direct composition yields g^2 = id; consequently g(I)=I and g belongs to G. The four displayed values give g(w)=z, so

\[
g(\pi q)=z/9=q/54,\qquad v(q/54)=-2-3=-5.
\]

This point is outside the prescribed radius-81 disc, which has minimum valuation -4. Its input pi q belongs to the literal logarithm branch because L016 proves q in J using the complete H-valued error, not by finite-series identification.

For the original infinite logarithm write log(1+pi)=q+h, h in H. If h = sum c_r pi^r, then c_0 in 3Z_3 and c_14,c_17,c_26 in Z_3. We have A(pi h) = (81/8)c_26 in 3^4 Z_3 and

\[
\phi(\pi h)=9c_{26}-\frac{31}{3}c_0+9c_{14}-9c_{17}\in\mathbb Z_3.
\]

Thus B(pi h) is in 3Z_3, and (A-B)(pi h) is in 3Z_3. Since v(w) = 1/27, v(z) = -3 and v(pi h) >= 15/27, the formula for g gives v(g(pi h)) >= -2. Consequently g(pi log(1+pi)) = q/54 + g(pi h) has valuation exactly -5: the error cannot cancel the lower-valuation term. Both the finite exact logarithm representative and the actual infinite-log input attain the radius.

### Certificate, source comparison and limitations

Run `PYTHONDONTWRITEBYTECODE=1 python3 scripts/coarse-ideal/check_degree_27_orbit.py`. The full certificate is `scripts/coarse-ideal/degree-27-orbit.json`. It replays every elementary operation in L016's stored diagonalization, checks integral subtraction coefficients and the exact transformed generator identity, verifies the full basis and its dual, and evaluates every generator of both branches. It records contents 0 for the first thirteen power-basis ideal inputs and 1 for the remaining fourteen; for pi q_1,...,pi q_13 it records (-2,-1,-1,-1,0,0,0,0,0,0,0,0,0), with every deep-ideal generator also checked. It verifies a basis-coordinate automorphism and its inverse, and independently checks the compact involution above, its integral I-matrix, g^2=id, and every deep-tail image generator. There are zero finite verification failures. The analytic completeness and whole-group equality are proved using L016 and the preceding argument, not inferred from this certificate or a preview.

The relevant comparison is the separate coarse prescription after (6.8), whose singleton radius is 81 at e=27 and floor(v(a))=0. It is not the rounded intermediate enclosure or the literal (6.8) endpoint. The discrepancy is produced from the original smaller union pi(O union J), beta=1, at a strict nonunit scalar and odd residue characteristic. No O-unit stability or enlarged-input premise is used.

This local negative result strengthens L016's membership obstruction to an actual whole-orbit coarse-bound violation. It does not contradict the differently stated native IUT IV tensor enclosures. Original initial theta data, pilot transport, identification of the full permitted image group, essentiality and normalized finite B >= A remain unresolved. Classification **POTENTIALLY_NEW** means only that the reused bounded source search found no matching field-specific result; no certified originality or original-IUT counterexample is claimed.

### Critical audit, 2026-10-05

The fixed-packet conclusion survives the approved audit. This verifies the existing result, without adding a theorem or establishing originality. The following checks address the load-bearing obligations rather than relying on a stored success flag.

**Complete analytic input.** In L016 the unit filtration removes one residue class at each of levels 1 through 13; its representatives need not be independent. The final unit lies in U_14, whose logarithm is H by the cited strict inequality 14/27 > 1/2. Compactness makes the logarithm image closed, so the passage from integer powers to Z_3 multiples is valid. For every omitted k >= 243, the block bound k-27v_3(k) >= 3^h-27h >= 108 tends to infinity and is at least 14. It therefore controls the full infinite tail, uniformly for all thirteen logarithms. These arguments establish both directions of the displayed equality for J, including that q is an actual logarithm. No precision-based identification is used.

**Finite data and certificates.** The three existing bounds, membership and orbit scripts were read and rerun successfully. A separately implemented audit, `PYTHONDONTWRITEBYTECODE=1 python3 scripts/coarse-ideal/audit_degree_27.py`, parses all thirteen representatives directly from L016's printed table and recomputes all 351 rational congruences. It imports neither earlier checker nor stored diagonalization. It checks the outer bound and separator on all forty generators, both branch upper inclusions, splitting values, functional integrality on I, the involution on every power-basis vector, its exact image q/54, and every one of the twenty-seven deep-tail images. Complete rational discrepancies and witness/tail vectors are in `scripts/coarse-ideal/degree-27-audit.json`; there are zero failed checks. Rerunning the original orbit script also replays all integral elementary operations and verifies both inverse matrices. Thus agreement does not depend solely on reusing a precomputed basis or on an abbreviated certificate preview.

**Whole orbit and field extreme.** The upper branch inclusions are genuine inclusions in I and I/9. The two nonintegral separator evaluations exclude precisely the next smaller rationally scaled lattices, giving contents 0 and -2. The cited primitive-basis extension applies over Z_3, not O. Z_3-stability of each input branch supplies every nonnegative power of 3 required in the saturation argument; zero is included. This verifies equality for the entire group, rather than only for the exhibited involution. The valuation of q is exactly -2 because its constant coefficient is 16/9 and all other fractional valuation classes are larger. The image q/54 has valuation -5, whereas all deep-tail images have valuation at least -2. The infinite-log witness therefore also attains -5, with no possible cancellation. The field hull follows from this attained extreme and the upper bound, not from lattice content alone.

**Exact source scope.** Rechecked [Dupuy–Hilado v2, §6.2, printed pp. 19–20](https://arxiv.org/pdf/2004.13108v2#page=19). Its toy hypotheses allow m=1, K_1=K and a=pi. The tensor order is O, so beta=1 meets its containment and valuation requirements. The singleton different norms cancel, floor(v(a))=0 and |6|_3=1/3: the separate post-(6.8) prescription is 27/(1/3)=81. Its group is the full extended lattice group used here. The n=1 part of the union in (6.3) already contains this witness. This refutes the resulting radius prescription for that auxiliary literal union; identifying it with the source's ind3-defined U still requires the appropriate input bridge. The nearby (6.2) and (6.8) constants are distinct. Footnote 7 and §6.3 do not establish the original permitted-group, tensor-packet or initial-data realization needed here. No native IUT theorem or original B >= A is refuted by this audit.

All direct mathematical inputs remain L015 and L016 plus the explicit standard citations already stated. There is no new DAG edge. The auxiliary objection is retained for a separately assessed applicability question; the original challenge stays unresolved.

## Mathlib

Full degree-27 exact orbit, logarithm lattice and auxiliary coarse-bound counterexample: **not checked**. Supporting valuation, log/exp, finite-lattice, primitive-basis-extension and rank-one automorphism coverage: **not checked**. The named published lemma supplies supporting lattice mathematics, not a matching full result or a Mathlib certificate. Unknown coverage is not absence.
