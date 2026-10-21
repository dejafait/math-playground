# L032 — Unconditional square-coordinate reduction for ordered (3,4,11)

## Hypotheses

Let A,B,C be positive integers with gcd(A,B,C)=1 and A^3+B^4=C^11. Bases equal to one are allowed. All conclusions below are necessary conditions; there is no asserted solution or exclusion of this signature.

The external input is Nuno Freitas, Bartosz Naskręcki and Michael Stoll, *The generalized Fermat equation with exponents 2, 3, n*, **Compositio Mathematica 156 (2020), no. 1, 77–113**, [DOI](https://doi.org/10.1112/S0010437X19007693), [author final PDF](https://www.mathe2.uni-bayreuth.de/stoll/papers/genfermat-final.pdf). Locators below are printed author-PDF pages: Lemma 2.3 (pp. 5–6), Proposition 2.4 (pp. 6–7), Tables 1–3 (pp. 9–10), Theorem 5.1 (pp. 16–17), Lemma 5.2 (pp. 18–19), Section 7.1 (pp. 23–24), and Lemma 7.3 (p. 26). The assessment identifies the author publication entry's 2019-06-13 revision; the PDF itself is dated June 10, 2019. The corrected final tables, also recorded in arXiv:1703.05058v3, are used.

## Conclusion

Put X=B^2, Y=A, Z=C and let F be the Frey curve

    F: v^2=u^3+3Au-2B^2.

There is d in {±1,±2,±3,±6} such that its quadratic twist F^(d) determines a rational point P on X_E(11), with a symplectic 11-torsion identification, for some

    E in {54a1,96a1,864a1,864b1,864c1}.

Here X_E is the source's modular-curve twist, not the coordinate X=B^2. Its j-image satisfies

    j(P)=1728 A^3/C^11,  1728-j(P)=1728 B^4/C^11,
    0<j(P)<1728,

and the original integer square condition X=B^2 remains required. The complete retained necessary residue cases are the following eight branches, with B^2 residues stated modulo 9. In every row 3 does not divide B.

| E | (i2,i3) in source tables | B parity | A mod 8 | A mod 3 | B^2 mod 9 | permitted d |
| --- | --- | --- | --- | --- | --- | --- |
| 54a1 | (1,7) | odd | 7 | 1 | 1 or 4 | 1,-3 |
| 96a1 | (5,1) | odd | 2 | -1 | 1 | 6 |
| 864a1 | (2,7) | even | 3 | 1 | 1 or 4 | ±2,±6 |
| 864a1 | (2,7) | even | 7 | 1 | 1 or 4 | ±2,±6 |
| 864b1 | (2,5) | even | 1 | 0 | 1 or 7 | ±1,±3 |
| 864b1 | (2,5) | even | 5 | 0 | 1 or 7 | ±1,±3 |
| 864b1 | (6,5) | odd | 6 | 0 | 1 or 7 | ±2,±6 |
| 864c1 | (5,5) | odd | 2 | 0 | 1 or 7 | ±2,±6 |

For 54a1, C is even and 3 does not divide C. For 96a1, 3 divides C and C is odd. For the other three labels gcd(C,6)=1. These are necessary statements about the source reduction, not a sufficient parametrization of solutions. All five labels survive these filters; the required zero-label or zero-integer-solution threshold is not met.

## Proof

### Applicability and modular location

The substitution gives X^2+Y^3=Z^11 exactly. All three coordinates are nonzero and positive. A prime divides X,Y,Z simultaneously if and only if it divides B,A,C simultaneously, since prime divisibility is unchanged by squaring B. Hence gcd(X,Y,Z)=1. A prime dividing any two coordinates divides the third by the equation, so the pairwise coprimality used in the source also holds. This argument covers units and does not invoke any independent unit-base exclusion.

The Frey discriminant is -1728 C^11, which is nonzero, and its j-invariant is 1728 A^3/C^11 (source equation (2.2), p. 5). Proposition 2.4 supplies residual irreducibility at 11; Lemma 2.3 supplies the quadratic twist with d in the stated set; Theorem 5.1 then supplies the eight symplectic modular twists at 11 modulo 24:

    27a1,54a1,96a1,288a1,288a2,864a1,864b1,864c1.

We import these theorems rather than reprove modularity, level lowering or the rational-isogeny analysis. The quadratic twist d of F and the distinction between X_E and X_E^- are different operations. Section 4 (p. 11) defines the latter using the Weil-pairing multiplier. The eight labels in the displayed Theorem 5.1 row use X_E, not X_E^-. In particular 288a2 records a different symplectic type obtained through its 2-isogeny to 288a1.

Section 7.1 excludes the three CM labels for nontrivial primitive solutions without GRH. Its covering-collection argument uses elliptic curves over a cubic field, of ranks one for d=-1 and two for d=-3, and cited Magma elliptic Chabauty. The complete relevant j-reconstruction leaves only zero-coordinate solutions. Our triple has no zero coordinate, so the remaining five labels are exactly those in the conclusion. This published computation is imported, not independently rerun. The ranks and Chabauty computation here are separate from Section 7.2's GRH-dependent degree-36 class groups; neither Table 5 nor Lemma 7.7 nor Theorem 7.1 is a premise.

### Every source local residue case

Use source a=X=B^2 and b=Y=A. The following tables list every residue subrow in Tables 1 and 2, expanding signs when they give different residues. Only columns relevant to this filter are repeated; source conductor and j columns remain part of the cited input. All residues are displayed as nonnegative representatives. Let D_o={±1,±3}, D_e={±2,±6}, D_all=D_o union D_e.

For Table 1 the square residue set modulo 4 is {0,1}; in addition an odd B has B^2=1 modulo 8. The last source case is already impossible regardless of being a square.

| i2 | X mod 4 | A mod 8 | source d | Square/source filter |
| --- | --- | --- | --- | --- |
| 1 | 1 | 7 | 1,-3 | retain |
| 1 | 3 | 7 | -1,3 | nonsquare |
| 2 | 0 | 1 | D_o | retain |
| 2 | 0 | 5 | D_o | retain |
| 2 | 0 | 3 | D_e | retain |
| 2 | 0 | 7 | D_e | retain |
| 3 | 2 | 1 | D_o | nonsquare |
| 3 | 2 | 5 | D_o | nonsquare |
| 3 | 2 | 3 | D_e | nonsquare |
| 3 | 2 | 7 | D_e | nonsquare |
| 4 | 1 | 0 | -2,6 | square-compatible; CM only after Table 3 |
| 4 | 3 | 0 | 2,-6 | nonsquare |
| 5 | 1 | 2 | D_e | retain |
| 5 | 3 | 2 | D_e | nonsquare |
| 6 | 1 | 6 | D_e | retain before symplectic test |
| 6 | 3 | 6 | D_e | nonsquare |
| 7 | 1 | 4 | -2,6 | source impossible |
| 7 | 3 | 4 | 2,-6 | source impossible and nonsquare |

For Table 2 the square residue set modulo 9 is {0,1,4,7}, obtained by squaring residues 0 through 8. The CM references below use Table 3 and the already imported Section 7.1, not a local nonsquare claim.

| i3 | X mod 9 | A mod 3 | source d | Square/global filter |
| --- | --- | --- | --- | --- |
| 1 | 1 | 2 | -3,6 | retain |
| 1 | 8 | 2 | 3,-6 | nonsquare |
| 2 | 0 | 1 | D_all | CM only |
| 2 | 0 | 2 | D_all | CM only |
| 3 | 3 | 1 | D_all | nonsquare |
| 3 | 6 | 1 | D_all | nonsquare |
| 4 | 3 | 2 | D_all | nonsquare |
| 4 | 6 | 2 | D_all | nonsquare |
| 5 | 1 | 0 | D_all | retain |
| 5 | 8 | 0 | D_all | nonsquare |
| 5 | 2 | 0 | D_all | nonsquare |
| 5 | 7 | 0 | D_all | retain |
| 6 | 4 | 0 | D_all | CM only |
| 6 | 5 | 0 | D_all | nonsquare |
| 7 | 1 | 1 | D_all | retain |
| 7 | 8 | 1 | D_all | nonsquare |
| 7 | 4 | 1 | D_all | retain |
| 7 | 5 | 1 | D_all | nonsquare |
| 8 | 2 | 1 | D_all | nonsquare |
| 8 | 7 | 1 | D_all | CM only |

To combine them we use precisely Table 3: i2=1 pairs only with i3 in {4,7}, giving 54a1; i2 in {2,6} pairs with i3 in {2,6,8}, {3,5}, {4,7}, giving respectively 288a1,864b1,864a1; i2 in {3,5} pairs with i3=1 or i3 in {3,5}, giving respectively 96a1 or 864c1; i2=4 pairs only with i3 in {3,5}, giving 27a1. Every other intersection is empty in the source. Intersect the permitted d sets as well. For example, the retained 96a1 case intersects D_e with {-3,6}, leaving only d=6. CM-only intersections disappear by Section 7.1, including the square-compatible i3=8 subrow; thus every remaining B is prime to 3.

There is one further essential symplectic filter. The nonzero squares modulo 11 are {1,3,4,5,9}, so 2 is a nonsquare and 3 a square. Lemma 5.2 says that i2=2 with d in D_o, or i2=6, is symplectic for 864b1 and anti-symplectic for 864a1. Conversely i2=2 with d in D_e is symplectic for 864a1 and anti-symplectic for 864b1. The surviving i2=5 cases are symplectic for both 96a1 and 864c1. Thus the coarse Table 3 possibility (i2,i3)=(6,7) for 864a1 is excluded, and its i2=2 possibilities require A=3 or 7 modulo 8. For 864b1, i2=2 requires A=1 or 5 modulo 8, whereas i2=6 remains permitted. The exclusive signs are already determined on inertia in the proof of Lemma 5.2. Its allowance for an unramified quadratic twist cannot reverse those signs, since such a twist is trivial on inertia. Thus an actual global symplectic identification must pass this test. No extra sign restriction at 3 is inferred; the source's corresponding symplectic distinction there collapses when 3 is a square modulo 11. This produces exactly the eight necessary branches in the conclusion.

The restrictions on C follow directly from the original equation and these residues. In the 54a1 case, odd B gives B^4=1 modulo 8 and A^3=7 modulo 8, so C is even; modulo 3 the sum is 2, so C is prime to 3. In the 96a1 case B^4=1 modulo 3 and A^3=-1 modulo 3, so 3 divides C; A even and B odd make C odd. In all other retained cases A^3+B^4 is odd and nonzero modulo 3, proving gcd(C,6)=1.

### Exact retained j-domains and full square constraint

Our primitive integer triple is also primitive over Z_2, and the displayed j identities give exactly the source definition of a 2-adically good j-invariant (p. 23). Thus Lemma 7.3 applies. Its proof uses only Table 1 and Lemma 5.2; the following Selmer computation, which assumes GRH, is not used. For completeness its domains before our square filter are:

    54a1: {2^-5 t^-11 : t in Z_2},
    96a1: 960+2048 Z_2, -64+2048 Z_2, -512+2048 Z_2,
    864a1: {1728-1024 t^2}, {1728+3072 t^2},
    864b1: {1728-3072 t^2}, {1728+1024 t^2}, 512+2048 Z_2,
    864c1: 960+2048 Z_2, -64+2048 Z_2, -512+2048 Z_2.

All braces here use t in Z_2. For 54a1, t=0 denotes the point at infinity and is excluded for our finite j. The domains 960+2048 Z_2 and -64+2048 Z_2 come from i2=3, with A=5 and 1 modulo 8 respectively; that entire row has X=2 modulo 4 and is incompatible with X=B^2. Hence **both 96a1 and 864c1 retain only -512+2048 Z_2**. The remaining displayed domains for the other labels are retained as necessary domains, without a claim that every value comes from a rational point.

The four near-1728 domains correspond in order to the even-B branches: 864a1 with A=3,7 modulo 8, and 864b1 with A=1,5 modulo 8. They can be sharpened without dropping the square condition. If k=v_2(B)>=1, C is odd and

    v_2(1728-j)=6+4k.

In each near-1728 domain the coefficient has valuation 10, so 10+2v_2(t)=6+4k and therefore v_2(t)=2k-2 is even and nonnegative. Also t is nonzero since B>0. This is necessary only, not a sufficient test for a fourth power. In the 54a1 domain v_2(j)=6-11v_2(C)=-5-11v_2(t), so v_2(t)=v_2(C)-1. The odd-B 864b1 branch retains 512+2048 Z_2. The full global constraint is still the exact identity (1728-j)C^11/1728=B^4 with positive integers A,B,C satisfying the hypotheses, not merely these valuations or domains. The inequalities 0<j<1728 follow from A^3,C^11>0 and B^4=C^11-A^3>0.

### Verification, relevance and limitations

The complete finite residue certificate is [scripts/three-four-eleven-reduction/filter-certificate.json](../scripts/three-four-eleven-reduction/filter-certificate.json), reproduced with `python3 scripts/three-four-eleven-reduction/check_filter.py`. It retains all 18 Table 1 and 20 Table 2 residue subrows and enumerates B modulo 36 and A modulo 24, enough for every displayed residue and d intersection. It applies the cited CM and symplectic tests and checks the complete eight-branch list. Five labels remain, versus the zero needed for a label-based exclusion; there are no finite-filter failures. Source comparison verifies the transcription; the script verifies elementary filtering, not the source's modularity, Chabauty computations, the existence of local modular points or a rational-point classification.

The independent critical audit on 2026-10-07 checked all 18/20 subrows against the primary Tables 1–2, all empty and nonempty cells of Table 3, and the exclusive signs in Lemma 5.2. Its separate implementation, `python3 scripts/three-four-eleven-reduction/audit_filter.py`, expands signed source rows independently and checks the full multisets of all 60 retained and 148 rejected records, including each d set and rejection reason, against the original certificate. It also compares every conclusion-row residue and d set, not only the four-column branch keys. The complete evidence is [scripts/three-four-eleven-reduction/audit-certificate.json](../scripts/three-four-eleven-reduction/audit-certificate.json). All checks pass; no branch or valuation correction is required. Page locators above were corrected using the printed footer numbers; earlier notes sometimes used zero-based PDF indices. The cited source computations are still not independently rerun.

All eight branch residue patterns occur in that finite enumeration. Such patterns need not solve the original equation even locally to every precision, and no simultaneous global solution is asserted. This reduction supplies narrowed necessary branches for a later global test. Repeating these finite filters alone cannot establish emptiness: a further global input or a separately assessed discriminating condition is required. The unconditional five-twist sector, infinitely many other signatures and the uniform Beal gap remain unresolved. No other ordered placement or exponent-divisor extension is claimed.

This is a local specialization and reproduction of cited mathematics. The elementary square, prime-support and valuation arguments are included because the source studies unrestricted primitive X^2+Y^3=Z^11 rather than the additional condition X=B^2. No originality or complete Beal candidate is claimed.

## Mathlib

Coverage of the full FNS modular reduction, CM computation and this ordered specialization: **not checked**. Supporting gcd, prime-divisibility, quadratic-residue and valuation declarations: **not checked**. Unknown availability is not evidence of absence. The named published results are the external inputs.
