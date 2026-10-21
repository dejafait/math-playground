# L028 — Scoped difference-of-fourth-powers exclusions

## Hypotheses

Let a,b,c be positive integers with gcd(a,b,c)=1 and p>=11 prime. Bases equal to one are permitted. Consider the ordered equation a^4+b^p=c^4.

The external input is Henri Darmon, *The equation x^4-y^4=z^p*, **C. R. Math. Rep. Acad. Sci. Canada 15 (6) (1993), 286–290, Theorem I**: under the Shimura–Taniyama conjecture, for prime p>=11 the equation X^4-Y^4=Z^p with gcd(X,Y)=1 has no nontrivial integer solution if p is congruent to 1 modulo 4, and has no nontrivial integer solution with Z even. See the [author copy, theorem on manuscript p. 2](https://www.math.mcgill.ca/darmon/pub/Articles/Research/10.Fermat-44p/paper.pdf#page=2); the equation and coprimality convention are on p. 1, and the essential odd/even cases on pp. 3–4. Nontriviality excludes zero coordinates; the source imposes no lower bound greater than one on the bases.

This inspected author copy is internally dated September 9, 2007; equality with the printed version has not been checked. Source scope and proof-case qualifications are recorded in drafts/literature/2026-10-06-fourth-prime-fourth-source-scope.md. The historical modularity hypothesis is discharged by **Breuil–Conrad–Diamond–Taylor, Theorem A**, *On the modularity of elliptic curves over Q: Wild 3-adic exercises*, J. Amer. Math. Soc. **14** (2001), 843–939: every elliptic curve over Q is modular. See [Theorem A, p. 1](https://www.imo.universite-paris-saclay.fr/~christophe.breuil/PUBLICATIONS/STW.pdf#page=1), [DOI](https://doi.org/10.1090/S0894-0347-01-00370-8), and foundations/02-standard-results.md.

For the divisor consequence, let A,B,C,x,y,z be positive integers with x,y,z>2, gcd(A,B,C)=1 and A^x+B^y=C^z.

## Conclusion

There is no positive primitive solution of a^4+b^p=c^4 in either of the following scopes:

1. p>=11 is prime and p is congruent to 1 modulo 4, with no parity restriction on b.
2. p>=11 is prime and b is even, with no congruence restriction on p modulo 4.

Consequently, no original primitive Beal solution satisfies 4|x, p|y, 4|z for such a prime p if either p is congruent to 1 modulo 4 or B is even. Only this ordered divisor pattern is asserted. No unrestricted exclusion for odd b and p congruent to 3 modulo 4, nor for small primes, is obtained here.

## Proof

Suppose a^4+b^p=c^4. A prime dividing a and b divides c^4 and hence c; a prime dividing a and c divides b^p and hence b; a prime dividing b and c divides a^4 and hence a. Each possibility contradicts gcd(a,b,c)=1. Thus the bases are pairwise coprime, by using the equation rather than an assertion about arbitrary triples.

Set (X,Y,Z)=(c,a,b). Rearranging gives

\[
X^4-Y^4=c^4-a^4=b^p=Z^p.
\]

Here gcd(X,Y)=gcd(c,a)=1. All three coordinates are positive and nonzero, so the solution is nontrivial in the source's sense. Also c^4>a^4, whence c>a and X is not equal to Y. No sign is absorbed into a fourth power. If a or b equals one, the corresponding source coordinate remains positive and nonzero and has empty prime support; all preceding coprimality arguments still hold. If c=1, the proposed equation is already impossible, since its left side is at least two. Thus the source covers every possible base-one case.

BCDT Theorem A makes Darmon's stated modularity premise unconditional. In the first scope the prime lower bound and congruence meet the first clause of Theorem I, which contradicts this nontrivial coprime solution. In the second scope Z=b is even and p>=11, so the even-Z clause gives the contradiction independently of the congruence of p. These are separate applications of the cited theorem. Its level-2 even case and level-32 split-Cartan odd case are imported, not independently reproved; the complementary nonsplit case is not used.

For the divisor consequence, suppose 4|x, p|y and 4|z. The selected exponents (4,p,4) lie in L002's set S. Its forward substitution gives positive integer bases

\[
a=A^{x/4},\qquad b=B^{y/p},\qquad c=C^{z/4}
\]

with a^4+b^p=c^4 and gcd(a,b,c)=1. The quotients are positive integers, and the new bases have exactly the prime supports of the old bases, including empty support at base one. The prime p and its congruence are unchanged. Moreover, because y/p is a positive integer, 2 divides b if and only if 2 divides B. Thus the first source clause transfers when p is congruent to 1 modulo 4, and the second transfers when B is even. Each reduced solution contradicts the corresponding exclusion above. No reverse lift to a prescribed original signature is required.

The achieved threshold is zero positive primitive solutions in precisely these two scopes and their stated forward divisor extensions. This is a local assembly of known results, not a new modular theorem or a complete Beal argument. L012's cube boundary and L027's fourth-plus-fourth placement are comparisons, not inputs. Infinitely many residual signatures, the blocked full-range Cao source proof, and the independent mixed-seventh algebra and packet gaps remain unresolved.

### Critical application audit — 2026-10-07, step 063

This audit uses the previously inspected author-copy Theorem I, equation (1) and parity proof cases, with the source-version qualification above. It checks the local application; it does not independently verify the modular proof or identify this copy with the printed version.

For gcd(X,Y)=1, a prime dividing X=c and Y=a would divide c^4-a^4=b^p and hence b, contradicting primitivity. The ordered substitution (X,Y,Z)=(c,a,b) has the correct sign, and the source power base Z is b. Since b^p>0, c>a>=1. Thus c>=2, every coordinate is nonzero, X differs from both Y and -Y, and XYZ=abc>=2. Neither a zero-coordinate exception nor an all-unit exception removes a possible positive solution. The a=1 and b=1 cases meet these same checks; c=1 is impossible. No lower bound greater than one on a or b is needed.

BCDT Theorem A covers every elliptic curve over Q, discharging the modularity premise in both branches without a semistability restriction. The first branch requires p>=11 prime and p congruent to 1 modulo 4; the second requires p>=11 prime and Z=b even. Neither is used as a converse. As applicability controls, p=11 with odd b meets neither branch, p=13 meets the first regardless of b, and p=5 meets neither because of the lower bound. These controls assert no existence in uncovered cases. If b=1, only the first branch can apply.

For the transfer, 4 and p belong to L002's S, and x/4, y/p and z/4 are positive integers. The identities (A^(x/4))^4=A^x, (B^(y/p))^p=B^y and (C^(z/4))^4=C^z verify the ordered equation. A prime common to a,b,c would, by L002, divide A,B,C, contradicting their gcd-one hypothesis. Put k=y/p>=1. If B is even then B^k is even; if B is odd then the product of k odd factors is odd. Hence b is even exactly when B is even, including B=1. No parity hypothesis on A or C or reverse lift is required.

All written source and transfer premises pass. No mathematical repair, additional signature exclusion or new external theorem is supplied by this audit. The sole direct local lemma input remains L002; foundations 01 and 02 supply the existing convention and BCDT citation. The full Beal gap, odd b at p congruent to 3 modulo 4, small primes outside this import, and the independent mixed-seventh assumptions remain unresolved here.

## Mathlib

Full matching coverage for Darmon's theorem, BCDT and this application: **not checked**. Supporting power, prime-support and coprimality declarations were not checked. No absence claim, formal-verification claim or independent modular computation is asserted. The external nonexistence results are cited precisely, and the specialization and forward transfer are proved above.
