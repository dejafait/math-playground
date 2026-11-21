# A rational sector-sextic preserver can increase the nonreal count from four to six

## Hypotheses

Let D=d/dx, let Z_c count nonreal polynomial roots with multiplicity,
and put
\[
 q(z)=1+z+\frac5{18}z^2,\qquad T=q(D),\qquad A=154449.
\]
Define the rational monic sextic
\[
\begin{split}
 f(x)={}&x^6+\frac{1188}{131}x^5+\frac{1947736}{51483}x^4
       +\frac{4353808}{51483}x^3+\frac{5490857}{51483}x^2\\
       &+\frac{3685712}{51483}x+\frac{8984777}{463347}.
\end{split}                                                     \tag{1}
\]

## Conclusion

All coefficients of q and f are strictly positive. The symbol has
q(0)=1, degree two, and its roots obey Re z<0 and
|Im z|=(-Re z)/3. The operator T preserves real-rootedness of every
real sextic, including arbitrary repeated roots and either nonzero
leading coefficient. Nevertheless
\[
 Z_c(f)=4,\qquad Z_c(Tf)=6.                                  \tag{2}
\]
Both counts include multiplicities. Thus the separately imposed
rationality, nonnegative-coefficient and universal real-rooted-sextic
preservation restrictions all hold simultaneously for this (4,6)
witness. This conclusion does not extend to the zero/two-count class
excluded by C020w. Independent critical audit1492 accepts this fixed
witness under precisely the stated hypotheses.

## Proof

**Preservation and symbol restrictions.** The roots of q are
-9/5+3i/5 and -9/5-3i/5, as follows by their sum -18/5 and product
18/5 and q's leading coefficient 5/18. They have negative real part
and the stated sector ratio, including its boundary. Hence the
preservation conclusion of audited C020w applies, with degree q=2<=6
and q(0)=1. Only its universal real-rooted-input preservation conclusion
is used; its two-count conclusion is not applied to f.

For the precise imported theorem behind that preservation interface,
see Thomas Craven and George Csordas, *Location of zeros. Part I:
Real polynomials and entire functions*, Illinois J. Math. **27**(2)
(1983), 244--278, Theorem 3.3 and remarks (1),(3), printed pp.257--258,
[primary scan](https://scispace.com/pdf/location-of-zeros-part-i-real-polynomials-and-entire-z3v2jd50yw.pdf).
Its Walsh convolution consequence is the version already inspected in
assessment1468/review1469 and reused in1488/review1489. To check the
specialization here explicitly, the real-rooted reference polynomial is
\[
 g(x)=Tx^6=x^4(x^2+6x+25/3).
\]
Its quadratic discriminant is 8/3>0. In the cited normalization, if
g=sum b_j x^j, then W(u,g)=sum_(k=0)^6 (6-k)!b_(6-k)u^(k).
The three nonzero coefficients b_6=1,b_5=6,b_4=25/3 give
W(u,g)/6!=u+u'+5u''/18. Walsh's closed-upper- and closed-lower-half-plane
consequences place every zero of this convolution on the real axis
when u is real rooted. Repeated roots are allowed in both polynomials;
the leading coefficient of W is 6! times the product of the leading
coefficients, so there is no degree loss. Linearity covers either
leading-coefficient sign. This is a recorded applicability check of
the imported preservation interface, not a new proof of Walsh.

**Direct image and translation.** Use the saved polynomials from
C020o as explicit definitions, independently checking the needed
identity rather than assuming its pending inverse audit:
\[
\begin{split}
 h(x)&=393x^3+1782x^2+2084x+558,\\
 P(x)&=154449x^6+473958x^5+1156683x^4+606132x^3
        +657762x^2-162175/3,\\
 F(x)&=h(x)^2+1.
\end{split}
\]
The complete ascending coefficient vector for both TP and F is
\[
 (311365,2325744,6331768,7865964,4813548,1400652,154449).        \tag{3}
\]
Indeed, if P_j=[x^j]P and coefficients outside 0<=j<=6 are zero,
the j-th image coefficient is
P_j+(j+1)P_(j+1)+(5/18)(j+2)(j+1)P_(j+2), which gives (3).
Squaring the displayed cubic and adding one gives the same vector.
Thus TP=F, with no reliance on inverse moments.

Direct binomial expansion gives f(x)=P(x+1)/A, with coefficients (1).
For any polynomial u, D^k(u(x+1))=u^(k)(x+1), so the constant-coefficient
operator commutes with this translation. Therefore
\[
 Tf(x)=F(x+1)/A=\frac{h(x+1)^2+1}{154449}\ge\frac1{154449}>0
       \quad(x\in\mathbb R).                               \tag{4}
\]
Its complete ascending coefficient vector is
\[
 \left(\frac{23203490}{154449},\frac{65771318}{154449},
 \frac{75134203}{154449},\frac{14738552}{51483},
 \frac{4711181}{51483},\frac{1974}{131},1\right).
\]
In particular both f and Tf have degree six, leading coefficient one
and rational strictly positive coefficients. The smallest coefficient
of f is 1, exceeding the required lower bound zero. Equation (4)
excludes every real output root; the fundamental theorem of algebra
then gives six nonreal roots counted with multiplicity. No simplicity
claim about the output is required. Translation by a real number and
scaling by a nonzero constant preserve root multiplicities and the
real/nonreal distinction, so it remains to count the real roots of P.

**Exact input count from the audited count interface.** There is also
a short count argument before the independent arithmetic certificate.
P(0)=-162175/3<0, whereas P(x) tends to positive infinity in each real
direction, since its degree is even and its leading coefficient is
positive. The intermediate value theorem gives a negative and a
positive real root. Thus P/A, a real monic sextic, has at most four
nonreal roots counted with multiplicity, and this count is even by
complex conjugation. It cannot be zero: C020w's preservation conclusion
would then make T(P/A)=F/A real rooted. It cannot be two: C020w's
two-count conclusion would give Z_c(F/A)<=2. Both conclusions contradict
F/A>0 on the real axis and its degree six. The only remaining count is
four. No coefficient-sign premise is needed to invoke C020w on P/A.
This argument uses its two-count statement only in a contradiction
branch where that statement's exact hypothesis is satisfied.

**Independent exact Sturm certificate.** Use the classical Sturm theorem in its
squarefree form: for a real polynomial coprime to its derivative,
the sign-variation drop in its signed remainder sequence from
-infinity to +infinity counts its real roots. A positive rescaling of
each remainder does not change that rule. We give the complete
polynomials, so no floating root preview or single evaluation is
being used as a count certificate.

Set S_0=3P and S_1=S_0'. Thereafter take the negative Euclidean
remainder, clearing its rational denominators and dividing out the
positive integer content, always by a positive multiplier. With
coefficient vectors in **ascending** order, the resulting sequence is
\[
\begin{split}
 S_0={}&(-162175,0,1973286,1818396,3470049,1421874,463347),\\
 S_1={}&(0,3946572,5455188,13880196,7109370,2780082),\\
 S_2={}&(21244925,44070054,-111417378,35890584,-72137508),\\
 S_3={}&(-8934397682925,-35555930659525,21301855128216,
                  -49337589698506),\\
 S_4={}&(-44971094689888174916875,-118493320081253974313436,
                  126584707461355888116048),\\
 S_5={}&(29362654455251567260891958254975,
                  126171402727656343640644465559104),\\
 S_6={}&(1).
\end{split}                                                   \tag{5}
\]
Each line denotes the polynomial with those coefficients. Exact
division verifies S_(i-1)=Q_i S_i-S_(i+1)/c_i, c_i>0, for i=1,...,5;
the final division of S_5 by S_6 has zero remainder. The full rational
Q_i and c_i, as well as the coefficient identities, are retained in
the certificate named below under `sturm/relations`. This recurrence
also defines the normalization unambiguously and permits independent
reproduction of (5). Since the last nonzero remainder is the constant
1, gcd(P,P') is constant, so all roots of P are simple.

The degrees are successively 6,5,4,3,2,1,0. Their signs at infinity are
\[
\begin{array}{c|rrrrrrr|c}
 &S_0&S_1&S_2&S_3&S_4&S_5&S_6&\text{variations}\\\hline
 -\infty&+&-&-&+&+&-&+&4\\
 +\infty&+&+&-&-&+&+&+&2
\end{array}
\]
Thus P has exactly 4-2=2 distinct real roots. Coprimality makes their
total multiplicity two as well; its degree six leaves precisely four
nonreal roots counted with multiplicity. The translation and scaling
already checked transfer this count to f, proving (2).

**Reproduction and limitations.** Run
`python3 scripts/quartic-differential/sector-sextic-four-to-six-1490.py`.
The standard-library rational-arithmetic script writes the full
certificate to
`scripts/quartic-differential/sector-sextic-four-to-six-1490.json`.
All 15 checks pass, including the direct and translated image
identities, complete coefficient signs, degree/monicity, reference
polynomial and discriminant, signed remainder identities, constant
gcd and exact count. The complete pair, Sturm polynomials, rational
quotients and positive scaling factors, endpoint signs, bounds and
failures fields were inspected. The output positivity assertion is
the algebraic square argument (4); a script boolean is not its proof.
The script imports neither Walsh nor a numerical root solver.

The ready EXPLORE assessment1488/review1489 authorized this one fixed
pair and translation test. The saved pair and preservation interface
were already available; the simultaneous admissibility and exact
(4,6) count are the local addition. No novelty beyond the sources
checked is certified. This limits a generic count-contraction claim
for sector preservers; it is compatible with C020w's smaller input
class. No actual-Xi factor correspondence, paid exceptional-divisor
loss, unbounded-degree estimate, signs, initialization or overlap is
supplied. The inverse-method and coefficient-test stops remain intact.
There is no candidate RH resolution.

**Independent critical audit — 18 November 2026, step1492.**
The fixed witness is accepted. This audit reproduces its rational
arithmetic independently and checks the imported preservation
specialization; it asserts no discovery beyond the sources checked.
C020w/audit1488 is reused under its accepted hypotheses, without
reopening the internal proofs of C020u/C020v. The ready EXPLORE
assessment1490, completed by source review1491, covers this exact audit.

For the symbol, direct multiplication verifies
q(z)=(5/18)((z+9/5)^2+(3/5)^2). Thus both roots have negative real
part, with sector ratio exactly 1/3; q(0)=1 and every coefficient
is positive. The reference g=x^4(x^2+6x+25/3) has four zeros at zero
and two distinct real zeros, since its quadratic discriminant is
8/3. In the cited Walsh normalization, the complete coefficients
(6-k)!b_(6-k)/6!, for k=0,...,6, are
(1,1,5/18,0,0,0,0). Hence the convolution is exactly 6!Tu for
every sextic u, with leading coefficient 6! times that of u.
All zeros of g and every real-rooted u belong to both the closed upper
and closed lower half-planes. The imported theorem and its remarks
therefore localize the convolution zeros in both half-planes, whose
intersection is the real axis. Neither g's fourfold zero nor repeated
zeros of u violate the source hypotheses. The nonzero leading
coefficient excludes the identically zero image and degree loss;
linearity allows either leading-coefficient sign. No all-real-rooted
symbol assumption on q is being substituted for this finite-degree
reference-polynomial argument.

The independent implementation uses sparse coefficient convolution
and the binomial translation formula, rather than the producer's
polynomial division, primitive normalization or Horner translation.
Every displayed coefficient in (1), (3) and (5) matches the original
certificate. It checks the complete identities TP=F=h^2+1,
f=P(x+1)/A and Tf=F(x+1)/A. All seven coefficients of each monic
degree-six polynomial are strictly positive, and min_j [x^j]f=1.
For every real x, h(x+1) is real and A=154449>0, proving the strict
bound (4). This last logical implication is the square argument,
not the producer's `output_no_real_roots` boolean, whose code alone
only tests A>0. The producer's symbol booleans likewise do not replace
the complete factorization and sector check above. No mathematical
defect is found in the canonical argument.

For the Sturm proof, all five complete rational quotient relations
are verified coefficientwise from the saved quotients, independently
of division. Their positive multipliers c_i, in order i=1,...,5,
are exactly
\[
\begin{split}
&131,\\
&4211600642/1179,\\
&4645415567286498801485939/2105800321,\\
&222551224487181236842204050766936113815488032/
  134717051451308465243092231,\\
&\frac{994951429141527914509471702921087402618466577803374451957330176}
 {10486404777431879138365093966044552810772956803598378652539651163475806955951105856475}.
\end{split}
\]
All numerators and denominators are positive. S_0=3P and S_1=S_0'
are checked exactly; subsequent degrees decrease by one, and each
relation has remainder -S_(i+1)/c_i of degree strictly below S_i.
Thus it is the actual Euclidean remainder, not an unrelated polynomial
identity. At a zero of S_i the two neighbors have opposite signs
because c_i>0. The verified terminal identity divides S_5 by S_6=1
with zero remainder. These relations imply gcd(S_0,S_1)=1, hence
gcd(P,P')=1, with no hidden repeated input roots. The leading signs
and degrees give the full infinity sign lists in the table, with
variation counts 4 and 2. Sturm therefore gives exactly two real
roots; squarefreeness makes their total multiplicity two. Real
translation and positive scaling transfer this count to f. The
output's count six requires only its degree and real-axis positivity,
not output simplicity.

The alternative IVT argument is also within scope. P(0)<0 and its
positive even-degree leading term give two distinct real roots, one
on each side of zero. Thus Z_c(P/A) is even and at most four.
Only under the hypothetical count-zero branch is real-rooted
preservation used; only under the hypothetical count-two branch is
C020w's two-count inequality used. P/A is real and monic of degree
six, and that input theorem imposes no coefficient-sign condition.
Its symbol conditions include the present sector boundary. Both
branches contradict the proved degree-six, strictly positive F/A;
the remaining count is four. This does not apply a two-count theorem
directly to the actual four-count input.

Run `python3 scripts/quartic-differential/sector-sextic-four-to-six-audit-1492.py`.
All 55 independent exact checks pass, with no failures; full identity
residuals, signed remainders, scaling factors, signs, bounds and
symbol normalization are saved in
`scripts/quartic-differential/sector-sextic-four-to-six-audit-1492.json`
and were inspected in full. A temporary-directory replay of the
original script also passes its 15 checks and reproduces the complete
saved certificate; its retained copy is
`scripts/quartic-differential/sector-sextic-four-to-six-replay-1492.json`.
The original source and certificate are unchanged. No floating root
approximations, inverse moments or new mathematical dependency are
used. C020w remains the sole direct local input: the Sturm argument
is an independent arithmetic check using the named external theorem.
No actual-Xi correspondence, exceptional-loss payment or all-degree
control is obtained. Prior stops1470/1473 remain in force within
their original scopes.

**Bounded imaginary-height diagnostic — 18 November 2026, step1495.**
This computational qualification does not change (2). For this exact f,
define f_s(x)=s^6 f(x/s), with s in {1/4,1/2,1,2,4}, retain the same
T, and put H_a(p)=sum_r max(|Im r|-a,0), with multiplicities. On only
the eight thresholds a in {0,1/8,1/4,1/2,1,2,4,8}, the approved
forty-pair falsification test finds no violation of
H_a(Tf_s)<=H_a(f_s). All forty signs are certified: twenty-five
deficits are strictly negative and fifteen are exactly zero. This is
not an all-a or all-sextic assertion, and supplies no payment for Xi.

Here is the full certification argument, using the standard named
Rouché theorem: if two holomorphic functions u,v on a neighborhood of
a closed disk satisfy |v|<|u| on its boundary, u+v and u have the same
number of zeros inside, with multiplicity. Each of the ten polynomials
is a monic rational sextic. Its complete ascending coefficients, six
rational complex centers c, radius r=1/10^7, and all Taylor coefficients
b_k=p^(k)(c)/k!, k=0,...,6, are saved in
`scripts/quartic-differential/sector-sextic-height-hinge-1495.json`.
Coefficients are computed exactly from
[x^j]f_s=s^(6-j)[x^j]f and
[x^j]Tp=p_j+(j+1)p_(j+1)+(5/18)(j+2)(j+1)p_(j+2), with out-of-range
coefficients zero. Taylor coefficients use the exact binomial expansion
b_k=sum_(j=k)^6 binom(j,k)p_j c^(j-k). Numerical roots select centers
only; they do not establish counts or signs.

For a complex rational z define U(z)=|Re z|+|Im z| and
L(z)=max(|Re z|,|Im z|), so L(z)<=|z|<=U(z). Every one of the sixty
disks satisfies the exact strict inequality
L(b_1)r-U(b_0)-sum_(k=2)^6 U(b_k)r^k>1/5000000000>0.
Compare p(c+w) with b_1 w on |w|=r. The inequality bounds the error
strictly below |b_1 w|, and b_1 is nonzero. Rouché gives exactly one
root with multiplicity in each open disk. All fifteen squared center
distances for each polynomial exceed 1/1000000, which exceeds
(2r)^2=1/25000000000000. Thus the six disks are disjoint and exhaust
the degree-six root multiset. This also certifies simplicity here;
the original count proof did not require output simplicity.

If Im c=0, conjugation preserves the disk and the real polynomial's
root set; uniqueness therefore makes its one root real. Otherwise
its root's absolute imaginary part belongs to
[max(0,|Im c|-r),|Im c|+r]. Applying the monotone function
y -> max(y-a,0) to these endpoints and summing gives rational bounds
I_l<=H_a(f_s)<=I_u and O_l<=H_a(Tf_s)<=O_u. The exact deficit interval
is [O_l-I_u,O_u-I_l]. All forty intervals are retained under
`grids/*/pairs`; all upper endpoints are nonpositive. At s=1,a=0
the interval is exactly
[-2868896633161/500000000000,-2868895633161/500000000000].
The fifteen zero intervals occur because every corresponding upper
height bound is at most a, so both hinge sums vanish exactly.

Run `python3 scripts/quartic-differential/sector-sextic-height-hinge-1495.py`.
Ten complete root certificates, sixty strict Rouché comparisons,
150 disjointness comparisons and forty hinge intervals pass, with
no failures or unresolved pairs. All centers and exact deficit bounds
were inspected, together with a complete selected rational margin;
the script evaluates every full rational comparison without truncation.
This is bounded exploration under assessment1493/recovery1494, not
a discovery of universal contraction. No grid extension is authorized
by the result. The inverse-positivity and coefficient-method failures
remain unchanged; actual-Xi realization, exceptional-loss payment and
unbounded-degree control remain open.

## Mathlib

Full matching Mathlib coverage of this explicit witness and the
sector-preservation interface has not been checked. Supporting inputs
are Walsh as precisely cited above, the named Sturm theorem, the
fundamental theorem of algebra and rational polynomial arithmetic.
The rational certificate is not a Lean proof; unchecked coverage is
not evidence of absence. Full matching Mathlib coverage of the bounded
hinge diagnostic and supporting Rouché theorem has not been checked.
