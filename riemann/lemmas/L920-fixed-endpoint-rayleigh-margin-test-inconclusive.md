# Lemma 920: the fixed endpoint Rayleigh-margin test is inconclusive

## Hypotheses

Use the family, opposite-pair convention, algebraic coefficients S_k,
head A, tail E and scaling D=diag(1,200,40000) of L919. Set lambda=0,
R=100, c=(1,-2,1), and B=5691/10^9. Import L917's complete panel0
coefficient enclosures under exactly its L037 arithmetic contracts;
the Decimal-library correctness in that input is assumed. No new
quadrature or zero census is performed. All zeros, their multiplicities,
and zeros on the cutoff boundary are retained as specified in L919.

## Conclusion

For the full and head Rayleigh quotients

    q_full = c^T D H2(0) D c / 6,
    q_head = c^T A(0)c / 6,

the saved intervals and complete tail bound imply the exact conservative
rational-decimal enclosures

    -0.000044222946 <= q_full <= 0.000045398584,
    -0.000045239559 <= q_head <= 0.000046415197.

The directional error satisfies

    |c^T E(0)c|/6 <= T_c,
    T_c = 178794260431/175872436523437500
        < 0.000001016614.

The exact computed head interval straddles B=0.000005691. In particular
its upper endpoint exceeds B, so this fixed test does **not** obstruct
L919's strict sufficient head margin. It also establishes neither that
margin's feasibility nor an H2 sign. The authorized test ends without
refining intervals, changing directions or sweeping parameters. This
is a reproduction/specialization of known variational and tail methods;
no new general theorem or progress beyond the checked sources is claimed.
The finite certificate and this specialization have not received a
separate independent audit.

## Proof

L917 panel0 is the closed interval [0,1/5120], so its complete S_2,...,S_6
enclosures apply at zero. No midpoint or pointwise quadrature value is
substituted. L919 gives D H2 D=A+E and real symmetry of A and E even
when some zeros are nonreal. Since c^T c=6 and Dc=(1,-400,40000),
ordinary matrix multiplication gives

    6 q_full = S_2-800 S_3+240000 S_4
                         -32000000 S_5+1600000000 S_6.       (1)

This identity can also be checked zero by zero: the numerator
contribution is

    zeta^(-4)(1-400 zeta^(-2)+40000 zeta^(-4))^2.

The square is algebraic, not a modulus square. The coefficient vector
of (1-400w+40000w^2)^2 is
(1,-800,240000,-32000000,1600000000). Expanding its absolute value
by the triangle inequality bounds the omitted numerator by

    sum_(p=4,6,8,10,12) w_p sum_(|zeta|>100)|zeta|^(-p),
    (w_4,w_6,w_8,w_10,w_12)
       =(1,800,240000,32000000,1600000000).                (2)

Every series in (2) is absolutely convergent by L919(10). Thus the
estimate covers the entire infinite complement with opposite-pair
multiplicity, including complex zeros. Boundary zeros belong to A,
not to this strict tail. With log100<5, L919(10) gives

    J_p = [4p/(5(p-1))]100^(1-p)(5+1/(p-1)).              (3)

The five exact values and their numerator weights are

| p | J_p | w_p |
|---|---|---|
| 4 | 4/703125 | 1 |
| 6 | 39/78125000000 | 800 |
| 8 | 9/191406250000000 | 240000 |
| 10 | 23/5062500000000000000 | 32000000 |
| 12 | 21/47265625000000000000000 | 1600000000 |

Their weighted sum divided by six is the displayed T_c. No sign of
c^T E c is assumed: these absolute values occur only in bounding the
error, not in replacing the exact coefficient identity (1).

For completeness, write [l_k,u_k] for the full saved panel0 interval
for S_k in `scripts/heat/low-time-h2-uniform-195.json`. Since the signs
in (1) alternate, exact interval arithmetic gives

    L=(l_2-800u_3+240000l_4-32000000u_5+1600000000l_6)/6,
    U=(u_2-800l_3+240000u_4-32000000l_5+1600000000u_6)/6.

The exact input decimals are treated as rationals, not binary floats.
Consequently q_full lies in [L,U]. The inputs need not be independent:
interval linear combinations enclose their actual joint value without
assuming attainability of either endpoint. Subtracting the unknown
signed tail gives

    q_head in [L-T_c,U+T_c].                              (4)

In particular the upper bound is U+T_c, with a plus sign. Using the
complete saved endpoints gives the rational-decimal enclosures in the
Conclusion and the exact inequalities L-T_c<B<U+T_c. Their full exact
rational operands, contributions, sums, differences and comparisons
are saved in `scripts/heat/h2-endpoint-rayleigh-206.json`.

The standard Rayleigh-Ritz characterization for a real symmetric
matrix implies lambda_min(A(0))<=q_head. The precise imported statement
is Alex Andoni (instructor), Yuanchu Dang and Yunfeng Guan (scribes),
COMS4995-8 Lecture13, 23 February 2021, Section5.3, Theorem15, p5:
https://www.cs.columbia.edu/~andoni/advancedS21/scribes/scribe13.pdf.
It applies because A is real symmetric by L919 and c is a nonzero real
vector; positivity is not a hypothesis. If (4) had upper endpoint <=B,
then the strict uniform margin of L919(3) would fail at zero. The
computed upper endpoint instead exceeds B. A large upper bound cannot
show the actual quotient exceeds B, and a negative lower bound cannot
show a negative actual quotient. Hence both feasibility and obstruction
remain undecided, exactly as the stopping test prescribes.

Run `python3 scripts/heat/h2-endpoint-rayleigh-206.py`. The program
reads only the saved certificate, hashes it, parses exact endpoints,
contracts the five signed terms and independently contracts all nine
matrix entries. The two interval contractions agree because all
anti-diagonal weights have the same sign. It evaluates the five complete
tail bounds (3) in Fraction arithmetic, forms (4), and compares exact
operands with B. All 23 finite checks pass, with zero failures. The
complete contraction, tail, head and comparison fields were inspected.
This finite arithmetic verification inherits analytic inclusion from
L917/L919; it neither verifies the Decimal library nor supplies a new
analytic zero-location premise. No original evidence was overwritten.

## Mathlib

Full matching coverage of this specialized endpoint interval calculation
has not been checked. The Rayleigh-Ritz input is the named theorem cited
above; its Mathlib declaration has not been checked. L917 retains its
conditional arithmetic qualification, and L919 retains the supporting
Jensen coverage and the limits of its formalization assessment. Unknown
coverage is not evidence of absence. This computation is not a Lean proof.
