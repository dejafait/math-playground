# L063 — One two-prime scalar bounds the finite Selmer quotient exponent

## Hypotheses

Retain every hypothesis of L026: E/Q is non-CM; p>=5 is good ordinary;
E[p] is surjective; p divides neither #E(F_p), the Manin constant nor
any Tamagawa factor; E(Q_p)[p]=0; a residual Kurihara number in
Sakamoto's N_(1,0) is nonzero with compatible Neron plus-period and
discrete-logarithm conventions; L(E,1)=0; w(E)=+1; and the quadratic
coefficient of the fixed primitive ordinary cyclotomic series is
independently certified nonzero. Write D=Sel(Q,E[p^infinity]) with
classical Kummer conditions, D_div for its maximal divisible subgroup,
and F=D/D_div. Use the localization conventions of L062.

Supply m>=1 and two distinct primes ell_1,ell_2 in Kim's P_m, namely
good primes not dividing N_E p with ell_i=1 and a_(ell_i)=ell_i+1
modulo p^m. Put N=ell_1 ell_2 and use Kim's actual ideal

\[
I_N=\sum_{\ell\mid N}(\ell-1,a_\ell-\ell-1)\mathbf Z_p.
\]

Supply the reduction d_m in Z/p^m Z of the actual Kurihara number

\[
\widetilde\delta_N=
\sum_{a\in(\mathbf Z/N)^\times}[a/N]^+
       \prod_{\ell\mid N}\log_{\eta_\ell}(a)
       \quad\text{in }\mathbf Z_p/I_N,
\]

and an independently certified integer 0<=v<m with
d_m in p^v(Z/p^m Z) but not in p^(v+1)(Z/p^m Z).
The symbols must use Kim's defining oriented integral and the total
real Neron period of the minimal target model; any different table
orientation or period requires an independently certified conversion.
The discrete logarithms use the fixed auxiliary generators. Only
certified unit changes of generators can be ignored for valuation.
Neither a scalar of a different system nor an arbitrary integer lift
at inadequate precision supplies d_m.

This is the exact covered specialization in
[the prior source assessment](../drafts/literature/2026-10-14-two-prime-scalar-exponent-certificate.md).
No particular curve, primes, scalar or successful localization class
is produced by these hypotheses.

## Conclusion

The finite quotient satisfies

\[
0\le\operatorname{length}_{\mathbf Z_p}F\le v,
\qquad p^v F=0.
\tag{1}
\]

Consequently, if one additionally supplies n>v and a classical class
c in Sel_(p^n)(E/Q) with p^v loc_p(c)!=0 at that same depth, L062
applies with e=v: L061's whole-system index is k=1, rationalized
classical localization has rank one, and its strict Selmer kernel is
a line. A zero test is inconclusive. The scalar alone selects neither
k=1 nor rational rank two. No exact minimum, optimal exponent, finite
Sha, rational Kummer membership or complex-order comparison is claimed.
The separate critical audit below passes under these unchanged premises.

## Proof

**Import the structure formula with its full premises.** L026 gives
corank D=2. Its arithmetic and residual-family assumptions are precisely
the other premises of L021 (where the same classical group is called S).
Apply L021 to obtain that F is finite and

\[
\operatorname{ord}(\widetilde\delta)=2,\qquad
\partial^{(\infty)}(\widetilde\delta)=0,\qquad
\operatorname{length}_{\mathbf Z_p}F
 =\partial^{(2)}(\widetilde\delta).
\tag{2}
\]

The primary imports are Chan-Ho Kim, *The structure of Selmer groups
and the Iwasawa main conjecture for elliptic curves*, publisher-hosted
author text dated 2025-05-12,
[Section 1.5.1 and Theorem 1.8(1)--(3), printed pp. 5--6](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf#page=6),
and [Theorem 1.10, printed p. 7, with its primitivity proof, p. 32](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf#page=8).
Residual surjectivity, the prime-to-p Manin constant and collection
nonvanishing give the structure theorem; the retained local torsion
and Tamagawa assumptions support the terminal valuation zero, as
checked in L021. We import these results without reproof. The finite-Sha
clauses of Theorem 1.8 are unused. Here partial^(2) is the minimum
actual scalar valuation over the two-prime indices, not a residual
minimum prime count and not the whole-Kato-system first index.

**Transfer precision in the actual coefficient ring.** Kim's
[Sections 1.2.2 and 1.4, printed pp. 3 and 5](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf#page=4)
give the ideal and scalar definitions above and the depth-m reduction
for N in N_m. Each generator of I_N is divisible by p^m, so
I_N is contained in p^m Z_p and the quotient map
Z_p/I_N -> Z/p^m Z exists. Moreover I_N is nonzero, since ell_1-1
is a nonzero integer in it. Thus I_N=p^s Z_p for a finite s>=m;
equality s=m is not assumed. The index lies in N_1 and has exactly
two prime factors, so it is among the indices in partial^(2).

Choose any lift x in Z_p of tilde-delta_N. Its reduction modulo p^m
is d_m. Since v<m, the stated residue condition implies
x in p^v Z_p and x not in p^(v+1) Z_p: membership modulo p^m lifts
to the first assertion because p^m Z_p is contained in p^v Z_p;
the second follows because otherwise the residue would belong to
p^(v+1)(Z/p^m Z). Hence v_p(x)=v. Every other lift is x+y with
y in p^s Z_p. Since s>=m>v, writing x=p^v u with u a unit gives
x+y=p^v(u+p^(s-v)z), also of valuation v. The valuation in Kim's
actual coefficient ring is therefore v, below its truncation depth s.
This verifies the actual value, rather than assigning a valuation to
a zero residue or assuming equality of coefficient ideals. The supplied
orientation, period and logarithm matching identifies this residue
with the source scalar; no unverified normalization is removed here.

**Compare a minimum with one value.** The two-prime minimum is at most
the valuation at this N. Thus (2) gives

\[
\operatorname{length}_{\mathbf Z_p}F
 =\partial^{(2)}(\widetilde\delta)
 \le v_p(\widetilde\delta_N)=v.
\]

No minimizer is supplied or searched for, and no equality with v follows
from a single index. By the finite Z_p-module structure theorem write
F as a finite direct sum of Z_p/p^(b_j) Z_p with b_j>=1, allowing
the empty sum when F=0. Its length is sum_j b_j, so every b_j is at
most v. Multiplication by p^v kills each factor, proving (1).
In particular v=0 forces the empty sum; for positive v the argument
does not force F=0. The paired structure in L021 is consistent with
this conservative bound but no sharper exponent is needed here.

**Conditional downstream application.** With the additional class and
n>v specified in the conclusion, every premise of L062 holds: all its
arithmetic conventions are retained, and (1) supplies its quotient
exponent with e=v. Its audited same-depth test gives k=1 and the
rank-one/strict-line statements. This application does not replace
m by n in the scalar computation, or use downward coefficient
transition as multiplication within a point quotient. The scalar
depth m certifies the exponent independently of the later class depth
n. No successful c is obtained from the scalar calculation.

This is REPRODUCTION by specialization of the assessed source package,
not a mathematical discovery beyond it. L023's existential scalar at
a depth above an already granted finite length is not an independent
finite-input bound and is not used. ATTEMPTS/021 and 029--031 remain
valid evidence against the stopped inferences. Scalar production,
successful classical localization, strict rational Kummer membership,
uniform coefficient production and arbitrary higher-order rational/
complex rank equality remain unresolved.

**Separate critical audit (2026-10-14).** The approved
[audit scope](../drafts/literature/2026-10-14-two-prime-exponent-critical-audit.md)
has been checked independently against the complete proof, L021's
minimum formula, all L026 premises and audited L062. No failed
implication, additional premise or stronger conclusion was found.
The primary coverage is reused as recorded there; this is verification
of the known-source specialization, not fresh theorem discovery or
production of any arithmetic input.

For the coefficient ring, put
\[
s=\min_{i=1,2}\{v_p(\ell_i-1),v_p(a_{\ell_i}-\ell_i-1)\},
\]
with valuation of zero interpreted as infinity. Both ell_i-1 are
nonzero integers, so s is finite. The ideal generated by these four
elements is exactly p^s Z_p, and the eligibility congruences give
s>=m. This checks the direction of the quotient map: reduction from
Z_p/p^s to Z_p/p^m is well-defined because p^s Z_p is contained in
p^m Z_p. Reversing this inclusion would not justify the reduction.
No assumption that one congruence has valuation exactly m enters.

Choose a representative x of the actual scalar. Membership of its
residue in p^v(Z/p^m) means x=p^v a+p^m b for a,b in Z_p.
If a were divisible by p, then x would be divisible by p^(v+1),
because m>=v+1, contradicting the stipulated nonmembership of d_m.
Thus x=p^v(a+p^(m-v)b) has valuation v. Changing its lift adds an
element of p^s Z_p and cannot change this valuation, since s>v.
This also checks the boundary v=m-1: the reduction modulo p of
x/p^v is still determined and nonzero, even when s>m. At v=0 the
actual scalar is a unit in its coefficient ring. If d_m were zero,
the argument would instead give only divisibility by p^m, with no
determined exact valuation; that case is excluded, not silently
treated as a certificate. The normalization and logarithm matching
are supplied hypotheses throughout this check, not results of it.

The imports have no circular corank premise. L026 obtains corank D=2
from its independently supplied arithmetic, residual, analytic and
quadratic-coefficient assumptions. These satisfy L021's hypotheses,
including its separate granted-corank requirement, and identify its
S/S_div with the present F. Hence the cited structural and primitivity
results give length(F)=partial^(2), with terminal valuation zero.
Neither finite Sha nor F=0 is used in that import. Since m>=1,
N belongs to Kim's N_1, is square-free and has exactly two factors.
Its finite valuation v is therefore one of the values over which
partial^(2) is minimized. The resulting inequality is partial^(2)<=v;
a smaller value at another index is allowed. The stronger cyclic
torsion condition defining Sakamoto's prime set is not needed for this
new index: it is retained only for the original residual-family
premise. The full source theorem is applied without imposing its
proof's deep minimizing-index choices on this supplied index.

For annihilation, the finite-module decomposition gives
length(F)=sum_j b_j and exponent p^(max_j b_j) when F is nonzero.
The already proved sum_j b_j<=v implies b_j<=v for every factor,
so multiplication by p^v is zero on all of F. For the empty sum F=0
the same conclusion holds, including v=0. Conversely v=0 leaves no
positive b_j. Positive v alone is not an assertion that a nonzero
finite factor occurs. Paired structure is available in L021 but is
not required for this conservative exponent; no improved exponent
or equality of length with v is claimed.

Finally suppose the additional classical c at depth n>v is supplied.
In L061's k=2 branch the image I=f(D) is finite, so the divisible
subgroup D_div maps to zero, as proved in L062. Since p^v F=0,
p^v x belongs to D_div for every x in D, and therefore p^v f(x)=0.
Use the audited coefficient isomorphisms at this very depth n:
alpha_n:Sel_(p^n)->D[p^n] and
beta_n:E(Q_p)/p^n E(Q_p)->L_p[p^n]. Their commuting square gives
\[
\beta_n(p^v\operatorname{loc}_p(c))
 =p^v f(\alpha_n(c))=0.
\]
Injectivity of beta_n contradicts the proposed nonzero test.
Thus the exhaustive k=1,2 alternatives select k=1, with the rank-one
localization and strict line stated in the conclusion. This retains a
possibly nonzero I in the excluded branch and uses neither integral
Tate-module surjectivity nor a rational point. Scalar depth m and
class depth n have independent roles; no relation between them beyond
m>v and n>v is needed. Multiplication takes place at depth n and is
not downward reduction to depth n-v. With v=0 it is the identity;
with n<=v it would always vanish. Even at n>v a zero class fails the
test in either branch, so a zero test cannot select k=2.

The continuation test therefore passes for the conditional certificate.
The audit establishes no actual d_m, successful c, rational membership
of the strict line, or arbitrary-curve rank comparison. It preserves
the stopping evidence in ATTEMPTS/021 and 029--031. The proof's direct
inputs remain exactly L021, L026 and L062; L061 enters through L062.
No new graph edge, source reproof or mathematical script is needed.

## Mathlib

Full matching arithmetic statement and Kim's imported structure and
primitivity theorems: not checked. Supporting DVR valuation, quotient
reduction and finite-module structure coverage: not checked. The
elementary precision and annihilation arguments are written above;
unknown coverage is not evidence of absence. Reproving Kim is neither
necessary nor attempted.
