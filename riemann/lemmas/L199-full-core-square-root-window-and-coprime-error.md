# Lemma 199: full-core square-root window and coprime error

**Hypotheses.** Use the exact integer displacement endpoints b,t of
L191 and the central-strip scales of L198: u=ab, v=cd with ordered
integer factors in [N,2N], |v−2N²|<=K N^(3/2), fixed K>0,
rho=N^(−1/2), and positive a± comparable to N². Let W be a
positive integer with W<=R. The full-core condition means b<=−W
and t>=W, including the zero displacement in this geometric condition
only. It does not assert that zero is allowed in the original sum.

**Conclusion.** Put

A=max(sqrt(a−²+W), sqrt(uN²+W), sqrt(uv+W),
      (W+rho²)/(2rho)),
B=min(sqrt(a+²−W), sqrt(4uN²−W), sqrt(u(v+1)−1−W)).       (1)

If any upper radicand is negative, or A>B, the window is empty.
Otherwise the full-core positive integers m are exactly [A,B]∩Z;
they automatically belong to M_in. Their coprime count is exactly

C_W(u,v)=Σ_(d|u) mu(d)(floor(B/d)−ceil(A/d)+1).             (2)

With D=B−A, this gives

|C_W(u,v)−(phi(u)/u)D| <= 2^omega(u),                     (3)

where omega counts distinct prime factors. For an empty window set
C_W=D=0. For sufficiently large N every nonempty window has
0<=D<1, and hence C_W is either zero or one.

For any family F of ordered quadruples in this strip with nonempty
windows, the summed density main term M_F and error budget E_F obey

M_F=Σ_F (phi(u)/u)D < #F <= E_F=Σ_F 2^omega(u)            (4)

when F is nonempty. Thus subtracting the absolute error in (3) gives
no positive lower bound, even before seeking L198's N³ threshold.
This is a limitation of that error estimate, not a proof that the
actual count is small or that the density approximation is false.

**Proof.**

The endpoints in L191 are integers. Since W is integral, b<=−W
is equivalent to every unrounded lower bound being <=−W, and
t>=W is equivalent to every unrounded upper bound being >=W.
The cutoff |r|<=R is automatic. The remaining conditions are

a−²+W<=m²<=a+²−W,
uN²+W<=m²<=4uN²−W,
uv+W<=m²<=u(v+1)−1−W,
2m rho−rho²>=W,  2m rho+rho²>=W.

The penultimate inequality implies the last since rho>0. Taking
positive square roots gives precisely (1), including its empty cases.
The first pair forces a−<=m<=a+, so m belongs to M_in, as defined
in L194. No additional safe-m condition is omitted. In particular the
strict floor-cell upper edge has retained its integer correction −1.

For a nonempty real interval the count of multiples of d is
floor(B/d)−ceil(A/d)+1, which is nonnegative even if there is no
multiple. Insert the finite identity
1_(gcd(m,u)=1)=Σ_(d|u,d|m) mu(d), proved by prime factorization
in L191, to obtain (2). A closed interval of length D/d has an integer
count differing from D/d by at most one, including a singleton.
Moreover Σ_(d|u) mu(d)/d=Π_(p|u)(1−1/p)=phi(u)/u,
and Σ_(d|u)|mu(d)|=2^omega(u). These identities prove (3).

To bound the length, the floor-cell restrictions alone give, whenever
the full window is nonempty,

D <= sqrt(u(v+1)−1−W)−sqrt(uv+W)
   = (u−1−2W)/(sqrt(u(v+1)−1−W)+sqrt(uv+W))
   <= u/(2sqrt(uv)) = (1/2)sqrt(u/v).

Nonemptiness ensures the numerator is nonnegative and both roots
are at least sqrt(uv). For sufficiently large N, the fixed-K strip
has v>=3N²/2, while u<=4N². Hence D<=sqrt(2/3)<1.
A closed interval shorter than one contains at most one integer.
Since phi(u)/u<=1 and 2^omega(u)>=1, summing proves (4).

## Relation to the threshold and qualifications

If W>=w N^(3/2) for a fixed w>0, a full-core cell has ell=t−b
at least 2W. Restricting also to the totient and opposite-side factor
thresholds in L198, any lower bound of order N³ for these coprime
full-core tuples would suffice for its criterion (with
eta<=min(2w, the chosen totient threshold)). No such lower bound
is established, and full-core cells need not capture all long cells.

L197's localization and aggregate pair bound imply #F=O_K(N³):
every nonempty window yields a real m between a− and a+ and
uv<=m²<=u(v+1)−1, hence u lies in its common localization
interval; the two ordered-pair populations each have size
O_K(N^(3/2)). This argument does not require an integer m to exist.
If M_F were bounded below by a positive multiple of N³, (4) would
force E_F to be at least that order too. Therefore the absolute
Möbius error cannot be treated as o(N³). Neither geometric window
occupancy nor coprimality of its possible unique integer follows
from a real-length density. Both remain arithmetic questions.

## Verification

`python3 scripts/heat/check_full_core_window.py` checks original
endpoint inequalities against (1), the exact divisor count, and (3)
on finite rational-parameter cases including empty and singleton
windows. It is an algebra check, not asymptotic evidence. The proof
above supplies the uniform length bound and error comparison.
No RH conclusion follows.

**Mathlib.** Not checked: availability of a Mathlib theorem for the full statement is unknown. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/
