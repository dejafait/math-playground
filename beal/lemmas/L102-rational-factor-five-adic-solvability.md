# L102 — Primitive five-adic points in both rational-factor systems

## Hypotheses

Use the full integral forms Q and H of L095, with Q(m,n)=3m²+mn+n².
All local variables lie in Z_5. The systems to be tested are

    I:  C=5m+u^5,       H(m,C)=a³;
    II: C=m+5^10 u^5,  H(m,5C)=5^11 a³.

In each, reconstruct A=ma and B=Q(m,dC)u with d=1 or 5 respectively.
Require every coordinate m,u,a,A,B,C nonzero, m,C units, and the
reconstructed triple locally primitive (at least one base a unit).
Real positivity and coprimality at other primes are outside this scope.

## Conclusion

Both complete systems admit such points, with m=u=1. In I one can take
C=6, B=45 and a congruent to 1 modulo 5; the reconstructed valuations
(v5(A),v5(B),v5(C)) are (0,1,0). In II take C=1+5^10 and
B=3+5C+25C², with a congruent to 2 modulo 5; all three bases are units.
Both points satisfy A³+B^5=C^11 with one common tuple per system.

Thus standalone five-adic nonexistence cannot exclude either system.
This does not supply integer points, global compatibility, a classification
of local valuations or an exclusion of the rational-factor branch.

## Proof

Import the strict Hensel criterion from Pete L. Clark, *Algebraic Number
Theory II: Valuations, Local Fields and Adeles*, Theorem 1.79, printed
p.58 of the inspected 161-page version, [author notes](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf).
For f in Z_5[X] and an integral seed b, v5(f(b))>2v5(f'(b)) gives an
exact root a with v5(a-b)>v5(f'(b)). The version and hypotheses are
recorded in `foundations/17-local-power-hensel-inputs.md`.
This standard result is cited, not reproved. Its application here is
needed because a finite residue seed alone is not an exact point.

For I fix m=u=1 and C=6. Then Q(1,6)=45. L095 identity (4) gives

    H(1,6)=6^11−45^5=178268931=:N_I.

For f_I(X)=X³−N_I, the seed 1 has error −178268930 of exact five-adic
valuation one (N_I is 6 modulo 25), and f_I'(1)=3 is a unit. Hensel
therefore gives a_I in Z_5 with a_I³=N_I and a_I=1 modulo five.
All of m,u,a_I are nonzero units; C is a unit and B=45 has valuation
one. Keeping these same fixed coordinates, set A=a_I. The two defining
equations and A³+B^5=C^11 follow from the displayed identity. Hence the
point is locally primitive; indeed A and C are units.

For II fix m=u=1 and C=1+5^10. Write n=5C and
q=Q(1,5C)=3+5C+25C². Then n−5=5^11. Substituting these exact
integers into L095 identity (4) gives

    H(1,5C)=(5C)^11−q^5(5C−5)
            =5^11(C^11−q^5).

Define the integer N_II=C^11−q^5. This identity proves divisibility
by 5^11 for this fixed tuple before any division. Since Z_5 is an
integral domain, H(1,5C)=5^11 a³ is equivalent, for these fixed
coordinates, to a³=N_II. No general normalization in m or u is assumed.
Now C=1 modulo 125, q=33 modulo 125 and 33^5=18 modulo 125. Hence
N_II=108 modulo 125, in particular N_II=3 modulo five.
For f_II(X)=X³−N_II, seed 2 has error −100 modulo 125 and thus
valuation two. Its derivative is 12, a unit. Strict Hensel applies
(2>0) and yields a_II=2 modulo five with a_II³=N_II.

Keep this same C,q,m,u, set A=a_II and B=q. Then A,B,C are units:
a_II=2, q=3 and C=1 modulo five. In particular every required
coordinate is nonzero and the triple is primitive locally. The exact
normalization identity proves the system-II H equation with its full
5^11 factor, while the definition of N_II proves A³+B^5=C^11.
Equivalently the reconstruction via L095 cancels exactly 5^11 in an
equality in the domain Z_5, without treating that factor as a unit.

The ready EXPLORE assessment is
`drafts/literature/2026-10-19-rational-factor-five-adic-feasibility.md`.
This is a local reproduction of assessed Hensel methods, not a claim of
new mathematics beyond the checked sources. Other-prime lifts and L101
are contextual only. In particular the I witness C=6 fails the global
restriction at three and is used only at five. Both integer systems and
other algebra types remain unresolved. Independent critical review is
recorded below.

Exact supporting arithmetic: run
`python3 scripts/rational-factor/check_five_lifts.py`.
All 24 assertions pass; the complete values, errors, valuations, full
scale identities and reconstruction checks are in
`scripts/rational-factor/five-lifts-certificate.json`.
Both full system records and every assertion were inspected. These
finite checks support the identities; the cited Hensel theorem proves
exact existence. The integer seeds themselves are not claimed solutions.

### Independent critical audit — 2026-10-19

Verdict: **PASS without correction** under the unchanged EXPLORE
assessment `drafts/literature/2026-10-19-rational-factor-five-adic-audit.md`.
This validates the two stated local points only. The only direct lemma
input remains audited L095; Clark Theorem 1.79 is imported by the precise
citation above. No original positive-integer converse is applied over
Z_5: the integral polynomial identity and direct reconstruction suffice.

For I, direct evaluation of the full H gives 178268931 and Q=45.
The exact error is −178268930=5(−35653786), with the latter factor
not divisible by five. The derivative is 3. Thus the strict Hensel
bound is 1>2·0, and its nearby root is congruent to 1 modulo five.
Consequently a and A=a are nonzero units. With the fixed m=u=1,
C=6 and B=45, both system equations hold and
A³+B^5=178268931+45^5=6^11. The valuation triple is exactly
(0,1,0), so allowing the nonunit B loses neither nonvanishing nor
local primitivity. The integer seed is not the exact root.

For II, independent evaluation gives

    C=9765626, n=48828130, q=2384186328125033,
    N=C^11−q^5=36395979004072395449078215217656724622251663633857348983.

Here n−5=48828125=5^11. Identity (4) in L095, with m=1, proves
H(1,n)=5^11 N as an equality of integers. In particular the quotient
is integral before considering any p-adic root. Multiplication by the
nonzero 5^11 is injective in Z_5, so for this fixed tuple the second
system equation is equivalent to a³=N. No inverse of 5^11 in Z_5
or general divided system in varying m,u is used.

The complete residue calculation modulo 125 is
(C,q,q^5,N,2³−N)=(1,33,18,108,25). Thus the last entry is divisible
by 25 but not by 125, giving exact error valuation two. The derivative
12 is a unit, so 2>2·0 and Clark gives an exact root congruent to 2
modulo five. Therefore A=a, B=q and C are all units, as are m,u;
every required coordinate is nonzero. Retaining this same C,q,m,u
throughout yields both the full scaled H equation and
A³+B^5=N+q^5=C^11. Cancellation changes no coordinate.

Independent supporting verification is reproducible with
`python3 scripts/rational-factor/audit_five_lifts.py`. It does not
import or run the original generator. A multinomial expansion checks
all complementary polynomial coefficients; Horner evaluation followed
by exact quotient and remainder independently recovers H and N.
Divisibility and nondivisibility check the exact valuations. All fields
of both original records and all 24 named assertions match, including
their counts, empty failure list and schema. The assigned A valuations
are justified by the preceding Hensel argument, not by evaluating an
unknown p-adic root or equating it with its seed. The full audit
certificate, including the original certificate hash, is
`scripts/rational-factor/five-lifts-audit-certificate.json`:
40/40 checks pass, with no failures. Both complete reconstructed records
and every assertion were inspected.

This closes the pending correctness audit, not a global Diophantine
gap or a novelty claim. In particular the I witness is not admissible
at three, and no common tuple across different primes is constructed.
Standalone exclusion at five remains retired; compatibility with a
global primitive integer solution and other algebra factors is unresolved.

## Mathlib

Full matching theorem for these systems and the supporting Hensel
declarations: **not checked**. Unknown coverage is not evidence of absence.
