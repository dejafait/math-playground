# L064 — The capped first conductor-389 Kurihara residue is zero

## Hypotheses

Use E/Q: y^2+y=x^3+x^2-2x, its minimal model and conductor 389
from audited L030, and the complete audited normalized functional
F=I/Omega(E)=-phi from L032, on the entire torsion-free relative
Gamma_0(389) module. Omega(E) is the total minimal real period and
{alpha,beta} is oriented from alpha to beta. Set p=7 and m=1.

Use Kim's P_1 convention: ell does not divide 389*7,
ell=1 mod 7 and a_ell=ell+1 mod 7. Among distinct increasing pairs
ell_1<ell_2<=500 with ell_1*ell_2<=100000, select the first in
lexicographic order. At each selected prime choose the least positive
primitive root. No rank, rational point or Selmer-size input is used.

Complete finite evidence is under `scripts/conductor389-kurihara/`:
`certificate.json` contains all eligibility and logarithm tables;
`terms.jsonl` contains every uncombined path and term;
`verification.json` records the complete independent replay;
`replay.jsonl` records every independently recomputed doubled contribution
and prefix sum. Reproduction from the notebook directory:

```bash
python3 scripts/conductor389-kurihara/build_certificate.py
python3 scripts/conductor389-kurihara/verify_certificate.py
python3 scripts/conductor389-kurihara/check_rejections.py
```

These programs preserve the L030/L032 inputs. The verifier imports no
producer or prior checker. Hashes bind the exact audited input bytes;
the mathematical normalization comes from L032, not hash agreement.

## Conclusion

The complete eligible-prime list under 500 is (113,281); hence the
selected pair is (113,281) and N=31753<=100000. The least primitive
root is 3 at each prime. With exponents taken modulo 7, the exact sum is

\[
\sum_{\substack{1\le a<31753\\(a,31753)=1}}
 F(\{\infty,a/31753\})
 (\log_{3,113}(a)\bmod7)(\log_{3,281}(a)\bmod7)
 =-1365.
\]

Consequently its Kim depth-one Kurihara residue is **0 in F_7**.
All 31360 unit-residue terms, including 13342 zero contributions modulo
seven, and all 319804 determinant-one path segments pass independent
replay. This is known-method reproduction. The bounded schedule stops
after this residue; it supplies no nonzero valuation input to L063 and
no conclusion about other indices, finite Selmer length, successful
localization, rational Kummer membership or the main BSD gap.

The separate fixed critical audit below passes. This validates the finite
negative result under the stated audited inputs; it changes none of the
remaining arithmetic or uniform-production gaps.

## Proof

**Imported definitions and applicability.** Import Chan-Ho Kim,
*The structure of Selmer groups and the Iwasawa main conjecture for
elliptic curves*, publisher-hosted author text dated 2025-05-12,
[Sections 1.2.2 and 1.4.1--1.4.3, printed pp. 3 and 5](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf#page=6).
These specify P_m, I_N, the plus-symbol and the finite logarithm-weighted
sum, including reduction modulo p^m at an eligible index. They do not
assert nonvanishing of the present sum. Coverage is reused from
`drafts/literature/2026-10-14-conductor389-two-prime-scalar-production.md`;
no reproof of Kim is needed.

Kim's defining identity is
2*pi*integral_0^infinity f(r+iy)dy=[r]^+ Omega_E^+ + i[r]^- Omega_E^-.
For the path infinity to r, dz=i*dy with y descending from infinity
to zero, giving 2*pi*i*integral_infinity^r f(z)dz equal to its left
side. Taking real parts and dividing by the same total minimal period
therefore identifies [r]^+=F({infinity,r}). L032 supplies F=-phi and
the full image in (1/2)Z, so reduction modulo seven uses the inverse
of each actual denominator. No reversal, half-plus projection,
connected-component period or Euler correction enters the sum.

Kim's Section 1.4.1 assumes residual irreducibility and a p-unit Manin
constant for its general integrality assertion. Here integrality at seven
instead follows from L032's independently audited half-integrality. No
such residual or Manin premise is silently certified, and no subsequent
Selmer theorem is invoked without its own full hypotheses.

**Complete capped eligibility.** Every prime ell<=500 with ell=1 mod7
is among the 71 integers 8,15,...,498. For every such integer the
certificate records all divisor trials through floor(sqrt(ell)); a
composite has a divisor in this range. The independent verifier also
tests every potential divisor 2,...,ell-1. Both classify exactly these
15 primes:
29,43,71,113,127,197,211,239,281,337,379,421,449,463,491.
None divides 389*7. Good reduction follows from L030's minimal
discriminant 389. For each such prime the producer retains the complete
histogram of y^2+y, all x right sides and all x point counts; the
verifier independently enumerates every y for every x in the displayed
equation. Adding the unique point at infinity gives respectively
36,32,82,105,117,190,205,235,294,356,376,438,474,491,519 points.
Thus only 105 and 294 are divisible by seven. Since
a_ell=ell+1-#E(F_ell), precisely 113 and 281 are in P_1 under the cap.
Their traces are 9 and -12. The complete sorted pair list consists
of the one pair, whose product 31753 meets the product cap. This proves
selection, rather than merely testing the selected primes.

**Fixed logarithms.** For each selected ell, `certificate.json` stores
all ell-1 successive powers of 3, their inverse exponent table on every
nonzero residue, and the failed full-orbit cardinalities of candidates
1 and 2. The verifier reconstructs the powers by repeated multiplication,
checks that they permute 1,...,ell-1, checks every inverse exponent by
modular powering, and tests 3^((ell-1)/q)!=1 for every prime q dividing
ell-1. This proves both primitivity and leastness, and fixes every log
before reduction modulo seven. It makes no generator-change inference.

**Complete paths and values.** Import Stein, *Modular Forms, a
Computational Approach*, online v0.1,
[weight-two Propositions 3.10/3.11 and Theorem 3.13](https://wstein.org/books/modform/modform/weight_two.html).
L030 already identifies their complete Manin presentation and saturated
integral quotient at level 389. These named results identify integral
paths and projective bottom-row cosets; no new modular-symbol theorem
is proved here.

For each unit a, `terms.jsonl` records a continued fraction for a/N,
every oriented segment, its SL_2(Z) lift h=(A,B;C,D), its coset i,
gamma=h*g_i^(-1), the entire 390-entry raw vector, all 65 quotient
coordinates and exact F value. The independent verifier evaluates the
continued fraction as a rational, starts at infinity, and checks for
every segment that det(h)=1, the start is B/D and the end is A/C in
canonical projective coordinates. Consecutive endpoints match and the
last endpoint is a/N. It identifies the coset by testing all 390
projective bottom rows, independently of the producer's modular-inverse
lookup. It verifies the full gamma matrix, det(gamma)=1, its lower-left
entry divisible by 389 and gamma*g_i=h. Thus each segment is exactly
the indicated oriented generator and telescoping proves the raw path.

From these segments the verifier reconstructs the full raw vector and
every quotient coordinate using L030's integral coordinates. It checks
evaluation both through all L032 generator values and through its
quotient functional. All 390 generator values, their equality with
-phi, every source and saturated relation, and the denominator two
are checked against the bound audited inputs. Reusing their proved
full-relative presentation and calibration is essential: finite path
agreement alone would not prove Neron normalization.

**Every summand and the sum.** The verifier independently enumerates
1<=a<N, excluding exactly the multiples of 113 or 281. Ordered term
equality and exhaustion reject omissions, duplicates and extras; the
actual and required cardinalities both equal 112*280=31360. Every term,
including zero weights and zero values, is retained. It reconstructs
both fixed logarithms, reduces the exact rational symbol modulo seven,
and compares the resulting product with the recorded contribution.

For independent accumulation let Y_a=2F({infinity,a/N}), an integer
by L032, and let b_a,c_a be the two exponent residues in {0,...,6}.
The complete replay gives sum_a Y_a*b_a*c_a=-2730; separately summing
the exact rational F values with the same weights gives -1365.
Their factor-two agreement is checked, as is every prefix of the integer
sum in `replay.jsonl`. Since 2^(-1)=4 mod7, the residue is
4*(-2730)=0 mod7, agreeing with rational reduction of -1365.
This is a full finite replay, not a preview, sampled sum or rounded
calculation. `verification.json` has seven passing grouped checks and
no failures, binding both the complete terms and the replay by SHA-256.

`rejection-checks.json` retains four bounded intended-error tests:
missing second term, duplicate first term, altered first contribution,
and an ineligible selected pair. Each fixture is explicitly a prefix;
the intended error is detected before its omitted suffix is reached.
Each fails for its specified reason. Original certificate, full terms,
verification and replay bytes remain unchanged. These checks supplement
the complete valid replay; they prove no universal software correctness.

No second pair, larger cap or higher depth is computed. A zero residue
does not have a certified valuation v<1, so L063's nonzero-residue premise
is absent. This failure of one bounded production test supplies no global
nonexistence or rank assertion. The known p=5 example in Kim's older
version is not used as computational evidence for this p=7 result.

**Separate critical audit, 2026-10-15.** The approved audit read all three
production/replay/rejection programs, the full L064 argument, relevant
audited L030/L032 proofs and the unchanged primary-source comparison.
Stein's generator is g{0,infinity}, matching the checked segment columns;
his presentation theorem removes torsion and refers injectivity to Manin,
Section 1.7. The theorem and audited presentation are imported, not
reproved by finite path agreement. The period, orientation and independent
integrality argument above survive review.

Run `python3 scripts/conductor389-kurihara/audit_fixed.py` from the
notebook directory in a checkout where its new output directory does not
yet exist. It deliberately refuses to overwrite existing audit evidence.
The complete retained output is in
`scripts/conductor389-kurihara/critical-audit-2026-10-15/`.
`complete-report.json` and `complete-replay.jsonl` are a fresh full
verifier execution; `audit.json` and `integer-check.jsonl` record the
distinct supplemental checks. The fresh report equals the entire original
report, and every retained and fresh replay row is independently checked.
The full replay covers all 71 candidate integers, all 15 finite-field
counts, both complete logarithm tables, all 390 normalized generator
values and their source/saturated relations, and every one of the 31360
unit paths with all 319804 segments and full 65-coordinate images.
No source, endpoint, denominator, logarithm or term mismatch was found.

For a distinct accumulation, sum the integers 2F(g_i) directly over the
segments of each already validated path, using their coset multiplicities.
This gives Y_a independently of the saved symbol value; all 31360 exact
comparisons pass. Reconstruct the logarithm residues by the bijections
3^k modulo 113 and 281, and group Y_a into bins
B_(i,j)=sum_(b_a=i,c_a=j) Y_a, for 0<=i,j<7. Each logarithm residue has
112/7=16 and 280/7=40 preimages respectively. The Chinese remainder
theorem therefore requires 640 units in each of the 49 bins. Every bin
has exactly that count, including zero-weight bins. All 49 integer
B_(i,j) are retained in `audit.json`; their weighted sum is
sum_(i,j) i*j*B_(i,j)=-2730. Independently adding the exact rational
values gives -1365. The streamed direct sum, grouped sum and every
old/fresh replay prefix agree, with 13342 zero contributions modulo seven.
This checks accumulation and coverage; it does not claim alternate-path
verification beyond the complete original-path replay.

All four original rejection certificates and complete prefix fixtures
were compared with their specified modifications and rerun into fresh
reports. The missing-second and duplicate-first cases each complete one
valid term and fail at the supplied second row with `unit ordering a=2`;
the altered contribution completes zero terms and fails at a=1; the
ineligible pair fails before opening any term replay. Thus every intended
error occurs before an omitted suffix, and none is an end-of-file
rejection. These are prefix tests, not complete altered certificates.
Every fresh failure report and existing prefix replay matches the
corresponding retained evidence. The before/after manifests verify all
37 original local/program/upstream artifacts are unchanged. All five
supplemental grouped checks pass with no failures. The audit preserves
the capped stop in ATTEMPTS/032 and produces no valuation v<1.

## Mathlib

Full matching finite conductor-389 Kurihara certificate: not checked.
Supporting modular-symbol, finite-field logarithm and exact finite-sum
coverage: not checked. Unknown coverage is not evidence of absence.
The cited primary definitions and audited L030/L032 provide the mathematical
inputs; the present contribution is a finite implementation and replay.
