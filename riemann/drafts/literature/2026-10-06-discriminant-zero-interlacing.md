# Zero-interlacing obstruction — bounded source comparison

TARGET: Test whether eventual nonpositivity of L367's discriminant forces zero interlacing of F_0 and G incompatible with their known zero information.
CHECKED: 2026-10-06
DECISION: SOURCE_BLOCKED
SEARCH_EVIDENCE: Exact differential-pencil, Sturm, Obreschkoff and zero-count/fluctuation searches completed; inspected primary separation/polynomial statements, but no matching weak eventual theorem or unconditional signed-count contradiction was established.
SOURCE_EVIDENCE: MIT 18.034 Spring 2009 Lecture 9, Theorem 9.1 and its full proof; Borcea–Brändén–Shapiro Master4 author PDF §3.1 p. 9 Theorems 9–10; DLMF 1.13.1–1.13.6 and 25.10(i); Carneiro–Chirre–Milinovich arXiv:2006.04288 §1.2–1.3, equations (1.1)–(1.4) and Corollaries 2–3; local L018 and L366–L370 relevant statements/zero cases.
COMPARISON: Sturm needs a common regular ODE; Obreschkoff and Hermite–Biehler need polynomial hyperbolicity/stability, not first-Laguerre positivity; the inspected signed S(t) estimates for n=0 assume RH, and infinite critical-line zeros alone give no contradiction.
GAP: Direct weak separation with common zeros is unproved; essential unconditional signed zero-count coverage for the actual-pair contradiction was not retrieved, and no count formula for G has yet been proved locally.
REASON: Park the dependent actual-count contradiction; prepare a narrower, independently testable direct separation target with the inspected coverage, rather than repeat inaccessible count-source browsing or assume RH.
SCOPE: This review does not approve the full actual-count contradiction; its direct weak-separation subproblem is separately assessed in 2026-10-06-discriminant-weak-separation.md.

## Relevance and local inspection

The main gap is global actual-theta mixed positivity and L367's total
signed margin relative to its remainder. The proposed intermediate target
would obstruct one sufficient discriminant certificate, not solve RH.
Inputs inspected: L018's exact completion/zero correspondence; L366 (1)
and L367 (1)–(3); L368 (1)–(8), including the nonzero complex carrier,
Euler logarithm and phase derivative; L370 (1)–(6) and its common-zero
case. F_0=2Ξ, whereas G is the real projection of Qbζ(5/2+it).
Nonvanishing of this complex carrier is not nonvanishing of G.

L368 supplies eventual strict positivity of G′²−GG″, with unevaluated
onset. L370 supplies a physical discriminant identity valid at zeros;
it supplies neither a Wronskian sign nor separation. Its full envelope
correction must remain if normalized functions are used. L370 expressly
allows F_0=G=0 and reports zero physical discriminant there, so strict
Sturm conclusions cannot simply be assumed for the weak inequality.
No new algebra or zero implication was derived in this literature turn.

Targeted notebook searches for interlacing, Sturm, Obreschkoff and
separation found no existing actual-pair separation result. The relevant
October discriminant reviews leave sharp-moment coverage blocked. Their
scope does not cover zero geometry. L354's stated count/gap obstruction
and L355 in the supplied overview concern generic sufficient conditions,
not this pair or the two-function discriminant. L365's fixed-regulator
stop is distinct and remains intact. No cross-notebook input is used.

## Inspected primary sources

1. [MIT 18.034, Spring 2009, Lecture 9](https://ocw.mit.edu/courses/18-034-honors-differential-equations-spring-2009/0cdeb657491010f0f8c60aa49f2d5248_MIT18_034s09_lec09.pdf),
   Theorem 9.1, printed pp. 1–2 (PDF pages 2–3), read with its full proof.
   Two independent solutions of the same homogeneous second-order ODE
   with continuous coefficients have alternating zeros. The proof uses
   a nowhere-zero Wronskian and opposite derivative signs at successive
   zeros. No such common ODE or Wronskian nonvanishing is established for
   F_0,G. This is supporting terminology, not an applicable import.
   Theorem 9.2 was inspected only as an adjacent comparison statement;
   no ordered-potential premise is available here.

2. J. Borcea, P. Brändén and B. Shapiro,
   *Pólya–Schur master theorems for circular domains and their boundaries*,
   [author PDF Master4](https://staff.math.su.se/shapiro/Articles/Master4.pdf),
   §3.1, printed p. 9, definitions and Theorems 9–10 (retrieved 2026-10-06;
   manuscript revision date not verified). The Wronskian characterization
   presupposes hyperbolic polynomials with degrees differing by at most
   one. Theorem 9 uses stability of f+ig; Theorem 10 uses real-rootedness
   of every real linear combination. Strict versions exclude common
   zeros. None supplies a theorem for real analytic functions on an
   eventual ray under a weak first differential inequality. No full-pencil
   real-rootedness or stability may be inserted as a premise.

3. [DLMF 1.13.1–1.13.6](https://dlmf.nist.gov/1.13#i), online display
   retrieved 2026-10-06, release number not recorded. Reuse its Wronskian
   convention. Abel's formula and fundamental-pair equivalences require
   solutions of the same equation; they are not arbitrary-pair facts.
   [DLMF 25.10(i)](https://dlmf.nist.gov/25.10#i) supplies the Hardy Z
   convention and infinitely many critical-line zeros, citing Titchmarsh
   (1986), §4.17. Via L018 this is relevant to F_0. It gives neither
   simplicity of every zero nor a signed counting discrepancy against G.

4. E. Carneiro, A. Chirre and M. B. Milinovich,
   *Large values of the argument of the Riemann zeta-function and its
   iterates*, [arXiv:2006.04288 PDF](https://arxiv.org/pdf/2006.04288),
   retrieved version, pp. 1–3, §1.2–1.3. The introduction states the
   Riemann–von Mangoldt formula with S(t), counting all strip zeros.
   Equations (1.1)–(1.4) and Corollary 2's n=0 signed omega results
   assume RH. The unconditional Corollary 3 is for n≥3, not S(t).
   These cannot furnish the unconditional signed S(t) input needed here.
   Proofs of the conditional omega theorems are not needed or imported.

## Search evidence and unread leads

Queries included `Sturm separation theorem solutions same differential
 equation zeros theorem DLMF`, `Obreschkoff theorem interlacing all real
 linear combinations real rooted polynomials`, `Riemann xi real zeros
 Hardy theorem primary Titchmarsh N(T)`, `Littlewood S(t) Omega plus minus
 log t log log t Riemann zeros theorem pdf author`, `S(t) Omega Selberg
 negative zeta pdf`, and `Sign changes of the function S(t) Korolev pdf`.
Chudnovsky–Seymour's author paper *The roots of the independence polynomial
of a clawfree graph*, §3 closing paragraph, was inspected as corroboration
of the polynomial scope and general/common-root distinction, not as an
additional separation input. Search failure establishes no novelty.

Unconditional-fluctuation leads: Selberg, *On the remainder in the formula
for N(T)* (1944), and *Contributions to the theory of the Riemann
zeta-function* (1946); Titchmarsh, §9.9; Korolev, *Sign changes of the
function S(t) on short intervals*, Izv. Math. 69 (2005), 719–731.
The accessible arXiv reference list verifies the Selberg bibliographic
leads. Essential unconditional theorem hypotheses/proof cases were not
read: MathNet PDF opens failed, the Rutgers Titchmarsh PDF text extraction
was unusable, screenshot calls exposed no readable images, and a narrowly
attempted local download failed DNS. Search snippets are not imported.
These are unread leads, not ready evidence, and do not justify dependent
mathematics. The previously blocked sharp discriminant mean is untouched.

## Decision and test

Do not claim the original incompatibility or import Sturm/Obreschkoff.
The original target remains parked for its essential count-source gap.
A direct local weak-separation question needs none of those missing
arithmetic sources and is separately assessed. Its downstream test is
whether a valid consequence survives common/multiple F_0 zeros and can
later support a counting comparison. A merely strict or no-common-zero
statement is insufficient. If weak separation fails, stop this obstruction;
if it succeeds, assess the precise unconditional count input separately.
No actual-family contradiction, new sign range, RH candidate or novel
mathematics is claimed. Full matching Mathlib coverage is not checked.
