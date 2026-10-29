# L116 — Conditional 42-kernel second-derivative enclosure

## Hypotheses

Use all of L101's fixed-curve analytic hypotheses and conventions:
E/Q is y²+y=x³+x²−2x, f=sum a_n q^n is its normalized
weight-two newform of exact conductor 389, and c=2*pi/sqrt(389).
The full elliptic L-series includes every Euler factor. The Fricke
eigenvalue is −1, L(E,1)=L'(E,1)=0, and |a_n|<=n for every n>=1,
as justified in L101 from its stated arithmetic and standard inputs.
The derivative below is the unnormalized L''(E,1), without division
by 2!, periods or an archimedean factor. No exact analytic order is
assumed. Set C=[3/10,1/2] and retain L101's kernels

\[
J_n(t)=\int_1^{128}e^{-tny}\frac{\log y}{y}\,dy,
\qquad S(t)=4\sum_{n=1}^{128}\frac{a_n}{n}J_n(t).
\]

Suppose the following finite data are supplied and valid:

- Rational c_l<=c<=c_u with [c_l,c_u] contained in C. Write
  c_*=(c_l+c_u)/2 and delta=(c_u−c_l)/2.
- Exact certificates identifying a_1,...,a_42 with the coefficients
  of this same f. Individual values for a_43,...,a_128 are not required;
  the all-n majorant remains a hypothesis through L101.
- For 1<=n<=42, finite rational endpoints l_n<=J_n(c_*)<=u_n.
  Write j_n=(l_n+u_n)/2 and e_n=(u_n−l_n)/2>=0.
- Rational s and eta>=0 satisfying
  |s−4*sum_(n=1)^42 (a_n/n)j_n|<=eta. The sum keeps every
  coefficient's sign. Exact rational summation permits eta=0.

These are conditional premises, not data produced by this lemma.
In particular midpoint integration must enclose the actual J_n(c_*);
precision requests, success flags or enclosures at a different
parameter do not suffice. No computed kernel endpoint is an input
to the proof of the conditional implication.

## Conclusion

Define the rational allowance and radius

\[
\beta=\frac{130}{387}\,2^{-14},\qquad
B_{42}=2^{-43}+200\delta+\beta
       +4\sum_{n=1}^{42}\frac{|a_n|}{n}e_n+\eta.
\]

Then

\[
\boxed{|L''(E,1)-s|<B_{42}.}
\]

Thus [s−B_42,s+B_42] is a valid conditional derivative enclosure.
For example, the sufficient verified widths delta<=2^-50,
e_n<=2^-50 for n<=42, and eta<=2^-43 imply

\[
B_{42}\le\beta+624\,2^{-50}
 <\beta+2^{-40}<2^{-14}.
\]

No such widths, finite inputs, signed value or zero exclusion are
established here. Since B_42>=beta>2^-40, this radius cannot supply
L101's original sufficient total-radius guarantee. This is no lower
bound on the true error. This result is REPRODUCTION: a conditional
finite-error specialization of known methods, not a new analytic-order
or BSD result beyond the assessed sources. The separate critical
audit of 2026-10-25, step 482, passes for this conditional implication,
as recorded below; it does not discharge the finite-data premises.

## Proof

**Imported results and scope.** The direct inputs are L101 and L115.
L101 specializes J. E. Cremona, *Algorithms for Modular Elliptic
Curves*, corrected second edition (1997), Section 2.13, printed
pp.42–43, Proposition 2.13.1 and its preceding Mellin proof
([primary chapter](https://johncremona.github.io/book/fulltext/chapter2.pdf#page=36)).
At r=2 its Fricke and lower-vanishing hypotheses give the full
unnormalized derivative identity with factor four. All those
hypotheses and the fixed normalization are retained here. The
coefficient majorant used in both inputs is the one in C. Wuthrich,
*Numerical modular symbols for elliptic curves*, arXiv:1608.06423v2,
Section 3.1, Lemma 4 and its proof, printed pp.6–7
([primary version](https://arxiv.org/pdf/1608.06423v2#page=6)).
The exact prior assessment is
`drafts/literature/2026-10-25-forty-two-kernel-contract.md`.
Neither the derivative identity, the coefficient bound nor the
audited analytic estimates are reproved. The difference requiring
proof is composition with only 42 certified finite summands.

**The original analytic partition.** L101's absolutely convergent
identity splits exactly as

\[
L''(E,1)=S(c)+R_F(c)+R_Y(c),
\]

where R_F contains n>128 with the full kernels on [1,infinity),
and R_Y contains y>128 for every n=1,...,128. Here these are the
signed residuals

\[
R_F(c)=4\sum_{n=129}^{\infty}\frac{a_n}{n}G_2(cn),\qquad
R_Y(c)=4\sum_{n=1}^{128}\frac{a_n}{n}
          \int_{128}^{\infty}e^{-cny}\frac{\log y}{y}\,dy.
\]

L101's equations (4) and (5) instead denote their nonnegative
absolute majorants by R_F and R_Y. Those majorants bound the
absolute values of the signed residuals defined here. L101 proves

\[
|R_F(c)|<\frac{520}{1161}2^{-48}<2^{-48},\qquad
|R_Y(c)|<\frac{80}{3}2^{-48}.
\]

These regions are disjoint, and therefore
|R_F(c)+R_Y(c)|<(83/3)*2^-48<2^-43. In particular,
the y>128 tails of n=43,...,128 remain included here even
though their finite kernel values will be discarded below.

**Transfer before disposal.** Every point between c and c_* lies in
C. L101's parameter estimate applies to the full S and gives

\[
|S(c)-S(c_*)|\le200\delta.
\]

Only now split the finite sum at the midpoint:

\[
S(c_*)=P_{42}(c_*)+T(c_*),\quad
P_{42}(c_*)=4\sum_{n=1}^{42}\frac{a_n}{n}J_n(c_*),\quad
T(c_*)=4\sum_{n=43}^{128}\frac{a_n}{n}J_n(c_*).
\]

By L115, since c_* belongs to C,

\[
|T(c_*)|\le4\sum_{n=43}^{128}\frac{|a_n|}{n}J_n(c_*)
 <\beta.
\]

The kernel is nonnegative, as required by that bound. No sensitivity
bound for P_42 or T is inferred from the signed full-sum bound.
No individual coefficient or kernel certificate for the discarded
block is needed. The block here concerns y in [1,128] only;
it neither replaces nor duplicates the original analytic remainders.

**Retained signs and finite errors.** Put
A=4*sum_(n=1)^42 (a_n/n)j_n. Each accepted kernel interval
gives |J_n(c_*)−j_n|<=e_n, so the finite triangle inequality gives

\[
|P_{42}(c_*)-A|
 \le4\sum_{n=1}^{42}\frac{|a_n|}{n}e_n.
\]

The center A uses signed a_n, including negative and zero values;
only the error majorant uses |a_n|. This argument also covers
zero-crossing kernel intervals. The premise |A−s|<=eta includes
all arithmetic and rounding in the chosen assembly. Combining
these estimates with the exact decomposition

\[
L''(E,1)-s=(R_F+R_Y)+(S(c)-S(c_*))+T(c_*)
                 +(P_{42}(c_*)-A)+(A-s)
\]

proves the displayed strict bound by the triangle inequality. The
strict analytic and block estimates justify strictness even when
one or more finite nonnegative error allowances vanish.

For the optional sufficient widths, |a_n|/n<=1 gives the retained
kernel allowance at most 4*42*2^-50=168*2^-50. The other three
non-block allowances are at most (128+200+128)*2^-50.
Thus B_42<=beta+624*2^-50<beta+1024*2^-50
=beta+2^-40. Finally beta+2^-40<2^-14 is equivalent to
130/387+2^-26<1, which follows from 387<257*2^26.
Also beta>2^-40 is equivalent to 130*2^26>387.
Both are strict integer comparisons. None is a claim about any
actual midpoint value or actual error.

**Qualifications and downstream use.** Future use needs the stated
42 exact coefficient identifications, valid finite kernel enclosures
at the correct c_*, a verified narrow c interval and the arithmetic
bound. L101's finite-integration containment requirements remain
applicable to any backend used to supply these premises; no backend
is certified here. Later nonvanishing would require a supplied signed
interval excluding zero, for example s−B_42>0 or s+B_42<0.
No such premise follows from this conditional theorem. The original
128-output contract and its missing certificates are unchanged.
Arbitrary-curve rank comparison, full Sha finiteness and refined BSD
remain unresolved, and no complete candidate is asserted.

### Separate critical audit — 2026-10-25, step 482

**Verdict and approved scope.** PASS for the conditional implication
and its optional sufficient-width comparison. The complete producing
proof, L101's analytic proof and separate audit, and L115's complete
proof and separate audit were checked under the prior SPECIALIZE
assessment `drafts/literature/2026-10-25-forty-two-kernel-contract-audit.md`.
The displayed signed residual definitions clarify a notation change
from L101; no bound, premise, conclusion or mathematical dependency
needed repair. This is a REPRODUCTION proof audit using the named
sources above, not a new analytic estimate or a finite-data replay.

**Normalization and hypotheses.** The curve, conductor, normalized
newform, all Euler factors and c agree with L101. The imported
Cremona identity requires analytic order at least two and Fricke
eigenvalue (-1)^(2-1)=-1. Both are retained: L(1)=L'(1)=0,
and L101 establishes finite order without assuming nonzero L''.
Lower vanishing removes the lower-order completion terms; the factor
2*2!=4 and kernel factor 1/(2-1)!=1 give L'' itself. No extra period,
2!, or gamma factor is introduced. The same all-n bound |a_n|<=n
applies to this normalized elliptic newform. Upstream arithmetic is
imported through audited L101, not newly replayed here.

**Every region and its sign.** Absolute convergence in L101 permits
splitting the full sum into n>128 with y>=1, and n<=128 split at
y=128. Shared integration endpoints have zero measure. The new
discarded region is precisely 43<=n<=128 with 1<=y<=128;
it contains neither the n>128 series nor any y>128 integral.
Thus in particular the y>128 portions for 43<=n<=128 remain
accounted for in R_Y. Triangle inequality bounds the signed R_F
and R_Y by L101's nonnegative majorants, rather than identifying
those majorants with the signed residuals. Their sum is strictly
less than (1+80/3)*2^-48=(83/3)*2^-48<2^-43,
since 520<1161 and 83<96. All signed and absolute versions
therefore have the meanings needed by the displayed exact decomposition.

**Full-sum transfer and discarded block.** Ordered endpoints enclosing
c give delta>=0, c_* in C and |c-c_*|<=delta. Convexity of C
puts the entire segment between the parameters in the domain where
L101 proves |S'|<5200/27<200. The mean value estimate therefore
controls the full S by 200*delta. Splitting S(c_*) afterwards is
an exact finite identity; it does not infer any partial-sum derivative
bound from a signed full-sum bound. Nonnegativity of each J_n(c_*)
and L115's uniform estimate give |T(c_*)|<beta, also at endpoints
of C. The unused 86 midpoint kernels need no individual evaluation.

**Finite data, strictness and numerical threshold.** Each valid
interval has |J_n(c_*)-j_n|<=e_n. Signed multiplication therefore
gives the center A exactly as written and the error weight
4*|a_n|/n, including negative or zero coefficients and intervals
crossing zero. The last term |A-s|<=eta includes every assembly
rounding error; eta=0 requires actual exact rational arithmetic.
All five errors in the displayed decomposition have their corresponding
allowances in B_42. The strict analytic bound (and separately the
strict block bound) makes their total strictly less than B_42,
even if delta, some e_n or eta vanish. Consequently the closed
interval is valid; its width is 2*B_42, not B_42.

At the optional widths the non-block contributions in units of
2^-50 are 128, at most 200, at most 4*42=168, and at most 128.
Their sum is 624<1024. The remaining comparisons are exact:
387<257*2^26 gives beta+2^-40<2^-14, while
130*2^26>387 gives beta>2^-40. Thus the stated sufficient
upper radius passes 2^-14 and cannot itself meet 2^-40.
This compares allowances, not the true error; it proves no
impossibility of a sharper certificate and no signed zero exclusion.

**Audit boundary and dependencies.** L101 and L115 are exactly the
direct mathematical inputs, so the existing DAG row is unchanged.
No actual coefficient identity, kernel artifact, narrow parameter
certificate, integration backend, provenance chain or signed arithmetic
output was validated in this audit. In particular nothing here silently
repairs the earlier production failures. Application must establish all
finite premises and then test a signed interval against zero. No
general rank equality, Sha finiteness or refined BSD follows, and
there is no complete candidate for the notebook's target.

## Mathlib

Full matching Mathlib coverage of this fixed conditional enclosure
was not checked; supporting integration and interval results were
not newly checked. No absence or formal-verification claim is made.
The named sources and the audited local inputs provide the informal
mathematical foundations of this finite composition.
