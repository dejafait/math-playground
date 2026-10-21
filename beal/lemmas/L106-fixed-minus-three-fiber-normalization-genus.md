# L106 — The fixed minus-three marked fiber curve has genus 75

## Hypotheses

Put phi(T)=(3T²+T+1)^5(1−5T), and fix the abstract quadratic field
K=Q(w), w²=−3. Define F0,F1 in Q[r,u,v] uniquely by

    phi(u+vw)−phi(r)=F0(r,u,v)+w F1(r,u,v).

Let X be the open subscheme F0=F1=0 on which

    D=v*((r−u)²+3v²)*phi(r)*(phi(r)−1)

is invertible. Let C be the reduced closure of X in projective
three-space, and let Ctilde be its normalization. Equivalently, close
only this open locus, rather than keeping every component of an
unsaturated homogenized pair of equations. Genus here means geometric
genus of this proper normalized curve.

No integer solution, positivity, prescribed component type of the
remaining degree-eight algebra, or rational-point existence is assumed.

## Conclusion

X is a smooth geometrically integral curve over Q, finite étale of
degree 990 over U=P¹_Q minus {0,1,infinity}, by s=phi(r).
Ctilde is geometrically connected and has genus 75. There is exactly one
geometric curve component of the stated reduced closure.

Its rational points on X correspond precisely to a rational root r of
phi(T)−s, together with a chosen root a in K\Q of that polynomial,
where s is rational and s is neither 0 nor 1. The other chosen root is
the conjugate b of a. The three roots are disjoint. There are two
markings for each such rational-root/quadratic-factor pair. The
involution v -> −v exchanges them. The genus assertion concerns this
fixed-field marked curve, not its unmarked quotient.

This supplies geometry for the minus-three branch only. It neither
classifies rational points nor solves either L095 integer system.
The separate critical audit below confirms the result without correction.

## Proof

### The exact model and marking

Write phi(T)=sum c_i T^i. Explicit equations, without a choice of complex
embedding, are

    F0 = sum_i c_i sum_{0<=j<=i, j even}
                    binom(i,j) u^(i−j) v^j (−3)^(j/2) − phi(r),
    F1 = sum_i c_i sum_{0<=j<=i, j odd}
                    binom(i,j) u^(i−j) v^j (−3)^((j−1)/2).

Over Q, linear independence of 1,w shows that F0=F1=0 is equivalent
to phi(a)=phi(r), with a=u+vw. Conjugation gives phi(b)=phi(r)
for b=u−vw. The condition v!=0 says a is not rational and generates K;
(r−a)(r−b)=(r−u)²+3v² excludes collision with r. Conversely any
specified nonrational root a in K has unique u,v in Q with a=u+vw;
v!=0 and its conjugate is the other root. A rational root cannot equal
a or b. The minimal polynomial (T−a)(T−b) is a rational quadratic
factor. Away from the branch values the three simple roots split off
a rational factor and this quadratic factor, leaving the entire étale
degree-eight complement. No field decomposition of that complement
is imposed. Reversing the chosen embedding sends v to −v and fixes r,u.

Over any algebraically closed characteristic-zero field containing w,
make the invertible linear change

    a=u+vw, b=u−vw;
    u=(a+b)/2, v=(a−b)/(2w).

The equations become exactly phi(a)=phi(b)=phi(r), since their two
linear combinations are F0+wF1 and F0−wF1. Invertibility of D becomes
pairwise distinctness of r,a,b and s!=0,1. Thus X after this base change
is the ordered three-distinct-root fiber product over U. This is a
scheme isomorphism, not just a correspondence on rational points.

The root cover phi:P¹ -> P¹ has degree eleven. On U it is finite étale;
all its roots have finite coordinate when s is finite. Its triple fiber
product is finite étale, and the pairwise-distinct subcover is finite
étale too: equality and inequality of two sections are open and closed
in an étale fiber product. Each geometric fiber has 11*10*9=990
points. These properties descend from the displayed base change to Q.
In particular X is smooth of pure dimension one. The computation is a
quadratic twist of the ordered cover, not the cover obtained by merely
forgetting the order of a,b.

### Branch values and geometric monodromy

Exact differentiation gives

    phi'(T)=−165T²(3T²+T+1)^4.

This calculation verifies the actual branch data for this model; it is
not a reproof of a covering or genus theorem. The quadratic q=3T²+T+1
has discriminant −11, two distinct roots, neither zero nor 1/5.
At s=0 its roots have multiplicity five each, and 1/5 has multiplicity
one. At T=0, phi(0)=1 and phi(T)−1 begins −55T³, so the ramification
index is three. No other point above 1 is critical: the only other
finite critical points are the roots of q, whose images are zero.
Hence the remaining eight roots above 1 are simple. Infinity has index
eleven because phi is a polynomial with leading coefficient −1215.
There are no other critical values. The branch permutations therefore
have cycle types

    0: (5,5,1),     1: (3,1,1,1,1,1,1,1,1),     infinity: (11).

The two critical roots' quadratic field Q(sqrt(−11)) is distinct from
the fixed marking field K; it does not change the preceding twist.

Work over C. The source of the eleven-sheeted root cover with the
branch preimages removed is connected, so its monodromy group G is
transitive. A transitive group of prime degree is primitive: translates
of a block partition the eleven letters into equally sized blocks,
whose size must divide eleven. The permutation above 1 is an actual
3-cycle with eight fixed letters. Jordan's theorem therefore gives
A_11 contained in G, by Gareth A. Jones, *Primitive permutation groups
containing a cycle*, arXiv:1209.5169v1, Theorem 1.1, p.1
[primary PDF](https://arxiv.org/pdf/1209.5169v1). This is the prime-cycle
clause, with 3<=11−3, not the later classification theorem. We import
Jordan's theorem without reproof. All three branch types are even;
loops about the punctures generate the fundamental group of the
three-punctured sphere, so G is contained in A_11. Thus G=A_11.

A_11 is transitive on ordered triples of distinct letters. Indeed any
bijection between the two triples extends to a permutation of eleven
letters; if it is odd, compose with a transposition of two of the eight
letters outside the target triple, making it even without changing
that triple. The triple cover is consequently connected. Here we use
the component/orbit correspondence for finite étale covers, Stacks
Project Theorem 58.6.2 [tag 0BND](https://stacks.math.columbia.edu/tag/0BND),
and its complex-cover realization from Milne, *Lectures on Étale
Cohomology*, v2.21 (22 March 2013), Theorems 3.1 and 21.3,
pp.27,130–131 [author PDF](https://www.jmilne.org/math/CourseNotes/LECc.pdf).
These theorems apply to the cover over U, not to a singular closure.
A connected smooth curve over an algebraically closed field is
irreducible: its regular local rings have one minimal prime, so distinct
irreducible components cannot meet and would disconnect the curve.
Thus X is geometrically integral. Its reduced closure is geometrically
integral also; closure of this irreducible open adds no other component.
Normalization gives its unique smooth proper model in characteristic
zero, with the same function field. It is geometrically connected and
has full constant field Q, since geometric integrality excludes a
nontrivial algebraic extension of Q in its function field.

### Complete cycle counts and genus

Local analytic continuation around a puncture permutes the 990 ordered
triples by applying the root permutation in each coordinate. A cycle
of length e gives a punctured disk cover whose completion is locally
z -> z^e, and hence contributes e−1 to ramification. This follows by
the classification of connected finite covers of a punctured complex
disk (its fundamental group is Z). It applies to the smooth proper
normalization; singularities of a chosen closure do not supply extra
branch contributions.

For the order-five permutation, a fixed triple would require three
fixed root letters, whereas there is only one. All 990 triples
therefore belong to cycles of length five: there are 198 cycles and
ramification sum 990−198=792. For the order-three permutation, exactly
8*7*6=336 triples are fixed. The other 654 triples form 218 cycles of
length three. The cycle count is 554 and ramification sum 436. The
11-cycle fixes no triple, so it has 90 cycles of length eleven and
ramification sum 900. These arguments exhaust every label, regardless
of the simultaneous choice of branch representatives.

Apply Riemann–Hurwitz over C to the smooth proper normalization and its
finite degree-990 map to P¹. Characteristic zero makes all ramification
tame. The hypotheses and formula are Stacks Project Lemmas 53.12.2 and
53.12.4 [tag 0C1B](https://stacks.math.columbia.edu/tag/0C1B). They give

    2g−2 = −2*990 + 792 + 436 + 900 = 148,
    g = 75.

Genus is unchanged by extension of the full constant field, by Stacks
Lemma 53.8.2 [tag 0BY6](https://stacks.math.columbia.edu/tag/0BY6).
Normalization and reduction preserve the geometric-genus interpretation,
Stacks Lemma 53.18.2 [tag 0CE0](https://stacks.math.columbia.edu/tag/0CE0).
This is not the arithmetic genus of an unsaturated intersection.

### Exact arithmetic evidence and limits

Run `python3 scripts/global-fiber-genus/certify.py`. Its full certificate
is `scripts/global-fiber-genus/certificate.json`: polynomial coefficients,
all 990 ordered labels, each induced permutation, all disjoint cycles,
all cycle closures and full-partition checks. The run passes 857 checks
with no failures, uses 990 labels against the cap 1000, and gives the
complete ramification sum 2128. The polynomial coefficients are

    [1,0,0,−55,−165,−594,−1100,−2145,−2475,−2970,−1782,−1215]

in ascending order. The elementary counts above independently account
for every induced cycle. The three stored root permutations are
representatives of individual conjugacy types, not a claimed branch
generator tuple with product one. Transitivity is proved using the
actual geometric group, not inferred from those representatives.

The continuation test succeeds: model, unique geometric component,
and exact genus are obtained within the cap. High genus alone does
not exclude rational points. Even rational points of X must separately
satisfy L095's simultaneous powers, gcd and positivity conditions to
produce a primitive integer solution. The minus-eleven quadratic,
other global factors, and every other residual signature remain open.

### Independent critical audit, 2026-10-20

The approved audit checks the entire assertion, including its scheme
structure, rather than treating the numerical genus as its premise.
It finds no mathematical correction.

For the model, adjoining w gives an invertible linear coordinate change:
the inverse uses only the nonzero constants 2 and w. The two defining
equations are equivalent as ideals to phi(a)−phi(r) and phi(b)−phi(r),
since their change-of-basis determinant is −2w. The inverted product D
is, up to a nonzero constant, the product of all three root differences
and s(s−1). Inverting that product inverts each factor. Consequently the
base-changed scheme is exactly the distinct ordered-triple subcover,
with no diagonal or nilpotent component retained. This verifies the
scheme comparison, not merely a set-theoretic implication. Over Q the
fixed basis (1,w) makes a=u+vw unique, and v!=0 makes Q(a)=K.
The involution exchanges the two roots of the same quadratic direct
factor. Neither a variable quadratic field nor the critical-point
field Q(sqrt(−11)) is substituted for K.

The root cover is finite over the affine s-line because its leading
coefficient −1215 is an invertible rational constant; its removed
critical locus is exactly the preimage of 0 and 1. Its degree is eleven.
The discriminant −11 of q and q(1/5)=33/25 exclude collisions in the
zero fiber. At one, T=0 has exact order three and no other critical point
lies over one. The polynomial has a unique pole of order eleven.
These facts verify every actual root-cover branch type. Connectedness
comes from the connected punctured source P¹(C), not the stored
permutations. Prime degree implies primitivity and the actual 3-cycle
has eight fixed letters, meeting Jones Theorem 1.1. The three actual
branch loops generate monodromy and are even, proving equality with
A_11. Adjusting parity on two unused letters proves the needed triple
transitivity. This checks all hypotheses of the cover comparison and
orbit statements cited above; no unproved branch-generator relation
for the certificate representatives is used.

Over C the triple subcover is connected and smooth, hence integral.
Faithfully flat extension from Qbar to C detects any geometric
disconnection or extra component, so geometric integrality holds over
Q. The reduced projective closure has the same function field and a
dense geometrically integral open. It is an integral projective curve;
in characteristic zero its function field is geometrically integral,
so the smooth proper model of that function field is geometrically
integral as well. Normalization of the closure is that model. In
particular its global regular functions form a finite extension of Q
inside the function field. A nontrivial such extension is separable
and would split after extension to Qbar, contradicting geometric
integrality. Thus H0 is exactly Q. This verifies the full-constant-field
premise for genus base change. The rational function s extends to a
nonconstant morphism from the smooth proper model to P¹, finite of
degree 990. Its restriction over U is the original finite étale cover,
so no ramification occurs away from the three punctures. At those
punctures the cycle-completion argument accounts for every point on
the normalization, including infinity. Characteristic zero supplies
tameness. The cited Riemann–Hurwitz and genus-base-change statements
therefore apply to this model.

For the finite evidence, `python3 scripts/global-fiber-genus/audit.py`
reads every value of the original certificate and imports no producer
code. It reconstructs the polynomial by a multinomial expansion,
checks the complete label list, verifies the action on every label
directly, and checks every edge of every stored cycle together with
the full disjoint partition and branch conjugacy types. It reconstructs
all 857 original check names and truth values and verifies the complete
top-level schema and equation strings. Its 6,822 checks pass with no
failures. The full independent report is
`scripts/global-fiber-genus/audit-certificate.json`; the original input's
SHA-256 is
`63295752a6ba4f0969d229038c7109e6cfa4c5869250f39f5e655604592352df`.
The actual degree is 990 against the required cap 1000. All three cycle
histograms, ramification sums 792,436,900, total 2128 and 2g−2=148
are confirmed. This full replay, not a preview of a JSON field, checks
the finite evidence. The script does not replace the geometric
arguments or independently prove the imported general theorems.

The continuation test passes without changing the argument, its scope
or mathematical inputs. This is verification of an existing local
specialization, not an additional theorem beyond the sources checked.
No rational points have been classified and no L095 integer system or
other residual signature has been excluded.

## Mathlib

Full matching genus computation and supporting monodromy/genus coverage
in Mathlib were not checked. The named primary inputs above are imported
as mathematical theorems; no Lean verification or independent proof of
Jordan, comparison of covers, or Riemann–Hurwitz is claimed.
