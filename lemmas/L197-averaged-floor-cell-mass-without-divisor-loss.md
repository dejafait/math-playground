# Lemma 197: averaged floor-cell mass without divisor loss

**Hypotheses.** Use L196's exact central-strip mass, for fixed K>0,
and the inherited positive bounded profile p of L195. In particular,
V=2N², T=K N^(3/2), R=O(N^(3/2)), h comparable to N^(3/2),
and M_in is contained in [a−,a+] with a+−a−=h/(2π) and
positive a± comparable to N², as in L194. All ordered factors are
integers in [N,2N]. The endpoints of each integer displacement cell
are exactly those of L191. Define ell=t−b for b<=t, and ell=0
for an empty cell. All constants may depend on the fixed scale
constants and profiles, and N is sufficiently large.

**Conclusion.** Write P_p(u)=Σ_(ab=u) p(a/N)p(b/N), with the original
ordered factor restrictions. The exact nonnegative central-strip mass

S_mid=Σ_(u,v,m∈M_in: |v−V|<=T, gcd(m,u)=1)
       P_p(u)P_p(v) phi(u)/u² alpha_m ell(u,v,m)             (1)

satisfies

0<=Y_mid^-<=S_mid=O_K(Nh).                                (2)

More specifically, uniformly in u,v in the product support,

Σ_(m∈M_in: gcd(m,u)=1) alpha_m ell(u,v,m)=O(R).             (3)

This removes the N^epsilon loss in L196 by averaging over m.
It does not prove S_mid=o(Nh), Y_mid^-=o(Nh), or a lower bound.

**Proof.**

A nonempty exact cell contains an integer r with |r|<=R and
uv<=m²+r<=u(v+1)−1. Hence

uv−R<=m²<=u(v+1)+R−1.                                    (4)

For two contributing integers m1<m2 in M_in, (4) implies

(m2−m1)(m2+m1)<=u+2R−1.

The right side is O(N²) and m2+m1 is bounded below by a positive
constant times N². Thus the diameter of the contributing m set is
O(1), and it contains O(1) integers. This also covers singleton cells;
if fewer than two m occur the same count is immediate. Each ell is
at most 2R and 0<alpha_m<=C by L194. Restricting this finite set
by gcd(m,u)=1 cannot increase its nonnegative weight. This proves
(3), while leaving the exact cell lengths and coprimality in its left
side. No statistical model of that restriction has been used.

It remains to count factor pairs in aggregate. By L196 every
contributing u lies in the common real interval

U=[(a−²−R)/(V+T+1), (a+²+R)/(V−T)].                       (5)

Indeed m lies between a− and a+, and the denominators are positive.
For clarity, its length can be split as

|U|=(a+²−a−²)/(V−T)
     +[a−²(2T+1)+R(2V+1)]/[(V−T)(V+T+1)].               (6)

The first term is O(h), since a+²−a−²=(a+−a−)(a++a−)
=O(h N²). The second is O_K(N^(3/2)) by direct use of the
stated scales. Thus |U|=O_K(N^(3/2)). The v strip has length
2T=O_K(N^(3/2)). Intersecting either interval with [N²,4N²]
can only reduce its pair count.

For any real interval J of length L>=0, fix an integer a in [N,2N].
The possible b with ab∈J lie in an interval of length L/a; therefore
there are at most L/a+1 of them. Summing over a gives

#{(a,b)∈([N,2N]∩Z)²: ab∈J}<=C(L+N),                    (7)

because a>=N and there are O(N) possible a. Since p is bounded
and positive, (7) also bounds Σ_(u∈J) P_p(u), up to a fixed
constant. Applying it to U and to [V−T,V+T] yields

Σ_(u∈U) P_p(u)=O_K(N^(3/2)),
Σ_(|v−V|<=T) P_p(v)=O_K(N^(3/2)).                        (8)

Reorder the finite nonnegative sum (1), retaining the exact inner
sum over coprime m. For u>=N², phi(u)/u²<=1/u<=N^(-2).
Equations (3), (5), and (8) now give

S_mid<=C R N^(-2)
          (Σ_(u∈U) P_p(u))(Σ_(|v−V|<=T) P_p(v))
     =O_K(RN)=O_K(N^(5/2))=O_K(Nh).

Finally L195's ordered identity and |q/p|<=1 show
Y_mid^-<=S_mid. This proves (2). ∎

## Qualifications and verification

This is an upper bound for the actual coprime sum with its original
floor lengths, not a replacement of those lengths by a mean value.
Enlarging the support to a Cartesian product occurs only in the positive
majorant after (3). The estimate uses aggregate ordered-pair counts
instead of a pointwise divisor bound. After division by Nh it is only
O_K(1), with K fixed. No limit in K or lower-bound conclusion follows.
Negative central-strip decay, exterior signed mass, and RH remain open.

Verification is analytic: exact strict-cell inequality (4), the difference
of squares for m multiplicity, rational identity (6), integer interval
count (7), and finite weighted rearrangement. Formalization requires
those statements with uniform constants and the last normalization;
no numerical inference or external theorem is used.

**Mathlib.** The availability of a Mathlib theorem for this full statement has not yet been established. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/

**Lean proof status.** Not yet formalized or validated. This status does not assert that the mathematical statement is incorrect.

**Lean proof command.**

Not available until a complete Lean proof has been validated.

**Lean proof code.**

Not yet available.
