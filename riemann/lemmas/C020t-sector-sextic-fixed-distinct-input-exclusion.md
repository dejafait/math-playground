# A fixed four-distinct-real-root input family excludes the sextic count increase

## Hypotheses

Let D=d/dy, 1/4<=t<=5/18, T=1+D+tD^2, and
\[
 R(y)=(y^2-1)(y^2-4)=y^4-5y^2+4,\quad
 Q(y)=y^2+b y+c,\quad F=T(RQ),
\]
where b,c are arbitrary real numbers. All root counts include
multiplicities unless explicitly called distinct. For statements about
the input nonreal count, additionally assume c>b^2/4. For a collision
residual, assume F=(y-d)^2H for some real d; H(d)=0 is allowed.

## Conclusion

F has at least four distinct real roots for every b,c. Thus, when
c>b^2/4, the input has exactly two nonreal roots and the output has
at most two. This fixed R family cannot supply the nominated (2,4)
witness. Every collision residual H has four distinct simple real
roots; the output at such a collision is entirely real-rooted.

The collision equations have no consistent singular system. Define
\[
 A=T(yR),\quad B=TR,\quad C=T(y^2R),
\]
and evaluate all expressions below at y=d:
\[
 \Delta=AB'-A'B,\quad N_b=BC'-CB',\quad N_c=CA'-AC'.       \tag{1}
\]
All collisions with c>b^2/4 are parametrized, necessarily and
sufficiently, by
\[
 \Delta<0,\quad M:=4N_c\Delta-N_b^2>0,\quad
 b=N_b/\Delta,\quad c=N_c/\Delta.                         \tag{2}
\]
Here d ranges over all real numbers, including the four roots of R.
For rational d,t these formulas give rational b,c whenever (2) holds.

The symbol has the required normalization, coefficient signs and
closed-sector zeros, and preserves every real-rooted sextic, including
repeated roots and either sign of the leading coefficient. No exclusion
for arbitrary four-real-root inputs, variable spacings, general allowed
symbols or their products is proved. Independent critical audit1478
accepts the stated fixed-family result and its preservation interface.

## Proof

**Known preservation input.** C020p with a=1 gives the symbol and
preservation assertions for the whole closed t interval. The imported
theorem is Thomas Craven and George Csordas, *Location of zeros. Part I:
Real polynomials and entire functions*, Illinois J. Math. **27**(2)
(1983), 244--278, Theorem3.3 and remarks(1),(3), pp.257--258,
[primary scan](https://scispace.com/pdf/location-of-zeros-part-i-real-polynomials-and-entire-z3v2jd50yw.pdf).
Its Walsh convolution specialization uses
Tx^6=x^4(x^2+6x+30t), whose remaining discriminant is
36-120t>=8/3. The factorial normalization and repeated-root interface
are supplied in C020p and assessment1468/review1469; no count inequality
is inferred from preservation. The new calculation below concerns
partial root counts, which that input does not supply.

**Exact collision solution, including singular systems.** Directly,
\[
\begin{split}
 B(y)&=y^4+4y^3+(12t-5)y^2-10y+4-10t,\\
 A(y)&=y^5+5y^4+(20t-5)y^3-15y^2+(4-30t)y+4,\\
 C(y)&=y^6+6y^5+(30t-5)y^4-20y^3+(4-60t)y^2+8y+8t.
\end{split}                                                   \tag{3}
\]
Since F=C+bA+cB, a double zero at d is exactly
Ab+Bc=-C, A'b+B'c=-C'. Cramer's rule gives (1)--(2) when
Delta!=0; admissibility is equivalent to M>0 since
c-b^2/4=M/(4 Delta^2).

We must first exclude singular consistent systems without dividing by
R(d), A(d), B(d) or Delta. Set r_j=R^(j)(d)/j!, so
r_0=d^4-5d^2+4, r_1=4d^3-10d, r_2=6d^2-5.
In x=y-d write Q(d+x)=x^2+B_0 x+C_0, with
B_0=b+2d, C_0=c+bd+d^2. The collision system becomes
\[
\begin{split}
 (r_0+2tr_1)B_0+(r_0+r_1+2tr_2)C_0&=-2tr_0,\\
 (r_0+2r_1+6tr_2)B_0+(r_1+2r_2+6tr_3)C_0&=-2r_0-6tr_1.
\end{split}                                                   \tag{4}
\]
Its determinant is Delta: the first column is (A-dB,A'-dB')
and the second is (B,B'). Elimination of B_0 in (4), with no
division, gives Delta C_0=N_0, where
\[
\begin{split}
 N_0&=(2t-2)r_0^2-6tr_0r_1-12t^2r_1^2+12t^2r_0r_2\\
 &=-\frac{15}{2}(tr_1+\tfrac25r_0)^2
   -\frac32t^2 E+(2t-\tfrac45)r_0^2,\\
 E&=3r_1^2-8r_0r_2=40d^4-92d^2+160\\
  &=40(d^2-\tfrac{23}{20})^2+\frac{1071}{10}.
\end{split}                                                   \tag{5}
\]
As t>=1/4 and 2t-4/5<=-11/45, (5) gives the uniform bound
N_0<=-3213/320<0. Therefore Delta=0 is inconsistent, even when
r_0=0. Under c>b^2/4, C_0=(d+b/2)^2+c-b^2/4>0, so
Delta C_0=N_0 also forces Delta<0. Conversely, the values (2)
satisfy both collision equations by Cramer's identities and give
c>b^2/4. This proves the exact parametrization with all singular
cases retained. The useful polynomial check
N_0=N_c+d N_b+d^2 Delta follows from (1), (3).

For a fully specified residual in any admissible collision, let
p_j be the coefficient of x^j in R(d+x)(x^2+B_0x+C_0), with
p_j=0 beyond degree six. Then
\[
 H(d+x)=\sum_{j=0}^4
  \big(p_{j+2}+(j+3)p_{j+3}+t(j+4)(j+3)p_{j+4}\big)x^j.       \tag{6}
\]
The first two output coefficients vanish by (4); the leading
coefficient in (6) is one. No exact-double or squarefree assumption
is built into this formula. We next determine its count without
sampling the admissibility region (2).

**Uniform reference roots and thresholds.** Put
\[
 J=B=TR,\quad K=R+2tR'=y^4+8ty^3-5y^2-20ty+4.
\]
The following strict enclosures hold throughout the closed t interval.
There are four simple real roots alpha_1<...<alpha_4 of J, K is
nonzero at each, and, for b_i=-2(alpha_i+tR(alpha_i)/K(alpha_i)),

| i | alpha_i | K(alpha_i) | b_i |
|---|---|---|---|
| 1 | (-4,-3) | (20,60) | (5,7) |
| 2 | (-2,-1) | (-6,-4) | (3,4) |
| 3 | (0,1) | (3,4) | (-1,0) |
| 4 | (1,2) | (-4,-2) | (-4,-3) |

Here is the complete rational interval certificate and its justification.
Partition t into the 32 closed cells
I_j=[1/4+j/1152,1/4+(j+1)/1152], j=0,...,31. The following
integer endpoints give the four root brackets after division by 10000:

```text
j     alpha1          alpha2          alpha3      alpha4
0   -38087 -38050   -18169 -18146    1460 1471   14756 14765
1   -38053 -38016   -18189 -18166    1452 1463   14750 14759
2   -38019 -37981   -18210 -18186    1444 1455   14744 14753
3   -37984 -37947   -18230 -18207    1436 1447   14738 14747
4   -37950 -37912   -18250 -18227    1427 1439   14732 14741
5   -37915 -37878   -18271 -18247    1419 1430   14726 14735
6   -37881 -37843   -18291 -18268    1411 1422   14720 14729
7   -37846 -37808   -18312 -18288    1403 1414   14714 14723
8   -37811 -37773   -18332 -18309    1394 1406   14708 14717
9   -37776 -37738   -18353 -18329    1386 1397   14702 14711
10  -37741 -37703   -18374 -18350    1378 1389   14696 14705
11  -37706 -37667   -18395 -18371    1370 1381   14690 14699
12  -37670 -37632   -18416 -18392    1361 1373   14684 14693
13  -37635 -37597   -18438 -18413    1353 1364   14678 14687
14  -37600 -37561   -18459 -18435    1345 1356   14672 14681
15  -37564 -37525   -18480 -18456    1337 1348   14666 14675
16  -37528 -37490   -18502 -18477    1328 1340   14660 14669
17  -37493 -37454   -18524 -18499    1320 1331   14654 14663
18  -37457 -37418   -18545 -18521    1312 1323   14648 14657
19  -37421 -37382   -18567 -18542    1304 1315   14642 14651
20  -37385 -37346   -18589 -18564    1295 1307   14636 14645
21  -37349 -37309   -18611 -18586    1287 1298   14630 14639
22  -37312 -37273   -18633 -18608    1279 1290   14625 14633
23  -37276 -37236   -18656 -18630    1270 1282   14619 14628
24  -37239 -37200   -18678 -18653    1262 1273   14613 14622
25  -37203 -37163   -18701 -18675    1254 1265   14607 14616
26  -37166 -37126   -18723 -18698    1245 1257   14601 14610
27  -37129 -37089   -18746 -18720    1237 1248   14595 14604
28  -37092 -37052   -18769 -18743    1229 1240   14589 14598
29  -37055 -37015   -18792 -18766    1220 1232   14583 14592
30  -37018 -36977   -18815 -18789    1212 1223   14578 14586
31  -36980 -36940   -18839 -18812    1204 1215   14572 14581
```

For every row and each bracket, J at its left and right endpoints
has signs (+,-),(-,+),(+,-),(-,+), respectively, for **all** t in
I_j. To check this, evaluate (3) at the two t endpoints: J at fixed
y is affine in t. The smallest signed endpoint value over the entire
table and both t endpoints is
731749108327/703125000000000>0. Thus IVT gives four roots in
four disjoint open brackets for every t in every cell. The monic
quartic degree exhausts all roots and forces simplicity. No root
monotonicity or numerical root approximations are assumed.

For each closed bracket Y and cell I_j, evaluate R(Y), R'(Y) by
ordinary interval Horner arithmetic and form
\[
 K_Y=R(Y)+2I_jR'(Y),\qquad
 B_Y=-2\big(Y+I_jR(Y)/K_Y\big).                         \tag{7}
\]
Interval addition adds endpoints; multiplication takes the minimum
and maximum of four endpoint products; [l,u]^{-1}=[1/u,1/l]
only when 0 is excluded. For all 128 boxes the K_Y signs are
(+,-,+,-), and the entire intervals Y,K_Y,B_Y lie strictly inside
the corresponding coarse table entries above. In particular no
division in (7) has a zero-containing denominator. These are rational
inclusions on closed boxes, not evaluations at isolated t values.
They imply b_1>b_2>b_3>b_4, with adjacent gaps greater than 1,3,2,
respectively. The exact smaller-box minimum gap is recorded in the
certificate but is unnecessary for the strict-order argument.

All arithmetic in this table is reproduced by
`python3 scripts/quartic-differential/sector-sextic-distinct-collision-1477.py`.
The adjacent JSON contains all 32 parameter cells, 128 root brackets,
complete endpoint-value intervals and K/threshold enclosures, the
coarse inclusion checks, symbolic collision polynomials, and every
verification flag. The table above and interval rules (7) specify all
finite checks independently of the bracket proposal method. Floating
roots only proposed these rational brackets; they play no role in
their acceptance or the proof. All 340 exact checks pass, with no
failures. Complete cell summaries, all bracket endpoints, coarse
table checks and algebra checks were inspected; every full interval
is retained in the certificate for independent replay.

**Root counts with threshold equalities and shared roots.** The product
rule gives
\[
 F=QJ+Q'K+tQ''R,
 \qquad F(\alpha_i)=K(\alpha_i)(b-b_i).                  \tag{8}
\]
If b>b_2, the indices (2,3,4) give strictly (-,+,-) values.
If b=b_2, use (1,3,4). If b_3<=b<b_2, use (1,2,4).
If b<b_3, use (1,2,3). These four cases cover every real b,
including every b=b_i. The c term disappears in (8), so there
is no restriction on c here. Since the monic sextic is positive
at both infinities, these three increasing signed points give four
distinct roots in four disjoint open intervals by IVT.

At a collision no selected strictly signed point equals d. Division
of (8)'s selected values by (alpha_i-d)^2>0 transfers the same
signs to the monic quartic H. Its two positive ends therefore give
four distinct real roots; degree four makes them all simple and
exhausts its roots. A root H(d)=0, or an unselected alpha_i=d,
does not affect this reasoning. With the extra squared real factor,
the collision output is entirely real-rooted, with multiplicities
added if the factors share a root. This proves the residual assertion
for every admissible (d,t), without testing a parameter grid or
discarding singular, endpoint or shared-root cases.

Finally, c>b^2/4 makes Q strictly positive and gives exactly one
nonreal conjugate pair; R has the four distinct real roots -2,-1,1,2.
The output count bound follows from its degree six and the four
distinct real roots just proved. Hence no pair-removing perturbation
within this fixed input family can yield the desired (2,4) witness.

**Independent audit1478 (18 November 2026).** The audit accepts this
argument, with its original hypotheses and limitations, as reproduction
of the local result. It does not certify originality. The independent
standard-library implementation
`scripts/quartic-differential/sector-sextic-distinct-audit-1478.py`
imports no previous mathematical code and uses no floating arithmetic.
Its full certificate is
`scripts/quartic-differential/sector-sextic-distinct-audit-1478.json`.
All 1471 exact checks pass with no failures. These are finite arithmetic
checks, not 1471 separate mathematical conclusions.

The replay reads every one of the 32 closed parameter cells and all
128 rational brackets from certificate1477, compares every endpoint
with this proof's integer table, and independently reconstructs every
J endpoint interval and every full K and threshold enclosure. At fixed
y, J is affine in t, so its endpoint ranges are exact on each cell.
All other ranges use inclusion-preserving rational interval arithmetic.
The cells have consecutive endpoints 1/4+j/1152 and cover both boundary
values, ending at 1/4+32/1152=5/18. The four disjoint brackets in
each cell lie strictly within the displayed coarse table. Four strict
sign changes give four distinct roots; degree four excludes any
additional root or multiplicity. No root tracking between cells is
needed. The minimum signed endpoint margin is exactly
731749108327/703125000000000, and the minimum adjacent threshold gap is
3480641043423441651708258411632377/2363945125221752283578637552760000;
both are strictly positive as required. The minimum absolute K bound
is 77109273652311/25000000000000>0.

Independent sparse polynomial arithmetic verifies (3), the product
rule (8), both rows and right sides of (4), its unchanged determinant,
the division-free elimination giving N_0, both square completions,
Cramer's identities, the shifted coefficient formula (6), and the
monic leading coefficient. It compares every saved symbolic polynomial
in certificate1477 and also verifies both recorded d=0 examples in
full. The real-variable implication of the square completion is
separate from these identity checks: E>=1071/10, t^2>=1/16 and
2t-4/5<=-11/45 make all three contributions to (5) nonpositive,
with the middle contribution <=-3213/320. Consequently Delta=0 is
inconsistent for every real d and all b,c, including R(d)=0. For
c>b^2/4, C_0>0 and Delta*C_0=N_0 force Delta<0. Conversely Delta<0
and M>0 give a consistent collision by Cramer's rule and the strict
pair margin M/(4 Delta^2)>0. No division by R, A, B or C_0 is used
to exclude a singular system.

For completeness, the four sign selections in (8) are checked on all
nine order/equality cells of b relative to b_1>b_2>b_3>b_4. The
arithmetic representative of a cell is legitimate because the signs
depend only on those comparisons. Directly, b>b_2 selects (2,3,4);
b=b_2 selects (1,3,4); b_3<=b<b_2 selects (1,2,4); and b<b_3
selects (1,2,3). Every selected value has strict sign (-,+,-),
regardless of c. Positivity at both infinities gives one real root in
each of the four disjoint open intervals separated by these points.
This is the analytic IVT argument, not a consequence of sampled roots.
At a collision, a selected point cannot equal d because F(d)=0 while
its selected value is nonzero. Division by its positive squared
distance to d transfers all three strict signs to H. The monic
quartic H therefore has four distinct roots, all simple by degree.
If H(d)=0, this is one of those simple roots and the multiplicity
in F is three; if an unselected reference point equals d, it was
never used as a strict sign point. Both cases are retained.

The preservation interface alone was also checked: for a=1 the
symbol roots have imaginary-to-negative-real ratio sqrt(4t-1)<=1/3,
including the double negative root at t=1/4. In the cited degree-six
Walsh theorem, g=Tx^6 is monic with four zero roots and a quadratic
factor of discriminant at least 8/3. Its factorial coefficients give
W(f,g)/6!=Tf exactly. Upper and lower closed-half-plane applications
put every output root on the real axis; neither input-root simplicity
nor a positive leading coefficient is required. This reuses the
inspected primary theorem from assessment1468/review1469 without
reproving it or auditing the unrelated remainder of C020p.

**Scope and reason for this calculation.** The unchanged EXPLORE
assessment1468/review1469 covers this sextic test. C020q and the
audited C020r/s are comparisons for a different repeated-root family,
not premises supplying root locations or thresholds here. A separate
exact calculation is necessary because no extremal or deformation
reduction was established. The inspected sources supply preservation,
not this partial-count conclusion; recorded searches do not certify
originality. The result is a local exclusion, not whole-class
impossibility or an RH candidate. Coefficient signs and rationality
were not needed for the exclusion, so imposing them cannot rescue
this family. Actual-Xi factor applicability, paid exceptional-divisor
loss, unbounded degrees, signs, initialization and overlap remain open.

## Mathlib

Full matching coverage of this fixed-family exclusion, collision
parametrization, uniform interval table and Walsh specialization has
not been checked. The certificate uses exact rational polynomial and
interval arithmetic and is not a Lean proof. Unknown coverage is not
evidence of absence.
