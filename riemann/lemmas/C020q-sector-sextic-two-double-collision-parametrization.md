# Exact regular parametrization of two-double-input sextic collisions

## Hypotheses

Let D=d/dx, 1/4<=t<=5/18, and T=1+D+tD^2. Let u,v,B,C be
real numbers with u!=v and C>B^2/4, and put
\[
 p(x)=(x-u)^2(x-v)^2(x^2+Bx+C).
\]
Suppose the output has a zero of multiplicity at least two at zero:
\[
 (Tp)(0)=(Tp)'(0)=0.                                      \tag{1}
\]
The location zero is a translation convention, not a restriction on
where a collision may occur. All root counts include multiplicities.

## Conclusion

Neither u nor v is zero. Set
\[
 l=-\frac{u+v}{uv},\qquad k=\frac1{uv},\qquad
 R(x)=(1+lx+kx^2)^2,
\]
so k!=0 and l^2-4k>0. Define
\[
\begin{array}{ll}
 a=1+4tl,& b=1+2l+2t(l^2+2k),\\
 c=1+4l+6t(l^2+2k),& d=2l+2(l^2+2k)+12tlk,\\
 f=-2t,& g=-2-12tl,\\
 \Delta=ad-bc,& N_B=fd-bg,\quad N_C=ag-fc.
\end{array}                                                   \tag{2}
\]
Lowercase b,c here are matrix entries, not the input coefficients B,C.
Every collision (1) satisfies
\[
 \Delta<0,\qquad B=N_B/\Delta,\qquad C=N_C/\Delta,
 \qquad M:=4N_C\Delta-N_B^2>0.                              \tag{3}
\]
In particular there are **no consistent singular collision systems**
in this family. The uniform strict bound responsible for this is
\[
 N_C=-30(tl+1/5)^2-6t^2(l^2-4k)+2t-4/5<-11/45.             \tag{4}
\]

Conversely, every real triple (l,k,t) satisfying the parameter interval,
k!=0, l^2>4k, Delta<0 and M>0 gives such a collision by (2)--(3).
The monic input is k^(-2)R(x)(x^2+Bx+C). Thus these are exact
necessary and sufficient conditions for this collision family.

The residual output quartic is explicit in (7) below. Its number of
real roots is **not determined here**. This result is a regularity
and elimination step, not the requested sextic (2,4) witness or a
whole-class exclusion. Independent critical audit is pending.

## Proof

**Input roots at the collision location.** If u=0, then v!=0 and
p(0)=p'(0)=0 while p''(0)=2v^2 C>0. Hence Tp(0)=2tv^2 C>0,
contradicting (1). The case v=0 is identical. This uses C>B^2/4>=0
and t>0, and handles a case lost by division by uv.

For uv!=0, the polynomial 1+lx+kx^2 equals
(x-u)(x-v)/(uv), and
\[
 l^2-4k=\frac{(u-v)^2}{u^2v^2}>0.                          \tag{5}
\]
The normalized input P=R(x)(x^2+Bx+C) equals k^2 p. Multiplication
by the positive nonzero constant k^2 preserves roots and their
multiplicities, and (1) holds for P as well.

**Collision equations and singular consistency.** In ascending powers,
write R=sum r_j x^j, where
\[
 (r_0,r_1,r_2,r_3,r_4)=(1,2l,l^2+2k,2lk,k^2).
\]
The two output coefficients that must vanish give exactly
\[
 aB+bC=f,\qquad cB+dC=g.                                  \tag{6}
\]
For example the constant coefficient of TP is
C+(B+2lC)+2t(1+2lB+(l^2+2k)C)=aB+bC+2t.
The linear coefficient is
(B+2lC)+2(1+2lB+(l^2+2k)C)
+6t(2l+(l^2+2k)B+2lkC)=cB+dC+2+12tl.
These verify both equations directly, without any root sampling.

Eliminating B from (6), by multiplying the second equation by a and
subtracting c times the first, gives Delta*C=N_C even when Delta=0.
Expansion and completion of the square give
\[
 N_C=-36t^2l^2-12tl+24t^2k+2t-2
     =-30(tl+1/5)^2-6t^2(l^2-4k)+2t-4/5.
\]
By (5) the second term in the last expression is strictly negative;
the first is nonpositive; and 2t-4/5<=2(5/18)-4/5=-11/45.
This proves (4), including both endpoints of the t interval. If
Delta=0, equation Delta*C=N_C is therefore impossible, regardless of
the values of the other matrix entries. No division by a,b,c or d
has been used, so their possible zero values are retained.

For Delta!=0, Cramer's rule gives (3)'s formulas. Because C>0 and
N_C<0, the equality Delta*C=N_C forces Delta<0. Finally
C-B^2/4=M/(4 Delta^2)>0, proving the remaining condition.

**Converse and residual polynomial.** If the stated inequalities in
(l,k,t) hold, 1+lx+kx^2 has two distinct real roots u,v: its degree
is two and its discriminant is positive. They are nonzero since its
constant coefficient is one. Its leading coefficient is k, so
k^(-2)R=(x-u)^2(x-v)^2. Define B,C by (3). Cramer's identities
aN_B+bN_C=f Delta and cN_B+dN_C=g Delta prove (6), and M>0 gives
C>B^2/4. Thus the input has exactly four real roots (u,v each twice)
and exactly two nonreal roots, and its output satisfies (1).

For a completely explicit residual, write P=sum_(j=0)^6 p_j x^j.
Its coefficients are
\[
\begin{split}
 p_0&=C,\quad p_1=B+2lC,\quad p_2=1+2lB+(l^2+2k)C,\\
 p_3&=2l+(l^2+2k)B+2lkC,\\
 p_4&=l^2+2k+2lkB+k^2C,\\
 p_5&=2lk+k^2B,\qquad p_6=k^2.
\end{split}
\]
The first two coefficients of TP vanish, and hence TP=x^2 H, with
\[
\begin{split}
 H(x)={}&(p_2+3p_3+12tp_4)
 +(p_3+4p_4+20tp_5)x\\
 &+(p_4+5p_5+30tp_6)x^2+(p_5+6p_6)x^3+p_6x^4.             \tag{7}
\end{split}
\]
Its leading coefficient is k^2>0, so H always has degree exactly
four. Equations (2)--(3) make every coefficient an explicit rational
function of the parameters. Formula (7) remains valid when H(0)=0
or H has repeated roots; no exact-double or squarefree hypothesis
was imposed. In particular, Z_c(Tp)=Z_c(H) at the collision. A
root-free H would already give the desired output count four. A
two-real-root residual alone is not that witness: at the collision
the output then has four real roots, counting the double root at zero.
Any proposed perturbation must separately certify the disappearance
of that pair and retention of the other required counts. Neither
such a perturbation nor a uniform real-root count for H is proved here.

**Purpose, verification and limitations.** Run
`python3 scripts/quartic-differential/sector-sextic-two-double-elimination-1472.py`.
The full certificate is
`scripts/quartic-differential/sector-sextic-two-double-elimination-1472.json`.
It records every sparse rational polynomial in (2), the full cleared
input/output coefficient arrays, the five residual numerators, the
square-completion identity, and ten exact algebra checks. The bound
N_C<-11/45 is proved by (4)--(5), not by a parameter grid. Singular
consistency would require N_C=0, so it is uniformly excluded. The
script's successful identities do not supply the still missing quartic
root count. An initial optional SymPy import was unavailable; the
saved executable uses standard-library rational arithmetic only.

This elementary elimination is necessary to retain singular cases
omitted by the earlier numerical screen. The unchanged EXPLORE
assessment1468/review1469 covers this fixed sextic test; no new known
root-count theorem or originality claim is imported. The Walsh
preservation interface and sector normalization are available in the
ready assessment and the separate C020p proof, but are not premises
of this algebraic collision reduction. C020n's quartic result,
C020o's inverse obstruction and C020p's fourfold exclusion are
comparisons, not count assumptions here. A rational choice of
(l,k,t) makes B,C rational, but no witness meeting all coefficient,
sector, preservation and count restrictions has been constructed.
General four-real-root inputs, products of factors, actual-Xi
correspondence, exceptional-divisor payment, unbounded degrees, signs,
initialization and overlap remain open. There is no RH candidate.

## Mathlib

Full matching coverage of this parametrization and its uniform bound
has not been checked. The proof uses elementary polynomial algebra
and Cramer's rule; the certificate is not a Lean proof. Unknown
coverage is not evidence of absence.
