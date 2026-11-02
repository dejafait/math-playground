# Corollary 645d: two unit residues can cancel exactly after inverse-Blaschke weighting

## Hypotheses

Retain only the scalar geometry and the complex scaled Blaschke factors
underlying L645 (6). Explicitly, fix

\[
 0<\delta<\tfrac12,\qquad a=\tfrac32,\qquad
 d=a-\delta,\qquad R=a-\tfrac\delta2,\qquad x=-d.
\]

For every integer \(n\ge5\), let \(t_j=j/n\), \(0\le j<n\), and
use the complex rational product

\[
 B_n(z)=\prod_{j=0}^{n-1}\frac{R(z-it_j)}{R^2+it_jz}.
 \tag{1}
\]

This is not a product of moduli. Its sign convention is exactly
\(R^2-\overline{it_j}z=R^2+it_jz\). A permitted synthetic cluster
contains \(x\) and at most two additional distinct points \(z_k\),
each satisfying

\[
 |z_k+d|<\delta/8,\qquad -\tfrac32<\Re z_k<-1,
 \qquad |z_k|<R.
 \tag{2}
\]

Every point has assigned residue one and is distinct from every grid
node. Define

\[
 S_n=B_n(x)\sum_{z_k\text{ in the cluster}}\frac1{B_n(z_k)}.
 \tag{3}
\]

There is no stipulated Xi zero, positive-real interpolant, actual PSD,
zero-separation assumption or derivative lower bound in this statement.
The cluster may depend on \(n\). All thresholds below fix \(\delta\).

## Conclusion

There is an explicitly defined admissible **two-point** cluster for
every integer \(n\ge N_\delta\) such that

\[
                         S_n=0.                         \tag{4}
\]

Here one valid threshold uses the positive constants

\[
 r=\min\{\delta/16,(d-1)/2\},\qquad
 c=\frac{d(R^4-1)}{(d^2+1)(R^4+d^2)},\qquad
 K=\frac1{(d-r)^2}+\frac1{(R^2-r)^2},
\]
\[
 N_\delta=\left\lceil\max\left\{5,\frac{2\pi}{cr},
                                      \frac{4\pi K}{c^2}\right\}\right\rceil.
 \tag{5}
\]

The second point is \(x+h_n\), where \(h_n\ne0\) is the limit of
the completely specified contraction iteration (12) below, and

\[
 |h_n|\le\frac{2\pi}{nc}\le r<\delta/8,
 \qquad R-|x+h_n|\ge7\delta/16.
 \tag{6}
\]

Consequently no positive \(c_\delta\) can lower-bound \(|S_n|\)
uniformly over the assessed clusters for all sufficiently large \(n\).
The loss is exact cancellation, not a polynomial or floating-point loss.
The construction covers unbounded logarithmic grid sizes: for example
\(\gamma_n=e^n\) has \(\lfloor\log\gamma_n\rfloor=n\).
These heights and poles are synthetic, not asserted zeta data.

This is a local obstruction to the proposed universal noncancellation
shortcut. It is not a disproof of RH, a failure theorem for every
contour detector, or a theorem about actual-Xi signs. A separate
conceptual audit on 1 November 2026 verified this construction under
exactly the stated hypotheses, without a mathematical correction;
the checks and limits are recorded below.

## Proof

### Standard input and the exact scope of the calculation

Use the **Banach contraction mapping theorem**, J. Lebl, *Basic Analysis*,
Volume I, Section 7.6.1, Definition 7.6.1 and
[Theorem 7.6.2 with proof](https://www.jirka.org/ra/html/sec_metpicard.html)
(unversioned author text, inspected in the source review on 1 November
2026), in its complete metric space form: a self-map with Lipschitz
constant strictly below one on a
nonempty complete metric space has a unique fixed point, obtained by
iteration from any starting point. This standard named theorem is
imported, not reproved. Below the space is a closed disk in \(\mathbb C\)
with the usual distance; all map and contraction bounds are explicit.

The local logarithm used below is the ordinary convergent power series
\(\ell(u)=\sum_{m\ge1}(-1)^{m+1}u^m/m\), \(|u|<1\), so
\(\ell(0)=0\), \(\ell'(u)=1/(1+u)\) and
\(\exp\ell(u)=1+u\). Import the series identity from
[NIST DLMF (4.6.1)](https://dlmf.nist.gov/4.6.E1), version 1.2.8
(15 September 2026), and the inverse-exponential identity and derivative
from Beck et al., *A First Course in Complex Analysis*,
[Section 5.2](https://complexanalysis.org/web/sec_complex-log.html),
Definition 5.2.2, (5.2.6) and the derivative argument. These were
inspected in the prior source review. Only \(|u|<1\) is used, so
\(1+u\) is in the right half-plane, within the principal branch's
domain. No boundary-series statement or unrestricted logarithm
additivity is needed. No global logarithm of \(B_n\) is chosen.
L645's finite-Blaschke convention is sourced there to S. Zakeri,
*A Course in Complex Analysis*,
[Notes and Comments, Section 8.3](https://zakerimath.com/CAbook/COM.html),
finite-division paragraph following Example 8.33. The division bound
itself is not reapplied here: this calculation concerns the exact
rational product. It supplies the finite-family difference left open
by the prior EXPLORE assessment; no known interpolation theorem is
reproved and no novelty beyond the inspected sources is asserted.

### 1. A local disk with all geometric and denominator margins

The parameter ranges give \(1<d<3/2\), \(5/4<R<3/2\),
\(R-d=\delta/2\), and \(0<r\le\delta/16<1/32\).
For every \(|h|\le r\),

\[
 \Re(x+h)\ge-d-r\ge-\tfrac32+15\delta/16>-\tfrac32,
\]
\[
 \Re(x+h)\le-d+r\le-(d+1)/2<-1,
 \qquad |x+h|\le d+r\le R-7\delta/16<R.
 \tag{7}
\]

Thus this entire closed disk meets the strict conditions (2) and
contains no grid node. For \(0\le t\le1\) its denominators obey

\[
 |x+h-it|\ge d-r>0,\qquad
 |R^2+it(x+h)|\ge|R^2-idt|-t|h|\ge R^2-r>0.
 \tag{8}
\]

The product is therefore holomorphic and nonzero on a neighborhood
of this closed disk. Globally its denominators are also nonzero on
\(|z|\le R\), since \(|R^2+itz|\ge R^2-R>0\). This checks the
actual complex convention, including \(t=0\).

### 2. The normalized product has a controlled logarithm

For \(|h|\le r\), define

\[
 L_n(h)=\sum_{j=0}^{n-1}\left[
 \ell\left(\frac{h}{x-it_j}\right)
 -\ell\left(\frac{it_jh}{R^2+it_jx}\right)\right].
 \tag{9}
\]

The two arguments have moduli at most \(r/d<1\) and
\(r/R^2<1\), respectively, strictly also on a neighborhood of the
closed disk. Hence (9) is a single holomorphic choice with \(L_n(0)=0\)
and the exact identity

\[
 e^{L_n(h)}=\frac{B_n(x+h)}{B_n(x)}.
\]

Set

\[
 A_n=\frac{L_n'(0)}n
 =\frac1n\sum_{j=0}^{n-1}
       \left(\frac1{x-it_j}-\frac{it_j}{R^2+it_jx}\right).
\]

For every real \(0\le t\le1\), direct rationalization gives

\[
 -\Re\left(\frac1{-d-it}-\frac{it}{R^2-idt}\right)
 =\frac{d(R^4-t^4)}{(d^2+t^2)(R^4+d^2t^2)}\ge c>0.
 \tag{10}
\]

The inequality follows by lowering the numerator to \(d(R^4-1)\)
and raising both positive denominator factors to their values at
\(t=1\). Consequently \(-\Re A_n\ge c\) and \(|A_n|\ge c\)
for every \(n\); no limiting Riemann sum or nonvanishing assumption
is required.

For \(|h|\le r\), differentiating (9) twice and using (8) yields

\[
 L_n''(h)=\sum_j\left[-\frac1{(x+h-it_j)^2}
                  -\frac{t_j^2}{(R^2+it_j(x+h))^2}\right],
 \qquad |L_n''(h)|\le nK.
\]

Let \(E_n(h)=L_n(h)-nA_nh\). Integration along the line segment
from zero to \(h\), contained in the disk, gives

\[
 |E_n'(h)|\le nK|h|,\qquad |E_n(h)|\le\tfrac12nK|h|^2.
 \tag{11}
\]

These are finite-product analytic estimates; their constants are
independent of \(n\) at the fixed \(\delta\).

### 3. Exact phase reversal by a specified contraction

Fix an integer \(n\ge N_\delta\), and put \(b_n=2\pi/(nc)\).
Then \(b_n\le r\) and \(Kb_n/c\le1/2\) by (5).
On the closed disk \(|h|\le b_n\), define

\[
 T_n(h)=\frac{i\pi-E_n(h)}{nA_n},\qquad
 h_n^{(0)}=0,\qquad h_n^{(m+1)}=T_n(h_n^{(m)}).
 \tag{12}
\]

Equation (11) gives

\[
 |T_n(h)|\le\frac\pi{nc}+\frac{K b_n^2}{2c}
       \le\frac{b_n}2+\frac{b_n}4=\frac{3b_n}4,
 \qquad |T_n'(h)|\le\frac{K b_n}{c}\le\frac12.
 \tag{13}
\]

The derivative bound integrated along the segment between two points
of this convex disk makes \(T_n\) Lipschitz with constant at most
\(1/2\). It is a self-map by the first bound. The disk is nonempty
and complete, so the named contraction theorem gives an exact limit
\(h_n=\lim_m h_n^{(m)}\), the unique fixed point there. Its defining
equation is

\[
               nA_nh_n+E_n(h_n)=L_n(h_n)=i\pi.
 \tag{14}
\]

In particular \(h_n\ne0\), since \(L_n(0)=0\). The iteration
is an explicit convergent definition of the family, not a numerical
root selection. Its usual contraction error bound is

\[
 |h_n-h_n^{(m)}|\le 2^{1-m}|h_n^{(1)}-h_n^{(0)}|
                 \le\frac{2^{1-m}\pi}{nc}.
\]

For an additional displacement check, (11) also gives

\[
 \left|h_n-\frac{i\pi}{nA_n}\right|
 \le\frac{K b_n^2}{2c}=\frac{2\pi^2K}{n^2c^3}.
 \tag{15}
\]

The bounds (6) follow from \(|h_n|\le b_n\le r\) and (7).
No root may escape the permitted neighborhood in this argument.

### 4. The unit-residue sum and the scope of the stop

Use the two distinct points \(x\) and \(x+h_n\), each with residue
one. Every strict admissibility condition, nonzero denominator and
nonzero value of \(B_n\) was checked above. Equations (9) and (14)
give exactly

\[
 B_n(x+h_n)=e^{i\pi}B_n(x)=-B_n(x),\qquad
 S_n=1+\frac{B_n(x)}{B_n(x+h_n)}=0.
\]

If a uniform positive lower bound existed beyond any onset, choose
an integer \(n\) beyond both that onset and \(N_\delta\). This
cluster would contradict it. The construction uses two of the allowed
three poles and stays a fixed positive distance from the disk boundary
for fixed \(\delta\), so boundary proximity is not the cause.

The two assigned residues are realizable in the elementary meromorphic
function \(1/(z-x)+1/(z-x-h_n)\), which has exactly those two simple
poles. This observation does not supply grid interpolation, a
positive-real interpolant, Xi symmetries or actual zero realization.
No full contour integral is identified with (3): dividing an arbitrary
meromorphic function by \(B_n\) can also introduce singularities at
grid nodes unless they are removed. Every singularity and boundary
hypothesis would need checking in an actual contour application.

Thus the precise failed claim is that positivity of these residues and
the assessed geometry alone prevent complex inverse-factor cancellation.
The result does not preclude an argument using additional actual-Xi
structure, an isolated pole, another weight or other contour data. The
normalization stops in C645a/C645b and the qualified rate improvement in
C645c are comparisons only; none is used to prove (4).

### Independent conceptual audit — 1 November 2026

The entire proof was checked against the unchanged fixed-\(\delta\)
statement and L645's factors/grid. The following checks make the
branch, sign and endpoint issues explicit; they do not strengthen the
claim or reprove the imported contraction theorem.

1. **Exact normalized product.** For each \(t=t_j\), the ratio of
   its factor at \(x+h\) to the factor at \(x\) is
   \[
    \frac{1+h/(x-it)}{1+ith/(R^2+itx)}.
   \]
   Both logarithm arguments in (9) stay strictly inside the unit disk,
   even when \(|h|=r\). Exponentiating each local logarithm and then
   multiplying these ratios gives the displayed identity after (9)
   exactly. There is no assertion that a sum equals a globally chosen
   principal logarithm. Negative real \(x\), the node \(t=0\), and
   the eventual value \(L_n(h_n)=i\pi\) create no branch crossing in
   these local arguments.
2. **Derivative sign and remainder.** Directly,
   \[
   -\Re\left(\frac1{-d-it}-\frac{it}{R^2-idt}\right)
    =\frac d{d^2+t^2}-\frac{dt^2}{R^4+d^2t^2}.
   \]
   Bringing these terms to a common denominator yields exactly (10).
   Since \(R>5/4>1\), the numerator's lower bound and the two
   denominator upper bounds are positive; hence \(c>0\) and
   \(|A_n|\ge c\) for each finite \(n\). Differentiating the second
   term of \(L_n'\) gives \((it)^2/(R^2+it(x+h))^2\), confirming
   the negative sign of the second term of \(L_n''\). Bounds (8)
   give \(nK\). The exact segment identities
   \[
    E_n'(h)=h\int_0^1L_n''(uh)\,du,\qquad
    E_n(h)=h^2\int_0^1(1-u)L_n''(uh)\,du
   \]
   verify both constants in (11), including complex \(h\).
3. **All integers beyond the threshold, including equality.** For
   every integer \(n\ge N_\delta\), (5) gives \(b_n\le r\) and
   \(Kb_n/c\le1/2\). Equality here is harmless: (13) still maps
   the closed disk into the concentric disk of radius \(3b_n/4\),
   and the Lipschitz constant is at most \(1/2<1\). Convexity
   justifies integrating the complex derivative between any two
   points. The denominator \(nA_n\) is nonzero and the closed disk
   is nonempty and complete. All hypotheses of Lebl's theorem hold.
   Its error estimate gives, for every integer \(m\ge0\),
   \(2^{1-m}|h_n^{(1)}-h_n^{(0)}|\), precisely the stated bound.
   Substitution into (11) gives the constant in (15). Thus (14)
   describes an exact fixed point, not just an asymptotic displacement.
4. **Strict admissibility and exact zero.** Positivity of \(r\)
   holds for every fixed \(0<\delta<1/2\). Even if \(b_n=r\),
   the margins are
   \[
    |h_n|\le\delta/16<\delta/8,\quad
    \Re(x+h_n)\ge-3/2+15\delta/16>-3/2,
   \]
   \[
    \Re(x+h_n)\le-(d+1)/2<-1,\quad
    R-|x+h_n|\ge7\delta/16>0.
   \]
   The anchor also satisfies these conditions. All cluster points
   have negative real part and hence avoid every grid node; (8)
   excludes denominator zeros. Equation (14) excludes \(h_n=0\).
   Thus both values of \(B_n\) are nonzero and their ratio is
   exactly \(-1\), proving \(S_n=0\) with two distinct unit
   residues for every stated \(n\).

**Audit verdict.** The existing synthetic obstruction is sound; no
threshold, sign, hypothesis or dependency correction is required.
This is independent verification of the saved construction, not a new
mathematical discovery. No uniformity as \(\delta\) approaches either
endpoint is claimed. Neither the rational two-pole example nor this
audit supplies actual-Xi realization/symmetries, finite-grid
interpolation by the residual, control of other zeros or multiplicities,
a permissible contour, or a boundary estimate uniform in the
\(n\)-dependent interpolant. In particular (3) has not been promoted
to a contour identity. The geometry/residue-only lower bound remains
stopped; a different weight or additional constraint requires its own
assessment and test.

## Mathlib

Full matching coverage for this finite-grid cancellation statement is
**not checked**; availability is unknown. The Banach contraction theorem
is a standard named mathematical input, but no specific Mathlib theorem
or formalization of the complex-log estimates has been verified here.
L645 retains its separately recorded supporting coverage. This informal
proof and the structural checker are not a Lean verification.
